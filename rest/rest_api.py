from flask import Flask
from flask import request
import json
import sys

version_api = "v0.1"
app = Flask(__name__)

@app.route("/api/" + version_api + "/profiling", methods=['GET'])
def profiling():
    return "OK"

@app.route("/api/" + version_api + "/alive", methods=['GET'])
def alive ():
    return "OK"

if __name__ == '__main__':

    app.run(debug=True)

