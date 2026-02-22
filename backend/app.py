from flask import Flask, request
from pymongo import MongoClient
import os

app = Flask(__name__)
client = MongoClient(os.getenv("MONGO_URI"))
db = client["todo_db"]
collection = db["todo_items"]

@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    item_name = request.form.get("itemName")
    item_desc = request.form.get("itemDescription")
    if not item_name or not item_desc:
        return "Missing data", 400
    collection.insert_one({"itemName": item_name, "itemDescription": item_desc})
    return "Item submitted successfully!"