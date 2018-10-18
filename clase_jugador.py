from clase_postes import postes
class jugador():
    
    def __init__(self,nombre):
        self.nombre = nombre
 
    def obtener_nombre(self):
        return(self.nombre)
    
    def jugar(self,poste_salida,poste_entrada):
        Si_Sale = poste_salida.seleccionar_poste_salida()
        #print(Si_Sale)
        if Si_Sale != "N":
            Si_Entra = poste_entrada.seleccionar_poste_entrada(Si_Sale)
            #print(Si_Entra)
            if Si_Entra != "N":
                #print("1")
                tamaño_a_mover = Si_Sale
                #print("2",tamaño_a_mover)
                #print(globals())
                disco_a_mover = globals()["disco"+str(tamaño_a_mover)]
                #print("3")
                postes.mover_discos(poste_salida,poste_entrada)
                #print("4")
                disco_a_mover.cambio_poste(poste_entrada.numero_poste)
                #print("5")
                globals()["disco"+str(tamaño_a_mover)] = disco_a_mover