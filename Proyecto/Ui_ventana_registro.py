# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\florm\Documents\Mate\Progra\Proyecto\ventana_registro.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Registro(object):
    def setupUi(self, Registro):
        Registro.setObjectName("Registro")
        Registro.resize(648, 405)
        self.boton_nuevo = QtWidgets.QPushButton(Registro)
        self.boton_nuevo.setGeometry(QtCore.QRect(240, 350, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.boton_nuevo.setFont(font)
        self.boton_nuevo.setObjectName("boton_nuevo")
        self.registro = QtWidgets.QLabel(Registro)
        self.registro.setGeometry(QtCore.QRect(250, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        self.registro.setFont(font)
        self.registro.setObjectName("registro")
        self.gridLayoutWidget = QtWidgets.QWidget(Registro)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(70, 66, 491, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_correo = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_correo.setFont(font)
        self.label_correo.setObjectName("label_correo")
        self.gridLayout.addWidget(self.label_correo, 0, 0, 1, 1)
        self.label_validacorreo = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_validacorreo.setFont(font)
        self.label_validacorreo.setObjectName("label_validacorreo")
        self.gridLayout.addWidget(self.label_validacorreo, 1, 1, 1, 1)
        self.label_password = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.gridLayout.addWidget(self.label_password, 2, 0, 1, 1)
        self.texto_correonuevo = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.texto_correonuevo.setFont(font)
        self.texto_correonuevo.setObjectName("texto_correonuevo")
        self.gridLayout.addWidget(self.texto_correonuevo, 1, 0, 1, 1)
        self.texto_passwnueva = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.texto_passwnueva.setFont(font)
        self.texto_passwnueva.setEchoMode(QtWidgets.QLineEdit.Password)
        self.texto_passwnueva.setObjectName("texto_passwnueva")
        self.gridLayout.addWidget(self.texto_passwnueva, 3, 0, 1, 1)
        self.label_confirmar = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label_confirmar.setFont(font)
        self.label_confirmar.setObjectName("label_confirmar")
        self.gridLayout.addWidget(self.label_confirmar, 4, 0, 1, 1)
        self.label_validapasw = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_validapasw.setFont(font)
        self.label_validapasw.setObjectName("label_validapasw")
        self.gridLayout.addWidget(self.label_validapasw, 3, 1, 1, 1)
        self.texto_confirmar = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.texto_confirmar.setFont(font)
        self.texto_confirmar.setEchoMode(QtWidgets.QLineEdit.Password)
        self.texto_confirmar.setObjectName("texto_confirmar")
        self.gridLayout.addWidget(self.texto_confirmar, 5, 0, 1, 1)
        self.label_coincidir = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.label_coincidir.setFont(font)
        self.label_coincidir.setObjectName("label_coincidir")
        self.gridLayout.addWidget(self.label_coincidir, 5, 1, 1, 1)

        self.retranslateUi(Registro)
        QtCore.QMetaObject.connectSlotsByName(Registro)

    def retranslateUi(self, Registro):
        _translate = QtCore.QCoreApplication.translate
        Registro.setWindowTitle(_translate("Registro", "Registro"))
        self.boton_nuevo.setText(_translate("Registro", "Crear"))
        self.registro.setText(_translate("Registro", "Registro:"))
        self.label_correo.setText(_translate("Registro", "Correo electrónico:"))
        self.label_validacorreo.setText(_translate("Registro", "Correo inválido"))
        self.label_password.setText(_translate("Registro", "Contraseña:"))
        self.label_confirmar.setText(_translate("Registro", "Confirmar contraseña:"))
        self.label_validapasw.setText(_translate("Registro", "Contraseña incorrecta"))
        self.label_coincidir.setText(_translate("Registro", "la contraseña no coincide"))

