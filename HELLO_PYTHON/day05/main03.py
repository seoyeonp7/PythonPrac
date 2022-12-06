import sys
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("main03.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btn_clicked)
        
    def btn_clicked(self):
        
        # arr45 = [1,2,3,4,5,6,7,8,
        # 9,10,11,12,13,14,15,16,17,
        # 18,19,20,21,22,23,24,25,26,27,
        # 28,29,30,31,32,33,34,35,36,37,
        # 38,39,40,41,42,43,44,45]        
        #
        # for i in range(1000):
        #     rnd = int(random()*45)
        #     a = arr45[0]
        #     arr45[0] = arr45[rnd]
        #     arr45[rnd] = a
        
        lotto=[]
        while True:
            num = random.randint(1,45)
            if num not in lotto:
                lotto.append(num)
            if len(lotto) == 6:
                break
       
            
        self.le1.setText(str(lotto[0]))
        self.le2.setText(str(lotto[1]))
        self.le3.setText(str(lotto[2]))
        self.le4.setText(str(lotto[3]))
        self.le5.setText(str(lotto[4]))
        self.le6.setText(str(lotto[5])) 
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
    