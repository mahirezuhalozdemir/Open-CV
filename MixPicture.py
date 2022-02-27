import cv2
import matplotlib.pyplot as plt
img1 = cv2.imread("picture.jpg")
#BGR- RGB'YE ÇEVİR
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread("picture2.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

print(img1.shape)
print(img2.shape)
img1=cv2.resize(img1, (600, 600))
img2=cv2.resize(img1, (600, 600))

#karıştırılmış resim
#alpha* img1 + beta*img2
blended = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.5, gamma=0)
plt.figure()
plt.imshow(blended)
cv2.waitKey()
cv2.destroyAllWindows()