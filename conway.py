import random
from PIL import Image
array=[]
sizex=102
sizey=sizex
img=[]

path="C:\\Users\\Julek\\Documents\\Coding\\Python\\conway\\test\\"

def updateCells():
    for i in range(1,sizex-1):
        for j in range(1,sizey-1):
            aliveCounter=countNeighbourAliveCells(i,j)
            if (array[i][j]):
                if (aliveCounter!=2 and aliveCounter!=3):
                    array[i][j]=3 # dead next (now alive)
            else:
                if (aliveCounter==3):
                    array[i][j]=2 # alive next
    for i in range(1,sizex-1):
        for j in range(1,sizey-1):
            if (array[i][j]==3): array[i][j]=0
            if (array[i][j]==2): array[i][j]=1
    
    

def countNeighbourAliveCells(x,y):
    aliveCounter=0
    if (array[x][y+1]%2): aliveCounter+=1
    if (array[x+1][y]%2): aliveCounter+=1
    if (array[x+1][y+1]%2): aliveCounter+=1
    if (array[x-1][y]%2): aliveCounter+=1
    if (array[x][y-1]%2): aliveCounter+=1
    if (array[x-1][y-1]%2): aliveCounter+=1
    if (array[x-1][y+1]%2): aliveCounter+=1
    if (array[x+1][y-1]%2): aliveCounter+=1
    
    return aliveCounter

def randomArray():
    for i in range(sizex):
        tmp=[]
        for j in range(sizey):
            if (i==0 or i==sizey-1 or j==0 or j==sizey-1): 
                tmp.append(0)
            else: tmp.append(random.randint(0,1))
        array.append(tmp)

def saveImage():
    im=Image.new( mode = "RGB", size = (sizex, sizey), color=(255,255,255))
    for i in range(sizex):
        for j in range(sizey):
            if (array[i][j]): im.putpixel ((i,j), (0,0,0,255))
    #im=im.resize((sizex*4,sizey*4))
    img.append(im)

randomArray()
#updateImage()
#img.show()

for i in range(10000):
    updateCells()
    saveImage()
    print (i)
    #img[i].save(path+str(i)+".png", format="PNG")

img[0].save(path+'imagedraw2.webp',
               save_all = True, append_images = img[1:], 
               optimize = False, duration = 1, format="WEBP")


