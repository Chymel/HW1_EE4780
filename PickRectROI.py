# Name: Carson Hymel
# Email: chyme21@lsu.edu
# Assignment: HW_1
# Due Date: 2/27/2022
# Class: EE 4780
# Professor: Dr. Xin Li

import cv2
import numpy as np
import argparse

ix, iy = -1, -1
# mouse callback function
# For more mouse event types, check https://docs.opencv.org/3.1.0/d7/dfc/group__highgui.html#ga927593befdddc7e7013602bca9b079b0
# For more drawing functions, check https://docs.opencv.org/3.1.0/dc/da5/tutorial_py_drawing_functions.html
refPt = []
def draw_rect(event, x, y, flags, param):
    global ix, iy, refPt
    if event == cv2.EVENT_LBUTTONDOWN:
        ix, iy = x, y
        refPt = [(x, y)]

    elif event == cv2.EVENT_LBUTTONUP:
        # try to drag the mouse before you release the left button
        ix, iy = x, y
        refPt.append((x, y))
        cv2.rectangle(param, refPt[0], refPt[1], (0,255,0), 2)



# Create a black image, a window and bind the function to window.  
img = cv2.imread('TestImages/2.baby.jpg')


# It is a good idea to first clone this image, 
# so that your drawing will not contaminate the original image
cloneImg = img.copy()

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_rect, cloneImg)

o = 0
while (1):
    cv2.imshow('image',cloneImg)
    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        print(ix, iy)

    if k == ord('c') or k == ord('C') or o == 1:
        print("C pressed")
        o = 1
        jx = cloneImg.shape[0]
        jy = cloneImg.shape[1]
        g = np.zeros([jx, jy], dtype='uint8')
        cv2.rectangle(g, refPt[0], refPt[1], (255, 255, 255), -1)
        if k == ord('h') or k == ord('H'):
            #cv2.rectangle(cloneImg, refPt[0], refPt[1], (255, 255, 255), -1)
            R, G, B = cv2.split(img)

            output1_R = cv2.equalizeHist(R)
            output1_G = cv2.equalizeHist(G)
            output1_B = cv2.equalizeHist(B)
            deltaJ = cv2.merge((output1_R, output1_G, output1_B))
            deltaJ = cv2.bitwise_and(img, deltaJ, mask = g)
            cloneImg = cv2.addWeighted(cloneImg, 1.0, deltaJ, 1.0, 0.0)
            print("H pressed")
            o = 0

    if k == ord('q'):
        break;

cv2.destroyAllWindows()

