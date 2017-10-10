import csv
import json
import numpy as np
import matplotlib.pyplot as plt
from pymongo import MongoClient

#Connection to MongoDB with specified Collection
client = MongoClient('localhost', 27017)
db = client['test_database']
collection = 'Nancy-2017.09.30-18.35.54'

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

timeold_server_glass_magnetic = 0
timenew_server_glass_magnetic = 0
coll_eval_server_glass_magnetic = []

# Analyze Timestamps
for x in db[collection].find():
    dict = json.loads(''.join(map(str, x['session'])))
    
    #PHONE
    if dict['sensortype'] == 'accelerometer' and dict['deviceid'] == 'ddd830aa7d688be5':
        timenew_client_phone_accelerometer = int(float(dict['clienttime']))
        if timeold_client_phone_accelerometer != 0:
            coll_eval_client_phone_accelerometer.append(timenew_client_phone_accelerometer - timeold_client_phone_accelerometer)
        timeold_client_phone_accelerometer = timenew_client_phone_accelerometer

        timenew_server_phone_accelerometer = int(float(dict['servertime']))
        if timeold_server_phone_accelerometer != 0 and (timenew_server_phone_accelerometer - timeold_server_phone_accelerometer) != 0:
            coll_eval_server_phone_accelerometer.append(timenew_server_phone_accelerometer - timeold_server_phone_accelerometer)
        timeold_server_phone_accelerometer = timenew_server_phone_accelerometer

    elif dict['sensortype'] == 'gyroscope' and dict['deviceid'] == 'ddd830aa7d688be5':
        timenew_client_phone_gyroscope = int(float(dict['clienttime']))
        if timeold_client_phone_gyroscope != 0:
            coll_eval_client_phone_gyroscope.append(timenew_client_phone_gyroscope - timeold_client_phone_gyroscope)
        timeold_client_phone_gyroscope = timenew_client_phone_gyroscope

        timenew_server_phone_gyroscope = int(float(dict['servertime']))
        if timeold_server_phone_gyroscope != 0 and (timenew_server_phone_gyroscope - timeold_server_phone_gyroscope) != 0:
            coll_eval_server_phone_gyroscope.append(timenew_server_phone_gyroscope - timeold_server_phone_gyroscope)
        timeold_server_phone_gyroscope = timenew_server_phone_gyroscope
        
    elif dict['sensortype'] == 'magneticfield' and dict['deviceid'] == 'ddd830aa7d688be5':
        timenew_client_phone_magnetic = int(float(dict['clienttime']))
        if timeold_client_phone_magnetic != 0:
            coll_eval_client_phone_magnetic.append(timenew_client_phone_magnetic - timeold_client_phone_magnetic)
        timeold_client_phone_magnetic = timenew_client_phone_magnetic

        timenew_server_phone_magnetic = int(float(dict['servertime']))
        if timeold_server_phone_magnetic != 0 and (timenew_server_phone_magnetic - timeold_server_phone_magnetic) != 0:
            coll_eval_server_phone_magnetic.append(timenew_server_phone_magnetic - timeold_server_phone_magnetic)
        timeold_server_phone_magnetic = timenew_server_phone_magnetic

    #WATCH
    elif dict['sensortype'] == 'accelerometer' and dict['deviceid'] == 'f7c3857f13a0234f':
        timenew_client_watch_accelerometer = int(float(dict['clienttime']))
        if timeold_client_watch_accelerometer != 0:
            coll_eval_client_watch_accelerometer.append(timenew_client_watch_accelerometer - timeold_client_watch_accelerometer)
        timeold_client_watch_accelerometer = timenew_client_watch_accelerometer

        timenew_server_watch_accelerometer = int(float(dict['servertime']))
        if timeold_server_watch_accelerometer != 0 and (timenew_server_watch_accelerometer - timeold_server_watch_accelerometer) != 0:
            coll_eval_server_watch_accelerometer.append(timenew_server_watch_accelerometer - timeold_server_watch_accelerometer)
        timeold_server_watch_accelerometer = timenew_server_watch_accelerometer

    elif dict['sensortype'] == 'gyroscope' and dict['deviceid'] == 'f7c3857f13a0234f':
        timenew_client_watch_gyroscope = int(float(dict['clienttime']))
        if timeold_client_watch_gyroscope != 0:
            coll_eval_client_watch_gyroscope.append(timenew_client_watch_gyroscope - timeold_client_watch_gyroscope)
        timeold_client_watch_gyroscope = timenew_client_watch_gyroscope

        timenew_server_watch_gyroscope = int(float(dict['servertime']))
        if timeold_server_watch_gyroscope != 0 and (timenew_server_watch_gyroscope - timeold_server_watch_gyroscope) != 0:
            coll_eval_server_watch_gyroscope.append(timenew_server_watch_gyroscope - timeold_server_watch_gyroscope)
        timeold_server_watch_gyroscope = timenew_server_watch_gyroscope
        
    elif dict['sensortype'] == 'magneticfield' and dict['deviceid'] == 'f7c3857f13a0234f':
        timenew_client_watch_magnetic = int(float(dict['clienttime']))
        if timeold_client_watch_magnetic != 0:
            coll_eval_client_watch_magnetic.append(timenew_client_watch_magnetic - timeold_client_watch_magnetic)
        timeold_client_watch_magnetic = timenew_client_watch_magnetic

        timenew_server_watch_magnetic = int(float(dict['servertime']))
        if timeold_server_watch_magnetic != 0 and (timenew_server_watch_magnetic - timeold_server_watch_magnetic) != 0:
            coll_eval_server_watch_magnetic.append(timenew_server_watch_magnetic - timeold_server_watch_magnetic)
        timeold_server_watch_magnetic = timenew_server_watch_magnetic

    #GLASS
    elif dict['sensortype'] == 'accelerometer' and dict['deviceid'] == '62c7c4a8aa33b123':
        timenew_client_glass_accelerometer = int(float(dict['clienttime']))
        if timeold_client_glass_accelerometer != 0:
            coll_eval_client_glass_accelerometer.append(timenew_client_glass_accelerometer - timeold_client_glass_accelerometer)
        timeold_client_glass_accelerometer = timenew_client_glass_accelerometer

        timenew_server_glass_accelerometer = int(float(dict['servertime']))
        if timeold_server_glass_accelerometer != 0 and (timenew_server_glass_accelerometer - timeold_server_glass_accelerometer) != 0:
            coll_eval_server_glass_accelerometer.append(timenew_server_glass_accelerometer - timeold_server_glass_accelerometer)
        timeold_server_glass_accelerometer = timenew_server_glass_accelerometer

    elif dict['sensortype'] == 'magneticfield' and dict['deviceid'] == '62c7c4a8aa33b123':
        timenew_client_glass_magnetic = int(float(dict['clienttime']))
        if timeold_client_glass_magnetic != 0:
            coll_eval_client_glass_magnetic.append(timenew_client_glass_magnetic - timeold_client_glass_magnetic)
        timeold_client_glass_magnetic = timenew_client_glass_magnetic

        timenew_server_glass_magnetic = int(float(dict['servertime']))
        if timeold_server_glass_magnetic != 0 and (timenew_server_glass_magnetic - timeold_server_glass_magnetic) != 0:
            coll_eval_server_glass_magnetic.append(timenew_server_glass_magnetic - timeold_server_glass_magnetic)
        timeold_server_glass_magnetic = timenew_server_glass_magnetic

# Show general statistics
print('----------------Number of Measurements-------------------------------------')
print ('Measurements for Phone Accelerometer: \t', len(coll_eval_client_phone_accelerometer) +1)
print ('Measurements for Phone Gyroscope: \t', len(coll_eval_client_phone_gyroscope) +1) 
print ('Measurements for Phone MagneticField: \t', len(coll_eval_client_phone_magnetic) +1)
print ('Measurements for Watch Accelerometer: \t', len(coll_eval_client_watch_accelerometer) +1)
print ('Measurements for Watch Gyroscope: \t', len(coll_eval_client_watch_gyroscope) +1)
print ('Measurements for Watch MagneticField: \t', len(coll_eval_client_watch_magnetic) +1)
print ('Measurements for Glass Accelerometer: \t', len(coll_eval_client_glass_accelerometer) +1)
print ('Measurements for Glass MagneticField: \t', len(coll_eval_client_glass_magnetic) +1)      
    

# 1. Show Evaluation Client Timestamps
plt.plot(coll_eval_client_phone_accelerometer)
plt.ylabel('timedifference in ms')
plt.title('Client Phone Accelerometer')
plt.show()

plt.plot(coll_eval_client_phone_gyroscope)
plt.ylabel('timedifference in ms')
plt.title('Client Phone Gyroscope')
plt.show()

plt.plot(coll_eval_client_phone_magnetic)
plt.ylabel('timedifference in ms')
plt.title('Client Phone MagneticField')
plt.show()

plt.plot(coll_eval_client_watch_accelerometer)
plt.ylabel('timedifference in ms')
plt.title('Client Watch Accelerometer')
plt.show()

plt.plot(coll_eval_client_watch_gyroscope)
plt.ylabel('timedifference in ms')
plt.title('Client Watch Gyroscope')
plt.show()

plt.plot(coll_eval_client_watch_magnetic)
plt.ylabel('timedifference in ms')
plt.title('Client Watch MagneticField')
plt.show()

plt.plot(coll_eval_client_glass_accelerometer)
plt.ylabel('timedifference in ms')
plt.title('Client Glass Accelerometer')
plt.show()

plt.plot(coll_eval_client_glass_magnetic)
plt.ylabel('timedifference in ms')
plt.title('Client Glass MagneticField')
plt.show()

print('----------------Client Timestamp Average------------------------------------------')
if (len(coll_eval_client_phone_accelerometer) != 0): print('Client Phone Accelerometer AVG: \t', (sum(coll_eval_client_phone_accelerometer)/float(len(coll_eval_client_phone_accelerometer))))
if (len(coll_eval_client_phone_gyroscope) != 0): print('Client Phone Gyroscope AVG: \t\t', (sum(coll_eval_client_phone_gyroscope)/float(len(coll_eval_client_phone_gyroscope))))
if (len(coll_eval_client_phone_magnetic) != 0): print('Client Phone MagneticField AVG: \t', (sum(coll_eval_client_phone_magnetic)/float(len(coll_eval_client_phone_magnetic))))
if (len(coll_eval_client_watch_accelerometer) != 0): print('Client Watch Accelerometer AVG: \t', (sum(coll_eval_client_watch_accelerometer)/float(len(coll_eval_client_watch_accelerometer))))
if (len(coll_eval_client_watch_gyroscope) != 0): print('Client Watch Gyroscope AVG: \t\t', (sum(coll_eval_client_watch_gyroscope)/float(len(coll_eval_client_watch_gyroscope))))
if (len(coll_eval_client_watch_magnetic) != 0): print('Client Watch MagneticField AVG: \t', (sum(coll_eval_client_watch_magnetic)/float(len(coll_eval_client_watch_magnetic))))
if (len(coll_eval_client_glass_accelerometer) != 0): print('Client Glass Accelerometer AVG: \t', (sum(coll_eval_client_glass_accelerometer)/float(len(coll_eval_client_glass_accelerometer))))
if (len(coll_eval_client_glass_magnetic) != 0): print('Client Glass MagneticField AVG: \t', (sum(coll_eval_client_glass_magnetic)/float(len(coll_eval_client_glass_magnetic))))

print('----------------Client Timestamp Variance------------------------------------------')
if (len(coll_eval_client_phone_accelerometer) != 0): print('Client Phone Accelerometer VAR: \t', (np.var(coll_eval_client_phone_accelerometer)))
if (len(coll_eval_client_phone_gyroscope) != 0): print('Client Phone Gyroscope VAR: \t\t', (np.var(coll_eval_client_phone_gyroscope)))
if (len(coll_eval_client_phone_magnetic) != 0): print('Client Phone MagneticField VAR: \t', (np.var(coll_eval_client_phone_magnetic)))
if (len(coll_eval_client_watch_accelerometer) != 0): print('Client Watch Accelerometer VAR: \t', (np.var(coll_eval_client_watch_accelerometer)))
if (len(coll_eval_client_watch_gyroscope) != 0): print('Client Watch Gyroscope VAR: \t\t', (np.var(coll_eval_client_watch_gyroscope)))
if (len(coll_eval_client_watch_magnetic) != 0): print('Client Watch MagneticField VAR: \t', (np.var(coll_eval_client_watch_magnetic)))
if (len(coll_eval_client_glass_accelerometer) != 0): print('Client Glass Accelerometer VAR: \t', (np.var(coll_eval_client_glass_accelerometer)))
if (len(coll_eval_client_glass_magnetic) != 0): print('Client Glass MagneticField VAR: \t', (np.var(coll_eval_client_glass_magnetic)))


# 2. Show Evaluation Server Timestamps
plt.plot(coll_eval_server_phone_accelerometer)
plt.ylabel('timedifference in ms')
plt.title('Server Phone Accelerometer')
plt.show()

plt.plot(coll_eval_server_phone_gyroscope)
plt.ylabel('timedifference in ms')
plt.title('Server Phone Gyroscope')
plt.show()

plt.plot(coll_eval_server_phone_magnetic)
plt.ylabel('timedifference in ms')
plt.title('Server Phone MagneticField')
plt.show()

plt.plot(coll_eval_server_watch_accelerometer)
plt.ylabel('timedifference in ms')
plt.title('Server Watch Accelerometer')
plt.show()

plt.plot(coll_eval_server_watch_gyroscope)
plt.ylabel('timedifference in ms')
plt.title('Server Watch Gyroscope')
plt.show()

plt.plot(coll_eval_server_watch_magnetic)
plt.ylabel('timedifference in ms')
plt.title('Server Watch MagneticField')
plt.show()

plt.plot(coll_eval_server_glass_accelerometer)
plt.ylabel('timedifference in ms')
plt.title('Server Glass Accelerometer')
plt.show()

plt.plot(coll_eval_server_glass_magnetic)
plt.ylabel('timedifference in ms')
plt.title('Server Glass MagneticField')
plt.show()

print('----------------Server Timestamp Average------------------------------------------')
if (len(coll_eval_server_phone_accelerometer) != 0): print('Server Phone Accelerometer AVG: \t', (sum(coll_eval_server_phone_accelerometer)/float(len(coll_eval_server_phone_accelerometer))))
if (len(coll_eval_server_phone_gyroscope) != 0): print('Server Phone Gyroscope AVG: \t\t', (sum(coll_eval_server_phone_gyroscope)/float(len(coll_eval_server_phone_gyroscope))))
if (len(coll_eval_server_phone_magnetic) != 0): print('Server Phone MagneticField AVG: \t', (sum(coll_eval_server_phone_magnetic)/float(len(coll_eval_server_phone_magnetic))))
if (len(coll_eval_server_watch_accelerometer) != 0): print('Server Watch Accelerometer AVG: \t', (sum(coll_eval_server_watch_accelerometer)/float(len(coll_eval_server_watch_accelerometer))))
if (len(coll_eval_server_watch_gyroscope) != 0): print('Server Watch Gyroscope AVG: \t\t', (sum(coll_eval_server_watch_gyroscope)/float(len(coll_eval_server_watch_gyroscope))))
if (len(coll_eval_server_watch_magnetic) != 0): print('Server Watch MagneticField AVG: \t', (sum(coll_eval_server_watch_magnetic)/float(len(coll_eval_server_watch_magnetic))))
if (len(coll_eval_server_glass_accelerometer) != 0): print('Server Glass Accelerometer AVG: \t', (sum(coll_eval_server_glass_accelerometer)/float(len(coll_eval_server_glass_accelerometer))))
if (len(coll_eval_server_glass_magnetic) != 0): print('Server Glass MagneticField AVG: \t', (sum(coll_eval_server_glass_magnetic)/float(len(coll_eval_server_glass_magnetic))))

print('----------------Server Timestamp Variance------------------------------------------')
if (len(coll_eval_server_phone_accelerometer) != 0): print('Server Phone Accelerometer VAR: \t', (np.var(coll_eval_server_phone_accelerometer)))
if (len(coll_eval_server_phone_gyroscope) != 0): print('Server Phone Gyroscope VAR: \t\t', (np.var(coll_eval_server_phone_gyroscope)))
if (len(coll_eval_server_phone_magnetic) != 0): print('Server Phone MagneticField VAR: \t', (np.var(coll_eval_server_phone_magnetic)))
if (len(coll_eval_server_watch_accelerometer) != 0): print('Server Watch Accelerometer VAR: \t', (np.var(coll_eval_server_watch_accelerometer)))
if (len(coll_eval_server_watch_gyroscope) != 0): print('Server Watch Gyroscope VAR: \t\t', (np.var(coll_eval_server_watch_gyroscope)))
if (len(coll_eval_server_watch_magnetic) != 0): print('Server Watch MagneticField VAR: \t', (np.var(coll_eval_server_watch_magnetic)))
if (len(coll_eval_server_glass_accelerometer) != 0): print('Server Glass Accelerometer VAR: \t', (np.var(coll_eval_server_glass_accelerometer)))
if (len(coll_eval_server_glass_magnetic) != 0): print('Server Glass MagneticField VAR: \t', (np.var(coll_eval_server_glass_magnetic)))
