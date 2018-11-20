T = eval(input("casos: \n"))


def permu(x):
    if len(x) <= 1:
        yield x
    else:
        for i in range(len(x)):
            for p in permu(x[:i] + x[i + 1:]):
                yield [x[i]] + p

if 0 < T < 10:
    for i in range(T):
        S = input("cadena:")
        if S.islower() == True:
            C = set()
            for carac in S:
                C.add(carac)
            #print(C)
            L = []
            for element in C:
                L.append(element)
            #print(L)
            
            P = list(permu(L))
            #print(P)

            contador_i = 0
            contador_i_1 = 0
            contador_i_2 = 0
            es_dynamic = 0
            for j in range(len(P)):
                las_frecs=[]
                for k in P[j]:
                    #print(str(j))
                    las_frecs.append(S.count(str(k)))
                errores = 0
                for k in range(len(las_frecs)-2):
                    contador_i_2 = las_frecs[k]
                    contador_i_1 = las_frecs[k+1]
                    contador_i = las_frecs[k+2]
                    #print(contador_i_2,contador_i_1,contador_i)
                    if contador_i_2 + contador_i_1 != contador_i:
                        errores = errores +1    
                if errores ==0:
                    es_dynamic = 1
                    break  
            if es_dynamic == 1:
                print("dynnamic")
            else:
                print("Not")