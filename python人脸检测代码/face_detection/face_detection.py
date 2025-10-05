import cv2


def detect():
    face_cascade = cv2.CascadeClassifier("./cascades/haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier("./cascades/haarcascade_eye.xml")
    camera = cv2.VideoCapture(0)
    cv2.namedWindow("camera", cv2.WINDOW_NORMAL)  # 创建一个可调整大小的窗口
    cv2.resizeWindow("camera", 800, 600)  # 设置窗口的初始大小
    while True:
        ret, frame = camera.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y: y + h, x: x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.03, minNeighbors=5, minSize=(20, 20))
            for ex, ey, ew, eh in eyes:
                cv2.rectangle(frame, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)
                print("双眼位置",x,y,w,h)
        cv2.imshow("camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    camera.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    detect()
