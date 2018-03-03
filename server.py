from flask import Flask, request, redirect, render_template, jsonify, g
from pymongo import MongoClient

dbclient = MongoClient('localhost', 27017)
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', data={})

if __name__ == '__main__':
    app.run(debug=True)