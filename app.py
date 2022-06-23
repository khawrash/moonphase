from flask import Flask, jsonify

app = Flask(__name__)

phase = {"phaseNumber": 1, "phaseName": "first quarter"}


@app.get("/phase")
def get_phase():
    return jsonify(phase)
