import numpy as np
import cv2
i=0

img1 = cv2.imread('img0.jpg')
img2 = cv2.imread('img1.jpg')
img3 = cv2.imread('img3.jpg')
height , width , layers =  img1.shape

video = cv2.VideoWriter('video.avi',-1,1,(width,height))

video.write(img1)
video.write(img2)
video.write(img3)

cv2.destroyAllWindows()
video.release()