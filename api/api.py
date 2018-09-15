from pathlib import Path

from flask import Flask, jsonify, request

ROOT_DIR = str(Path(__file__).parents[2])
app = Flask(__name__)  # define app using Flask


@app.route('/calendar/heartbeat', methods=['GET'])
def heartbeat():
    return jsonify({"who": 'Hello <3'})


@app.route('/calendar/available-times', methods=['GET'])
def available_times():
    query = request.args.get('q').lower().rstrip().lstrip()

    response = []

    return jsonify(response)


@app.route('/calendar/interviewer/add-slot', methods=['GET'])
def suggestions_club():
    query = request.args.get('q').lower().rstrip().lstrip()

    response = []

    return jsonify(response)


@app.route('/calendar/interviewee/choose-slot', methods=['GET'])
def suggestions_club():
    query = request.args.get('q').lower().rstrip().lstrip()

    response = []

    return jsonify(response)


@app.route('/calendar/search', methods=['GET'])
def suggestions_club():
    query = request.args.get('q').lower().rstrip().lstrip()

    response = []

    return jsonify(response)


app.run(debug=False, port=8080, host='0.0.0.0')
