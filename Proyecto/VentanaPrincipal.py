import sys
import os
import json
import Tops
import Tops_copias
import numpy as np
import matplotlib.pyplot as plt 
import pylatex
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from Ui_ventana_principal import * 
from PyQt5 import QtWidgets, QtCore
from pylatex import Document, Section, Tabular, Math, Axis, \
    Plot, Command, Figure
from pylatex.utils import  NoEscape

pg.setConfigOption('background', 'w')
current = os.getcwd()


class Ventana_principal(QtWidgets.QWidget, Ui_MainWindow):
  def __init__(self):
    QtWidgets.QWidget.__init__(self)
    self.setupUi(self)
    self.texto_nog.setValidator(QtGui.QIntValidator(1000000,100000000))
    self.texto_nog_2.setValidator(QtGui.QIntValidator(1000000,100000000))
    self.texto_nog_3.setValidator(QtGui.QIntValidator(1000000,100000000))
    self.creatingTable()
    self.boton_visualizar.clicked.connect(self.tablas2016)
    self.boton_visualizar.clicked.connect(self.graficas2016)
    self.checkBox_grandes.clicked.connect(self.exclusivos)
    self.checkBox_mes.clicked.connect(self.exclusivos)
    self.checkBox_USAC.clicked.connect(self.exclusivos)
    self.checkBox_proveedores.clicked.connect(self.exclusivos)
    self.boton_actualizar.clicked.connect(self.actualizar2016)
    
    self.boton_visualizar_2.clicked.connect(self.tablas2017)
    self.boton_visualizar_2.clicked.connect(self.graficas2017)
    self.checkBox_grandes_2.clicked.connect(self.exclusivos2)
    self.checkBox_mes_2.clicked.connect(self.exclusivos2)
    self.checkBox_USAC_2.clicked.connect(self.exclusivos2)
    self.checkBox_proveedores_2.clicked.connect(self.exclusivos2)
    self.boton_actualizar_2.clicked.connect(self.actualizar2017)

    self.boton_visualizar_4.clicked.connect(self.tablas2018)
    self.boton_visualizar_4.clicked.connect(self.graficas2018)
    self.checkBox_grandes_4.clicked.connect(self.exclusivos3)
    self.checkBox_mes_4.clicked.connect(self.exclusivos3)
    self.checkBox_USAC_4.clicked.connect(self.exclusivos3)
    self.checkBox_proveedores_3.clicked.connect(self.exclusivos3)
    self.boton_actualizar_4.clicked.connect(self.actualizar2018)
    
    self.boton_pdf.clicked.connect(self.reportes)

  def exclusivos(self):
    if self.checkBox_grandes.isChecked() == True:
      self.checkBox_mes.setChecked(False)
      self.checkBox_USAC.setChecked(False)
      self.checkBox_proveedores.setChecked(False)
    if self.checkBox_mes.isChecked() == True:
      self.checkBox_grandes.setChecked(False)
      self.checkBox_USAC.setChecked(False)
      self.checkBox_proveedores.setChecked(False)      
    if self.checkBox_USAC.isChecked() == True:
      self.checkBox_mes.setChecked(False)
      self.checkBox_grandes.setChecked(False)
      self.checkBox_proveedores.setChecked(False)
    if self.checkBox_proveedores.isChecked() == True:
      self.checkBox_mes.setChecked(False)
      self.checkBox_grandes.setChecked(False) 
      self.checkBox_USAC.setChecked(False)   

  def exclusivos2(self):
    if self.checkBox_grandes_2.isChecked() == True:
      self.checkBox_mes_2.setChecked(False)
      self.checkBox_USAC_2.setChecked(False)
      self.checkBox_proveedores_2.setChecked(False)
    if self.checkBox_mes_2.isChecked() == True:
      self.checkBox_grandes_2.setChecked(False)
      self.checkBox_USAC_2.setChecked(False)
      self.checkBox_proveedores_2.setChecked(False)      
    if self.checkBox_USAC_2.isChecked() == True:
      self.checkBox_mes_2.setChecked(False)
      self.checkBox_grandes_2.setChecked(False)
      self.checkBox_proveedores_2.setChecked(False)
    if self.checkBox_proveedores_2.isChecked() == True:
      self.checkBox_mes_2.setChecked(False)
      self.checkBox_grandes_2.setChecked(False) 
      self.checkBox_USAC_2.setChecked(False)    

  def exclusivos3(self):
    if self.checkBox_grandes_4.isChecked() == True:
      self.checkBox_mes_4.setChecked(False)
      self.checkBox_USAC_4.setChecked(False)
      self.checkBox_proveedores_3.setChecked(False)
    if self.checkBox_mes_4.isChecked() == True:
      self.checkBox_grandes_4.setChecked(False)
      self.checkBox_USAC_4.setChecked(False)
      self.checkBox_proveedores_3.setChecked(False)      
    if self.checkBox_USAC_4.isChecked() == True:
      self.checkBox_mes_4.setChecked(False)
      self.checkBox_grandes_4.setChecked(False)
      self.checkBox_proveedores_3.setChecked(False)
    if self.checkBox_proveedores_3.isChecked() == True:
      self.checkBox_mes_4.setChecked(False)
      self.checkBox_grandes_4.setChecked(False) 
      self.checkBox_USAC_4.setChecked(False)   

  def creatingTable(self):
    self.tableWidget = QtWidgets.QTableWidget(self.frame_7)
    self.tableWidget.move(50,60)
    self.tableWidget.resize(285,365)
    self.tableWidget.setStyleSheet("gridline-color: rgb(0, 0, 0);")
    self.tableWidget.setRowCount(10)
    self.tableWidget.setColumnCount(2)
    self.tableWidget.setColumnWidth(0, 160)
    self.tableWidget.setColumnWidth(1, 100)

  def tablas2016(self):
    if self.checkBox_grandes.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2016_copia.json') :
        print("Entre a compia 2016")
        table_data = Tops_copias.top10(2016)
      else:
        table_data = Tops.top10(2016)
      QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 3)
      self.label.move(210,20)      
      self.label.setText("Compras más grandes realizadas en el 2016")
      self.tableWidget.resize(270,365)  
      self.tableWidget.setColumnWidth(0, 160)
      self.tableWidget.setColumnWidth(1, 100) 
      self.tableWidget.setRowCount(10)
      self.tableWidget.setColumnCount(2)
      self.tableWidget.setHorizontalHeaderLabels(["Contratante","Monto"])
      for i, [comprador, monto] in enumerate(table_data):
        self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(comprador))
        self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(monto))


    if self.checkBox_mes.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2016_copia.json') :
        table_data = Tops_copias.topmes(2016)
      else:
        table_data = Tops.topmes(2016)      
      QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 3)
      self.label.move(210,20)
      self.label.setText("Compras más grandes por mes en el 2016")
      self.tableWidget.move(30,60)
      self.tableWidget.resize(300,410)
      self.tableWidget.setRowCount(12)
      self.tableWidget.setColumnCount(4)
      self.tableWidget.setColumnWidth(0, 100)
      self.tableWidget.setColumnWidth(1, 150)
      self.tableWidget.setColumnWidth(2, 150)
      self.tableWidget.setColumnWidth(3, 100)
      self.tableWidget.setHorizontalHeaderLabels(["Mes","Proveedor","Contratante","Monto"])
      for i, [mes, proveedor, contratante, monto] in enumerate(table_data):
        self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(mes))
        self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(proveedor))
        self.tableWidget.setItem(i,2,QtWidgets.QTableWidgetItem(contratante))
        self.tableWidget.setItem(i,3,QtWidgets.QTableWidgetItem(monto))

    if self.checkBox_USAC.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2016_copia.json') :
        table_data = Tops_copias.top10_USAC(2016)
      else:
        table_data = Tops.top10_USAC(2016)
      QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 3)
      self.label.move(50,20)
      self.label.resize(800, 31)
      self.label.setText("Compras más grandes realizadas por la Universidad de San Carlos en el 2016")
      self.tableWidget.resize(270,365)  
      self.tableWidget.setColumnWidth(0, 160)
      self.tableWidget.setColumnWidth(1, 100) 
      self.tableWidget.setRowCount(10)
      self.tableWidget.setColumnCount(2)   
      self.tableWidget.setHorizontalHeaderLabels(["Contratante","Monto"])
      for i, [comprador, monto] in enumerate(table_data):
        self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(comprador))
        self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(monto))

    if self.checkBox_proveedores.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2016_copia.json') :
        table_data = Tops_copias.top10_prov(2016)
      else:
        table_data = Tops.top10_prov(2016)
      QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 3)
      self.label.move(210,20)
      self.label.setText("Proveedores que más vendieron en 2016")
      self.tableWidget.resize(270,365)  
      self.tableWidget.setColumnWidth(0, 160)
      self.tableWidget.setColumnWidth(1, 100) 
      self.tableWidget.setRowCount(10)
      self.tableWidget.setColumnCount(2)
      self.tableWidget.setHorizontalHeaderLabels(["Proveedor","Monto"])
      for i, [proveedor, monto] in enumerate(table_data):
        self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(proveedor))
        self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(str(monto)))

  def graficas2016(self):
    if self.checkBox_grandes.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2016_copia.json') :
        data = Tops_copias.top10(2016)
      else:
        data = Tops.top10(2016)
      self.graphicsView.plotItem.showGrid(True, True, 0.7)
      self.graphicsView.setMouseEnabled(x=False, y=False)
      x = []
      y = []
      for i, [comprador, monto] in enumerate(data):
        x.append(i+1)
        y.append(float(monto)) 
      bg1 = pg.BarGraphItem(x = x, height = y, width=0.5, brush=QtGui.QBrush(QtGui.QColor(159, 0, 170)))
      self.graphicsView.addItem(bg1)
      self.graphicsView.setXRange(1,10)

    if self.checkBox_mes.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2016_copia.json') :
        data = Tops_copias.topmes(2016)
      else:
        data = Tops.topmes(2016)
      self.graphicsView.plotItem.showGrid(True, True, 0.7)
      self.graphicsView.setMouseEnabled(x=False, y=False)
      x = []
      y = []
      for i, [mes, proveedor, contratante, monto] in enumerate(data):
        x.append(i+1)
        y.append(float(monto)) 
      bg1 = pg.BarGraphItem(x = x, height = y, width=0.5, brush=QtGui.QBrush(QtGui.QColor(85, 255, 0)))
      self.graphicsView.addItem(bg1)
      self.graphicsView.setXRange(1,12)

    if self.checkBox_USAC.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2016_copia.json') :
        data = Tops_copias.top10_USAC(2016)
      else:
        data = Tops.top10_USAC(2016)
      self.graphicsView.plotItem.showGrid(True, True, 0.7)
      self.graphicsView.setMouseEnabled(x=False, y=False)
      x = []
      y = []
      for i, [comprador, monto] in enumerate(data):
        x.append(i+1)
        y.append(float(monto)) 
      bg1 = pg.BarGraphItem(x = x, height = y, width=0.5, brush=QtGui.QBrush(QtGui.QColor(0, 145, 255)))
      self.graphicsView.addItem(bg1)
      self.graphicsView.setXRange(1,10)      

    if self.checkBox_proveedores.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2016_copia.json') :
        data = Tops_copias.top10_prov(2016)
      else:
        data = Tops.top10_prov(2016)
      self.graphicsView.plotItem.showGrid(True, True, 0.7)
      self.graphicsView.setMouseEnabled(x=False, y=False)
      x = []
      y = []
      for i, [comprador, monto] in enumerate(data):
        x.append(i+1)
        y.append(float(monto)) 
      bg1 = pg.BarGraphItem(x = x, height = y, width=0.5, brush=QtGui.QBrush(QtGui.QColor(255, 122, 5)))
      self.graphicsView.addItem(bg1)
      self.graphicsView.setXRange(1,10)

  def tablas2017(self):
    if self.checkBox_grandes_2.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2017_copia.json') :
        table_data = Tops_copias.top10(2017)
      else:
        table_data = Tops.top10(2017)
      QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 3)
      self.label.move(210,20) 
      self.label.setText("Compras más grandes realizadas en el 2017")
      self.tableWidget.resize(270,365)  
      self.tableWidget.setColumnWidth(0, 160)
      self.tableWidget.setColumnWidth(1, 100) 
      self.tableWidget.setRowCount(10)
      self.tableWidget.setColumnCount(2)
      self.tableWidget.setHorizontalHeaderLabels(["Contratante","Monto"])
      for i, [comprador, monto] in enumerate(table_data):
        self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(comprador))
        self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(monto))

    if self.checkBox_mes_2.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2017_copia.json') :
        table_data = Tops_copias.topmes(2017)
      else:
        table_data = Tops.topmes(2017)
      QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 3)
      self.label.move(210,20) 
      self.label.setText("Compras más grandes por mes en el 2017")
      self.tableWidget.move(30,100)
      self.tableWidget.resize(300,410)
      self.tableWidget.setRowCount(12)
      self.tableWidget.setColumnCount(4)
      self.tableWidget.setColumnWidth(0, 100)
      self.tableWidget.setColumnWidth(1, 150)
      self.tableWidget.setColumnWidth(2, 150)
      self.tableWidget.setColumnWidth(3, 100)
      self.tableWidget.setHorizontalHeaderLabels(["Mes","Proveedor","Contratante","Monto"])
      for i, [mes, proveedor, contratante, monto] in enumerate(table_data):
        self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(mes))
        self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(proveedor))
        self.tableWidget.setItem(i,2,QtWidgets.QTableWidgetItem(contratante))
        self.tableWidget.setItem(i,3,QtWidgets.QTableWidgetItem(monto))

    if self.checkBox_USAC_2.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2017_copia.json') :
        table_data = Tops_copias.top10_USAC(2017)
      else:
        table_data = Tops.top10_USAC(2017)
      QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 3)
      self.label.move(50,20) 
      self.label.resize(800, 31)
      self.label.setText("Compras más grandes realizadas por la Universidad de San Carlos en el 2017")
      self.tableWidget.resize(270,365)  
      self.tableWidget.setColumnWidth(0, 160)
      self.tableWidget.setColumnWidth(1, 100) 
      self.tableWidget.setRowCount(10)
      self.tableWidget.setColumnCount(2)   
      self.tableWidget.setHorizontalHeaderLabels(["Contratante","Monto"])
      for i, [comprador, monto] in enumerate(table_data):
        self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(comprador))
        self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(monto))

    if self.checkBox_proveedores_2.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2017_copia.json') :
        table_data = Tops_copias.top10_prov(2017)
      else:
        table_data = Tops.top10_prov(2017)
      QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 3)
      self.label.move(210,20)
      self.label.setText("Proveedores que más vendieron en 2017")
      self.tableWidget.resize(270,365)  
      self.tableWidget.setColumnWidth(0, 160)
      self.tableWidget.setColumnWidth(1, 100) 
      self.tableWidget.setRowCount(10)
      self.tableWidget.setColumnCount(2)
      self.tableWidget.setHorizontalHeaderLabels(["Proveedor","Monto"])
      for i, [proveedor, monto] in enumerate(table_data):
        self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(proveedor))
        self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(str(monto)))

  def graficas2017(self):
    if self.checkBox_grandes_2.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2017_copia.json') :
        data = Tops_copias.top10(2017)
      else:
        data = Tops.top10(2017)
      self.graphicsView.plotItem.showGrid(True, True, 0.7)
      self.graphicsView.setMouseEnabled(x=False, y=False)
      x = []
      y = []
      for i, [comprador, monto] in enumerate(data):
        x.append(i+1)
        y.append(float(monto)) 
      bg1 = pg.BarGraphItem(x = x, height = y, width=0.5, brush=QtGui.QBrush(QtGui.QColor(159, 0, 170)))
      self.graphicsView.addItem(bg1)
      self.graphicsView.setXRange(1,10)

    if self.checkBox_mes_2.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2017_copia.json') :
        data = Tops_copias.topmes(2017)
      else:
        data = Tops.topmes(2017)
      self.graphicsView.plotItem.showGrid(True, True, 0.7)
      self.graphicsView.setMouseEnabled(x=False, y=False)
      x = []
      y = []
      for i, [mes, proveedor, contratante, monto] in enumerate(data):
        x.append(i+1)
        y.append(float(monto)) 
      bg1 = pg.BarGraphItem(x = x, height = y, width=0.5, brush=QtGui.QBrush(QtGui.QColor(85, 255, 0)))
      self.graphicsView.addItem(bg1)
      self.graphicsView.setXRange(1,12)

    if self.checkBox_USAC_2.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2017_copia.json') :
        data = Tops_copias.top10_USAC(2017)
      else:
        data = Tops.top10_USAC(2017)
      self.graphicsView.plotItem.showGrid(True, True, 0.7)
      self.graphicsView.setMouseEnabled(x=False, y=False)
      x = []
      y = []
      for i, [comprador, monto] in enumerate(data):
        x.append(i+1)
        y.append(float(monto)) 
      bg1 = pg.BarGraphItem(x = x, height = y, width=0.5, brush=QtGui.QBrush(QtGui.QColor(0, 145, 255)))
      self.graphicsView.addItem(bg1)
      self.graphicsView.setXRange(1,10)   

    if self.checkBox_proveedores_2.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2017_copia.json') :
        data = Tops_copias.top10_prov(2017)
      else:
        data = Tops.top10_prov(2017)
      self.graphicsView.plotItem.showGrid(True, True, 0.7)
      self.graphicsView.setMouseEnabled(x=False, y=False)
      x = []
      y = []
      for i, [comprador, monto] in enumerate(data):
        x.append(i+1)
        y.append(float(monto)) 
      bg1 = pg.BarGraphItem(x = x, height = y, width=0.5, brush=QtGui.QBrush(QtGui.QColor(255, 122, 5)))
      self.graphicsView.addItem(bg1)
      self.graphicsView.setXRange(1,10)

  def tablas2018(self):
    if self.checkBox_grandes_4.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2018_copia.json') :
        table_data = Tops_copias.top10(2018)
      else:
        table_data = Tops.top10(2018)
      QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 3)
      self.label.move(210,20) 
      self.label.setText("Compras más grandes realizadas hasta octubre 2018")
      self.tableWidget.resize(270,365)  
      self.tableWidget.setColumnWidth(0, 160)
      self.tableWidget.setColumnWidth(1, 100) 
      self.tableWidget.setRowCount(10)
      self.tableWidget.setColumnCount(2)
      self.tableWidget.setHorizontalHeaderLabels(["Contratante","Monto"])
      for i, [comprador, monto] in enumerate(table_data):
        self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(comprador))
        self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(monto))

    if self.checkBox_mes_4.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2018_copia.json') :
        table_data = Tops_copias.topmes(2018)
      else:
        table_data = Tops.topmes(2018)
      QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 3)
      self.label.move(210,20)       
      self.label.setText("Compras más grandes por mes hasta octubre 2018")
      self.tableWidget.move(30,100)
      self.tableWidget.resize(300,410)
      self.tableWidget.setRowCount(10)
      self.tableWidget.setColumnCount(4)
      self.tableWidget.setColumnWidth(0, 100)
      self.tableWidget.setColumnWidth(1, 150)
      self.tableWidget.setColumnWidth(2, 150)
      self.tableWidget.setColumnWidth(3, 100)
      self.tableWidget.setHorizontalHeaderLabels(["Mes","Proveedor","Contratante","Monto"])
      for i, [mes, proveedor, contratante, monto] in enumerate(table_data):
        self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(mes))
        self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(proveedor))
        self.tableWidget.setItem(i,2,QtWidgets.QTableWidgetItem(contratante))
        self.tableWidget.setItem(i,3,QtWidgets.QTableWidgetItem(monto))

    if self.checkBox_USAC_4.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2018_copia.json') :
        table_data = Tops_copias.top10_USAC(2018)
      else:
        table_data = Tops.top10_USAC(2018)
      QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 3)
      self.label.move(50,20)
      self.label.resize(800, 31)
      self.label.setText("Compras más grandes realizadas por la Universidad de San Carlos hasta octubre 2018")
      self.tableWidget.resize(270,365)  
      self.tableWidget.setColumnWidth(0, 160)
      self.tableWidget.setColumnWidth(1, 100) 
      self.tableWidget.setRowCount(10)
      self.tableWidget.setColumnCount(2)   
      self.tableWidget.setHorizontalHeaderLabels(["Contratante","Monto"])
      for i, [comprador, monto] in enumerate(table_data):
        self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(comprador))
        self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(monto))

    if self.checkBox_proveedores_3.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2018_copia.json') :
        table_data = Tops_copias.top10_prov(2018)
      else:
        table_data = Tops.top10_prov(2018)
      QtWidgets.QTabWidget.setCurrentIndex(self.tabWidget, 3)
      self.label.move(210,20) 
      self.label.resize(800, 31)
      self.label.setText("Proveedores que más vendieron hasta octubre 2018")
      self.tableWidget.resize(270,365)  
      self.tableWidget.setColumnWidth(0, 160)
      self.tableWidget.setColumnWidth(1, 100) 
      self.tableWidget.setRowCount(10)
      self.tableWidget.setColumnCount(2)
      self.tableWidget.setHorizontalHeaderLabels(["Proveedor","Monto"])
      for i, [proveedor, monto] in enumerate(table_data):
        self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(proveedor))
        self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(str(monto)))

  def graficas2018(self):
    if self.checkBox_grandes_4.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2018_copia.json') :
        data = Tops_copias.top10(2018)
      else:
        data = Tops.top10(2018)
      self.graphicsView.plotItem.showGrid(True, True, 0.7)
      self.graphicsView.setMouseEnabled(x=False, y=False)
      x = []
      y = []
      for i, [comprador, monto] in enumerate(data):
        x.append(i+1)
        y.append(float(monto)) 
      bg1 = pg.BarGraphItem(x = x, height = y, width=0.5, brush=QtGui.QBrush(QtGui.QColor(159, 0, 170)))
      self.graphicsView.addItem(bg1)
      self.graphicsView.setXRange(1,10)

    if self.checkBox_mes_4.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2018_copia.json') :
        data = Tops_copias.topmes(2018)
      else:
        data = Tops.topmes(2018)
      self.graphicsView.plotItem.showGrid(True, True, 0.7)
      self.graphicsView.setMouseEnabled(x=False, y=False)
      x = []
      y = []
      for i, [mes, proveedor, contratante, monto] in enumerate(data):
        x.append(i+1)
        y.append(float(monto)) 
      bg1 = pg.BarGraphItem(x = x, height = y, width=0.5, brush=QtGui.QBrush(QtGui.QColor(85, 255, 0)))
      self.graphicsView.addItem(bg1)
      self.graphicsView.setXRange(1,10)

    if self.checkBox_USAC_4.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2018_copia.json') :
        data = Tops_copias.top10_USAC(2018)
      else:
        data = Tops.top10_USAC(2018)
      self.graphicsView.plotItem.showGrid(True, True, 0.7)
      self.graphicsView.setMouseEnabled(x=False, y=False)
      x = []
      y = []
      for i, [comprador, monto] in enumerate(data):
        x.append(i+1)
        y.append(float(monto)) 
      bg1 = pg.BarGraphItem(x = x, height = y, width=0.5, brush=QtGui.QBrush(QtGui.QColor(0, 145, 255)))
      self.graphicsView.addItem(bg1)
      self.graphicsView.setXRange(1,10)   

    if self.checkBox_proveedores_3.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2018_copia.json') :
        data = Tops_copias.top10_prov(2018)
      else:
        data = Tops.top10_prov(2018)
      self.graphicsView.plotItem.showGrid(True, True, 0.7)
      self.graphicsView.setMouseEnabled(x=False, y=False)
      x = []
      y = []
      for i, [comprador, monto] in enumerate(data):
        x.append(i+1)
        y.append(float(monto)) 
      bg1 = pg.BarGraphItem(x = x, height = y, width=0.5, brush=QtGui.QBrush(QtGui.QColor(255, 122, 5)))
      self.graphicsView.addItem(bg1)
      self.graphicsView.setXRange(1,10)

  def actualizar2016(self):
    current = os.getcwd()
    if os.path.isfile(current +'\\concurso_2016_copia.json') :
      with open(current + '\\concurso_2016_copia.json') as outfile:
        data = json.load(outfile)
    else:
      with open(current + '\\concurso_2016.json') as outfile:
        data = json.load(outfile)      
    nueva_info = {}
    entidad_padre = self.comboBox_padre.currentText()
    entidad = self.texto_entidad.text()
    compradora = self.texto_compradora.text()
    nog = self.texto_nog.text()
    modalidad = self.texto_modalidad.text()
    nit = self.texto_nit.text()
    monto = self.texto_monto.text()
    temp_publi = self.fecha_publicacion.date()
    publicacion = str(temp_publi.toPyDate())
    temp_mes_publi = temp_publi.month()
    if temp_mes_publi ==1:
      mes_publi = 'Enero'
    if temp_mes_publi ==2:
      mes_publi = 'Febrero'
    if temp_mes_publi ==3:
      mes_publi = 'Marzo'
    if temp_mes_publi ==4:
      mes_publi = 'Abril'
    if temp_mes_publi ==5:
      mes_publi = 'Mayo'
    if temp_mes_publi ==6:
      mes_publi = 'Junio'
    if temp_mes_publi ==7:
      mes_publi = 'Julio'
    if temp_mes_publi == 8:
      mes_publi = 'Agosto'
    if temp_mes_publi ==9:
      mes_publi = 'Septiembre'
    if temp_mes_publi ==10:
      mes_publi = 'Octubre'
    if temp_mes_publi ==11:
      mes_publi = 'Noviembre'
    if temp_mes_publi ==12:
      mes_publi = 'Diciembre'
    temp_adju = self.fecha_adjudicacion.date() 
    adjudicacion = str(temp_adju.toPyDate())
    nueva_info['TIPO DE ENTIDAD PADRE']= entidad_padre
    nueva_info['TIPO DE ENTIDAD']= entidad
    nueva_info['ENTIDAD COMPRADORA']= compradora
    nueva_info['NOG CONCURSO']= nog 
    nueva_info['MODALIDAD']= modalidad
    nueva_info['NIT']= nit
    nueva_info['MONTO']= monto
    nueva_info['FECHA DE PUBLICACIÓN']= publicacion
    nueva_info['MES DE PUBLICACIÓN']= mes_publi
    nueva_info['FECHA DE ADJUDICACIÓN']= adjudicacion
    print(nueva_info)
    data.append(nueva_info)
    with open(current + 'concurso_2016_copia.json', 'w') as outfile:
      json.dump(data, outfile) 
    print(data[len(data)-1])  

  def actualizar2017(self):
    current = os.getcwd()
    if os.path.isfile(current +'\\concurso_2017_copia.json') :
      with open(current + '\\concurso_2017_copia.json') as outfile:
        data = json.load(outfile)
    else:
      with open(current + '\\concurso_2017.json') as outfile:
        data = json.load(outfile)    
    nueva_info = {}
    entidad_padre = self.comboBox_padre_2.currentText()
    entidad = self.texto_entidad_2.text()
    compradora = self.texto_compradora_2.text()
    nog = self.texto_nog.text()
    modalidad = self.texto_modalidad_2.text()
    nit = self.texto_nit_2.text()
    monto = self.texto_monto_2.text()
    temp_publi = self.fecha_publicacion_2.date()
    publicacion = str(temp_publi.toPyDate())
    temp_mes_publi = temp_publi.month()
    if temp_mes_publi ==1:
      mes_publi = 'Enero'
    if temp_mes_publi ==2:
      mes_publi = 'Febrero'
    if temp_mes_publi ==3:
      mes_publi = 'Marzo'
    if temp_mes_publi ==4:
      mes_publi = 'Abril'
    if temp_mes_publi ==5:
      mes_publi = 'Mayo'
    if temp_mes_publi ==6:
      mes_publi = 'Junio'
    if temp_mes_publi ==7:
      mes_publi = 'Julio'
    if temp_mes_publi == 8:
      mes_publi = 'Agosto'
    if temp_mes_publi ==9:
      mes_publi = 'Septiembre'
    if temp_mes_publi ==10:
      mes_publi = 'Octubre'
    if temp_mes_publi ==11:
      mes_publi = 'Noviembre'
    if temp_mes_publi ==12:
      mes_publi = 'Diciembre'
    temp_adju = self.fecha_adjudicacion_2.date() 
    adjudicacion = str(temp_adju.toPyDate())
    nueva_info['TIPO DE ENTIDAD PADRE']= entidad_padre
    nueva_info['TIPO DE ENTIDAD']= entidad
    nueva_info['ENTIDAD COMPRADORA']= compradora
    nueva_info['NOG CONCURSO']= nog 
    nueva_info['MODALIDAD']= modalidad
    nueva_info['NIT']= nit
    nueva_info['MONTO']= monto
    nueva_info['FECHA DE PUBLICACIÓN']= publicacion
    nueva_info['MES DE PUBLICACIÓN']= mes_publi
    nueva_info['FECHA DE ADJUDICACIÓN']= adjudicacion
    data.append(nueva_info)
    with open(current + 'concurso_2017_copia.json', 'w') as outfile:
      json.dump(data, outfile) 

  def actualizar2018(self):
    current = os.getcwd()
    if os.path.isfile(current +'\\concurso_2018_copia.json') :
      with open(current + '\\concurso_2018_copia.json') as outfile:
        data = json.load(outfile)
    else:
      with open(current + '\\concurso_2018.json') as outfile:
        data = json.load(outfile)    
    nueva_info = {}
    entidad_padre = self.comboBox_padre_3.currentText()
    entidad = self.texto_entidad_3.text()
    compradora = self.texto_compradora_3.text()
    nog = self.texto_nog_3.text()
    modalidad = self.texto_modalidad_3.text()
    nit = self.texto_nit_3.text()
    monto = self.texto_monto_3.text()
    temp_publi = self.fecha_publicacion_3.date()
    publicacion = str(temp_publi.toPyDate())
    temp_mes_publi = temp_publi.month()
    if temp_mes_publi ==1:
      mes_publi = 'Enero'
    if temp_mes_publi ==2:
      mes_publi = 'Febrero'
    if temp_mes_publi ==3:
      mes_publi = 'Marzo'
    if temp_mes_publi ==4:
      mes_publi = 'Abril'
    if temp_mes_publi ==5:
      mes_publi = 'Mayo'
    if temp_mes_publi ==6:
      mes_publi = 'Junio'
    if temp_mes_publi ==7:
      mes_publi = 'Julio'
    if temp_mes_publi == 8:
      mes_publi = 'Agosto'
    if temp_mes_publi ==9:
      mes_publi = 'Septiembre'
    if temp_mes_publi ==10:
      mes_publi = 'Octubre'
    if temp_mes_publi ==11:
      mes_publi = 'Noviembre'
    if temp_mes_publi ==12:
      mes_publi = 'Diciembre'
    temp_adju = self.fecha_adjudicacion_3.date() 
    adjudicacion = str(temp_adju.toPyDate())
    nueva_info['TIPO DE ENTIDAD PADRE']= entidad_padre
    nueva_info['TIPO DE ENTIDAD']= entidad
    nueva_info['ENTIDAD COMPRADORA']= compradora
    nueva_info['NOG CONCURSO']= nog 
    nueva_info['MODALIDAD']= modalidad
    nueva_info['NIT']= nit
    nueva_info['MONTO']= monto
    nueva_info['FECHA DE PUBLICACIÓN']= publicacion
    nueva_info['MES DE PUBLICACIÓN']= mes_publi
    nueva_info['FECHA DE ADJUDICACIÓN']= adjudicacion
    data.append(nueva_info)
    with open(current + 'concurso_2018_copia.json', 'w') as outfile:
      json.dump(data, outfile) 

  def reportes(self):
    if self.checkBox_grandes.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2016_copia.json') :
        table_data = Tops_copias.top10(2016)
      else:
        table_data = Tops.top10(2016)
        geometry_options = { "margin": "2cm", "includeheadfoot": True}
        reporte = pylatex.Document(geometry_options=geometry_options)
        reporte.preamble.append(Command('title', self.label.text()))
        reporte.preamble.append(Command('date', NoEscape(r'\today')))
        reporte.append(NoEscape(r'\maketitle'))
        with reporte.create(Tabular('cl cl ')) as table:
            table.add_hline()
            table.add_row(["Contratante"] + ["Monto"], strict = False)
            table.add_hline()
            for i, [comprador, monto] in enumerate(table_data):
                table.add_row([comprador] +[monto], strict = False)
            table.add_hline()  
            xs = []
            ys = []
            for i, [comprador, monto] in enumerate(table_data):
                xs.append(i+1)
                ys.append(float(monto))
            plt.bar(xs,ys,width= 0.5, align='center', color="#800080")
            plt.xticks(xs,np.arange(1,10))
            plt.title('Grafica')
        with reporte.create(Figure(position="'htbp'")) as gragh:
            gragh.add_plot()
        reporte.generate_pdf(self.label.text(), clean_tex=True)

    if self.checkBox_grandes_2.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2017_copia.json') :
        table_data = Tops_copias.top10(2017)
      else:
        table_data = Tops.top10(2017)
        geometry_options = { "margin": "2cm", "includeheadfoot": True}
        reporte = pylatex.Document(geometry_options=geometry_options)
        reporte.preamble.append(Command('title', self.label.text()))
        reporte.preamble.append(Command('date', NoEscape(r'\today')))
        reporte.append(NoEscape(r'\maketitle'))
        with reporte.create(Tabular('cl cl ')) as table:
            table.add_hline()
            table.add_row(["Contratante"] + ["Monto"], strict = False)
            table.add_hline()
            for i, [comprador, monto] in enumerate(table_data):
                table.add_row([comprador] +[monto], strict = False)
            table.add_hline()  
            xs = []
            ys = []
            for i, [comprador, monto] in enumerate(table_data):
                xs.append(i+1)
                ys.append(float(monto))
            plt.bar(xs,ys,width= 0.5, align='center', color="#800080")
            plt.xticks(xs,np.arange(1,10))
            plt.title('Grafica')
        with reporte.create(Figure(position="'htbp'")) as gragh:
            gragh.add_plot()
        reporte.generate_pdf(self.label.text(), clean_tex=True)

    if self.checkBox_grandes_4.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2018_copia.json') :
        table_data = Tops_copias.top10(2018)
      else:
        table_data = Tops.top10(2018)
        geometry_options = { "margin": "2cm", "includeheadfoot": True}
        reporte = pylatex.Document(geometry_options=geometry_options)
        reporte.preamble.append(Command('title', self.label.text()))
        reporte.preamble.append(Command('date', NoEscape(r'\today')))
        reporte.append(NoEscape(r'\maketitle'))
        with reporte.create(Tabular('cl cl ')) as table:
            table.add_hline()
            table.add_row(["Contratante"] + ["Monto"], strict = False)
            table.add_hline()
            for i, [comprador, monto] in enumerate(table_data):
                table.add_row([comprador] +[monto], strict = False)
            table.add_hline()  
            xs = []
            ys = []
            for i, [comprador, monto] in enumerate(table_data):
                xs.append(i+1)
                ys.append(float(monto))
            plt.bar(xs,ys,width= 0.5, align='center', color="#800080")
            plt.xticks(xs,np.arange(1,10))
            plt.title('Grafica')
        with reporte.create(Figure(position="'htbp'")) as gragh:
            gragh.add_plot()
        reporte.generate_pdf(self.label.text(), clean_tex=True)

    if self.checkBox_mes.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2016_copia.json') :
        table_data = Tops_copias.topmes(2016)
      else:
        table_data = Tops.topmes(2016)
        geometry_options = { "margin": "2cm", "includeheadfoot": True}
        reporte = pylatex.Document(geometry_options=geometry_options)
        reporte.preamble.append(Command('title', self.label.text()))
        reporte.preamble.append(Command('date', NoEscape(r'\today')))
        reporte.append(NoEscape(r'\maketitle'))
        with reporte.create(Tabular('cl cl ')) as table:
            table.add_hline()
            table.add_row(["Contratante"] + ["Monto"], strict = False)
            table.add_hline()
            for i, [comprador, monto] in enumerate(table_data):
                table.add_row([comprador] +[monto], strict = False)
            table.add_hline()  
            xs = []
            ys = []
            for i, [comprador, monto] in enumerate(table_data):
                xs.append(i+1)
                ys.append(float(monto))
            plt.bar(xs,ys,width= 0.5, align='center', color="#00FF00")
            plt.xticks(xs,np.arange(1,10))
            plt.title('Grafica')
        with reporte.create(Figure(position="'htbp'")) as gragh:
            gragh.add_plot()
        reporte.generate_pdf(self.label.text(), clean_tex=True)

    if self.checkBox_mes_2.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2017_copia.json') :
        table_data = Tops_copias.topmes(2017)
      else:
        table_data = Tops.topmes(2017)
        geometry_options = { "margin": "2cm", "includeheadfoot": True}
        reporte = pylatex.Document(geometry_options=geometry_options)
        reporte.preamble.append(Command('title', self.label.text()))
        reporte.preamble.append(Command('date', NoEscape(r'\today')))
        reporte.append(NoEscape(r'\maketitle'))
        with reporte.create(Tabular('cl cl ')) as table:
            table.add_hline()
            table.add_row(["Contratante"] + ["Monto"], strict = False)
            table.add_hline()
            for i, [comprador, monto] in enumerate(table_data):
                table.add_row([comprador] +[monto], strict = False)
            table.add_hline()  
            xs = []
            ys = []
            for i, [comprador, monto] in enumerate(table_data):
                xs.append(i+1)
                ys.append(float(monto))
            plt.bar(xs,ys,width= 0.5, align='center', color="#00FF00")
            plt.xticks(xs,np.arange(1,10))
            plt.title('Grafica')
        with reporte.create(Figure(position="'htbp'")) as gragh:
            gragh.add_plot()
        reporte.generate_pdf(self.label.text(), clean_tex=True)

    if self.checkBox_mes_4.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2018_copia.json') :
        table_data = Tops_copias.topmes(2018)
      else:
        table_data = Tops.topmes(2018)
        geometry_options = { "margin": "2cm", "includeheadfoot": True}
        reporte = pylatex.Document(geometry_options=geometry_options)
        reporte.preamble.append(Command('title', self.label.text()))
        reporte.preamble.append(Command('date', NoEscape(r'\today')))
        reporte.append(NoEscape(r'\maketitle'))
        with reporte.create(Tabular('cl cl ')) as table:
            table.add_hline()
            table.add_row(["Contratante"] + ["Monto"], strict = False)
            table.add_hline()
            for i, [comprador, monto] in enumerate(table_data):
                table.add_row([comprador] +[monto], strict = False)
            table.add_hline()  
            xs = []
            ys = []
            for i, [comprador, monto] in enumerate(table_data):
                xs.append(i+1)
                ys.append(float(monto))
            plt.bar(xs,ys,width= 0.5, align='center', color="#00FF00")
            plt.xticks(xs,np.arange(1,10))
            plt.title('Grafica')
        with reporte.create(Figure(position="'htbp'")) as gragh:
            gragh.add_plot()
        reporte.generate_pdf(self.label.text(), clean_tex=True)

    if self.checkBox_USAC.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2016_copia.json') :
        table_data = Tops_copias.top10_USAC(2016)
      else:
        table_data = Tops.top10_USAC(2016)
        geometry_options = { "margin": "2cm", "includeheadfoot": True}
        reporte = pylatex.Document(geometry_options=geometry_options)
        reporte.preamble.append(Command('title', self.label.text()))
        reporte.preamble.append(Command('date', NoEscape(r'\today')))
        reporte.append(NoEscape(r'\maketitle'))
        with reporte.create(Tabular('cl cl ')) as table:
            table.add_hline()
            table.add_row(["Contratante"] + ["Monto"], strict = False)
            table.add_hline()
            for i, [comprador, monto] in enumerate(table_data):
                table.add_row([comprador] +[monto], strict = False)
            table.add_hline()  
            xs = []
            ys = []
            for i, [comprador, monto] in enumerate(table_data):
                xs.append(i+1)
                ys.append(float(monto))
            plt.bar(xs,ys,width= 0.5, align='center', color="#008080")
            plt.xticks(xs,np.arange(1,10))
            plt.title('Grafica')
        with reporte.create(Figure(position="'htbp'")) as gragh:
            gragh.add_plot()
        reporte.generate_pdf(self.label.text(), clean_tex=True)

    if self.checkBox_USAC_2.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2017_copia.json') :
        table_data = Tops_copias.top10_USAC(2017)
      else:
        table_data = Tops.top10_USAC(2017)
        geometry_options = { "margin": "2cm", "includeheadfoot": True}
        reporte = pylatex.Document(geometry_options=geometry_options)
        reporte.preamble.append(Command('title', self.label.text()))
        reporte.preamble.append(Command('date', NoEscape(r'\today')))
        reporte.append(NoEscape(r'\maketitle'))
        with reporte.create(Tabular('cl cl ')) as table:
            table.add_hline()
            table.add_row(["Contratante"] + ["Monto"], strict = False)
            table.add_hline()
            for i, [comprador, monto] in enumerate(table_data):
                table.add_row([comprador] +[monto], strict = False)
            table.add_hline()  
            xs = []
            ys = []
            for i, [comprador, monto] in enumerate(table_data):
                xs.append(i+1)
                ys.append(float(monto))
            plt.bar(xs,ys,width= 0.5, align='center', color="#008080")
            plt.xticks(xs,np.arange(1,10))
            plt.title('Grafica')
        with reporte.create(Figure(position="'htbp'")) as gragh:
            gragh.add_plot()
        reporte.generate_pdf(self.label.text(), clean_tex=True)

    if self.checkBox_USAC_4.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2018_copia.json') :
        table_data = Tops_copias.top10_USAC(2018)
      else:
        table_data = Tops.top10_USAC(2018)
        geometry_options = { "margin": "2cm", "includeheadfoot": True}
        reporte = pylatex.Document(geometry_options=geometry_options)
        reporte.preamble.append(Command('title', self.label.text()))
        reporte.preamble.append(Command('date', NoEscape(r'\today')))
        reporte.append(NoEscape(r'\maketitle'))
        with reporte.create(Tabular('cl cl ')) as table:
            table.add_hline()
            table.add_row(["Contratante"] + ["Monto"], strict = False)
            table.add_hline()
            for i, [comprador, monto] in enumerate(table_data):
                table.add_row([comprador] +[monto], strict = False)
            table.add_hline()  
            xs = []
            ys = []
            for i, [comprador, monto] in enumerate(table_data):
                xs.append(i+1)
                ys.append(float(monto))
            plt.bar(xs,ys,width= 0.5, align='center', color="#008080")
            plt.xticks(xs,np.arange(1,10))
            plt.title('Grafica')
        with reporte.create(Figure(position="'htbp'")) as gragh:
            gragh.add_plot()
        reporte.generate_pdf(self.label.text(), clean_tex=True)

    if self.checkBox_proveedores.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2016_copia.json') :
        table_data = Tops_copias.top10_prov(2016)
      else:
        table_data = Tops.top10_prov(2016)
        geometry_options = { "margin": "2cm", "includeheadfoot": True}
        reporte = pylatex.Document(geometry_options=geometry_options)
        reporte.preamble.append(Command('title', self.label.text()))
        reporte.preamble.append(Command('date', NoEscape(r'\today')))
        reporte.append(NoEscape(r'\maketitle'))
        with reporte.create(Tabular('cl cl ')) as table:
            table.add_hline()
            table.add_row(["Contratante"] + ["Monto"], strict = False)
            table.add_hline()
            for i, [comprador, monto] in enumerate(table_data):
                table.add_row([comprador] +[monto], strict = False)
            table.add_hline()  
            xs = []
            ys = []
            for i, [comprador, monto] in enumerate(table_data):
                xs.append(i+1)
                ys.append(float(monto))
            plt.bar(xs,ys,width= 0.5, align='center', color="#FF4500")
            plt.xticks(xs,np.arange(1,10))
            plt.title('Grafica')
        with reporte.create(Figure(position="'htbp'")) as gragh:
            gragh.add_plot()
        reporte.generate_pdf(self.label.text(), clean_tex=True)

    if self.checkBox_proveedores_2.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2017_copia.json') :
        table_data = Tops_copias.top10_prov(2017)
      else:
        table_data = Tops.top10_prov(2017)
        geometry_options = { "margin": "2cm", "includeheadfoot": True}
        reporte = pylatex.Document(geometry_options=geometry_options)
        reporte.preamble.append(Command('title', self.label.text()))
        reporte.preamble.append(Command('date', NoEscape(r'\today')))
        reporte.append(NoEscape(r'\maketitle'))
        with reporte.create(Tabular('cl cl ')) as table:
            table.add_hline()
            table.add_row(["Contratante"] + ["Monto"], strict = False)
            table.add_hline()
            for i, [comprador, monto] in enumerate(table_data):
                table.add_row([comprador] +[monto], strict = False)
            table.add_hline()  
            xs = []
            ys = []
            for i, [comprador, monto] in enumerate(table_data):
                xs.append(i+1)
                ys.append(float(monto))
            plt.bar(xs,ys,width= 0.5, align='center', color="#FF4500")
            plt.xticks(xs,np.arange(1,10))
            plt.title('Grafica')
        with reporte.create(Figure(position="'htbp'")) as gragh:
            gragh.add_plot()
        reporte.generate_pdf(self.label.text(), clean_tex=True)

    if self.checkBox_proveedores_4.isChecked() == True:
      if os.path.isfile(current +'\\concurso_2018_copia.json') :
        table_data = Tops_copias.top10_prov(2018)
      else:
        table_data = Tops.top10_prov(2018)
        geometry_options = { "margin": "2cm", "includeheadfoot": True}
        reporte = pylatex.Document(geometry_options=geometry_options)
        reporte.preamble.append(Command('title', self.label.text()))
        reporte.preamble.append(Command('date', NoEscape(r'\today')))
        reporte.append(NoEscape(r'\maketitle'))
        with reporte.create(Tabular('cl cl ')) as table:
            table.add_hline()
            table.add_row(["Contratante"] + ["Monto"], strict = False)
            table.add_hline()
            for i, [comprador, monto] in enumerate(table_data):
                table.add_row([comprador] +[monto], strict = False)
            table.add_hline()  
            xs = []
            ys = []
            for i, [comprador, monto] in enumerate(table_data):
                xs.append(i+1)
                ys.append(float(monto))
            plt.bar(xs,ys,width= 0.5, align='center', color="#FF4500")
            plt.xticks(xs,np.arange(1,10))
            plt.title('Grafica')
        with reporte.create(Figure(position="'htbp'")) as gragh:
            gragh.add_plot()
        reporte.generate_pdf(self.label.text(), clean_tex=True)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MyWindow = Ventana_principal()
    MyWindow.show()
    app.exec_()