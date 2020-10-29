import cv2
import numpy as np

img= cv2.imread('Imagen.jpg')
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(img.shape)
print(img[0][0])
img= cv2.resize(img,(256,256))

cv2.imwrite("ResizeImagen.jpg",img)
img= cv2.imread('Imagen.jpg')
img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(img.shape)
print(img[0][0])

img[0][0]=0
img[0][1]=0
img[0][2]=0

cv2.imwrite('grayImagen.jpg',img)

matriz=np.zeros((256,256),np.float32)
print(matriz.shape)
cv2.imwrite('matrizimagen.jpg',matriz)
img=cv2.cvtColor(matriz,cv2.COLOR_GRAY2BGR)
print(img.shape)
cv2.imwrite('matrizcolorimagen.jpg',img)


#Solo para linux
cv2.imshow('Imagen',img)
cv2.waitKey(0)

