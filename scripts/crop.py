from glob import escape
import cv2
import numpy as np
import os

#tesseract obj
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

#path to image
pathToImage = r"C:\Users\gabri\Desktop\bebo\screenshots"

#saving path
pathToImageCropped = r"C:\Users\gabri\Desktop\bebo\img"

#to load list with entries from screenshot directory
imageList = [f for f in os.listdir(pathToImage) if f.endswith('.png')]

# print(imageList)

w=0

#iteration loop for items on list above
for i in imageList:

    img = cv2.imread(os.path.join(pathToImage, i))
    #to read image from dir

    croppedImage = img[1368:2097, 955:1377]
    # #array image to crop [height start:height finish, width start:width end]

    grayImage = cv2.cvtColor(croppedImage, cv2.COLOR_BGR2GRAY)
    #to gray out the image, so we can use the binary threshold

    (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
    #binary threshold to generate black and white image

    imageInvertedBitwise = cv2.bitwise_not(blackAndWhiteImage)
    #get binary values and invert them to generate sharper images
    
    cv2.imwrite(os.path.join(pathToImageCropped , str(w) +'.png'), imageInvertedBitwise)
    #write image to path

    w += 1
    #increase w counting by 1

