from clase_postes import postes
class discos():
    
    def __init__(self,tamaño,poste):
        self.tamaño = tamaño
        self.poste = poste
        
    def cambio_poste(self,nuevo_poste):
        self.poste = nuevo_poste
