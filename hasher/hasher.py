import hashlib
import flask
from flask import request, jsonify
import json

app = flask.Flask(__name__)

def calculate_hash(data):
    data = data.encode('utf-8')
    to_return = {}
    to_return['sha1'] = hashlib.sha1(data).hexdigest()
    to_return['sha256'] = hashlib.sha256(data).hexdigest()
    to_return['md5'] = hashlib.md5(data).hexdigest()
    return json.dumps(to_return)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hey!</p>"

@app.route('/api/v1/generate', methods=['POST'])
def read_req():
    fle = request.get_json(force=True)
    strng = fle["string"]
    return calculate_hash(strng), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0')