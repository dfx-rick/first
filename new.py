import cv2
import numpy as np
import matplotlib.pylab as plt

img=cv2.imread('lanesample.jpg')
img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(img)
plt.show()

#Sample Code