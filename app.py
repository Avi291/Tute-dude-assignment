from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

app = Flask(__name__)

# 🔗 MongoDB Atlas connection
# mongo_uri = os.environ.get("MONGO_URI")
client = MongoClient("mongodb+srv://aniruddhakspeed17_db_user:qCqTvVV1eG9CYssO@cluster0.eoodxzw.mongodb.net/?appName=Cluster0")
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

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)