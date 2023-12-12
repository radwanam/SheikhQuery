from flask import Flask, request, jsonify
from pymongo import *
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/cardbase"
mongo = PyMongo(app)
client = MongoClient('localhost', 27017)
db = client["your_database_name"]
laymancollection = db['laymanenglish']

def search():
    data = request.get_json()
    query = data.get("query", "")

    results = laymancollection.find({"$text": {"$search": query}})

    search_results = []
    for result in results:

        search_results.append({
            "title": result.get("title"),
            "description": result.get("description"),
            "url": result.get("url"),
        })

    return jsonify(search_results)


