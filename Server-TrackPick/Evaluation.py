import csv
import json
import numpy as np
import pymongo
import matplotlib.pyplot as plt
from pymongo import MongoClient

#Connection to MongoDB with specified Collection
client = MongoClient('localhost', 27017)
db = client['test_database']
collection = 'NIRANJANPICKINGHOME2-2017.10.24-20.37.16'

# Client Timestamp Variables
timeold_client_phone_accelerometer = 0
timenew_client_phone_accelerometer = 0
coll_eval_client_phone_accelerometer = []

timeold_client_phone_gyroscope = 0
timenew_client_phone_gyroscope = 0
coll_eval_client_phone_gyroscope = []

timeold_client_phone_magnetic = 0
timenew_client_phone_magnetic = 0
coll_eval_client_phone_magnetic = []

timeold_client_watch_accelerometer = 0
timenew_client_watch_accelerometer = 0
coll_eval_client_watch_accelerometer = []

timeold_client_watch_gyroscope = 0
timenew_client_watch_gyroscope = 0
coll_eval_client_watch_gyroscope = []

timeold_client_watch_magnetic = 0
timenew_client_watch_magnetic = 0
coll_eval_client_watch_magnetic = []

timeold_client_glass_accelerometer = 0
timenew_client_glass_accelerometer = 0
coll_eval_client_glass_accelerometer = []

timeold_client_glass_gyroscope = 0
timenew_client_glass_gyroscope = 0
coll_eval_client_glass_gyroscope = []

timeold_client_glass_magnetic = 0
timenew_client_glass_magnetic = 0
coll_eval_client_glass_magnetic = []

# Server Timestamp Variables
timeold_server_phone_accelerometer = 0
timenew_server_phone_accelerometer = 0
coll_eval_server_phone_accelerometer = []

timeold_server_phone_gyroscope = 0
timenew_server_phone_gyroscope = 0
coll_eval_server_phone_gyroscope = []

timeold_server_phone_magnetic = 0
timenew_server_phone_magnetic = 0
coll_eval_server_phone_magnetic = []

timeold_server_watch_accelerometer = 0
timenew_server_watch_accelerometer = 0
coll_eval_server_watch_accelerometer = []

timeold_server_watch_gyroscope = 0
timenew_server_watch_gyroscope = 0
coll_eval_server_watch_gyroscope = []

timeold_server_watch_magnetic = 0
timenew_server_watch_magnetic = 0
coll_eval_server_watch_magnetic = []

timeold_server_glass_accelerometer = 0
timenew_server_glass_accelerometer = 0
coll_eval_server_glass_accelerometer = []

timeold_server_glass_gyroscope = 0
timenew_server_glass_gyroscope = 0
coll_eval_server_glass_gyroscope = []

timeold_server_glass_magnetic = 0
timenew_server_glass_magnetic = 0
coll_eval_server_glass_magnetic = []

# Time Difference Variables
coll_eval_difference_phone_accelerometer = []
coll_eval_difference_phone_gyroscope = []
coll_eval_difference_phone_magnetic = []
coll_eval_difference_watch_accelerometer = []
coll_eval_difference_watch_gyroscope = []
coll_eval_difference_watch_magnetic = []
coll_eval_difference_glass_accelerometer = []
coll_eval_difference_glass_gyroscope = []
coll_eval_difference_glass_magnetic = []

all_dicts = []
# Analyze Timestamps
for x in db[collection].find():
    all_dicts.append(json.loads(''.join(map(str, x['session']))))

newlist = sorted(all_dicts, key=lambda k: k['clienttime']) 

for dict in newlist:
    #PHONE
    if dict['sensortype'] == 'accelerometer' and dict['deviceid'] == 'ddd830aa7d688be5':
        timenew_client_phone_accelerometer = int(float(dict['clienttime']))
        if timeold_client_phone_accelerometer != 0:
            coll_eval_client_phone_accelerometer.append(timenew_client_phone_accelerometer - timeold_client_phone_accelerometer)
        timeold_client_phone_accelerometer = timenew_client_phone_accelerometer
        
    elif dict['sensortype'] == 'gyroscope' and dict['deviceid'] == 'ddd830aa7d688be5':
        timenew_client_phone_gyroscope = int(float(dict['clienttime']))
        if timeold_client_phone_gyroscope != 0:
            coll_eval_client_phone_gyroscope.append(timenew_client_phone_gyroscope - timeold_client_phone_gyroscope)
        timeold_client_phone_gyroscope = timenew_client_phone_gyroscope
        
    elif dict['sensortype'] == 'magneticfield' and dict['deviceid'] == 'ddd830aa7d688be5':
        timenew_client_phone_magnetic = int(float(dict['clienttime']))
        if timeold_client_phone_magnetic != 0:
            coll_eval_client_phone_magnetic.append(timenew_client_phone_magnetic - timeold_client_phone_magnetic)
        timeold_client_phone_magnetic = timenew_client_phone_magnetic

    #WATCH
    elif dict['sensortype'] == 'accelerometer' and dict['deviceid'] == 'f7c3857f13a0234f':
        timenew_client_watch_accelerometer = int(float(dict['clienttime']))
        if timeold_client_watch_accelerometer != 0:
            coll_eval_client_watch_accelerometer.append(timenew_client_watch_accelerometer - timeold_client_watch_accelerometer)
        timeold_client_watch_accelerometer = timenew_client_watch_accelerometer

    elif dict['sensortype'] == 'gyroscope' and dict['deviceid'] == 'f7c3857f13a0234f':
        timenew_client_watch_gyroscope = int(float(dict['clienttime']))
        if timeold_client_watch_gyroscope != 0:
            coll_eval_client_watch_gyroscope.append(timenew_client_watch_gyroscope - timeold_client_watch_gyroscope)
        timeold_client_watch_gyroscope = timenew_client_watch_gyroscope
        
    elif dict['sensortype'] == 'magneticfield' and dict['deviceid'] == 'f7c3857f13a0234f':
        timenew_client_watch_magnetic = int(float(dict['clienttime']))
        if timeold_client_watch_magnetic != 0:
            coll_eval_client_watch_magnetic.append(timenew_client_watch_magnetic - timeold_client_watch_magnetic)
        timeold_client_watch_magnetic = timenew_client_watch_magnetic

    #GLASS
    elif dict['sensortype'] == 'accelerometer' and dict['deviceid'] == '62c7c4a8aa33b123':
        timenew_client_glass_accelerometer = int(float(dict['clienttime']))
        if timeold_client_glass_accelerometer != 0:
            coll_eval_client_glass_accelerometer.append(timenew_client_glass_accelerometer - timeold_client_glass_accelerometer)
        timeold_client_glass_accelerometer = timenew_client_glass_accelerometer

    elif dict['sensortype'] == 'gyroscope' and dict['deviceid'] == '62c7c4a8aa33b123':
        timenew_client_glass_gyroscope = int(float(dict['clienttime']))
        if timeold_client_glass_gyroscope != 0:
            coll_eval_client_glass_gyroscope.append(timenew_client_glass_gyroscope - timeold_client_glass_gyroscope)
        timeold_client_glass_gyroscope = timenew_client_glass_gyroscope

    elif dict['sensortype'] == 'magneticfield' and dict['deviceid'] == '62c7c4a8aa33b123':

        timenew_client_glass_magnetic = int(float(dict['clienttime']))
        if timeold_client_glass_magnetic != 0:
            coll_eval_client_glass_magnetic.append(timenew_client_glass_magnetic - timeold_client_glass_magnetic)
        timeold_client_glass_magnetic = timenew_client_glass_magnetic

for dict in all_dicts:
    #PHONE
    if dict['sensortype'] == 'accelerometer' and dict['deviceid'] == 'ddd830aa7d688be5':
        timenew_server_phone_accelerometer = int(float(dict['servertime']))
        if timeold_server_phone_accelerometer != 0 and (timenew_server_phone_accelerometer - timeold_server_phone_accelerometer) != 0:
            coll_eval_server_phone_accelerometer.append(timenew_server_phone_accelerometer - timeold_server_phone_accelerometer)
            coll_eval_difference_phone_accelerometer.append(timeold_server_phone_accelerometer-timeold_client_phone_accelerometer)
        timeold_server_phone_accelerometer = timenew_server_phone_accelerometer
        timeold_client_phone_accelerometer = int(float(dict['clienttime']))
        
    elif dict['sensortype'] == 'gyroscope' and dict['deviceid'] == 'ddd830aa7d688be5':
        timenew_server_phone_gyroscope = int(float(dict['servertime']))
        if timeold_server_phone_gyroscope != 0 and (timenew_server_phone_gyroscope - timeold_server_phone_gyroscope) != 0:
            coll_eval_server_phone_gyroscope.append(timenew_server_phone_gyroscope - timeold_server_phone_gyroscope)
            coll_eval_difference_phone_gyroscope.append(timeold_server_phone_gyroscope-timeold_client_phone_gyroscope)
        timeold_server_phone_gyroscope = timenew_server_phone_gyroscope
        timeold_client_phone_gyroscope = int(float(dict['clienttime']))
    
    elif dict['sensortype'] == 'magneticfield' and dict['deviceid'] == 'ddd830aa7d688be5':
        timenew_server_phone_magnetic = int(float(dict['servertime']))
        if timeold_server_phone_magnetic != 0 and (timenew_server_phone_magnetic - timeold_server_phone_magnetic) != 0:
            coll_eval_server_phone_magnetic.append(timenew_server_phone_magnetic - timeold_server_phone_magnetic)
            coll_eval_difference_phone_magnetic.append(timeold_server_phone_magnetic-timeold_client_phone_magnetic)
        timeold_server_phone_magnetic = timenew_server_phone_magnetic
        timeold_client_phone_magnetic = int(float(dict['clienttime']))

    #WATCH
    elif dict['sensortype'] == 'accelerometer' and dict['deviceid'] == 'f7c3857f13a0234f':
        timenew_server_watch_accelerometer = int(float(dict['servertime']))
        if timeold_server_watch_accelerometer != 0 and (timenew_server_watch_accelerometer - timeold_server_watch_accelerometer) != 0:
            coll_eval_server_watch_accelerometer.append(timenew_server_watch_accelerometer - timeold_server_watch_accelerometer)
            coll_eval_difference_watch_accelerometer.append(timeold_server_watch_accelerometer-timeold_client_watch_accelerometer)
        timeold_server_watch_accelerometer = timenew_server_watch_accelerometer
        timeold_client_watch_accelerometer = int(float(dict['clienttime']))

    elif dict['sensortype'] == 'gyroscope' and dict['deviceid'] == 'f7c3857f13a0234f':
        timenew_server_watch_gyroscope = int(float(dict['servertime']))
        if timeold_server_watch_gyroscope != 0 and (timenew_server_watch_gyroscope - timeold_server_watch_gyroscope) != 0:
            coll_eval_server_watch_gyroscope.append(timenew_server_watch_gyroscope - timeold_server_watch_gyroscope)
            coll_eval_difference_watch_gyroscope.append(timeold_server_watch_gyroscope-timeold_client_watch_gyroscope)
        timeold_server_watch_gyroscope = timenew_server_watch_gyroscope
        timeold_client_watch_gyroscope = int(float(dict['clienttime']))
   
    elif dict['sensortype'] == 'magneticfield' and dict['deviceid'] == 'f7c3857f13a0234f':
        timenew_server_watch_magnetic = int(float(dict['servertime']))
        if timeold_server_watch_magnetic != 0 and (timenew_server_watch_magnetic - timeold_server_watch_magnetic) != 0:
            coll_eval_server_watch_magnetic.append(timenew_server_watch_magnetic - timeold_server_watch_magnetic)
            coll_eval_difference_watch_magnetic.append(timeold_server_watch_magnetic-timeold_client_watch_magnetic)
        timeold_server_watch_magnetic = timenew_server_watch_magnetic
        timeold_client_watch_magnetic = int(float(dict['clienttime']))

    #GLASS
    elif dict['sensortype'] == 'accelerometer' and dict['deviceid'] == '62c7c4a8aa33b123':
        timenew_server_glass_accelerometer = int(float(dict['servertime']))
        if timeold_server_glass_accelerometer != 0 and (timenew_server_glass_accelerometer - timeold_server_glass_accelerometer) != 0:
            coll_eval_server_glass_accelerometer.append(timenew_server_glass_accelerometer - timeold_server_glass_accelerometer)
            coll_eval_difference_glass_accelerometer.append(timeold_server_glass_accelerometer-timeold_client_glass_accelerometer)
        timeold_server_glass_accelerometer = timenew_server_glass_accelerometer
        timeold_client_glass_accelerometer = int(float(dict['clienttime']))

    elif dict['sensortype'] == 'gyroscope' and dict['deviceid'] == '62c7c4a8aa33b123':
        timenew_server_glass_gyroscope = int(float(dict['servertime']))
        if timeold_server_glass_gyroscope != 0 and (timenew_server_glass_gyroscope - timeold_server_glass_gyroscope) != 0:
            coll_eval_server_glass_gyroscope.append(timenew_server_glass_gyroscope - timeold_server_glass_gyroscope)
            coll_eval_difference_glass_gyroscope.append(timeold_server_glass_gyroscope-timeold_client_glass_gyroscope)
        timeold_server_glass_gyroscope = timenew_server_glass_gyroscope
        timeold_client_glass_gyroscope = int(float(dict['clienttime']))

    elif dict['sensortype'] == 'magneticfield' and dict['deviceid'] == '62c7c4a8aa33b123':
        timenew_server_glass_magnetic = int(float(dict['servertime']))
        if timeold_server_glass_magnetic != 0 and (timenew_server_glass_magnetic - timeold_server_glass_magnetic) != 0:
            coll_eval_server_glass_magnetic.append(timenew_server_glass_magnetic - timeold_server_glass_magnetic)
            coll_eval_difference_glass_magnetic.append(timeold_server_glass_magnetic-timeold_client_glass_magnetic)
        timeold_server_glass_magnetic = timenew_server_glass_magnetic
        timenew_client_glass_magnetic = int(float(dict['clienttime']))

# Delete last Server Timestamp Difference due to buffer flush in the end
if (len(coll_eval_server_phone_accelerometer) != 0): del coll_eval_server_phone_accelerometer[-1]
if (len(coll_eval_server_phone_gyroscope) != 0): del coll_eval_server_phone_gyroscope[-1]
if (len(coll_eval_server_phone_magnetic) != 0): del coll_eval_server_phone_magnetic[-1]
if (len(coll_eval_server_watch_accelerometer) != 0): del coll_eval_server_watch_accelerometer[-1]
if (len(coll_eval_server_watch_gyroscope) != 0): del coll_eval_server_watch_gyroscope[-1]
if (len(coll_eval_server_watch_magnetic) != 0): del coll_eval_server_watch_magnetic[-1]
if (len(coll_eval_server_glass_accelerometer) != 0): del coll_eval_server_glass_accelerometer[-1]
if (len(coll_eval_server_glass_gyroscope) != 0): del coll_eval_server_glass_gyroscope[-1]
if (len(coll_eval_server_glass_magnetic) != 0): del coll_eval_server_glass_magnetic[-1]

# Show general statistics
print('----------------Number of Measurements-------------------------------------')
print ('Measurements for Phone Accelerometer: \t', len(coll_eval_client_phone_accelerometer) +1)
print ('Measurements for Phone Gyroscope: \t', len(coll_eval_client_phone_gyroscope) +1) 
print ('Measurements for Phone MagneticField: \t', len(coll_eval_client_phone_magnetic) +1)
print ('Measurements for Watch Accelerometer: \t', len(coll_eval_client_watch_accelerometer) +1)
print ('Measurements for Watch Gyroscope: \t', len(coll_eval_client_watch_gyroscope) +1)
print ('Measurements for Watch MagneticField: \t', len(coll_eval_client_watch_magnetic) +1)
print ('Measurements for Glass Accelerometer: \t', len(coll_eval_client_glass_accelerometer) +1)
print ('Measurements for Glass Gyroscope: \t', len(coll_eval_client_glass_gyroscope) +1)
print ('Measurements for Glass MagneticField: \t', len(coll_eval_client_glass_magnetic) +1)      
    

# 1. Show Evaluation Client Timestamps
plt.plot(coll_eval_client_phone_accelerometer)
plt.ylabel('timedifference in ms')
plt.title('Client Phone Accelerometer')
plt.savefig('Images/Client_Phone_Accelerometer.png')
plt.show()
plt.clf()

plt.plot(coll_eval_client_phone_gyroscope)
plt.ylabel('timedifference in ms')
plt.title('Client Phone Gyroscope')
plt.savefig('Images/Client_Phone_Gyroscope.png')
plt.show()
plt.clf()

plt.plot(coll_eval_client_phone_magnetic)
plt.ylabel('timedifference in ms')
plt.title('Client Phone MagneticField')
plt.savefig('Images/Client_Phone_MagneticField.png')
plt.show()
plt.clf()

plt.plot(coll_eval_client_watch_accelerometer)
plt.ylabel('timedifference in ms')
plt.title('Client Watch Accelerometer')
plt.savefig('Images/Client_Watch_Accelerometer.png')
plt.show()
plt.clf()

plt.plot(coll_eval_client_watch_gyroscope)
plt.ylabel('timedifference in ms')
plt.title('Client Watch Gyroscope')
plt.savefig('Images/Client_Watch_Gyroscope.png')
plt.show()
plt.clf()

plt.plot(coll_eval_client_watch_magnetic)
plt.ylabel('timedifference in ms')
plt.title('Client Watch MagneticField')
plt.savefig('Images/Client_Watch_MagneticField.png')
plt.show()
plt.clf()

plt.plot(coll_eval_client_glass_accelerometer)
plt.ylabel('timedifference in ms')
plt.title('Client Glass Accelerometer')
plt.savefig('Images/Client_Glass_Accelerometer.png')
plt.show()
plt.clf()

plt.plot(coll_eval_client_glass_gyroscope)
plt.ylabel('timedifference in ms')
plt.title('Client Glass Gyroscope')
plt.savefig('Images/Client_Glass_Gyroscope.png')
plt.show()
plt.clf()

plt.plot(coll_eval_client_glass_magnetic)
plt.ylabel('timedifference in ms')
plt.title('Client Glass MagneticField')
plt.savefig('Images/Client_Glass_MagneticField.png')
plt.show()
plt.clf()

print('----------------Client Timestamp Average------------------------------------------')
if (len(coll_eval_client_phone_accelerometer) != 0): print('Client Phone Accelerometer AVG: \t', (sum(coll_eval_client_phone_accelerometer)/float(len(coll_eval_client_phone_accelerometer))))
if (len(coll_eval_client_phone_gyroscope) != 0): print('Client Phone Gyroscope AVG: \t\t', (sum(coll_eval_client_phone_gyroscope)/float(len(coll_eval_client_phone_gyroscope))))
if (len(coll_eval_client_phone_magnetic) != 0): print('Client Phone MagneticField AVG: \t', (sum(coll_eval_client_phone_magnetic)/float(len(coll_eval_client_phone_magnetic))))
if (len(coll_eval_client_watch_accelerometer) != 0): print('Client Watch Accelerometer AVG: \t', (sum(coll_eval_client_watch_accelerometer)/float(len(coll_eval_client_watch_accelerometer))))
if (len(coll_eval_client_watch_gyroscope) != 0): print('Client Watch Gyroscope AVG: \t\t', (sum(coll_eval_client_watch_gyroscope)/float(len(coll_eval_client_watch_gyroscope))))
if (len(coll_eval_client_watch_magnetic) != 0): print('Client Watch MagneticField AVG: \t', (sum(coll_eval_client_watch_magnetic)/float(len(coll_eval_client_watch_magnetic))))
if (len(coll_eval_client_glass_accelerometer) != 0): print('Client Glass Accelerometer AVG: \t', (sum(coll_eval_client_glass_accelerometer)/float(len(coll_eval_client_glass_accelerometer))))
if (len(coll_eval_client_glass_gyroscope) != 0): print('Client Glass Gyroscope AVG: \t', (sum(coll_eval_client_glass_gyroscope)/float(len(coll_eval_client_glass_gyroscope))))
if (len(coll_eval_client_glass_magnetic) != 0): print('Client Glass MagneticField AVG: \t', (sum(coll_eval_client_glass_magnetic)/float(len(coll_eval_client_glass_magnetic))))

print('----------------Client Timestamp Variance------------------------------------------')
if (len(coll_eval_client_phone_accelerometer) != 0): print('Client Phone Accelerometer VAR: \t', (np.var(coll_eval_client_phone_accelerometer)))
if (len(coll_eval_client_phone_gyroscope) != 0): print('Client Phone Gyroscope VAR: \t\t', (np.var(coll_eval_client_phone_gyroscope)))
if (len(coll_eval_client_phone_magnetic) != 0): print('Client Phone MagneticField VAR: \t', (np.var(coll_eval_client_phone_magnetic)))
if (len(coll_eval_client_watch_accelerometer) != 0): print('Client Watch Accelerometer VAR: \t', (np.var(coll_eval_client_watch_accelerometer)))
if (len(coll_eval_client_watch_gyroscope) != 0): print('Client Watch Gyroscope VAR: \t\t', (np.var(coll_eval_client_watch_gyroscope)))
if (len(coll_eval_client_watch_magnetic) != 0): print('Client Watch MagneticField VAR: \t', (np.var(coll_eval_client_watch_magnetic)))
if (len(coll_eval_client_glass_accelerometer) != 0): print('Client Glass Accelerometer VAR: \t', (np.var(coll_eval_client_glass_accelerometer)))
if (len(coll_eval_client_glass_gyroscope) != 0): print('Client Glass Gyroscope VAR: \t', (np.var(coll_eval_client_glass_gyroscope)))
if (len(coll_eval_client_glass_magnetic) != 0): print('Client Glass MagneticField VAR: \t', (np.var(coll_eval_client_glass_magnetic)))


# 2. Show Evaluation Server Timestamps
plt.plot(coll_eval_server_phone_accelerometer)
plt.ylabel('timedifference in ms')
plt.title('Server Phone Accelerometer')
plt.savefig('Images/Server_Phone_Accelerometer.png')
plt.clf()

plt.plot(coll_eval_server_phone_gyroscope)
plt.ylabel('timedifference in ms')
plt.title('Server Phone Gyroscope')
plt.savefig('Images/Server_Phone_Gyroscope.png')
plt.clf()

plt.plot(coll_eval_server_phone_magnetic)
plt.ylabel('timedifference in ms')
plt.title('Server Phone MagneticField')
plt.savefig('Images/Server_Phone_MagneticField.png')
plt.clf()

plt.plot(coll_eval_server_watch_accelerometer)
plt.ylabel('timedifference in ms')
plt.title('Server Watch Accelerometer')
plt.savefig('Images/Server_Watch_Accelerometer.png')
plt.clf()

plt.plot(coll_eval_server_watch_gyroscope)
plt.ylabel('timedifference in ms')
plt.title('Server Watch Gyroscope')
plt.savefig('Images/Server_Watch_Gyroscope.png')
plt.clf()

plt.plot(coll_eval_server_watch_magnetic)
plt.ylabel('timedifference in ms')
plt.title('Server Watch MagneticField')
plt.savefig('Images/Server_Watch_MagneticField.png')
plt.clf()

plt.plot(coll_eval_server_glass_accelerometer)
plt.ylabel('timedifference in ms')
plt.title('Server Glass Accelerometer')
plt.savefig('Images/Server_Glass_Accelerometer.png')
plt.clf()

plt.plot(coll_eval_server_glass_gyroscope)
plt.ylabel('timedifference in ms')
plt.title('Server Glass Gyroscope')
plt.savefig('Images/Server_Glass_Gyroscope.png')
plt.clf()

plt.plot(coll_eval_server_glass_magnetic)
plt.ylabel('timedifference in ms')
plt.title('Server Glass MagneticField')
plt.savefig('Images/Server_Glass_MagneticField.png')
plt.clf()

print('----------------Server Timestamp Average------------------------------------------')
if (len(coll_eval_server_phone_accelerometer) != 0): print('Server Phone Accelerometer AVG: \t', (sum(coll_eval_server_phone_accelerometer)/float(len(coll_eval_server_phone_accelerometer))))
if (len(coll_eval_server_phone_gyroscope) != 0): print('Server Phone Gyroscope AVG: \t\t', (sum(coll_eval_server_phone_gyroscope)/float(len(coll_eval_server_phone_gyroscope))))
if (len(coll_eval_server_phone_magnetic) != 0): print('Server Phone MagneticField AVG: \t', (sum(coll_eval_server_phone_magnetic)/float(len(coll_eval_server_phone_magnetic))))
if (len(coll_eval_server_watch_accelerometer) != 0): print('Server Watch Accelerometer AVG: \t', (sum(coll_eval_server_watch_accelerometer)/float(len(coll_eval_server_watch_accelerometer))))
if (len(coll_eval_server_watch_gyroscope) != 0): print('Server Watch Gyroscope AVG: \t\t', (sum(coll_eval_server_watch_gyroscope)/float(len(coll_eval_server_watch_gyroscope))))
if (len(coll_eval_server_watch_magnetic) != 0): print('Server Watch MagneticField AVG: \t', (sum(coll_eval_server_watch_magnetic)/float(len(coll_eval_server_watch_magnetic))))
if (len(coll_eval_server_glass_accelerometer) != 0): print('Server Glass Accelerometer AVG: \t', (sum(coll_eval_server_glass_accelerometer)/float(len(coll_eval_server_glass_accelerometer))))
if (len(coll_eval_server_glass_gyroscope) != 0): print('Server Glass Gyroscope AVG: \t', (sum(coll_eval_server_glass_gyroscope)/float(len(coll_eval_server_glass_gyroscope))))
if (len(coll_eval_server_glass_magnetic) != 0): print('Server Glass MagneticField AVG: \t', (sum(coll_eval_server_glass_magnetic)/float(len(coll_eval_server_glass_magnetic))))

print('----------------Server Timestamp Variance------------------------------------------')
if (len(coll_eval_server_phone_accelerometer) != 0): print('Server Phone Accelerometer VAR: \t', (np.var(coll_eval_server_phone_accelerometer)))
if (len(coll_eval_server_phone_gyroscope) != 0): print('Server Phone Gyroscope VAR: \t\t', (np.var(coll_eval_server_phone_gyroscope)))
if (len(coll_eval_server_phone_magnetic) != 0): print('Server Phone MagneticField VAR: \t', (np.var(coll_eval_server_phone_magnetic)))
if (len(coll_eval_server_watch_accelerometer) != 0): print('Server Watch Accelerometer VAR: \t', (np.var(coll_eval_server_watch_accelerometer)))
if (len(coll_eval_server_watch_gyroscope) != 0): print('Server Watch Gyroscope VAR: \t\t', (np.var(coll_eval_server_watch_gyroscope)))
if (len(coll_eval_server_watch_magnetic) != 0): print('Server Watch MagneticField VAR: \t', (np.var(coll_eval_server_watch_magnetic)))
if (len(coll_eval_server_glass_accelerometer) != 0): print('Server Glass Accelerometer VAR: \t', (np.var(coll_eval_server_glass_accelerometer)))
if (len(coll_eval_server_glass_gyroscope) != 0): print('Server Glass Gyroscope VAR: \t', (np.var(coll_eval_server_glass_gyroscope)))
if (len(coll_eval_server_glass_magnetic) != 0): print('Server Glass MagneticField VAR: \t', (np.var(coll_eval_server_glass_magnetic)))

# 3. Evaluate Timedifference Client Server
plt.plot(coll_eval_difference_phone_accelerometer)
plt.ylabel('timedifference in ms')
plt.title('Difference Phone Accelerometer')
plt.savefig('Images/Difference_Phone_Accelerometer.png')
plt.clf()

plt.plot(coll_eval_difference_phone_gyroscope)
plt.ylabel('timedifference in ms')
plt.title('Difference Phone Gyroscope')
plt.savefig('Images/Difference_Phone_Gyroscope.png')
plt.clf()

plt.plot(coll_eval_difference_phone_magnetic)
plt.ylabel('timedifference in ms')
plt.title('Difference Phone MagneticField')
plt.savefig('Images/Difference_Phone_MagneticField.png')
plt.clf()

plt.plot(coll_eval_difference_watch_accelerometer)
plt.ylabel('timedifference in ms')
plt.title('Difference Watch Accelerometer')
plt.savefig('Images/Difference_Watch_Accelerometer.png')
plt.clf()

plt.plot(coll_eval_difference_watch_gyroscope)
plt.ylabel('timedifference in ms')
plt.title('Difference Watch Gyroscope')
plt.savefig('Images/Difference_Watch_Gyroscope.png')
plt.clf()

plt.plot(coll_eval_difference_watch_magnetic)
plt.ylabel('timedifference in ms')
plt.title('Difference Watch MagneticField')
plt.savefig('Images/Difference_Watch_MagneticField.png')
plt.clf()

plt.plot(coll_eval_difference_glass_accelerometer)
plt.ylabel('timedifference in ms')
plt.title('Difference Glass Accelerometer')
plt.savefig('Images/Difference_Glass_Accelerometer.png')
plt.clf()

plt.plot(coll_eval_difference_glass_gyroscope)
plt.ylabel('timedifference in ms')
plt.title('Difference Glass Gyroscope')
plt.savefig('Images/Difference_Glass_Gyroscope.png')
plt.clf()

plt.plot(coll_eval_difference_glass_magnetic)
plt.ylabel('timedifference in ms')
plt.title('Difference Glass MagneticField')
plt.savefig('Images/Difference_Glass_MagneticField.png')
plt.clf()

print('----------------difference Timestamp Average------------------------------------------')
if (len(coll_eval_difference_phone_accelerometer) != 0): print('Difference Phone Accelerometer AVG: \t', (sum(coll_eval_difference_phone_accelerometer)/float(len(coll_eval_difference_phone_accelerometer))))
if (len(coll_eval_difference_phone_gyroscope) != 0): print('Difference Phone Gyroscope AVG: \t', (sum(coll_eval_difference_phone_gyroscope)/float(len(coll_eval_difference_phone_gyroscope))))
if (len(coll_eval_difference_phone_magnetic) != 0): print('Difference Phone MagneticField AVG: \t', (sum(coll_eval_difference_phone_magnetic)/float(len(coll_eval_difference_phone_magnetic))))
if (len(coll_eval_difference_watch_accelerometer) != 0): print('Difference Watch Accelerometer AVG: \t', (sum(coll_eval_difference_watch_accelerometer)/float(len(coll_eval_difference_watch_accelerometer))))
if (len(coll_eval_difference_watch_gyroscope) != 0): print('Difference Watch Gyroscope AVG: \t', (sum(coll_eval_difference_watch_gyroscope)/float(len(coll_eval_difference_watch_gyroscope))))
if (len(coll_eval_difference_watch_magnetic) != 0): print('Difference Watch MagneticField AVG: \t', (sum(coll_eval_difference_watch_magnetic)/float(len(coll_eval_difference_watch_magnetic))))
if (len(coll_eval_difference_glass_accelerometer) != 0): print('Difference Glass Accelerometer AVG: \t', (sum(coll_eval_difference_glass_accelerometer)/float(len(coll_eval_difference_glass_accelerometer))))
if (len(coll_eval_difference_glass_gyroscope) != 0): print('Difference Glass Gyroscope AVG: \t', (sum(coll_eval_difference_glass_gyroscope)/float(len(coll_eval_difference_glass_gyroscope))))
if (len(coll_eval_difference_glass_magnetic) != 0): print('Difference Glass MagneticField AVG: \t', (sum(coll_eval_difference_glass_magnetic)/float(len(coll_eval_difference_glass_magnetic))))

print('----------------difference Timestamp Variance------------------------------------------')
if (len(coll_eval_difference_phone_accelerometer) != 0): print('Difference Phone Accelerometer VAR: \t', (np.var(coll_eval_difference_phone_accelerometer)))
if (len(coll_eval_difference_phone_gyroscope) != 0): print('Difference Phone Gyroscope VAR: \t', (np.var(coll_eval_difference_phone_gyroscope)))
if (len(coll_eval_difference_phone_magnetic) != 0): print('Difference Phone MagneticField VAR: \t', (np.var(coll_eval_difference_phone_magnetic)))
if (len(coll_eval_difference_watch_accelerometer) != 0): print('Difference Watch Accelerometer VAR: \t', (np.var(coll_eval_difference_watch_accelerometer)))
if (len(coll_eval_difference_watch_gyroscope) != 0): print('Difference Watch Gyroscope VAR: \t', (np.var(coll_eval_difference_watch_gyroscope)))
if (len(coll_eval_difference_watch_magnetic) != 0): print('Difference Watch MagneticField VAR: \t', (np.var(coll_eval_difference_watch_magnetic)))
if (len(coll_eval_difference_glass_accelerometer) != 0): print('Difference Glass Accelerometer VAR: \t', (np.var(coll_eval_difference_glass_accelerometer)))
if (len(coll_eval_difference_glass_gyroscope) != 0): print('Difference Glass Gyroscope VAR: \t', (np.var(coll_eval_difference_glass_gyroscope)))
if (len(coll_eval_difference_glass_magnetic) != 0): print('Difference Glass MagneticField VAR: \t', (np.var(coll_eval_difference_glass_magnetic)))