import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

lenna = mpimg.imread('../notebooks/lenna.bmp').copy()
flag = mpimg.imread('georgia.png')



lenna = lenna.astype(np.float32) / 255.0

h_flag, w_flag = flag.shape[:2]
h_lenna, w_lenna = lenna.shape[:2]


hstart = 0
wstart = w_lenna - w_flag

# Replace top right corner pixels
lenna[hstart:hstart+h_flag, wstart:wstart+w_flag, :] = flag

plt.imshow(lenna)
plt.axis('off')
plt.show()
