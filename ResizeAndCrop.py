import cv2
img=cv2.imread("original.jpg",1)
#1 renkli, 0 siyah-beyaz
print("boyut:",img.shape)
cv2.imshow("orijinal",img)

#resize işlemi
imgNew=cv2.resize(img,(800,800))
print("boyut:",imgNew.shape)
cv2.imshow("resize",imgNew)


#kırpma işlemi
imgCropped=img[:200,:300]
#200=yükseklik ve 300=genişlik
cv2.imshow("crop",imgCropped)
cv2.waitKey(0)