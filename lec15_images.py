#http://www.python-course.eu/python_image_processing.php
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img=mpimg.imread('io/unknown.png')
img.shape()
plt.axis("off")
plt.imshow(img);plt.show()
lum_img = img[:,:,1]

plt.axis("off")
plt.imshow(lum_img);plt.show()

####
windmills = mpimg.imread('io/windmills.png')
plt.axis("off")
plt.imshow(windmills);plt.show()

def tint(imag, percent):
    """
    imag: the image which will be shaded
    percent: a value between 0 (image will remain unchanged
             and 1 (image will completely white)
    """
    tinted_imag = imag + (np.ones(imag.shape) - imag) * percent
    return tinted_imag
windmills = mpimg.imread('io/windmills.png')
tinted_windmills = tint(windmills, 0.8)
plt.axis("off")
plt.imshow(tinted_windmills);plt.show()

def shade(imag, percent):
    """
    imag: the image which will be shaded
    percent: a value between 0 (image will remain unchanged
             and 1 (image will be blackened)
    """
    tinted_imag = imag * (1 - percent)
    return tinted_imag
windmills = mpimg.imread('io/windmills.png')
tinted_windmills = shade(windmills, 0.4)
plt.imshow(tinted_windmills);plt.show()

