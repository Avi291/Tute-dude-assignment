from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/api')
def get_data():
    # Read data from backend file
    with open('data.json', 'r') as file:
        data = json.load(file)

    # Return JSON response
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)