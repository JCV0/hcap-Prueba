import numpy as np

#Funcion que calcula la matriz resultante C después de aplicar la operacion convolucion de A*B

def convolucion(A,B,C):
    for row in range(0,len(A)-2):
        for col in range(0,len(A[row])-2):
            C[row][col]=A[row][col]*B[0][0]+A[row][col+1]*B[0][1]+A[row][col+2]*B[0][2]+A[row+1][col]*B[1][0]+A[row+1][col+1]*B[1][1]+A[row+1][col+2]*B[1][2]+A[row+2][col]*B[2][0]+A[row+2][col+1]*B[2][1]+A[row+2][col+2]*B[2][2]
    return C

#=============================Ejercicio en clase=====================================
matriz1=[[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
filtro= [[1,0,2],[5,0,9],[6,2,1]]

A=np.array(matriz1)
B=np.array(filtro)
C=np.zeros((2,2))

#============================Ejercicio en canvas====================================
matriz2=[[1,2,3,4,5,6],[7,8,9,10,11,12],[0,0,1,16,17,18],[0,1,0,7,23,24],[1,7,6,5,4,3]]
filtro2=[[1,1,1],[0,0,0],[2,10,3]] 

E=np.array(matriz2)
F=np.array(filtro2)
G=np.zeros((3,4))

print("\nEjercicio en clase\n")
print(convolucion(A,B,C))
print("\nEjercicio Canvas\n")
print(convolucion(E,F,G))

