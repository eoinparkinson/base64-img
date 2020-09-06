# Simple Python Flask App to output base64 of image url.

The files here are ready to deploy to Heroku.

There is only one query parameter, "url". The image url must be a direct link to the image, and publically accessible. 

Endpoint would look like ```/api/v1/img-base64?url=[your-url-here]```

Python libraries used:
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [base-64](https://docs.python.org/3/library/base64.html)
* [requests](https://requests.readthedocs.io/en/master/)

This is free to use for everyone, enjoy :)
