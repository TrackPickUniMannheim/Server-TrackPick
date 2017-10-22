import pika
import sys
import time
import json
import csv
from pika import exceptions
import logging
import os
from collections import deque

#@Developers: Niranjan Basnet, Zuli Wu

#Module Description: Handling incoming streams for database interaction.

# Expected Stream format: "{"deviceid":"d37825daa97041dd","sensortype":"accelerometer","
# data":[{"timestamp":"1496078282698","x":"2.23517e-7","y":"9.77631","z":"0.812348"},{"timestamp":"1496078282698","x":"2.23517e-7","y":"9.77631","z":"0.812348"}]}

class _CallbackResult(object):
    """ CallbackResult is a non-thread-safe implementation for receiving
    callback results; INTERNAL USE ONLY!
    """
    __slots__ = ('_value_class', '_ready', '_values')
    def __init__(self, value_class=None):



        self._value_class = value_class
        self._ready = None
        self._values = None
        self.reset()

    def reset(self):

        self._ready = False
        self._values = None

LOGGER = logging.getLogger(__name__)

userid = " ".join(sys.argv[1:]) # Userid from the terminal signifies the collection name for the user
datenow = time.strftime('%Y.%m.%d-%H.%M.%S') # Date time signifies the unique timestamp recorded in session
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

def close(self,reply_code=200,reply_text='Normal Shutdown'):
        try:
            if self.is_closed:
                LOGGER.debug('Close called on closed connection (%s): %s',
                             reply_code, reply_text)
                return
            LOGGER.info('Closing connection (%s): %s', reply_code, reply_text)
            self._user_initiated_close = True
            for impl_channel in pika.compat.dictvalues(self._impl._channels):
                channel = impl_channel._get_cookie()
                if channel.is_open:
                    try:
                        channel.close(reply_code, reply_text)
                    except exceptions.ChannelClosed as exc:
                        # Log and suppress broker-closed channel
                        LOGGER.warning('Got Channel Closed exception while closing channel '
                                       'from connection.close: %r', exc)
                    finally:
                        self._cleanup()

            self._impl.close(reply_code, reply_text)
            self._flush_output(self._closed_result.is_ready)

        except:
            print("Connection could not be closed")
def cleanup(self):
    self._impl.ioloop.deactivate_poller()
    self._ready_events.clear()
    self._opened_result.reset()
    self._open_error_result.reset()
    self._closed_result.reset()

def queue_purge(self, queue=''):

        with _CallbackResult(self._MethodFrameCallbackResultArgs) as \
                purge_ok_result:
            self._impl.queue_purge(callback=purge_ok_result.set_value_once,
                                   queue=queue,
                                   nowait=False)

            self._flush_output(purge_ok_result.is_ready)
            return purge_ok_result.value.method_frame

def queue_delete(self, queue='', if_unused=False, if_empty=False):

        with _CallbackResult(self._MethodFrameCallbackResultArgs) as \
                delete_ok_result:
            self._impl.queue_delete(callback=delete_ok_result.set_value_once,
                                    queue=queue,
                                    if_unused=if_unused,
                                    if_empty=if_empty,
                                    nowait=False)

            self._flush_output(delete_ok_result.is_ready)
            return delete_ok_result.value.method_frame


def callback(ch, method, properties, indata):
    if indata is None:
        print("No data in the queue. Please restart the session to fill the queue first")
    else:

        indata = indata.decode('utf-8')
        #Dequeue from incoming data stream here
        try:
            DONE = False
            if(indata=='sessionclosed'):
                print("Inside the Done folder")
                DONE = True
            #Loading data from the incoming data
            else:
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
                mainClientDataAll = dict['data']
                #Removing the extra brackets to make it parsable for the data

                #Loop over buffered data and insert each value seperately into mongo
                for x in range(0,len(mainClientDataAll)):
                    mainClientData = mainClientDataAll[x]
                    dict = mainClientData
                    #Main data from the client
                    xData = dict['x']
                    yData = dict['y']
                    zData = dict['z']
                    clientTime = dict['timestamp']
                    if sensorType is "video":
                        videoname = dict['videoname']
                    #Preparation of the data for effecient insertion
                    insertData = '{"servertime":' + '"' + serverTime + '",' + '"sensortype":' + '"' + sensorType +'",' + '"deviceid":' + '"' + deviceId + '",' + '"clienttime":' + '"' + clientTime + '",' + '"x":' + '"' + xData + '",' + '"y":' + '"' + yData + '",' + '"z":' + '"' + zData + '",' + '"videofilename":' + '"' + videoname + '"}'

                    print(insertData)

                    db.get_collection(name=getcoll).insert_one(  # Database instance finaldata as "Key"
                        # [insertdata] as "Value" as documents
                        {

                            "session": [insertData]

                        }
                    )
                #DONE = True
        except:
            print("Data Parse was not possible for the data. Please try again....")

        #DONE = True
        print('Data successfully stored into MongoDB')

        if DONE is True:
            print("Creating CSV now")
            try:
                coll_sensors = []
                coll_devices = []

                #from pymongo import MongoClient
                #client = MongoClient('localhost', 27017)
                # db = client['test_database']
                for x in db[collname].find():
                    coll_record = []
                    dict = json.loads(''.join(map(str, x['session'])))

                    if not dict['deviceid'] in coll_devices:
                        coll_devices.append(dict['deviceid'])

                    if not dict['sensortype'] in coll_sensors:
                        coll_sensors.append(dict['sensortype'])

                for y in coll_devices :
                    for z in coll_sensors :
                        coll_records = []
                        for x in db[collname].find():
                            coll_record = []
                            dict = json.loads(''.join(map(str, x['session'])))

                            if dict['deviceid'] == y and dict['sensortype'] == z:
                                coll_record.append(dict['servertime'])
                                coll_record.append(dict['sensortype'])
                                coll_record.append(dict['deviceid'])
                                coll_record.append(dict['clienttime'])
                                coll_record.append(dict['x'])
                                coll_record.append(dict['y'])
                                coll_record.append(dict['z'])
                                coll_records.append(coll_record)

                        if not len(coll_records) == 0:
                            csvname =collname+ y+'-'+z+'.csv'
                            csvname = str(csvname)

                            with open(csvname, "w") as f:
                                fields = ['servertime','sensortype','deviceid','clienttime','x','y','z']
                                writer = csv.DictWriter(f, fieldnames=fields)
                                writer.writeheader()
                                writer = csv.writer(f)
                                writer.writerows(coll_records)


                print('Data Extraction was successfull!')
                try:
                    channel.queue_delete(queue='trackPick')
                    print("Queue is deleted")
                except:
                    print("Queue was not cleared")
                connection.close()

            except Exception as e: print(e)


channel.basic_consume(callback, queue='trackPick')

channel.queue_declare(exclusive=True)

channel.start_consuming()

connection.close()
