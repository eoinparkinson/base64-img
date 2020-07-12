import base64
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/api/v1/img-base64")
def home():
    if 'url' in request.args:
        try:

            url = str(request.args['url'])
            return base64.b64encode(requests.get(url).content)
        except:
            return "Error: Invalid url. Url must be a direct link to image."
    else:
        return "Error: No url field provided. Please specify a url using ?url=www.your-url-here.com"



if __name__ == "__main__":
    app.run()
