import random


def cubierta(puntos):
    puntos = sorted(set(puntos)) # Elimina puntos repetidos

    if len(puntos) <= 1:
        return puntos # Verifica que hayan suficientes puntos

    def direccion_angulo(o, a, b): # Determina la dirección en la que se mide el ángulo OAB si es
                        # respecto a las agujas del reloj (-1), en contra de (1) o 0 si son colineales. 
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    cubierta_convexa_inferior = []
    for p in puntos: # Construye la cubierta  convexa inferior
        while len(cubierta_convexa_inferior) >= 2 and direccion_angulo(cubierta_convexa_inferior[-2], cubierta_convexa_inferior[-1], p) <= 0:
            cubierta_convexa_inferior.pop() # Elimina los puntos que encierra la cubierta al agrearle el punto p
        cubierta_convexa_inferior.append(p)

    cubierta_convexa_superior = []
    for p in reversed(puntos): # Construye la cubierta  convexa superior
        while len(cubierta_convexa_superior) >= 2 and direccion_angulo(cubierta_convexa_superior[-2], cubierta_convexa_superior[-1], p) <= 0:
            cubierta_convexa_superior.pop() # Elimina los puntos que encierra la cubierta al agrearle el punto p
        cubierta_convexa_superior.append(p)

    return cubierta_convexa_inferior[:-1] + cubierta_convexa_superior[:-1] #Une las cubiertas de arriba y abajo



def potencia(c): #conjunto potencia del conjunto de puntos

    if len(c) == 0:
        return [[]]
    r = potencia(c[:-1])
    return r + [s + [c[-1]] for s in r]

N = eval(input("cantidad de puntos: \n" ))
tamaño_Cubierta = 0
while tamaño_Cubierta == 0 or tamaño_Cubierta > 4*10**15:
    if 1 < N < 51:
        Puntos=[]
        for i in range(N):
            x = random.randrange(-1000,1000)
            y = random.randrange(-1000,1000)
            punto = (x,y)
            Puntos.append(punto)
        #print(Puntos)
        tamaño_Cubierta = 0

        subconjuntos_puntos = potencia(Puntos)
        #print(subconjuntos_puntos)
        for subconjunto in subconjuntos_puntos:
            cubierta_subconjunto_puntos = cubierta(subconjunto)
            tamaño_Cubierta = tamaño_Cubierta + len(cubierta_subconjunto_puntos)
            #print(subconjunto," ",tamaño_Cubierta)
                 
    else:
        print("cantidad no válida")

for i in range(len(Puntos)):
    coordenadas = Puntos[i]
    print(coordenadas)
    
