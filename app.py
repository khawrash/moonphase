from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

phase = {"phaseNumber": 1, "phaseName": "first quarter"}


@app.get("/phase")
def get_phase():
    return jsonify(phase)
