import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("main0x.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.com ="123"
        self.setComRandom()
        self.pb.clicked.connect(self.myClick)
        
    def setComRandom(self):
        arr9 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
        for i in range(1000):
            rnd = int(random()*9)
    
            a = arr9[0]
            arr9[0] = arr9[rnd]
            arr9[rnd] = a
        
        self.com  = str(arr9[0])+""+str(arr9[1])+""+str(arr9[2])
        print("com111",self.com)
        
    def myClick(self):
        print("myClick실행")
        
        mine = self.le.text()
        print("com",self.com)
        s = self.getStrike(mine,self.com)
        b = self.getBall(mine,self.com)
        
        str_old = self.te.toPlainText()
        str_new = mine+" "+str(s)+"S"+str(b)+"B\n"
        
        self.te.setText(str_old+str_new)
        self.le.setText("")
        
        if s==3: 
            QMessageBox.question(None,'야구게임',self.com +"을(를) 맞혔습니다.",QMessageBox.Yes,QMessageBox.NoButton)

    
    def getStrike(self,mine,com):
        print("getStrike실행")
        ret = 0
        m1 = mine[0:1]
        m2 = mine[1:2]
        m3 = mine[2:3]
        
        c1 = com[0:1]
        c2 = com[1:2]
        c3 = com[2:3]
        
        if c1==m1 : ret+=1
        if c2==m2 : ret+=1
        if c3==m3 : ret+=1
        
        return ret
    
    def getBall(self,mine,com):
        print("getBall실행")
        ret = 0
        m1 = mine[0:1]
        m2 = mine[1:1]
        m3 = mine[2:1]
        
        c1 = com[0:1]
        c2 = com[1:2]
        c3 = com[2:3]
        
        if c1==m2 or c1==m3: ret+=1
        if c2==m1 or c2==m3: ret+=1
        if c3==m1 or c2==m2: ret+=1
        
        return ret
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()