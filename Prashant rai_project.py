# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 17:42:41 2021

@author: dell
"""


import cv2
import numpy as np
#taking the input
image= cv2.imread(r"C:/Users/dell/Desktop/red.jpeg",1)

#definig the LIGHTS AS CURRENT STATE AS FALSE
RED =False
YELLOW =False
GREEN= False

#converting the image to hsv 
img = cv2.cvtColor (image,cv2.COLOR_BGR2HSV)
font = cv2.FONT_HERSHEY_COMPLEX
 
#gray
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#masking the blue color so that the there is no falacy i the detection of the circle
mask_blue= cv2.inRange(img, (110,50,50), (130,255,255))
res_blue = cv2.bitwise_and(img, img,mask=mask_blue)
blue_gray =cv2.cvtColor(res_blue,cv2.COLOR_BGR2GRAY)
cv2.imshow("DIP",blue_gray)

#threshing
_,thresh = cv2.threshold(gray, 25, 50,cv2.THRESH_BINARY)
cv2.imshow("DIP",thresh)

#we have use here the cv2.RETR_EXTERNAL  so that to find the exxternal contours of the systen
contours , hierachy = cv2.findContours(thresh, cv2.RETR_EXTERNAL  , cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

#approx function so that the precise contours can be defined 
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.003*cv2.arcLength(cnt,True), True)
    print(len(approx)) 
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    
   # here we have find the rectangle which is blue
    if(len(approx) == 4 and image[y,x,0]>128 and image[y,x,0]<= 255 and image[y,x,1]<127 and image[y,x,2]<127 ) :
         cv2.drawContours(image, [approx], -1, (255,255,0),2)
         print(len(approx))
    #priting the array of the rectangle 
         print([approx])
         
         #here we have find out coordinates of the rectangle
         P = (approx[0][0][0],approx[0][0][1]) 
         Q = (approx[1][0][0] ,approx[1][0][1])
         R = (approx[2][0][0] ,approx[2][0][1])         
         S = (approx[3][0][0] ,approx[3][0][1])         
         print(P,Q,R,S)
         
         # taking out the minimum and maximum coordinate of the blue rectangle
         x_min = approx[0][0][0]
         y_min = approx[0][0][1]
         x_max = approx[2][0][0]
         y_max = approx[2][0][1]
         print(x_min, y_min)
         print(x_max , y_max )
         
         #we have print the rectangle so that we can know how much blue rectangle are there but according to our situation there is only one
         cv2.putText(image,"Rectangle", (x,y), font, 0.75, (125,125,255),2)

#now we have detected the circles
detected_circle = cv2.HoughCircles(blue_gray, cv2.HOUGH_GRADIENT ,1,24 ,param1 =50,param2 = 22, minRadius= 0,maxRadius = 0)
num = len(detected_circle[0])
print(num)
a=0
while(num>a):
    
    # now we have find the center of the circle as houghcircle return center and radius
    X = detected_circle[0][a][0]
    Y = detected_circle[0][a][1]
    X = int(X)
    Y = int(Y)
    print((X,Y))
    
    
    #the circle on which the operation to be perfomed should be in the range of blue rectangle 
    if(X>x_min and X<x_max and Y<y_max and Y>y_min):
         print( "enterd inside the rectangle")
         
         # showing the color of the coordinate  one  by one of the circle 
         print(image[Y,X])
         if(image[Y,X,0]<50 and image[Y,X,1]<50 and image[Y,X,2]>190):
              RED = True
              print("passed1")
         elif(image[Y,X,0]<127 and image[Y,X,1]>128 and image[Y,X,1]<=255 and image[Y,X,2]>128 and image[Y,X,2]<=255):
              YELLOW = True
              print("passed2")
         elif(image[Y,X,0]<50 and image[Y,X,1]>180 and image[Y,X,2]<50):
              GREEN = True
              print("passed3")
    a=a+1 
 #drawing the boundary of the circle to just see that where the circles are drawing     
detected_circle = np.uint16(np.around(detected_circle))
for i in detected_circle[0,:]:
             #draw the outer circle 
     cv2.circle(image, (i[0],i[1]), i[2], (250,250,0),3)
             # draw the center of the circle
     cv2.circle(image,(i[0],i[1]),2,(0,0,255),3)  
if(RED == True and YELLOW == False and GREEN == False):
            print("RED")
elif(RED == False and YELLOW == True and GREEN == False):
            print("YELLOW")
elif(RED == False and YELLOW == False and GREEN == True):
            print("GREEN")
else:
            print("ERROR!!!!!!!!!")                 

cv2.imshow("image",image)
cv2.imshow("gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
