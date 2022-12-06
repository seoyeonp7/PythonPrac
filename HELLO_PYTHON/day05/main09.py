import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("main09.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb1.clicked.connect(self.myClick)
        self.pb2.clicked.connect(self.myClick)
        self.pb3.clicked.connect(self.myClick)
        self.pb4.clicked.connect(self.myClick)
        self.pb5.clicked.connect(self.myClick)
        self.pb6.clicked.connect(self.myClick)
        self.pb7.clicked.connect(self.myClick)
        self.pb8.clicked.connect(self.myClick)
        self.pb9.clicked.connect(self.myClick)
        self.pb0.clicked.connect(self.myClick)
        self.pbCall.clicked.connect(self.myCall)
        
    def myClick(self,num):
        str_old = self.le.text()
        str_new = str_old + self.sender().text()
        
        self.le.setText(str_new)
    
    def myCall(self):
        str_tel = self.le.text()
        QMessageBox.question(None,'Calling',"Calling "+str(str_tel),QMessageBox.Yes,QMessageBox.NoButton)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()