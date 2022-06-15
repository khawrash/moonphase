from flask import Flask, jsonify

app = Flask(__name__)

phase = [
    {"phase_number": 1, "phase_name": "first quarter"},
]


@app.get("/phase")
def get_phase():
    return jsonify(phase)
