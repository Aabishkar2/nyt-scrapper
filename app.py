from flask import Flask
from flask import jsonify 
from flask import request
from flask import render_template
from flask_cors import CORS
import json
from functions.NewYorkTimes import nyJson, contentGetter

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return nyJson()

@app.route("/content")
def content():
    return contentGetter()

if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0')