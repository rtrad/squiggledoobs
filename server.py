from flask import Flask, request, redirect, render_template, json, g
from pymongo import MongoClient
from bson.json_util import dumps
import datetime

dbclient = MongoClient('localhost', 27017)
db = dbclient.squiggledoobs
app = Flask(__name__)


@app.route('/')
def index():
    time_upper = (datetime.datetime.now() - datetime.datetime(1970,1,1)).total_seconds()
    time_lower = time_upper - 30
    recordings = db.recordings.find({'timestamp' : {'$gte' : time_lower}})
    data = dumps(recordings)
    return render_template('index.html', data=data)
        


if __name__ == '__main__':
    app.run(debug=True)
    