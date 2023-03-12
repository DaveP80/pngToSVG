import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r"C:\Users\example\Downloads\example.png", 1)
# Loading the image
#resize image with fractions
half = cv2.resize(image, (0, 0), fx = 0.33, fy = 0.33)
bigger = cv2.resize(image, (900, 900))
 
stretch_near = cv2.resize(image, (500, 500),
               interpolation = cv2.INTER_LINEAR)
 
 
Titles =["Original", "Half", "Bigger", "Interpolation Nearest"]
images =[image, half, bigger, stretch_near]
count = 4
 
for i in range(count):
    plt.subplot(2, 2, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])
 
plt.show()