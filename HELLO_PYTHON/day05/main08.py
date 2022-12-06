import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("main08.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myClick)
        
    def drawLine(self,cnt):
        ret =""
        for i in range(cnt):
            ret+="*"
        ret+="\n"
        return ret;
    
    def myClick(self):
        etf = int(self.le_f.text())
        etl = int(self.le_l.text())
        txt=""
        
        for i in range(etf,etl+1):
            txt += self.drawLine(i)
            
        self.pte.setPlainText(txt)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    