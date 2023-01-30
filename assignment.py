#!python
#221 flask-post-requests

from flask import Flask, request, render_template
from flask_cors import CORS
import random
import time, json

web = Flask(__name__)
CORS(web)

def textfile():
    quotes = ["Spread love everywhere you go. Let no one ever come to you without leaving happier.","When you reach the end of your rope, tie a knot in it and hang on.","Always remember that you are absolutely unique. Just like everyone else."]
    file = open("quotes.txt", "w")
    for i in quotes:
        i +="\n"
        file.write(i)

@web.route("/",methods=['POST','GET'])
def main():
    file = open("quotes.txt", "r")
    quotes = file.readlines()
    quote = random.choice(quotes)
    return f'{quote}'
    
@web.route("/admin",methods=['POST','GET'])
def admin():
    global file
    file = open('quotes.txt', 'r')
    def working():
        Lines = file.readlines()
        count = 0
        for line in Lines:
            count += 1
            if line == "":
                line.truncate()
            yield f"Quote {count}: '{line.strip()}'</br>"
    working()
    
    file2 = "https://code.jquery.com/jquery-3.6.1.js"
    file2 = file2.working()

@web.route("/new",methods=['POST','GET'])
def new():
    file = open("quotes.txt", "r")
    quotes = file.readlines()
    count = -1
    for line in quotes:
        count += 1
        quotes = list(quotes)
        quote = [item.split('\n')[0] for item in quotes]
    return quote

@web.route("/newquotes",methods=['POST','GET'])
def newquote():
    file = open("quotes.txt", "r")
    quotes = file.readlines()
    new_data = request.form
    new_data = dict(new_data)
    if new_data['val1'] not in quotes:
        with open('quotes.txt', 'a') as i:
            i.write(f"{new_data['val1']}\n")
            return "addition a success"
    else:
        print("Already entered")

textfile()
web.run()
