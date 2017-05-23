import pika
import sys
import time


#Device and sensor definitions
Device1 = 'F909023'
Sensor11 = 'Acceleromter'
Sensor12 = 'Magnetometer'
Sensor13 = 'Gyroscope'
Document11 = Device1+Sensor11
Document12 = Device1+Sensor12
Document13 = Device1+Sensor13

Device2 = 'F909022'
Sensor21 = 'Acceleromter'
Sensor22 = 'Magnetometer'
Sensor23 = 'Gyroscope'
Document21 = Device1+Sensor21
Document22 = Device1+Sensor22
Document23 = Device1+Sensor23

Device3 = 'F909021'
Sensor31 = 'Acceleromter'
Sensor32 = 'Magnetometer'
Sensor33 = 'Gyroscope'
Document31 = Device1+Sensor31
Document32 = Device1+Sensor32
Document33 = Device1+Sensor33


userid = " ".join(sys.argv[1:]) # Userid from the terminal signifies the collection name for the user
datenow = time.strftime("%d/%m/%Y-%X") # Date time signifies the unique timestamp recorded in session
datenow = str(datenow)
collname = userid+'-'+datenow # Collection name when new instance is created

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['test_database']
collection = db['test_database'] # test_database to mock up and test instead of the actual database 'trackpick'

if collection is not None: # See whether the instance of database is created or not

    print('Database Instance Present')

db.create_collection(collname)
getcoll = db.get_collection(collname)
getcoll = str(getcoll)
getcoll = getcoll[129:-2]
if getcoll == collname: # See whether collection is created or not
    print('Collection with name '+ collname + 'successfully created')
    # Creating Documents for First Device here
    if Device1 == 'F909023' and Sensor11 == 'Acceleromter':
        db.get_collection(name=getcoll).insert_one(
            {
                "deviceid": Device1,    # Device 1 with first sensor and so on
                "sensor": Sensor11,
                "values":[
                    {

                    }
                ]
            }
        )
        print("Document11 Created")
    if Device1 == 'F909023' and Sensor12 == 'Magnetometer':
        db.get_collection(name=getcoll).insert_one(
        {
                "deviceid": Device1,
                "sensor": Sensor12,
                "values": [
                    {

                     }
                    ]
        }
        )
        print("Document12 Created")

    if Device1 == 'F909023' and Sensor13 == 'Gyroscope':
        db.get_collection(name=getcoll).insert_one(
        {
                "deviceid": Device1,
                "sensor": Sensor13,
                "values": [
                    {

                     }
                    ]
        }
        )

        print("Document13 Created")
    # Creating documents for second device
    if Device2 == 'F909022' and Sensor21 == 'Acceleromter':
        db.get_collection(name=getcoll).insert_one(
            {
                "deviceid": Device2,    # Device 1 with first sensor and so on
                "sensor": Sensor21,
                "values":[
                    {

                    }
                ]
            }
        )
        print("Document21 Created")
    if Device2 == 'F909022' and Sensor22 == 'Magnetometer':
        db.get_collection(name=getcoll).insert_one(
        {
                "deviceid": Device2,
                "sensor": Sensor22,
                "values": [
                    {

                     }
                    ]
        }
        )
        print("Document22 Created")

    if Device2 == 'F909022' and Sensor23 == 'Gyroscope':
        db.get_collection(name=getcoll).insert_one(
        {
                "deviceid": Device2,
                "sensor": Sensor23,
                "values": [
                    {

                     }
                    ]
        }
        )

        print("Document23 Created")
    #Creating documents for third device

    if Device3 == 'F909021' and Sensor31 == 'Acceleromter':
        db.get_collection(name=getcoll).insert_one(
            {
                "deviceid": Device3,    # Device 1 with first sensor and so on
                "sensor": Sensor31,
                "values":[
                    {

                    }
                ]
            }
        )
        print("Document31 Created")
    if Device3 == 'F909021' and Sensor32 == 'Magnetometer':
        db.get_collection(name=getcoll).insert_one(
        {
                "deviceid": Device3,
                "sensor": Sensor32,
                "values": [
                    {

                     }
                    ]
        }
        )
        print("Document32 Created")

    if Device3 == 'F909021' and Sensor33 == 'Gyroscope':
        db.get_collection(name=getcoll).insert_one(
        {
                "deviceid": Device3,
                "sensor": Sensor33,
                "values": [
                    {

                     }
                    ]
        }
        )

        print("Document33 Created")



else:
    print('Collection not created')

#Start with connection with queue and fetch the data

print ('Fetching data...')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost')) # Connection with the designated queue
channel = connection.channel()

channel.queue_declare(queue='trackPick')

def callback(ch, method, properties, indata):
    if indata is None:
        print("No data in the queue")
    else:
        print("Queue name is %r" % indata)


channel.basic_consume(callback,
                      queue='trackPick')

channel.queue_declare(exclusive=True)

channel.start_consuming()

connection.close()






