"""
This algorithm counts the number of houses from sattelite view map.
It takes an image and based upon the grey value of the houses, segmentation is done
After that, using findContour() function, it counts the number of contours/blobs
Test images in ./images folder
"""


import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread("images/map_snippet2.png", 0)
fig1 = plt.figure(1)
plt.imshow(img, 'gray')
plt.title("Gray scale image")

ret, thresh = cv2.threshold(img, 242, 255, cv2.THRESH_TOZERO_INV)   # every pixel below the threshold is turned white
ret, thresh_final = cv2.threshold(thresh, 240, 255, cv2.THRESH_TOZERO)  # every pixel below the threshold is turned black
# using the above 2 lines, we only took values in range [240, 242]

fig2 = plt.figure(2) 
plt.imshow(thresh_final, 'gray')
plt.title("After applying thresholding")

# applying morphological operaations to reduce noise
kernel = np.ones((3,3), np.uint8)
morph_img = cv2.erode(thresh_final, kernel, iterations=1)

fig3 = plt.figure(3)
plt.imshow(morph_img, 'gray')
plt.title("After applying morphological operations")

# applying canny edge detection and finding contours in the image
canny_img = cv2.Canny(morph_img, 254, 255)  # see readme for threshold detail
contours, hierarchy = cv2.findContours(canny_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contour_count = len(contours)

# using findContours() function to count the white blobs. 
# using this function on morph_img is better than using it on canny_img

blob, hierarchy = cv2.findContours(morph_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
blob_count = len(blob)


fig4 = plt.figure(4) 

plt.subplot(211)
plt.imshow(canny_img, 'gray')   # this will count the number of contours in the images
plt.xlabel("Count = " + str(contour_count))
plt.ylabel("Detecting # of contours")
plt.title("Comparing results od 2 different techniques")

plt.subplot(212)
plt.imshow(morph_img, 'gray')   # this will count the number of white blobs in the images
plt.xlabel("Count = " + str(blob_count))
plt.ylabel("Detecting # of blobs")


plt.show()

