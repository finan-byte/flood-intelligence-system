from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "RainGuard AI Backend is running",
        "system": "SIH26071"
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "online",
        "system": "RainGuard AI"
    })


if __name__ == "__main__":
    app.run(debug=True)
