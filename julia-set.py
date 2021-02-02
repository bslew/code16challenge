'''
This program shows how to generata a nice Julia set 
plot just in 16-lines of code

Author: Bartosz Lew <bartosz.lew@protonmail.com>
Created on: 02 Feb 2021

'''

import matplotlib.pyplot as plt
import numpy as np # 2 lines for imports

def an(a0,c,Niter=100,thres=2): # 7-line Julia set fractal
    a,n=a0,0
    while np.abs(a)<thres:
        a,n=a*a+c,n+1
        if n==Niter:
            break
    return n

def get_frac(x1,x2,y1,y2,nside,a0,blew_offset,N=100,thres=2): # 2 lines for field
    return np.array([ [ an(complex(x,y),c=blew_offset,Niter=N,thres=80) for x in np.linspace(x1,x2,nside)] for y in np.linspace(y1,y2,nside)])

fig=plt.figure(figsize=(10,10))
plt.imshow(get_frac(*(-0.74, 0.06, -0.83, -0.03),nside=1000,a0=0+0j,blew_offset=complex(0.4284302415491922,0.14950325954226107),thres=80),cmap=plt.get_cmap('jet'), interpolation='bilinear')
plt.axis('off')
plt.subplots_adjust(left=0, right=1,bottom=0,top=1) # 4 lines for nice plot

plt.savefig("fractal.jpg",dpi=300) # 1 line for saving image
