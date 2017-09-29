import csv
import json

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client['test_database']

collection = '-28/09/2017-09:31:06'
coll_records = []
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
    coll_records.append(coll_record)

# Iterate through the list of collection records and write them to the csv file
    csvname = '-28-09-2017-09.31.06.csv'
    with open(csvname, "w") as f:
        fields = ['servertime','sensortype','deviceid','clienttime','x','y','z']
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer = csv.writer(f)
        writer.writerows(coll_records)