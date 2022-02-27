import cv2

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)
# video kaydetme işlemi:
writer = cv2.VideoWriter("recording.mp4", cv2.VideoWriter_fourcc(*"DIVX"), 20,
                         (width, height))
# fourcc (sadece windows için),çerçeveleri sıkıştırmak için kullanılan 4 karakterli codec kodu
# 20, frame per second (her saniyede göreceğimiz resim sayısı)
# video okuma işlemi
while True:
    ret, frame = cap.read()
    cv2.imshow("video", frame)
    # save
    writer.write(frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
writer.release()
cv2.destroyAllWindows()


