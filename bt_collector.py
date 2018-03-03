import serial
import io
from pymongo import MongoClient
import datetime

dbclient = MongoClient('localhost', 27017)
db = dbclient.squiggledoobs
recordings = db.recordings


device_location_map = {
        0 : (33.781799, -84.368374),
        1 : (33.780853, -84.367591),
        2 : (33.780228, -84.367065)
    }


def main():
    ser = serial.Serial('COM9', 115200, timeout=5)
    sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
    
    while(True):
        device_id = sio.readline()
        if device_id != "":
            recording = {
                    'timestamp' : (datetime.datetime.now() - datetime.datetime(1970,1,1)).total_seconds(),
                    'device_id' : int(device_id),
                    'location' : device_location_map[int(device_id)]
                }
        
if __name__ == '__main__':
    main()
    