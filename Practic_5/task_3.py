import matplotlib.pyplot as plt
import numpy as np
from numpy import newaxis

def calculateMadelbrot(N_max,some_threshold,nx,ny):
    x=np.linspace(-2,1,nx)
    y=np.linspace(-1.5,1.5,ny)
    c=x[:,newaxis]+1j*y[newaxis,:]

    z=c
    for j in range(N_max):
        z=z**2+c
    mandelbrot_set=(abs(z)<some_threshold)
    return mandelbrot_set
mandelbrot_set=calculateMadelbrot(int(input()),50.,601,401)
plt.imshow(mandelbrot_set,cmap='gray')
plt.show()
