class postes():
    
    def __init__(self,numero_poste,discos_apilados):
        self.numero_poste = numero_poste
        self.discos_apilados = discos_apilados   
    
    def seleccionar_poste_salida(self):
        if len(self.discos_apilados) > 0 :
            return(min(self.discos_apilados))
        else:
            print("No hay discos en el poste " , self.numero_poste)
            return("N")
    
    def seleccionar_poste_entrada(self,tamaño_disco):
        if tamaño_disco < min(self.discos_apilados,default=999):
            print("El poste " , self.numero_poste," acepta disco de tamaño " ,tamaño_disco )
            return("S")
        else:
            print("El poste " , self.numero_poste, " tiene un disco de tamaño menor a ", tamaño_disco)
            return("N") 

    @staticmethod         
    def mover_discos(poste_salida,poste_entrada):
        poste_entrada.discos_apilados.append(min(poste_salida.discos_apilados))
        poste_salida.discos_apilados.remove(min(poste_salida.discos_apilados))
        print("Se movió el disco ", min(poste_entrada.discos_apilados), " del poste ", poste_salida.numero_poste, " al poste ", poste_entrada.numero_poste)