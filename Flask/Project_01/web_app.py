from flask import Flask, render_template 
from os import path 
print (path.isdir('./templates/'))

app = Flask(__name__)

@app.route('/')
def hello ():
    if path.isdir('./templates/'):
        return render_template('index.html')
    return "Hello_World_01"

app.run(debug=True)