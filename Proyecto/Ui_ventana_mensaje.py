# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\florm\Documents\Mate\Progra\Proyecto\ventana_mensaje.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cuadro_mensaje(object):
    def setupUi(self, cuadro_mensaje):
        cuadro_mensaje.setObjectName("cuadro_mensaje")
        cuadro_mensaje.resize(291, 179)
        self.label = QtWidgets.QLabel(cuadro_mensaje)
        self.label.setGeometry(QtCore.QRect(80, 50, 181, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(cuadro_mensaje)
        QtCore.QMetaObject.connectSlotsByName(cuadro_mensaje)

    def retranslateUi(self, cuadro_mensaje):
        _translate = QtCore.QCoreApplication.translate
        cuadro_mensaje.setWindowTitle(_translate("cuadro_mensaje", "Dialog"))
        self.label.setText(_translate("cuadro_mensaje", "¡Correo inválido!"))

