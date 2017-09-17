import pika
import sys
import time
import json

#@Developers: Niranjan Basnet, Zuli Wu

#Module Description: Handling incoming streams for database interaction.

# Expected Stream format: "{"deviceid":"d37825daa97041dd","sensortype":"accelerometer","
# data":[{"timestamp":"1496078282698","x":"2.23517e-7","y":"9.77631","z":"0.812348"}]}

userid = " ".join(sys.argv[1:]) # Userid from the terminal signifies the collection name for the user
datenow = time.strftime("%d/%m/%Y-%X") # Date time signifies the unique timestamp recorded in session
datenow = str(datenow)
collname = userid+'-'+datenow # Collection name when new instance is created

try:

    from pymongo import MongoClient
    client = MongoClient('localhost', 27017)
    db = client['test_database']
    collection = db['test_database'] # test_database to mock up and test instead of the actual database 'trackpick'

    if collection is not None: # See whether the instance of database is created or not

        print('Connecting with Database...')

    db.create_collection(collname)
    getcoll = db.get_collection(collname)
    getcoll = str(getcoll)
    getcoll = getcoll[129:-2]
    if getcoll == collname: # See whether collection is created or not
        print("Collection with name "+ collname + "successfully created")
    else:
        print("Collection not created")
except:
    print("Database not found...Please start the MongoDB and try again...") # Checks exception for no database
    exit()


print ("Fetching data and inserting into database...")

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) # Connection with the designated queue
channel = connection.channel()

channel.queue_declare(queue='trackPick')

def callback(ch, method, properties, indata):
    if indata is None:
        print("No data in the queue")
    else:

        indata = indata.decode('utf-8')
        #Dequeue from incoming data stream here
        try:
            #Loading data from the incoming data
            data = json.loads(indata)
            #Passing onto the dictionary to parse first level data
            dict = data
            serverTime = dict['servertime']
            # Passing onto the dictionary to parse second level data
            clientData = dict['cdata']
            # Passing onto the dictionary to parse third level data
            dict = clientData
            sensorType = dict['sensortype']
            deviceId = dict['deviceid']
            mainClientData = dict['data']
            #Removing the extra brackets to make it parsable for the data
            mainClientData = mainClientData[0]
            dict = mainClientData
            #Main data from the client
            xData = dict['x']
            yData = dict['y']
            zData = dict['z']
            clientTime = dict['timestamp']
            #Preparation of the data for effecient insertion
            insertData = '{"servertime":' + '"' + serverTime + '",' + '"sensortype":' + '"' + sensorType +'",' + '"deviceid":' + '"' + deviceId + '",' + '"clienttime":' + '"' + clientTime + '",' + '"x":' + '"' + xData + '",' + '"y":' + '"' + yData + '",' + '"z":' + '"' + zData + '"}'

            print(insertData)

            db.get_collection(name=getcoll).insert_one(  # Database instance finaldata as "Key"
                # [insertdata] as "Value" as documents
                {

                    "session": [insertData]

                }
            )
        except:
            print("Data Parse was not possible for the data. Please try again....")

channel.basic_consume(callback, queue='trackPick')

channel.queue_declare(exclusive=True)

channel.start_consuming()

connection.close()
