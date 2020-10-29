import cv2

img= cv2.imread('Imagen.jpg')
img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
print(img.shape)
print(img[0][0])
img= cv2.resize(img,(256,256))

#Solo para linux 
cv2.imwrite("ResizeImagen.jpg",img)
cv2.imshow('Imagen',img)
cv2.waitKey(0)
