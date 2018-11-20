T = eval(input("casos: \n"))

if 0 < T < 10:
    for i in range(T):
        N = eval(input("habitaciones: \n"))
        if 0 < N < 10**5:
            S = input("cadena:")
            cuentaR = 0 
            cuentaG = 0
            cuentaB = 0
            for carac in S: #contar la letra que esta más veces
                if carac == 'R':
                    cuentaR += 1
                if carac == "G":
                    cuentaG += 1
                if carac == "B":
                    cuentaB += 1
            contador = 0
            if cuentaR == max(cuentaR,cuentaG,cuentaB):
                contador = cuentaB + cuentaG
            if cuentaG == max(cuentaR,cuentaG,cuentaB):
                contador = cuentaB + cuentaR
            if cuentaB == max(cuentaR,cuentaG,cuentaB):
                contador = cuentaG + cuentaR

            print(contador)
