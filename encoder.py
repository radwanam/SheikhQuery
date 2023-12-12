from flask import Flask, request, jsonify
from bson import ObjectId
import json

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return super().default(o)
