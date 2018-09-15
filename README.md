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
│   ├── available-times [GET]
│   └── available-times [POST]
│
└── admin/
    └── view-all [GET]
```

## How to use
### 1) Interviewer
The Interviewer can post a slot, in which he/she has time to interview somebody in!

|                    Route                 | Method | Parameters | 
|------------------------------------------|----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|/interviews_calendar/interviewer/add-slots|POST|{"interviewers": list of strings, the names of the interviewers, "interviewee": string(optional field) the name of the interviewee, "start_times": list of strings, the datetime of the available times}|
#### Examples:
##### POST Request sample
```http request
curl -X POST \
  http://0.0.0.0:8080/interviews_calendar/interviewer/add-slots \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{"interviewers": ["Morgan", "Geni mardoc", "JC-Quillet"], "start_times": ["12-1-2017 22:30", "01-01-2018 10:30"]}'
```
##### POST Response example
```json
[
    {
        "end_time": "Friday 2017-12-01 from 23:30:00.",
        "interviewee": "",
        "interviewers": [
            "Morgan",
            "Geni mardoc",
            "JC-Quillet"
        ],
        "start_time": "Friday 2017-12-01 from 22:30:00."
    },
    {
        "end_time": "Monday 2018-01-01 from 11:30:00.",
        "interviewee": "",
        "interviewers": [
            "Morgan",
            "Geni mardoc",
            "JC-Quillet"
        ],
        "start_time": "Monday 2018-01-01 from 10:30:00."
    }
]
```

###2) Interviewee
The Interviewee can view all the available slots (slots which no candidate took yet), and he/she can pick one to have an interview in.


| Route | Method | Parameters |
|------------------------------------------------|----|----------------------------------------------------------------------------------------------------------------------------------------|
|/interviews_calendar/interviewee/available-times|GET |-|
|/interviews_calendar/interviewee/available-times|POST|{"interviewee": interviewee name, "slot_id": id of the time slot (consider that it's the zero-based array slot from the previous route)}|
#### Examples:
##### GET Request sample
```http request
curl -X GET \
  http://0.0.0.0:8080/interviews_calendar/interviewee/available-times \
  -H 'cache-control: no-cache'
```
##### GET Response example
```json
[
    {
        "end_time": "Friday 2017-12-01 from 23:30:00.",
        "interviewee": "",
        "interviewers": [
            "Morgan",
            "Geni mardoc",
            "JC-Quillet"
        ],
        "start_time": "Friday 2017-12-01 from 22:30:00."
    },
    {
        "end_time": "Monday 2018-01-01 from 11:30:00.",
        "interviewee": "",
        "interviewers": [
            "Morgan",
            "Geni mardoc",
            "JC-Quillet"
        ],
        "start_time": "Monday 2018-01-01 from 10:30:00."
    }
]
```
##### POST Request sample
```http request
curl -X POST \
  http://0.0.0.0:8080/interviews_calendar/interviewee/available-times \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
	"interviewee": "interviewee name :)",
	"slot_id": 1
}'
```
##### POST Response example
```json
{
    "end_time": "Monday 2018-01-01 from 11:30:00.",
    "interviewee": "interviewee name :)",
    "interviewers": [
        "Morgan",
        "Geni mardoc",
        "JC-Quillet"
    ],
    "start_time": "Monday 2018-01-01 from 10:30:00."
}
```

###3) System Admin
The system Admin can view all the slots scheduled on the calender so far.

| Route | Method | Parameters | 
|-----------------------------------|---|-|
|/interviews_calendar/admin/view-all|GET|-|
#### Examples:
##### GET Request sample
```http request
curl -X GET \
  http://0.0.0.0:8080/interviews_calendar/admin/view-all \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json'
```
##### GET Response example
```Json
[
    {
        "end_time": "Friday 2017-12-01 from 23:30:00.",
        "interviewee": "",
        "interviewers": [
            "Morgan",
            "Geni mardoc",
            "JC-Quillet"
        ],
        "start_time": "Friday 2017-12-01 from 22:30:00."
    },
    {
        "end_time": "Monday 2018-01-01 from 11:30:00.",
        "interviewee": "interviewee name :)",
        "interviewers": [
            "Morgan",
            "Geni mardoc",
            "JC-Quillet"
        ],
        "start_time": "Monday 2018-01-01 from 10:30:00."
    }
]
```

###4) All
Anybody can search for the added slots in the calendar in a specific time frame

| Route | Method | Parameters | 
|---------------------------|---|-|
|/interviews_calendar/search|GET|-|

#### Examples:
##### GET Request sample
```http request
curl -X GET \
  'http://0.0.0.0:8080/interviews_calendar/search?start_date=01-01-2018-10:30&end_date=05-05-2018-10:30' \
  -H 'cache-control: no-cache' \
```
##### GET Response example
```json
[
    {
        "end_time": "Monday 2018-01-01 from 11:30:00.",
        "interviewee": "",
        "interviewers": [
            "Morgan",
            "Geni mardoc",
            "JC-Quillet"
        ],
        "start_time": "Monday 2018-01-01 from 10:30:00."
    }
]
```
