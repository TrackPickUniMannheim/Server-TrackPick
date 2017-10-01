import csv
import json
import numpy as np
import matplotlib.pyplot as plt
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['test_database']

collection = 'Nancy-2017.09.30-18.35.54'
coll_records = []
timeold = 0
timenew = 0
coll_eval = []

for x in db[collection].find():
    coll_record = []
    dict = json.loads(''.join(map(str, x['session'])))
    coll_record.append(dict['servertime'])
    coll_record.append(dict['sensortype'])
    coll_record.append(dict['deviceid'])
    coll_record.append(dict['clienttime'])
    coll_record.append(dict['x'])
    coll_record.append(dict['y'])
    coll_record.append(dict['z'])
    coll_records.append(coll_record)     #export everything from the collection

    #for evaluation and diagram creation
    if dict['sensortype'] == 'accelerometer' and dict['deviceid'] == 'f7c3857f13a0234f':
        timenew = int(float(dict['clienttime']))
        if timeold != 0:
            coll_eval.append(timenew - timeold)
        timeold = timenew

#plot clienttime differences
plt.plot(coll_eval)
plt.ylabel('timedifference in ms')
plt.show()

# Iterate through the list of collection records and write them to the csv file
csvname = collection+'-phone-accelerometer.csv'
with open(csvname, "w") as f:
    fields = ['servertime','sensortype','deviceid','clienttime','x','y','z']
    writer = csv.DictWriter(f, delimiter=',', lineterminator='\n', fieldnames=fields)
    #writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer = csv.writer(f)
    writer.writerows(coll_records)