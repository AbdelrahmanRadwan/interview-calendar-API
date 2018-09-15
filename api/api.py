from pathlib import Path

from interviews_calendar.calendar import Calendar

from flask import Flask, jsonify, request

ROOT_DIR = str(Path(__file__).parents[2])
app = Flask(__name__)

interviews_calendar = Calendar()


@app.route('/interviews_calendar/heartbeat', methods=['GET'])
def heartbeat():
    return jsonify({"who": 'Hello <3'})


@app.route('/interviews_calendar/admin/view-all', methods=['GET'])
def view_calendar():
    response = interviews_calendar.get_slots()
    return jsonify(response)


@app.route('/interviews_calendar/interviewee/available-times', methods=['GET', 'POST'])
def available_times():
    req = request.get_json()
    if request.method == 'GET':
        response = interviews_calendar.get_available_slots()
        print(response)
        return jsonify(response)

    elif request.method == 'POST':
        interviewee = req["interviewee"]
        slot_id = req["slot_id"]
        response = interviews_calendar.set_interview(interviewee=interviewee, slot_id=slot_id)
        return jsonify(response)


@app.route('/interviews_calendar/interviewer/add-slots', methods=['POST'])
def add_available_times():
    req = request.get_json()
    interviewers = req["interviewers"]
    interviewee = req.get("interviewee") or ""
    start_times = req["start_times"]

    added_slots = interviews_calendar.add_slots(interviewers=interviewers,
                                                interviewee=interviewee,
                                                start_times=start_times)
    response = added_slots

    return jsonify(response)


@app.route('/interviews_calendar/search', methods=['GET'])
def search():
    req = request.get_json()
    start_date = req["start_date"]
    end_date = req["end_date"]

    response = interviews_calendar.search(start_date=start_date,
                                          end_date=end_date)
    print(response)
    return jsonify(response)



app.run(debug=False, port=8080, host='0.0.0.0')
