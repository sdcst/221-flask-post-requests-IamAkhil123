#!python3
import random as r 
from flask import Flask, request
from flask_cors import CORS
import time, json 
import random 

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def main():
    x = random.randint(0)
    file = 'quotes.txt'
    t = open(file, 'r')
    data = t.read()
    mydata = data.split('\n')
    a = mydata[x]
    return a 

@app.route("?/admin", methods=["POST"])
def admin():
    t = open('quotes.txt', 'r')
    data = t.read()
    mydata = data.split('\n')
    return mydata
app.run()   

