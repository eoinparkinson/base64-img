import base64
import requests
from flask import Flask, request
import time
from urllib.parse import urlparse

app = Flask(__name__)

#Basic image url to base64 (working)
@app.route("/api/v1/img-base64")
def home():
    if 'url' in request.args:
        try:
            query = str(request.args['url'])
            #time.sleep(2)
            return base64.b64encode(requests.get(query).content)
        except:
            return "Error: Invalid url. Url must be a direct link to image."
    else:
        return "Error: No url field provided. Please specify a url using ?url=www.your-url-here.com"

#Taking in two lists, and outputting a graph in image base64 format.(in progress)
@app.route("/api/v1/graph-img")
def graphImage():
    tmpXVal = str(request.args.get("xVal"))
    tmpYVal = str(request.args.get("yVal"))
    tmpGraphType = str(request.args.get("graphType"))

    return (tmpXVal+tmpYVal+tmpGraphType)



if __name__ == "__main__":
    app.run(debug=True)
