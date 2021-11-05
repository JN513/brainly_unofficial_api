from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def index():
    return "Hello, World!"


@app.route("/repository", methods=["GET"])
def get_repository():
    return redirect("https://github.com/JN513/brainly_unofficial_api")


if __name__ == "__main__":
    if os.environ.get("ENV") == "development":
        port = int(os.environ.get("PORT", 5000))
        app.run(debug=True, host="0.0.0.0", port=port)
