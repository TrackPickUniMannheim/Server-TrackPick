import pika
import sys
import time


userid = " ".join(sys.argv[1:]) # Userid from the terminal signifies the collection name for the user

datenow = time.strftime("%d/%m/%Y-%X") # Date time signifies the unique timestamp recorded in session

datenow = str(datenow)
collname = userid+'-'+datenow # Collection name when new instance is created

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['test_database']
collection = db['test_database'] # test_database to mock up and test the actual database 'trackpick'

if collection is not None: # See whether the instace of database is created or not

    print('Database Instance Present')

db.create_collection(collname)
getcoll = db.get_collection(collname)
getcoll = str(getcoll)
getcoll = getcoll[129:-2]
if getcoll == collname: # See whether collection is created or not
    print('Collection with name '+ collname + 'successfully created')
else:
    print('Collection not created')

#Start with connection

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






