#!python3
from flask import Flask, request
from flask_cors import CORS
import time, json

app = Flask(__name__)   
CORS(app)               

@app.route("/",methods=['POST','GET'])
def main():
    return "Hello World (use /help endpoint for a list of options)"

@app.route("/post",methods=['POST'])
def postData():
    data = request.form
    data = dict(data)
    if 'greeting' not in data:
        data['greeting'] = "Hello!"
    return json.dumps(data)


@app.route("/help",methods=['GET','POST'])
def help():
    return """
    Acceptable endpoints: 
    /     : General
    /help : this page
    /html : html result
    /getData: a GET method only endpoint
    /json : a POST method only endpoint that takes a json payload
    """

@app.route("/html",methods=['GET'])
def html():
    return "<h1>Hello World</h1>"

@app.route("/getData")
def getData():
    x = request.args
    output = dict(x)
    output['title'] = "This is a response from a GET request"
    return json.dumps(output)

@app.route("/json",methods=['POST'])
def jsondata():
    output = {
        "greeting" : "Hello World",
        "success" : 100,
        "timestamp" : time.time()
    }
    x = request.form
    x = dict(x)
    output['payload'] = x
    return json.dumps(output)

app.run()           
