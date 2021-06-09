import json

def readJSON(path):
    f = open(path)
    return json.load(f)