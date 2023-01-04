#!python3
from flask import Flask,request
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)

@app.route("/post",methods=["POST"])
def postResponse():
    # a simple echo server that response with the payload received.
    payload = request.form
    data = dict(payload)
    print(data)
    return json.dumps(data)

app.run()




import requests

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, json = myobj)

#print the response text (the content of the requested file):

print(x.text)

