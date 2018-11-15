import numpy as np 

T = eval(input("Número de casos de prueba: \n"))
los_aplica =[]
if 0 < T < 1001:
    for i in range(T):
        N = (input("tamaño y entero: \n"))
        entrada = list(map(int, N.split())) #arma una lista con los números dados 
        tamaño = entrada[0] #el primer elemento es el tamaño de sucesión
        entero = entrada[1] # el segundo elemento es el entero m

        if 0 < tamaño < 31 and 0 < entero < 1001:
            v = (input("valores: \n "))
            valores = list(map(int, v.split())) #arma una lista con los elementos dados 
            sucesion = np.array(valores)
           # valores_n = sucesion[sucesion<1 or sucesion >1000]
            valores_menores = sucesion < 1 
            valores_mayores = sucesion > 1000 
            valores_n = valores_menores + valores_mayores
            if np.any(valores_n):
                print("Los valores están fuera del rango")
            else:

                aplica = 0

                if len(valores) == tamaño:
                    for longitud in range(1,len(sucesion)+1):
                        for inicio in range(len(sucesion)-longitud+1):
                            #print("longitud: ",longitud, " inicio: ",sucesion[inicio] )
                            SUB = sucesion[inicio:(inicio+longitud)] # arma las subsucesiones de la sucesion principal
                            #print("subsucesiones principales ", SUB)
                            no_aplica = 0

                            for sublongitud in range(1,len(SUB)+1):
                                for subinicio in range(len(SUB)-sublongitud+1):
                                    #print("longitud: ",longitud, " inicio: ",sucesion[inicio] )
                                    subs = SUB[subinicio:(subinicio+sublongitud)] # arma las subsucesiones de la sucesion principal
                                    suma_subs = sum(subs)
                                    #print("chiquitas ", subs,"suma ", suma_subs)

                                    if suma_subs % entero > 0:
                                        no_aplica = no_aplica +1

                            if no_aplica == 0:
                                aplica = aplica + 1
        
                los_aplica.append(aplica)
    for i in range(len(los_aplica)):
        buenas = los_aplica[i]
        print(buenas)

else:
    print("número de pruebas no válido")
        
               
    