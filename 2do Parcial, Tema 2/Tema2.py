from clase_matriz import *

T = eval(input("Ingrese el número de matrices \n" ))#pedir el numero de matrices

if 0 < T < 101:
    for i in range(T):
        N =eval(input("Ingrese el tamaño de la matriz \n"))# pedir el tamaño de las matrices
        if 1 < N < 101:
            m = Matrix(N,N)
            for i in range(N):
                v = (input("Ingrese los valores de la fila, utilice espacios para separar cada valor: \n "))
                valores = list(map(int, v.split()))
                m.armar_matriz(i,valores)
                #m.show_matrix()
            traza_mayor = 0
            for k in range(1,N+1): #k indica el tamaño de la submatriz se buscan las esquinas superiores izquierdas de las posibles submatrices
                for fila in range(0, N-k+1): #fila indica las filas que puede tener una submatriz de tamaño k
                    for columna in range(0,N-k+1):#columna indica las columna que puede tener una submatriz de tamaño k
                        submatriz = Matrix(k,k)
                        for h in range(0,k):
                            for l in range(0,k):
                                submatriz.define_elementos(h,l,m._elementos[fila+h][columna+l])
                                #submatriz.show_matrix()
                    
                                traza = 0
                                for k_i in range(0,k):
                                    traza = traza + submatriz._elementos[k_i][k_i]
                                    if traza > traza_mayor:
                                        traza_mayor = traza

            print("La traza máxima es:",traza_mayor)
            
        else:
            print("Ingrese un número menor que 100")
else:
    print("Ingrese un número menor que 100")
