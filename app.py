import base64
import requests
from flask import Flask, request

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


if __name__ == "__main__":
    app.run(debug=True)
