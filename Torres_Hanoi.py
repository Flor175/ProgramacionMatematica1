import sys 
from Ui_interfaz_hanoi import *
from clase_postes import *
from clase_discos import *
from clase_reporte import *


class MainWindow(QtWidgets.QWidget, Ui_MainWindow):
        def __init__(self, parent = None):
            QtWidgets.QWidget.__init__(self, parent)
            self.setupUi(self)

            self.Disco1 = discos(1,1)
            self.Disco2 = discos(2,1)
            self.Disco3 = discos(3,1)
            self.Disco4 = discos(4,1)
            self.Disco5 = discos(5,1)
            self.Disco6 = discos(6,1)
            self.Disco7 = discos(7,1)
            self.Disco8 = discos(8,1)
            
            self.Poste1 = postes(1,[8,7,6,5,4,3,2,1])
            self.Poste2 = postes(2,[])
            self.Poste3 = postes(3,[])

            self.jugadas = 0
                
            self.postes_salida.currentIndexChanged['QString'].connect(self.postes_disponibles_entrada)
            self.postes_salida.currentIndexChanged['QString'].connect(self.poste_seleccionado)
            self.boton_mover.clicked.connect(self.EventoMovimiento)
            self.boton_mover.clicked.connect(self.postes_disponibles_salida)
            self.boton_mover.clicked.connect(self.contador)
            self.pushButton.clicked.connect(self.juego_finalizado)
            self.boton_mover.clicked.connect(self.validar_final_juego)
            


        def postes_disponibles_salida(self):
            self.postes_salida.clear()
            if len(self.Poste1.discos_apilados) > 0:
                if min(self.Poste1.discos_apilados,default = 10) < min(self.Poste2.discos_apilados,default = 10) or min(self.Poste1.discos_apilados,default = 0) < min(self.Poste3.discos_apilados,default = 10):
                    self.postes_salida.addItem("Poste 1")
            if len(self.Poste2.discos_apilados) > 0:
                if min(self.Poste2.discos_apilados,default = 10) < min(self.Poste1.discos_apilados,default = 10) or min(self.Poste2.discos_apilados,default = 0) < min(self.Poste3.discos_apilados,default = 10):
                    self.postes_salida.addItem("Poste 2")
            if len(self.Poste3.discos_apilados) > 0:
                if min(self.Poste3.discos_apilados,default = 10) < min(self.Poste1.discos_apilados,default = 10) or min(self.Poste3.discos_apilados,default = 0) < min(self.Poste2.discos_apilados,default = 10):
                    self.postes_salida.addItem("Poste 3")
                

        def postes_disponibles_entrada(self):
            if self.postes_salida.count() > 0:
                self.postes_entrada.clear()
                item = self.postes_salida.currentText()
                if item=="Poste 1":
                    poste_elegido = self.Poste1
                if item=="Poste 2":
                    poste_elegido = self.Poste2
                if item=="Poste 3":
                    poste_elegido = self.Poste3
                if min(self.Poste1.discos_apilados,default=11) > min(poste_elegido.discos_apilados,default=10):
                    self.postes_entrada.addItem("Poste 1")
                if min(self.Poste2.discos_apilados,default=11) > min(poste_elegido.discos_apilados,default=10):
                    self.postes_entrada.addItem("Poste 2")
                if min(self.Poste3.discos_apilados,default=11) > min(poste_elegido.discos_apilados,default=10):
                    self.postes_entrada.addItem("Poste 3")
        
        def EventoMovimiento(self):
            item = self.postes_salida.currentText()
            if item=="Poste 1":
                poste_elegido_salida = self.Poste1
            if item=="Poste 2":
                poste_elegido_salida = self.Poste2
            if item=="Poste 3":
                poste_elegido_salida = self.Poste3

            item = self.postes_entrada.currentText()
            if item=="Poste 1":
                poste_elegido_entrada = self.Poste1
            if item=="Poste 2":
                poste_elegido_entrada = self.Poste2
            if item=="Poste 3":
                poste_elegido_entrada = self.Poste3
            print("poste_elegido_salida.discos_apilados",poste_elegido_salida.discos_apilados)
            print("poste_elegido_entrada.discos_apilados",poste_elegido_entrada.discos_apilados)
            
            poste_nuevo = poste_elegido_entrada.numero_poste
            print("poste_nuevo",poste_nuevo)
            longitud = min(poste_elegido_salida.discos_apilados,default=10)
            if longitud == 1:
                disco_a_mover = self.Disco1
            if longitud == 2:
                disco_a_mover = self.Disco2
            if longitud == 3:
                disco_a_mover = self.Disco3
            if longitud == 4:
                disco_a_mover = self.Disco4
            if longitud == 5:
                disco_a_mover = self.Disco5
            if longitud == 6:
                disco_a_mover = self.Disco6
            if longitud == 7:
                disco_a_mover = self.Disco7
            if longitud == 8:
                disco_a_mover = self.Disco8

            print(longitud)
            print("disco_a_mover.poste",disco_a_mover.poste)
            x = 90 +(poste_nuevo-1)*220 - 8*longitud
            y = 370 -30*(len(poste_elegido_entrada.discos_apilados))
            print(x,y)
            postes.mover_discos(poste_elegido_salida,poste_elegido_entrada)
            disco_a_mover.cambio_poste(poste_nuevo)

            item = self.postes_salida.currentText()
            if item=="Poste 1":
                self.Poste1 = poste_elegido_salida 
            if item=="Poste 2":
                self.Poste2 = poste_elegido_salida 
            if item=="Poste 3":
                self.Poste3 = poste_elegido_salida

            item = self.postes_entrada.currentText()
            if item=="Poste 1":
                self.Poste1 = poste_elegido_entrada
            if item=="Poste 2":
                self.Poste2 = poste_elegido_entrada
            if item=="Poste 3":
                self.Poste3 = poste_elegido_entrada 
            
            if longitud == 1:
                self.Disco1 = disco_a_mover
                self.disco1.move(x,y)
            if longitud == 2:
                self.Disco2 = disco_a_mover
                self.disco2.move(x,y)
            if longitud == 3:
                self.Disco3 = disco_a_mover
                self.disco3.move(x,y)
            if longitud == 4:
                self.Disco4 = disco_a_mover
                self.disco4.move(x,y)
            if longitud == 5:
                self.Disco5 = disco_a_mover
                self.disco5.move(x,y)
            if longitud == 6:
                self.Disco6 = disco_a_mover
                self.disco6.move(x,y)
            if longitud == 7:
                self.Disco7 = disco_a_mover
                self.disco7.move(x,y)
            if longitud == 8:
                self.Disco8 = disco_a_mover
                self.disco8.move(x,y)

            reporte.escribir_fila(str(self.jugadas),str(poste_elegido_salida.numero_poste),str(disco_a_mover.tamaño), str(poste_elegido_entrada.numero_poste))
            
        def contador(self):
            self.jugadas = self.jugadas + 1 
            self.contador_jugadas.setText("Jugadas realizadas: " + str(self.jugadas))

        def poste_seleccionado(self):
            if self.postes_salida.count() > 0:
                item = self.postes_salida.currentText()
                if item=="Poste 1":
                    poste_elegido_salida = self.Poste1
                if item=="Poste 2":
                    poste_elegido_salida = self.Poste2
                if item=="Poste 3":
                    poste_elegido_salida = self.Poste3
                
                longitud = min(poste_elegido_salida.discos_apilados,default=10)
                if longitud == 1:
                    disco_a_mover = self.disco1
                if longitud == 2:
                    disco_a_mover = self.disco2
                if longitud == 3:
                    disco_a_mover = self.disco3
                if longitud == 4:
                    disco_a_mover = self.disco4
                if longitud == 5:
                    disco_a_mover = self.disco5
                if longitud == 6:
                    disco_a_mover = self.disco6
                if longitud == 7:
                    disco_a_mover = self.disco7
                if longitud == 8:
                    disco_a_mover = self.disco8
                self.disco1.setFrameShape(QtWidgets.QFrame.Panel)
                self.disco1.setFrameShadow(QtWidgets.QFrame.Raised)
                self.disco2.setFrameShape(QtWidgets.QFrame.Panel)
                self.disco2.setFrameShadow(QtWidgets.QFrame.Raised)
                self.disco3.setFrameShape(QtWidgets.QFrame.Panel)
                self.disco3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.disco4.setFrameShape(QtWidgets.QFrame.Panel)
                self.disco4.setFrameShadow(QtWidgets.QFrame.Raised)
                self.disco5.setFrameShape(QtWidgets.QFrame.Panel)
                self.disco5.setFrameShadow(QtWidgets.QFrame.Raised)
                self.disco6.setFrameShape(QtWidgets.QFrame.Panel)
                self.disco6.setFrameShadow(QtWidgets.QFrame.Raised)
                self.disco7.setFrameShape(QtWidgets.QFrame.Panel)
                self.disco7.setFrameShadow(QtWidgets.QFrame.Raised)
                self.disco8.setFrameShape(QtWidgets.QFrame.Panel)
                self.disco8.setFrameShadow(QtWidgets.QFrame.Raised)
                disco_a_mover.setFrameShape(QtWidgets.QFrame.Box)
                disco_a_mover.setFrameShadow(QtWidgets.QFrame.Plain)
                disco_a_mover.setLineWidth(2)
        
        def juego_finalizado(self):
            MainWindow.close
            reporte.terminar_tabla()
            reporte.terminarReporte()
            reporte.compilarReporte()
        
        def validar_final_juego(self):
            if len(self.Poste3.discos_apilados)==8:
                self.juego_finalizado()
            


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mi_app = MainWindow()
    mi_app.postes_disponibles_salida()
    mi_app.postes_disponibles_entrada()
    reporte = Reporte("Jugadas_Realizadas")
    reporte.crearPreambulo()
    reporte.iniciarReporte()
    reporte.iniciar_tabla(4)
    reporte.escribir_fila("Jugada no.","Poste seleccionado","Disco seleccionado", "Poste de llegada")
    mi_app.show()
    sys.exit(app.exec())
  

