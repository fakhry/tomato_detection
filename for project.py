import cv2
import numpy as np
img=cv2.imread("tom4.jpeg")   # Reading the image
img=cv2.resize(img,(512,512))   #Resizing the image
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #convert BGR to HSV

#########################################################

lower_red= np.array([0,50,50])  #hsv for lower range of red
upper_red = np.array([10,255,255]) #hsv for upper range of red
mask = cv2.inRange(hsv, lower_red, upper_red) # making mask
##################################################

lower_green= np.array([36,25,25])  #hsv for lower range of red
upper_green = np.array([80,255,255]) #hsv for upper range of red
mask1 = cv2.inRange(hsv, lower_green, upper_green) # making mask

##################################################
res_r = cv2.bitwise_and(img,img, mask= mask) # ِANDing the mask and the image to show the red only
res_g=cv2.bitwise_and(img,img, mask= mask1) # ANDِing the mask and the image to show the green only
tot=cv2.bitwise_or(res_r,res_g) # ORing res_r with res_g



cv2.imshow('',img)     #to show the real image
cv2.imshow('mask',mask)     #to show the mask
cv2.imshow('mask1',mask1)   #to show the mask
cv2.imshow('red only',res_r)   #to show the result of red only
cv2.imshow('green only',res_g)   #to show the result of green only
cv2.imshow("modified",tot)       #to show the result of ORing res_r with res_g
cv2.waitKey(0)
cv2.destroyAllWindows()