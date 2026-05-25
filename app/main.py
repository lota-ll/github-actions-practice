from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({"status": "ok", "host": socket.gethostname()})

@app.route("/health")
def health():
    return jsonify({"healthy": True})
