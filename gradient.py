from math import sqrt
from math import ceil
import random
from PIL import Image

sizex=500
sizey=500
img=Image.new( mode = "RGB", size = (sizex, sizey), color=(255,255,255))
path="/home/synch/Documents/Coding/python"

points=[ [[0,0],[255,0,0]],[[sizex-1,sizey-1],[0,255,0]],[[200,200],[0,0,255]]]
numberOfPoints=3
for i in range(sizex):
    for j in range(sizey):
        r=0
        g=0
        b=0
        dis=[]
        disSum=0
        for z in range(numberOfPoints):
            dis.append(0)

        for z in range(numberOfPoints):
            dis[z]=sqrt( (points[z][0][0]-i)**2+(points[z][0][1]-j)**2 )
            disSum+=dis[z]

        for z in range(numberOfPoints):
            r+=(dis[z]/disSum)*points[z][1][0]
            g+=(dis[z]/disSum)*points[z][1][1]
            b+=(dis[z]/disSum)*points[z][1][2]
        r=ceil(r)
        g=ceil(g)
        b=ceil(b)
        img.putpixel ((i,j), (r, g, b))

img.save(path+'gradient.png', format="PNG")


