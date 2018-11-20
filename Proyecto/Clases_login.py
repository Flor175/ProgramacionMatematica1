import re

class login():

    def __init__(self,email):
        self.email = email

    def correo_usuario(self, correo):
        if re.match("[(a-zA-Z0-9._%+-)]+@[(a-z0-9_-.)]+[.][(a-z)]{2,}$",correo):
            return True
        else:
            print("correo inválido")    


class contraseña():

espacio=False  #variable de inicialización para identificar espacios
validar=False #variable de inicialización para identificar número de caracteres
long=len(self.texto_passwnueva.text()) #Calcula la longitud de la contraseña
y=self.texto_passwnueva.text().isalnum()#True si es alfanumérica, False si no lo es.(Nos interesa que sea False)
mayuscula=False #variable iniciliazción para contar las letras mayúsculas
minuscula=False #variable iniciliazción para contar las letras minúsculas
numeros=False #variable iniciliazción para contar los números
correcto=True

            for carac in self.texto_passwnueva.text(): #ciclo for que recorre caracter por caracter en la contraseña

                if carac.isspace()==True: #Saber si el caracter es un espacio
                    espacio=True #si encuentra un espacio se cambia el valor a True

                if carac.isupper()== True: #saber si hay mayuscula
                        mayuscula=True #Si encuentra al menos una Mayuscula cambia a True
                    
                if carac.islower()== True: #saber si hay minúsculas
                        minuscula=True #Si encuentra al menos una minúscula cambia a True
                    
                if carac.isdigit()== True: #saber si hay números
                        numeros=True #Si encuentra al menos un número cambia a True

            if espacio ==True: #este valor indica que encontró un espacio
                self.label_validapasw.setText("La contraseña no puede contener espacios")                
            else:
                validar=True #se escoge con el fin de garantizar que no hay espacios
                #y pasar al número mínimo de caracteres que contiene la contraseña
                
                        
            if long < 5 and validar==True: #Se garantiza que la contraseña posea mínimo 8 caracteres sin espacios.
                self.label_validapasw.setText("Mínimo 5 caracteres")
                validar=False


            if mayuscula==True and minuscula==True and numeros==True and y==False and validar==True:  
                self.label_validapasw.clear()
                self.texto_passwnueva.setStyleSheet("border: 2px solid green;")
            else:
                correcto=False #Quiere decir que no cumple al menos uno de los requisitos
                self.texto_passwnueva.setStyleSheet("border: 2px solid red;")

            if correcto==False and validar==True: #No cumpla al menos un requisito, no contiene espacios y es mayor o igual a 8 caracteres.
                self.label_validapasw.setText("La contraseña no es segura")
