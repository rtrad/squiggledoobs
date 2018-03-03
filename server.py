from flask import Flask, request, redirect, render_template, json, g
from pymongo import MongoClient

dbclient = MongoClient('localhost', 27017)
db = dbclient.squiggledoobs
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', data=[{ 'device_id' : 0, 'location' : (80,80), 'people' : 40, 'timestamp' : 1520046817}])
    
# @app.route('/api/data/', methods = ['POST'])
# def add_data():
    


if __name__ == '__main__':
    app.run(debug=True)