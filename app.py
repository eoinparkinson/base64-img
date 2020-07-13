import base64
import requests
from flask import Flask, request
import time

app = Flask(__name__)

#Basic image url to base64 (working)
@app.route("/api/v1/img-base64")
def home():
    if 'url' in request.args:
        try:

            url = str(request.args['url'])
            time.sleep(2)
            return base64.b64encode(requests.get(url).content)
        except:
            return "Error: Invalid url. Url must be a direct link to image."
    else:
        return "Error: No url field provided. Please specify a url using ?url=www.your-url-here.com"

#Taking in two lists, and outputting a graph in image base64 format.
@app.route("/api/v1/graph-img")
def graphImage():
    if "xVal" and "yVal" in request.args:
        try:
            tmpXVal = str(request.args['xVal'])
            tmpYVal = str(request.args['yVal'])
            return ("xVal = " + tmpXVal + " and yVal = " + tmpYVal)
        except:
            return "Error: This is the 'except' issue."
    else:
        return "Error: No parameters provided."





if __name__ == "__main__":
    app.run()
