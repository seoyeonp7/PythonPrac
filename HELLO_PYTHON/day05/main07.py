import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("main07.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btn_clicked)
        self.le_mine.returnPressed.connect(self.btn_clicked)
        
    def btn_clicked(self):

        mine = self.le_mine.text()
        com=""
        result=""
        
        rdm = random.random()
        if rdm>0.66:
            com = "가위"
        elif rdm>0.33:
            com = "바위"
        else :
            com = "보"
        
        if com =="가위" and mine=="가위": result="비김"
        if com =="가위" and mine=="바위": result="이김"
        if com =="가위" and mine=="보": result="짐"
        
        if com =="바위" and mine=="가위": result="짐"
        if com =="바위" and mine=="바위": result="비김"
        if com =="바위" and mine=="보": result="이김"
        
        if com =="보" and mine=="가위": result="이김"
        if com =="보" and mine=="바위": result="짐"
        if com =="보" and mine=="보": result="비김"
        
        self.le_com.setText(com)
        self.le_result.setText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    