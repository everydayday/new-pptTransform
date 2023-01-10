import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('pptTransform')
        self.setGeometry(300, 300, 1000, 600)
        
    

        qte = QTextEdit(self)
        qte.setGeometry(0,0,600,500)
        # qte.move(0, 0)

        
        
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())