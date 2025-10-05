import cv2
import numpy as np
import os
import pandas as pd
import face_recognition

# 读取人脸数据库
face_db_path = './face_recognition_images_db/face_db.xlsx'

if not os.path.exists(face_db_path):
    col_name = ['Name', 'Path'] + [str(i) for i in range(1, 129)]
    face_db = pd.DataFrame(columns=col_name)
    for root, _, files in os.walk('./face_recognition_images_db/train_db/'):
        for idx, file in enumerate(sorted(files)):
            face_db.loc[idx, 'Name'] = file.split('.')[0]
            tmp_path = os.path.join(root, file)
            face_db.loc[idx, 'Path'] = tmp_path
            tmp_img = cv2.imread(tmp_path)[:, :, ::-1]  # BGR to RGB
            tmp_face = face_recognition.face_locations(tmp_img)  # detect face area, hog & cnn
            tmp_face_encode = face_recognition.face_encodings(tmp_img, tmp_face)[0]
            face_db.loc[idx, '1':'128'] = np.array(tmp_face_encode)
    face_db.to_excel(face_db_path, index=False)
else:
    face_db = pd.read_excel(face_db_path)

# 打开摄像头
capture = cv2.VideoCapture(0)
if not capture.isOpened():
    raise IOError('Camera Open Error, Please Check...')

while True:
    ret, frame = capture.read()
    if not ret:
        break

    frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    frame_rgb = frame[:, :, ::-1]
    faces_loc = face_recognition.face_locations(frame_rgb)
    faces_encode = face_recognition.face_encodings(frame_rgb, faces_loc)

    for (top, right, bottom, left), face_encode in zip(faces_loc, faces_encode):
        matches = face_recognition.compare_faces(list(face_db.loc[:, '1':'128'].values), face_encode, tolerance=0.55)
        distances = face_recognition.face_distance(list(face_db.loc[:, '1':'128'].values), face_encode)
        min_distance_idx = np.argmin(distances)
        name = 'Unknown'
        if matches[min_distance_idx]:
            name = face_db.loc[min_distance_idx, 'Name']

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 3)
        cv2.rectangle(frame, (left, bottom - 30), (right, bottom), (0, 0, 255), 3)
        cv2.putText(frame, name, (left + 10, bottom - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255))

    cv2.imshow('Face Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
