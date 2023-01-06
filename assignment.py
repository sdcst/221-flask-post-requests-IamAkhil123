#!python
from flask import Flask,request
from flask_cors import CORS
import json
import sqlite3
import random
app = Flask(__name__)
CORS(app)

@app.route("/going",methods=["POST"])
def postResponse():
    nop=True
    # a simple echo server that response with the payload received.
    payload = request.form
    print(request.form)
    print(payload)
    data = dict(payload)
    print(data)
    saf=data['get']
    if saf!='bce52a22495d704233dd4e720e942dbf63d0561ed813d77fd38776357db7108e':
        return 'incorect'
    file = 'quote.db'
    connection = sqlite3.connect(file)
    print(connection)

    cursor = connection.cursor()
    query = "select quote from customers"
    cursor.execute(query)
    result = cursor.fetchall()
    wild=[]
    for g in result:
        g=g[0]
        wild.append(g.split(' '))
    new=data['quote']
    new=new.split(',')
    nu=0
    for i in result:
        i=i[0]            
        if i in new:
            new.remove(i)
            nop==False
            che=False
        elif nop==True:
            che=True
    if che==True:
        for l in new:
            wild=new[nu].split(' ')
            x=len(wild)
            x=round(x/2)+random.randint(-1,1)
            if x>=len(wild):
                x=round(x/2)
            che=''.join(['%', f'{wild[1]}', '%'])
            w=wild[-1].split('-')
            che2=''.join(['%', f'{w[0]}', '%'])
            che3=''.join(['%', f'{wild[x]}', '%'])
            kil=0
            if che2==che3 or che==che2:
                queries=[che,che3]
            else:
                queries=[che,che2,che3]
            for j in queries:
                q = f"select * from customers where quote like '{j}'"
                r = cursor.execute(q)
                data = list(r)
                if data!=[]:
                    kil=kil+1
                print(j, data)
                if kil==2:
                    new.remove(l)
    data2 = [
        new
        ]
    if data2==[[]]:
        return'quote alredy in the system'
    for i in data2:
        i=i[0]
        query = f"insert into customers (quote) values ('{i}')" 
        print(query)
        cursor.execute(query)
    connection.commit()
    
    
    return json.dumps(data2)
@app.route("/",methods=['POST','GET'])
def main():
    return "hi"

app.run("0.0.0.0")