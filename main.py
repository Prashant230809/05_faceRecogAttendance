import face_recognition
import cv2
import numpy as np
import datetime
import csv

video_capture = cv2.VideoCapture(0)
# Load known faces
# Use double backslashes or a single forward slash for directory separators
harrys_image = face_recognition.load_image_file("C:\\Users\\HP\\OneDrive\\Documents\\GitHub\\Python\\Projects\\05_faceRecogAttendance\\faces\\harry.jpg")
harry_encoding = face_recognition.face_encodings(harrys_image)[0]
rohan_image = face_recognition.load_image_file("C:\\Users\\HP\\OneDrive\\Documents\\GitHub\\Python\\Projects\\05_faceRecogAttendance\\faces\\rohan.jpg")
rohan_encoding = face_recognition.face_encodings(rohan_image)[0]

know_face_encoding = [harry_encoding, rohan_encoding]
known_face_names = ["Prashant ", "Rohan"]
# list of expected students
students = known_face_names.copy()
face_locations = []
face_encodings = []

# Get the current time
now = datetime.datetime.now()
current_date = now.strftime("%Y-%m-%d %H-%M-%S")

f = open(f"{current_date}.csv", "w+", newline="")
lnwriter = csv.writer(f)

while True:
    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # recognise faces
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(know_face_encoding, face_encoding)
        face_distance = face_recognition.face_distance(know_face_encoding, face_encoding)
        best_match_index = np.argmin(face_distance)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # add the name 
        if name in known_face_names:
            font = cv2.FONT_HERSHEY_SIMPLEX
            bottonLeftCornerOfText = (10, 100)
            fontScale = 1.5
            fontColor = (255, 0, 0)
            thickness = 3
            lineType = 2

            cv2.putText(frame, name + "Present", bottonLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)

            if name in students:
                students.remove(name)
                current_time = now.strftime("%H-%M-%S")
                lnwriter.writerow([name, current_time])

        cv2.imshow("Attendance", frame)
        if cv2.waitKey(1) & 0xff == ord("q"):
            break

video_capture.release()
cv2.destroyAllWindows()
f.close()