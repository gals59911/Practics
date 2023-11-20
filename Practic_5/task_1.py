from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
fname = '865becf76c5d3d10b65cae29657461fd.png'
img = np.array(Image.open(fname).convert("L"))
plt.imshow(img,cmap='Spectral')
plt.show()
plt.imshow(img,cmap="gray")
plt.show()
crop_face = img[10:-50, 100:-50]
plt.imshow(crop_face,cmap="gray")
plt.show()
sy, sx = crop_face.shape
y, x = np.ogrid[0:sy, 0:sx]
y.shape, x.shape
centerx, centery = (210, 110) 
mask = (((y - centery)**2)/4 + ((x - centerx)**2)/2) >55**2
crop_face[mask] = 0
plt.imshow(crop_face,cmap='gray')
plt.show()

