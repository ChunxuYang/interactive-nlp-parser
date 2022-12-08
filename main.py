from flask import Flask, request
# cors
from flask_cors import CORS
from extract import extract

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/extraction', methods=['POST'])
def extraction():
    # url is in body
    url = request.json['url']
    return extract(url).__dict__


if __name__ == '__main__':
    app.run()
