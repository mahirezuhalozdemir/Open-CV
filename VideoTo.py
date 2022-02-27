import cv2
import time
videoname="Video.mp4"
#video içe aktarma capture olarak geçer ve cap olarak kısaltılır
#capture=yakalamak
cap=cv2.VideoCapture(videoname)
print("width: ",cap.get(3))
#get fonksiyonunun 3.indeksi genişliği verir
print("heigth: ",cap.get(4))
#get fonksiyonunun 4.indeksi yüksekliği verir

if cap.isOpened()== False:
    print("error")

while True:
    ret, frame=cap.read()
 #read fonksiyonu bize 2 değer döndürür
#frame, videonun içindeki her bir resim
#return,videonun dönüp dönmediğini döndürür
    if ret==True:
        time.sleep(0.20)
        cv2.imshow("video", frame)
    else:
        break
    if cv2.waitKey(1) &0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


