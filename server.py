from flask import Flask, request, redirect, render_template, json, g
from pymongo import MongoClient
from bson.json_util import dumps
from bson.code import Code
import datetime

dbclient = MongoClient('localhost', 27017)
db = dbclient.squiggledoobs
app = Flask(__name__)

agg = {
        0 : {
            'location' : (33.781799, -84.368374),
            'activity_v' : 0
            },
        1 : {
            'location' : (33.774839, -84.364906),
            'activity_v' : 0
            },
        2 : {
            'location' : (33.768096, -84.361430),
            'activity_v' : 0
            }
    }


@app.route('/')
def index():
    time_upper = (datetime.datetime.now() - datetime.datetime(1970,1,1))
    time_lower = (time_upper - datetime.timedelta(minutes = 10)).total_seconds()
    # recordings = db.recordings.find()
    recordings = db.recordings.find({'timestamp' : {'$gte' : time_lower}})
    for rec in recordings:
        agg[rec['device_id']]['activity_v'] += rec['activity_v']
    # print agg
    data = dumps(agg)
    # data[1]

    print data[1]
    return render_template('index.html', data=agg)



if __name__ == '__main__':
    app.run(debug=True)
