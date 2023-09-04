# Face-Recogntition-with-Real-Time-Attendance

This is a Face Recognition Software using Computer Vision. 
It marks the Realtime Attendance Marking using Firebase.
Use own firebase database links and tokens. Otherwise it will never work.

Anyone using the source code needs to download these follwoing python libraries for using this source code :
os
pickle
cv2
face_recognition
cvzone
numpy
firebase_admin
datetime

For marking the attendance 1 time in 24 hours(actual condition), one needs to update this code :
{if secondElapsed > 60: } to {if secondElapsed>86400} 

**Constraints :**
It can't predict which face is real image and which face is artificial(image shown on the camera)
