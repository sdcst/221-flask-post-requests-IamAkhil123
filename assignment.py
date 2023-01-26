#!python
from flask import Flask, request, render_template
from flask_cors import CORS
import random
import time, json

web = Flask(__name__)
CORS(web)

def textfile():
    quotes = ["My unmatched perspicacity coupled with sheer indefatigability makes me a feared opponent in any realm of human endeavor.", "The truth is crazy in a world full of lies", ]
    file = open("quotes.txt", "w")
    for i in quotes:
        i +="\n"
        file.write(i)

@web.route("/",methods=['POST','GET'])
def main():
    #sample url: http://127.0.0.1:5000/
    #output: a text string literal, includes information for help
    #response is not json encoded
    file = open("entry.txt", "r")
    quotes = file.readlines()
    quote = random.choice(quotes)
    return f"As once said, '{quote}'"
    
@web.route("/admin",methods=['POST','GET'])
def admin():
    #sample url: http://127.0.0.1:5000/
    #output: a text string literal, includes information for help
    #response is not json encoded\
    global file
    file = open('entry.txt', 'r')
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
    #sample url: http://127.0.0.1:5000/
    #output: a text string literal, includes information for help
    #response is not json encoded\
    file = open("entry.txt", "r")
    quotes = file.readlines()
    count = -1
    for line in quotes:
        count += 1
        quotes = list(quotes)
        quote = [item.split('\n')[0] for item in quotes]
    return quote

@web.route("/newquotes",methods=['POST','GET'])
def newquote():
    #sample url: http://127.0.0.1:5000/
    #output: a text string literal, includes information for help
    #response is not json encoded\
    file = open("entry.txt", "r")
    quotes = file.readlines()
    new_data = request.form
    new_data = dict(new_data)
    if new_data['val1'] not in quotes:
        with open('entry.txt', 'a') as i:
            i.write(f"{new_data['val1']}\n")
            return "addition a success"
    else:
        print("Already entered")

textfile()
web.run()   