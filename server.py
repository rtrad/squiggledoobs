from flask import Flask, request, redirect, render_template, json, g
from pymongo import MongoClient
from bson.json_util import dumps
from bson.code import Code
import datetime

dbclient = MongoClient('localhost', 27017)
db = dbclient.squiggledoobs
app = Flask(__name__)

agg = {
        1 : {
            'location' : (33.7816899, -84.3683153),
            'activity_v' : 0,
            'count' : 0
            },
        2 : {
            'location' : (33.7806076, -84.3673886),
            'activity_v' : 0,
            'count' : 0
            },
        3 : {
            'location' : (33.7800137, -84.3668665),
            'activity_v' : 0,
            'count' : 0
            },
        4 : {
            'location' : (33.7794260, -84.3664867),
            'activity_v' : 0,
            'count' : 0
            },
        5 : {
            'location' : (33.7780078, -84.3657849),
            'activity_v' : 0,
            'count' : 0
            },
        6 : {
            'location' : (33.7744780, -84.3647942),
            'activity_v' : 0,
            'count' : 0
            }
    }


@app.route('/')
def index():
    # time_upper = (datetime.datetime.now() - datetime.datetime(1970,1,1))
    # time_lower = (time_upper - datetime.timedelta(minutes = 10)).total_seconds()
    time_lower = 1520084629.944

    # recordings = db.recordings.find()
    recordings = db.recordings.find({'timestamp' : {'$gte' : time_lower}})
    for rec in recordings:
        agg[rec['device_id']]['activity_v'] += rec['activity_v']**2
        agg[rec['device_id']]['count'] += 1

    # for dev in agg:
        # agg[dev]['activity_v'] = agg[dev]['activity_v']/agg[dev]['count']
    # print agg
    data = dumps(agg)
    # data[1]

    print (data[1])
    return render_template('index.html', data=agg)



if __name__ == '__main__':
    app.run(debug=True)
