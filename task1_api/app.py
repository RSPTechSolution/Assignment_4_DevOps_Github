from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/api")
def api():
    with open("D:/FullStackDeveloper/DevOps/Python/Assignment_3_DevOps_flask/task1_api/data.json", "r") as file:
        data = json.load(file)
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=5001, debug=True)