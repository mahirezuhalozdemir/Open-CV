import cv2
import matplotlib.pyplot as plt

cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    ret,frame=cap.read()
    if ret:
        face_rect=face_cascade.detectMultiScale(frame,minNeighbors=10)
        for (x, y, w, h) in face_rect:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 10)
        cv2.imshow("face detect",frame)
    if cv2.waitKey(1) & 0xFF ==ord("q"): break
cap.release()
cv2.destroyAllWindows()