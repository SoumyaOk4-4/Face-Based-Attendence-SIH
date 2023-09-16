import face_recognition
import cv2
import numpy as np
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

video_capture = cv2.VideoCapture(1)  # inbuild=0, webcam=1

CSE23_108_image = face_recognition.load_image_file("pictures/CSE23_108.jpg")
CSE23_108_encoding = face_recognition.face_encodings(CSE23_108_image)[0]

CSE23_96_image = face_recognition.load_image_file("pictures/CSE23_96.jpg")
CSE23_96_encoding = face_recognition.face_encodings(CSE23_96_image)[0]

CSE23_114_image = face_recognition.load_image_file("pictures/CSE23_114.jpg")
CSE23_114_encoding = face_recognition.face_encodings(CSE23_114_image)[0]

known_face_encoding = [
    CSE23_108_encoding,
    CSE23_96_encoding,
    CSE23_114_encoding,
]

known_faces_names = [
    "Soumya Chakraborty",
    "Ratul Mondal",
    "Debopriyo Dhar",
]

students = known_faces_names.copy()

face_locations = []
face_encodings = []
face_names = []
s = True

# Initialize the Google Sheets API
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json", scope
)
gc = gspread.authorize(credentials)

# Open the Google Sheet by its title
google_sheet_title = "techtetries team"  # Replace with your Google Sheet title
worksheet = gc.open(
    "techtetries team"
).sheet1  # Use the appropriate sheet name or index

while True:
    now = datetime.now()  # Get the current date and time
    current_date = now.strftime("%Y-%m-%d")  # Define the current date

    _, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations
        )
        face_names = []

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(
                known_face_encoding, face_encoding
            )
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]

            face_names.append(name)
            if name in known_faces_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 100)
                fontScale = 1.5
                fontColor = (255, 0, 0)
                thickness = 3
                lineType = 2

                cv2.putText(
                    frame,
                    name + " Present",
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    thickness,
                    lineType,
                )

                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H:%M:%S")
                    # Update the Google Sheet with attendance data
                    row_to_insert = [current_date, name, current_time]
                    worksheet.append_row(row_to_insert)

    cv2.imshow("Face Recognition Based Attendance System \t (Press 'q' To Exit)", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video_capture.release()
cv2.destroyAllWindows()
