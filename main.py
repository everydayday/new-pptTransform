import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit
from PyQt5.QtWidgets import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('pptTransform')
        self.setGeometry(300, 300, 1000, 600)
        
    

        qte = QTextEdit(self)
        qte.setGeometry(50,50,600,500)
        
        
        qbtn1 = QPushButton('생성하기',self)
        qbtn1.setGeometry(650,50,300,100)
        qbtn1.clicked.connect(self.button_clicked)

        
        
        self.show()
        
    def button_clicked(self):
        print('button')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())