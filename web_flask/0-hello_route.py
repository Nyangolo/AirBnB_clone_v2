#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/airbnb-onepage/')
def hello():
    return 'Hello, this is the content served from /airbnb-onepage/'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

