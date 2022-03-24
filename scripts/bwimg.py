import cv2 
import os
import numpy as np
#libs imported

imagePath = r"C:\Users\gabri\Desktop\bebo\img\0.png"
#path to image

originalImage = cv2.imread(imagePath)
#to read image into array on opencv

grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
#to gray out the image, so we can use the binary threshold

(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
#binary threshold to generate black and white image

imageInvertedBitwise = cv2.bitwise_not(blackAndWhiteImage)
#get binary values and invert them to generate sharper images 

cv2.imshow('Colored Image', originalImage)
cv2.imshow('Gray Image', grayImage)
cv2.imshow('BW Image', blackAndWhiteImage)
cv2.imshow('BW Inverted', imageInvertedBitwise)
#show both images

cv2.waitKey(0)
cv2.destroyAllWindows()
#terminates windows after keypress from user