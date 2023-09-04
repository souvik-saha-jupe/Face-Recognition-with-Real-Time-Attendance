import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://faceattendancerealtime-fa778-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Souvik Saha",
            "major": "Power Engg",
            "starting_year": 2021,
            "total_attendance": 17,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2023-09-04 19:25:21"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "126454":
        {
            "name": "Bob Dylan",
            "major": "Music",
            "starting_year": 2020,
            "total_attendance": 4,
            "standing": "C",
            "year": 3,
            "last_attendance_time": "2022-08-08 02:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)