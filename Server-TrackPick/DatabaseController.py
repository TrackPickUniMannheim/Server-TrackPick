import pika
import sys
import time
import json

#@Developers: Niranjan Basnet, Zuli Wu

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
            data = json.loads(indata)
            #print('*********************************')
            #print('*********************************')
            #print('*********************************')
            #print('*********************************')
            ##print('*********************************')
            #print('*********************************')
            #print('This is Original data')
            print(data)
            #print('*********************************')
            #print('*********************************')
            #print('THis is string data')
            #print('*********************************')
            #print('*********************************')
            #data = str(data)
            tdata = '"'+str(data)+'"'
            print(tdata)
            predata = tdata.split("'")
            print(predata)
            #print('*********************************')
            #print('*********************************')
            #print('THIS IS SINGELTON DATA')
            #print(predata[3]) #servertime
            #print('------------------------------------------------------------------------------------')
            #print(predata[11]) #timestamp
            #print('------------------------------------------------------------------------------------')
            #print(predata[15]) #z
            #print('------------------------------------------------------------------------------------')
            #print(predata[19]) #x
            ##print('------------------------------------------------------------------------------------')
            #print(predata[23]) #y
            #print('------------------------------------------------------------------------------------')
            #print(predata[27]) #Device id   '"sensortype":'+'"'+predata[31]+'",'+
            #print('------------------------------------------------------------------------------------')
            #print(predata[31]) #sensor type
            #print('*********************************')

            # Data Transformation

            insertData = '{"servertime":'+'"'+predata[3]+'",'+ '"sensortype":'+'"'+predata[31]+'",'+'"clienttime":'+'"'+predata[11]+'",'+'"x":'+'"'+predata[31]+'",'+'"y":'+'"'+predata[31]+'",'+'"z":'+'"'+predata[31]+'"}'
            print('*********************************')
            print('The data that will be inserted is')
            print('*********************************')
            print(insertData)
            db.get_collection(name=getcoll).insert_one(  # Database instance finaldata as "Key"
                 #[indata] as "Value" as documents
                {

                    "session": [insertData]

                }
            )
        except:
            print("Data Parse not possible")





channel.basic_consume(callback, queue='trackPick')


channel.queue_declare(exclusive=True)

channel.start_consuming()



connection.close()






