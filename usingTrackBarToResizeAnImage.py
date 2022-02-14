# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 17:41:25 2022

@author: Vineet Kumar Srivastava
"""
import cv2

windowName = "Resize Image"
trackbarValue = "Scale (001/100)"
trackbarType = "Type: \n 0: Scale Up \n 1: Scale Down (0/1)"

maxScaleUp = 100
scaleValue = 1
scaleType = 0
maxType = 1
scaleFactor = 1.0

# load an image
image = cv2.imread("truth.png")

# Create a window to display results
cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)

# Callback functions
def scaleTypeImage(*args):
    global scaleType
    global scaleValue
    global scaleFactor
    scaleType = args[0]
    
    #print("scale type:{}".format(scaleType))
    if scaleType == 1: # scale down
        #scaleImage(1)
        scaleFactor = 1 - scaleValue/100.0
    else: # scale up
        scaleFactor = 1 + scaleValue/100.0
    
    if scaleFactor ==0 :
        scaleFactor = 1
    
    scaledImage = cv2.resize(image, None, fx=scaleFactor,\
            fy = scaleFactor, interpolation = cv2.INTER_LINEAR)
    
    cv2.imshow(windowName, scaledImage)

def scaleImage(*args):
    global scaleValue
    global scaleType
    global scaleFactor
    
    scaleValue = args[0]
    
    #print("scale value:{}".format(scaleValue))
    if scaleType ==  1: # scale down
        scaleFactor = 1 - scaleValue/100.0
    else: # scale up
        scaleFactor = 1 + scaleValue/100.0
    
    if scaleFactor == 0:
        scaleFactor = 1
    
    scaledImage = cv2.resize(image, None, fx=scaleFactor,\
            fy = scaleFactor, interpolation = cv2.INTER_LINEAR)
    
    cv2.imshow(windowName, scaledImage)

scaleImage(1)    
cv2.createTrackbar(trackbarValue, windowName, scaleValue, maxScaleUp, scaleImage)
cv2.createTrackbar(trackbarType, windowName, scaleType, maxType, scaleTypeImage)


while True:
    c = cv2.waitKey(10)
    if c==27:
        break

cv2.destroyAllWindows()

