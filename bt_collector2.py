import serial
import io
from pymongo import MongoClient
import datetime

dbclient = MongoClient('localhost', 27017)
db = dbclient.squiggledoobs
recordings = db.recordings



def main():
    ser = serial.Serial('COM11', 115200, timeout=5)
    sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
    
    while(True):
        activity_v = sio.readline()
        if activity_v != "":
            try:
                recording = {
                        'timestamp' : (datetime.datetime.now() - datetime.datetime(1970,1,1)).total_seconds(),
                        'activity_v' : int(activity_v),
                        'device_id' : 1
                    }
                print recordings.insert_one(recording)
            except:
                print 'bt signal error or db insert error'
        
if __name__ == '__main__':
    main()
    