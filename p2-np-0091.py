import numpy as np
# Ian gutierrez NC 0091
# ejemplos de numpy  Numerical python 
print("--- espaciado linealmente en array ---0091")
arre=np.linspace(start=0,stop=1,num=5)
print(arre)
print("--- Matrix identidad en 2D array ---0091")
matrix=np.eye(3)
print(matrix)
print("--- Genera numeros al azar(aleatorios) en 2D array ---0091")
numale=np.random.random((3,4)) # genera 12 numeros aleatorios
print(numale)
print("generar 9 numeros aleatorios entre de 0 y 1")
numale=np.random.random((3,3)) # genera 12 numeros aleatorios
print(numale)
# como generar 9 números aleatorios comprendidos entre 1 y 20
# con numpy en un arreglo de 3 por 3
print("generar 9 numeros aleatorios entre de 1 y 20")
arre = np.random.randint(1, 21, size=9).reshape(3, 3)
print(arre)
print("ian gutierrez NC = 0091")