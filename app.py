from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB Atlas connection
mongo_uri = os.environ.get("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["student_db"]
collection = db["students"]

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        # Insert into MongoDB
        collection.insert_one({
            "name": name,
            "email": email
        })

        return redirect(url_for('success'))

    except Exception as e:
        # Show error on same page
        return render_template('form.html', error=str(e))
    
# MongoDB Atlas connection
client = MongoClient(os.getenv("MONGO_URI"))
db = client["todo_db"]
collection = db["todo_items"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get("itemName")
    item_desc = request.form.get("itemDescription")

    if not item_name or not item_desc:
        return jsonify({"error": "Missing fields"}), 400

    collection.insert_one({"itemName": item_name, "itemDescription": item_desc})
    return "Item submitted successfully!"

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)