from flask import Flask, request
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world! running on %s' % request.host

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
