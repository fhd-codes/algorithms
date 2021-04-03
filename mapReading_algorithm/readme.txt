
About algorithm
================
This algorithm counts the number of houses from sattelite view map.
It takes an image and based upon the grey value of the houses, segmentation is done
After that, using findContour() function, it counts the number of contours/blobs
Test images in ./images folder




Info. (copied from interet)
======
Canny does use two thresholds (upper and lower):

1- If a pixel gradient is higher than the upper threshold, the pixel is accepted as an edge
2- If a pixel gradient value is below the lower threshold, then it is rejected.
3- If the pixel gradient is between the two thresholds, then it will be accepted only if it is connected to a pixel that is above the upper threshold.


Canny recommended a upper:lower ratio between 2:1 and 3:1.