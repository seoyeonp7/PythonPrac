import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("main04.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btn_clicked)
        
    def btn_clicked(self):
        
        arr=["짝","홀"]
        rdm = random.randint(0,1)
        result=""
        
        leMine = self.leMine.text()
        leCom = str(arr[rdm])
        
        if leCom==leMine:
            result="승리!"
        else :
            result="패배!"
        
        self.leCom.setText(leCom)
        self.leResult.setText(result)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    