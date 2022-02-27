import cv2
#computer vision
#open cv kütüphanesi
#resmi içe aktarma
image=cv2.imread("picture.jpg",0)
#0 = grayscale
cv2.imshow("ilk_resim",image)
k=cv2.waitKey(0) &0xFF
if k==27:
    cv2.destroyAllWindows()
elif k==ord('q'):
    cv2.imWrite("picture.png",image)
    cv2.destroyAllWindows()