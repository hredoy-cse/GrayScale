# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 12:50:22 2022

@author: hredoy
"""

import cv2
img = cv2.imread('baby.png', 0)
# shape prints the tuple (height,weight,channels)
row = img.shape[0]
print("Row = ", row)
col = img.shape[1]
print("Col = ", col)
totalPixel = row * col
print("Total Pixel = ", totalPixel)


# img will be a numpy array of the above shape

print("All pixel of image array = \n", img)
print("\n")
 
# finding constrast 

max1 = img.max()
print("Maximum pixel = ", max1)
min1 = img.min()
print("Minimum pixel = ", min1)
dif = max1 - min1
print("Contrast is = ", dif)

# finding Brightness

print("Sum of all pixel =",img.sum())        
print("Brightness is = ", img.sum() / totalPixel)