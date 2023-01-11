import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from pptx import Presentation   


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('pptTransform')
        self.setGeometry(300, 300, 1000, 600)
        self.setWindowIcon(QIcon('powerpoint.png'))
        

        self.qte = QTextEdit(self)   ## self.qte 안 하니 button_clicked 시, qte를 attribute로 인식 못함.
        self.qte.setGeometry(50,50,600,500)
        
        
        self.qbtn1 = QPushButton('생성하기',self)
        self.qbtn1.setGeometry(650,50,300,100)
        self.qbtn1.clicked.connect(self.button_clicked)

        
        
        self.show()
        
    def button_clicked(self):
        lyrics = self.qte.toPlainText()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())