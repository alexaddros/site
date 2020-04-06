import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

 
class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('C:/Users/skopc/Desktop/Final/scroll/main.ui', self)
        self.initUI()
    
    def initUI(self):
        self.pushButton.clicked.connect(self.send)
        self.setWindowTitle('Sender')  

    def send(self):
        title = self.title.text()
        text = self.text.toPlainText()
        sign = self.sign.text()
        title, text, sign
    
    def connect_and_send(self, data):
        

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
