class usuarios():

    def __init__(self,email,password):
        self.email = email
        self.password = password
        self.usuario = dict()
        self.usuario_nuevo = dict()
       # self.usuario_nuevo =dict()


    def agregar_usuario(self):
        self.usuario_nuevo["Correo"] = self.email
        self.usuario_nuevo["Contraseña"] =self.password
        print(self.usuario_nuevo)

   