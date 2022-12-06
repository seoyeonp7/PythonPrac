import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("main06.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btn_clicked)
        
    def btn_clicked(self):
        dan = self.le.text()
        idan = int(dan)
        result = ""
        for i in range(1,10):
            # result += str(idan)+"*"+str(i)+"="+str(idan*i)+"\n"
            result += f"{idan}*{i}={idan*i}\n"
        
        self.te.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    