import random
from PIL import Image

sizex=10000
sizey=1000
img=Image.new( mode = "RGB", size = (sizex, sizey), color=(255,255,255))
path="C:\\Users\\Julek\\Documents\\Coding\\Python\\gradient\\"

start=[255,0,255]
end=[255,255,112]
diff=[]
for i in range(3):
    diff.append(end[i]-start[i])
    diff[i]/=sizex

#print (diff)

for i in range(sizex):
    for j in range(sizey):
        img.putpixel ( (i,j), ( round(start[0]+diff[0]*i),round(start[1]+diff[1]*i),round(start[2]+diff[2]*i) ) )

img.save(path+'gradient.png', format="PNG")


