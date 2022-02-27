import cv2
import numpy as np
img=np.zeros((512,512,3),np.uint8)
# a canvas
#print(img.shape)
#cv2.imshow("siyah",img)

#add a line
cv2.line(img,(0,0),(512,512),(0,255,0),3)
#picture:start point,end point,colour,thick
#open cv = BGR(blue,green,red)
#cv2.imshow("line",img)


#add a rectangle
cv2.rectangle(img,(0,0),(256,256),(255,0,0),3,cv2.FILLED)
#picture:start point,end point,colour,thick,filled
#cv2.imshow("rectangle",img)

#add a circle
cv2.circle(img,(300,300),45,(0,0,255),cv2.FILLED)
#cv2.imshow("circle",img)
#picture: center,radius,colour

cv2.putText(img,"image",(350,350),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
#picture: start point,font,thick,colour
cv2.imshow("text",img)
cv2.waitKey(0)
