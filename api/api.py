import sys
import os

from flask import Flask, jsonify, request

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from interviews_calendar.calendar import Calendar

app = Flask(__name__)
interviews_calendar = Calendar()


@app.route('/interviews_calendar/heartbeat', methods=['GET'])
def heartbeat():
    """
    A dummy route to check if the endpoints is up or not!
    :return:
    """
    return jsonify({"who": 'Hello <3'})


@app.route('/interviews_calendar/admin/view-all', methods=['GET'])
def view_calendar():
    """
    The Admin may need to check the whole added slots with or whithout interviewee assigned to them!
    :return: all the slots added to the system so far
    """
    response = interviews_calendar.get_slots()
    return jsonify(response)


@app.route('/interviews_calendar/interviewee/available-times', methods=['GET', 'POST'])
def available_times():
    """
    the interviewee's interface through the interviewer's schedule, from where he/she can view and select a slot
    :return: return the assigned time or the whole available times
    """
    req = request.get_json()
    if request.method == 'GET':
        response = interviews_calendar.get_available_slots()
        return jsonify(response)

    elif request.method == 'POST':
        interviewee = req["interviewee"]
        slot_id = req["slot_id"]
        response = interviews_calendar.set_interview(interviewee=interviewee, slot_id=slot_id)
        return jsonify(response)


@app.route('/interviews_calendar/interviewer/add-slots', methods=['POST'])
def add_available_times():
    """
    Add valid slot for specific interviewers
    :return: the added slots at this moment
    """
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
    """
    Search function to view all the slots available in the given range
    :return: Objects which meet the given datetime time range
    """
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    response = interviews_calendar.search(start_date=start_date,
                                          end_date=end_date)
    return jsonify(response)


app.run(debug=False, port=8080, host='0.0.0.0')  # Running on http://0.0.0.0:8080/
