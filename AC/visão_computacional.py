# -*- coding: utf-8 -*-
"""Visão computacional.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KjBwaNLMdmvwLlQLEIDzkhtio2bsGkvP
"""

# Commented out IPython magic to ensure Python compatibility.
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import Image

# %matplotlib inline

# Read image as gray scale.
img_hand = cv2.imread("foto.jpeg", 0)

# Set color map to gray scale for proper rendering.
plt.imshow(img_hand, cmap="gray")
print(img_hand)

# print the first pixel of the first black box
print(img_hand[0, 0])
# print the first white pixel to the right of the first black box
print(img_hand[0, 6])

# Read in image
mao = cv2.imread("foto.jpeg", 1)

# print the size  of image
print("Image size (H, W, C) is:", mao.shape)

# print data-type of image
print("Data type of image is:", mao.dtype)

plt.imshow(mao)

# Split the image into the B,G,R components
img_NZ_bgr = cv2.imread("foto.jpeg", cv2.IMREAD_COLOR)
b, g, r = cv2.split(img_NZ_bgr)

# Show the channels
plt.figure(figsize=[20, 5])

plt.subplot(141);plt.imshow(r, cmap="gray");plt.title("Red Channel")
plt.subplot(142);plt.imshow(g, cmap="gray");plt.title("Green Channel")
plt.subplot(143);plt.imshow(b, cmap="gray");plt.title("Blue Channel")

# Merge the individual channels into a BGR image
imgMerged = cv2.merge((b, g, r))
# Show the merged output
plt.subplot(144)
plt.imshow(imgMerged[:, :, ::-1])
plt.title("Merged Output")

img_hsv = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2HSV)

# Split the image into the H,S,V components
h,s,v = cv2.split(img_hsv)

# Show the channels
plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(h, cmap="gray");plt.title("H Channel");
plt.subplot(142);plt.imshow(s, cmap="gray");plt.title("S Channel");
plt.subplot(143);plt.imshow(v, cmap="gray");plt.title("V Channel");
plt.subplot(144);plt.imshow(img_NZ_rgb);   plt.title("Original");

# read the image as Color
img_NZ_bgr = cv2.imread("foto.jpeg", cv2.IMREAD_COLOR)
print("img_NZ_bgr shape (H, W, C) is:", img_NZ_bgr.shape)

# read the image as Grayscaled
img_NZ_gry = cv2.imread("foto.jpeg", cv2.IMREAD_GRAYSCALE)
print("img_NZ_gry shape (H, W) is:", img_NZ_gry.shape)