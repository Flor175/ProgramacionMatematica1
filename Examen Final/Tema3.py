import numpy as np 
import random

N = eval(input("tamaño de la matriz: \n"))


def listaAleatorios(n):  #función para armar las filas de la matriz
      lista = [0]  * n
      for i in range(n):
          lista[i] = random.randint(0,10)
      return lista

arrays = [] #lista  de filas para armar la matriz
r = [] #lista de los valores mínimos de las filas
for i in range(N):
    filas = listaAleatorios(N)
    rs = min(filas) #obtener el mínimo valor de cada fila
    r.append(rs) #agregarlo a la lista
    arrays.append(filas) 
 

matriz = np.matrix(arrays) #armar la matriz
print(matriz)

c = [] #lista de los valores máximos de las columnas
for i in range(0,N):
    columnas = matriz[:,i]
    cs = max(columnas) #obtener el máximo valor de cada fila
    c.append(int(cs)) #agregarlo a la lista

R = max(r)
C = min(c)

if R == C:
    print(0)
else:
    for j in range(len(filas)):
        for i in range(len(columnas)):
            valor_fila = matriz[j,i]
            print("Este es: ",valor_fila)
            if valor_fila < C:
                cambio_filas = 0
                cambio_filas = cambio_filas + 1
                print("contador: ", cambio_filas)

    
    for i in range(len(columnas)):
        for j in range(len(filas)):
            valor_columna = matriz[j,i]
            print("Este también: ",valor_columna)
            if valor_columna > R:
                cambio_columnas = 0
                cambio_columnas = cambio_columnas + 1
                print("contador: ", cambio_columnas)

    entero = min(cambio_filas,cambio_columnas)
    print(entero)
                
                




   



   





