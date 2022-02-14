# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 12:16:55 2022

@author: Vineet Kumar Srivastava
"""
import cv2
import math

# Lists to store the points
top_left = []
bottom_right = []

def drawRectangle(action, x, y, flags, userdata):
  # Referencing global variables 
  global top_left, bottom_right
  
  # Action to be taken when left mouse button is pressed
  if action==cv2.EVENT_LBUTTONDOWN:
    print("Mouse Button Down pressed")
    top_left = [(x,y)]
    
  # Action to be taken when left mouse button is released
  elif action==cv2.EVENT_LBUTTONUP:
    print("Mouse button Up Pressed")
    bottom_right = [(x,y)]
    cv2.rectangle(source, top_left[0], bottom_right[0], (255, 0, 255), thickness=2, lineType=cv2.LINE_AA);
    cropped_image = source[top_left[0][1]:bottom_right[0][1], top_left[0][0]:bottom_right[0][0]]
    cv2.imshow("Cropped Image", cropped_image)
    cv2.imwrite("../data/images/face.jpg", cropped_image)
    
source = cv2.imread("../data/images/sample.jpg",1)

dummy = source.copy()

cv2.namedWindow("Window")

fontScale = 0.6
fontFace = cv2.FONT_HERSHEY_COMPLEX
fontColor = (255, 255, 255)
fontThickness = 1
text = "Choose top left corner, and drag,?"

# Get the text box height and width and also the baseLine
textSize, baseLine = cv2.getTextSize(text,fontFace,fontScale,fontThickness)
textWidth,textHeight = textSize

# highgui function called when mouse events occur
cv2.setMouseCallback("Window", drawRectangle)
k = 0
# loop until escape character is pressed
while k!=27 :
  
  cv2.imshow("Window", source)
  cv2.putText(source, text,
              (20,textHeight+10), cv2.FONT_HERSHEY_SIMPLEX, 
              0.6,(255,255,255), 1 );
  k = cv2.waitKey(20) & 0xFF


cv2.destroyAllWindows()

