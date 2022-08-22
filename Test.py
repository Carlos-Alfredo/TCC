import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


cam1='/93AD8275CCBBCE0F33ECA60847959EDF_CAM_137'
path='C:/Users/carlo/Documents/TCC'
img_files=os.listdir(path+cam1)

sumhist=np.zeros(256)
n_img=0
for filename in img_files:
	img = cv2.imread(path+cam1+'/'+filename, 0)
	#cv2.imshow("image",img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	hist = cv2.calcHist([img],[0],None,[256],[0,256])
	#cv2.calcHist(images, channels, mask, histSize, ranges[, hist[, accumulate]])
	#images : it is the source image of type uint8 or float32 represented as “[img]”.
	#channels : it is the index of channel for which we calculate histogram. For grayscale image, its value is [0] and color image, you can pass [0], [1] or [2] to calculate histogram of blue, green or red channel respectively.
	#mask : mask image. To find histogram of full image, it is given as “None”.
	#histSize : this represents our BIN count. For full scale, we pass [256].
	#ranges : this is our RANGE. Normally, it is [0,256].
	sumhist=sumhist+hist
	n_img=n_img+1

hist_avg=sumhist/n_img
plt.plot(hist_avg)
plt.show()