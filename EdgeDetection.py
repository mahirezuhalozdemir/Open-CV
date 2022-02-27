import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("london.jpg", 0)
"""
plt.figure()
plt.imshow(img, cmap="gray")
plt.axis("off")
"""

edges = cv2.Canny(image=img, threshold1=0, threshold2=255)
"""
plt.figure()
plt.imshow(edges, cmap="gray")
plt.axis("off")
"""
#alt ve üst threshold belirlerken medyan değeri ile belirli bir değer çarpılır. %67'si alınmış olur.
median_val= np.median(img)
print(median_val) #117

low= int(max(0,(1-0.33)*median_val))
high= int(min(255,(1+0.33)*median_val))

print(low) #78
print(high) #155

edges=cv2.Canny(image=img,threshold1=low, threshold2=high)
"""
plt.figure()
plt.imshow(edges, cmap="gray")
plt.axis("off")
"""
#blur
#kernel size artarsa bulanıklık artar
blurred_img= cv2.blur(img, ksize=(7,7))

plt.figure()
plt.imshow(edges, cmap="gray")
plt.axis("off")

edges=cv2.Canny(image=blurred_img, threshold1=low, threshold2=high)
plt.figure()
plt.imshow(edges, cmap="gray")
plt.axis("off")
