
#!/usr/bin/python
# -*- coding: utf-8 -*-
# Convierte temperaturas F a C viceversa 
# Esqueleto de uso diario
# Por ________________
# Solo recordando que este templete esta para la versión QT4 y no es funcional QT5 nueva versiones

# Favor de checar este URL: https://pythonspot.com/category/pyqt5/

import sys
from PyQt5 import QtCore, QtGui, uic
 
qtCreatorFile = "conversionFC.ui"   # este se cambia por el de Uds.
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # AQUI VAN LOS BOTONES
        self.cmdDeCaF.clicked.connect(self.DeCaF)
        self.cmdDeFaC.clicked.connect(self.DeFaC)
        self.cmdSalir.clicked.connect(self.Salir)


    
# Una cosa son Botones y otra son Funciones, deben ser nombre únicos.
# Cuidar la identación, es lo parte que exige python.
  
   # De C a F      
    def DeCaF(self):
        cel = float(self.txtC.text())      
        fahr = cel * 9 / 5.0 + 32
        self.txtF.setValue(int(fahr + 0.5))

        
   # De F a C     
    def DeFaC(self):
        fahr = self.txtF.value()
        cel = ((fahr - 32) * 5) / 9
        self.txtC.setText(str(cel))
     
        
    # Cerrar y salir    
    def Salir(self):
        QtGui.qApp.closeAllWindows()
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())