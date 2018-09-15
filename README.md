# interview-calendar-API.

## How to Run
- Install the requirements
```
pip3 install -r requirements.txt
```
- Run the Endpoint
```
python3 api/api.py
```

📖 API Documentation
================
## Routes Design
Route based URL: http://0.0.0.0:8080/
```
interviews_calendar/
├── search/
│   └── [GET]
│  
├── interviewer/
│   └── add-slots [POST]
│
├── heartbeat/
│   └── [GET]
│
├── interviewee/
│   ├── available-times: [GET]
│   └── available-times [POST]
│
└── admin/
    └── view-all [GET]
```

## How to use
1) Interviewer
The Interviewer can post a slot, in which he/she has time to interview somebody in!

| Route | Method | Parameters | 
|-------|--------|------------|
|/interviews_calendar/interviewer/add-slots|POST|{"interviewers": list of strings, the names of the interviewers, "interviewee": string(optional field) the name of the interviewee, "start_times": list of strings, the datetime of the available times}|
### Example:
```
curl -X POST \
  http://0.0.0.0:8080/interviews_calendar/interviewer/add-slots \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 379c5e98-6a15-b2f6-0ed7-9e8acad73dbb' \
  -d '{"interviewers": ["Morgan", "Geni mardoc", "JC-Quillet"], "start_times": ["12-1-2017 22:30", "01-01-2018 10:30"]}'
```


2) Interviewee
The Interviewee can view all the available slots (slots which no candidate took yet), and he/she can pick one to have an interview in.


| Route | Method | Parameters |
|-------|--------|------------|
|/interviews_calendar/interviewee/available-times|GET|-|
|/interviews_calendar/interviewee/available-times|POST|{"interviewee": interviewee name, "slot_id": id of the time slot (consider that it's the zero-based array slot from the previous route)}|
### Examples:
#### GET
```

```
#### POST
```

```

3) System Admin
The system Admin can view all the slots scheduled on the calender so far.

| Route | Method | Parameters | Example | 
|-------|--------|------------|---------|
|/interviews_calendar/admin/view-all|GET|-|curl -X GET http://0.0.0.0:8080/interviews_calendar/admin/view-all|

4) All
Anybody can search for the added slots in the calendar in a specific time frame

| Route | Method | Parameters | Example | 
|-------|--------|------------|---------|
|/interviews_calendar/search|GET|{"start_date": string represents the datetime of the range start, "end_date": string represents the datetime of the range end}|curl -X GET http://0.0.0.0:8080/interviews_calendar/search |
