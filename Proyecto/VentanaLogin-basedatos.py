import re
import sys
from Ui_login import *
from Ui_ventana_registro import *  
from Ui_ventana_mensaje import *  
from VentanaPrincipal import *
import base_datos 
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
import Enviar_correo

class Cuadro_dialogo(QtWidgets.QWidget, Ui_cuadro_mensaje):
        def __init__(self):
            QtWidgets.QDialog.__init__(self)
            self.setupUi(self)

class Ventana_Registro(QtWidgets.QWidget, Ui_Registro): 
        def __init__(self):
            QtWidgets.QWidget.__init__(self)
            self.setupUi(self)

            self.texto_correonuevo.textChanged.connect(self.validar_correo)
            self.texto_passwnueva.textChanged.connect(self.validar_password)
            self.texto_confirmar.textChanged.connect(self.confirmar)
            self.boton_nuevo.clicked.connect(self.crear_nuevo)
            self.dialogo = Cuadro_dialogo()
                   
        def validar_correo(self,email):
            email = self.texto_correonuevo.text()
            validar = re.match('^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$', email, re.I)
            if email == "":
                self.texto_correonuevo.setStyleSheet("border: 2px solid yellow;")
                self.label_validacorreo.setText("Correo inválido")
                return False
            elif not validar:
                self.texto_correonuevo.setStyleSheet("border: 2px solid red;")
                self.label_validacorreo.setText("Correo inválido")
                return False
            else:
                self.texto_correonuevo.setStyleSheet("border: 2px solid green;")
                self.label_validacorreo.clear()
                return True

        def validar_password(self):
            
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
                return False

            if self.texto_passwnueva.text() == "":
                return False

            if mayuscula==True and minuscula==True and numeros==True and y==False and validar==True:  
                self.label_validapasw.clear()
                self.texto_passwnueva.setStyleSheet("border: 2px solid green;")
                return True
            else:
                correcto=False #Quiere decir que no cumple al menos uno de los requisitos
                self.texto_passwnueva.setStyleSheet("border: 2px solid red;")
                return False

            if correcto==False and validar==True: #No cumpla al menos un requisito, no contiene espacios y es mayor o igual a 8 caracteres.
                self.label_validapasw.setText("La contraseña no es segura")
                return False

        def confirmar(self, confirmacion = None, contra = None):
            contra = self.texto_passwnueva.text()
            confirmacion = self.texto_confirmar.text()
            if confirmacion == contra:
                self.texto_confirmar.setStyleSheet("border: 2px solid green;")
                self.label_coincidir.clear()
                return True
            elif confirmacion == "":
                return False
            else:
                self.texto_confirmar.setStyleSheet("border: 2px solid red;")
                self.label_coincidir.setText("la contraseña no coincide")
                return False
                    
        def registro_usuarios(self):
            correo = self.texto_correonuevo.text()
            contraseña = self.texto_passwnueva.text()
            base_datos.Database()
            base_datos.cursor.execute("SELECT * FROM `usuarios` WHERE `correo` = ? AND `contraseña` = ?", (correo, contraseña))
            if base_datos.cursor.fetchone() is not None:
                self.dialogo.label.setText("Usuario ya existente")
                self.dialogo.show()
                return False
            else:
                base_datos.cursor.execute("INSERT INTO `usuarios` (correo, contraseña) VALUES(?, ?)",(correo, contraseña))
                base_datos.conn.commit()
                base_datos.cursor.execute("SELECT * FROM `usuarios` WHERE `correo` = ? AND `contraseña` = ?", (correo, contraseña))
                print(base_datos.cursor.fetchone())
                return True

        def crear_nuevo(self):
            email =self.texto_correonuevo.text()
            if self.validar_correo(email) == True and self.validar_password() == True and self.confirmar() == True:
                correo = self.texto_correonuevo.text()
                contraseña = self.texto_passwnueva.text()
                base_datos.Database()
                base_datos.cursor.execute("SELECT * FROM `usuarios` WHERE `correo` = ? AND `contraseña` = ?", (correo, contraseña))
                if base_datos.cursor.fetchone() is not None:
                    self.dialogo.label.setText("Usuario ya existente")
                    self.dialogo.show()
                else:
                    base_datos.cursor.execute("INSERT INTO `usuarios` (correo, contraseña) VALUES(?, ?)",(correo, contraseña))
                    base_datos.conn.commit()
                    base_datos.cursor.execute("SELECT * FROM `usuarios` WHERE `correo` = ? AND `contraseña` = ?", (correo, contraseña))
                    print(base_datos.cursor.fetchone())
                    Enviar_correo.enviar_correo(correo)
                    self.dialogo.label.setText("Usuario creado")
                    self.dialogo.show()
                    self.close()
            elif email == "":
                return False
            else:
                self.dialogo.label.setText("datos incorrectos")
                self.dialogo.show()

class Ventana_Login(QtWidgets.QWidget, Ui_Login):
        def __init__(self, parent = None):
            QtWidgets.QWidget.__init__(self, parent)
            self.setupUi(self)

            self.boton_ingresar.clicked.connect(self.validar_usuario)
            self.mensaje = Cuadro_dialogo()
            self.registro = Ventana_Registro()
            self.boton_crear.clicked.connect(self.abrir_registro)
            self.VentanaPrincipal = Ventana_principal()

        def validar_usuario(self):
            correo = self.texto_correo.text()
            contraseña = self.texto_password.text()
            base_datos.Database()
            base_datos.cursor.execute("SELECT * FROM `usuarios` WHERE `correo` = ? AND `contraseña` = ?", (correo, contraseña))
            if base_datos.cursor.fetchone() is not None:
                self.VentanaPrincipal.show()
                self.close()
            else:
                self.mensaje.label.setText("datos incorrectos")
                self.mensaje.show()


        def abrir_registro(self):
            self.registro.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MyWindow = Ventana_Login()
    MyWindow.show()
    app.exec_()
