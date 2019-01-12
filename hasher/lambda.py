import hashlib
import json

def calculate_hash(data):
    to_return = {}
    to_return['sha1'] = hashlib.sha1(data).hexdigest()
    to_return['sha256'] = hashlib.sha256(data).hexdigest()
    to_return['md5'] = hashlib.md5(data).hexdigest()
    return json.dumps(to_return)

def handler(event,context):
    fle = event
    strng = fle["string"]
    return calculate_hash(strng), 200