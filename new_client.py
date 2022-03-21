from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.Qt import QUrl, QDesktopServices
import requests
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Client")
        self.setFixedSize(400, 400)
        self.label1 = QLabel("Enter your hostname:", self)
        self.text = QLineEdit(self)
        self.text.move(10, 30)
        self.label2 = QLabel("Answer:", self)
        self.label2.move(10, 60)

        self.label3 = QLabel("Enter your api key:", self)
        self.text = QLineEdit(self)
        self.text.move(10, 30)
        self.label4 = QLabel("Answer:", self)
        self.label4.move(10, 60)

        self.label5 = QLabel("Enter the IP of site to geolocate:", self)
        self.text = QLineEdit(self)
        self.text.move(10, 30)
        self.label6 = QLabel("Answer:", self)
        self.label6.move(10, 60)

        self.button = QPushButton("Send", self)
        self.button.move(10, 90)

        self.button.clicked.connect(self.on_click)
        self.button.pressed.connect(self.on_click)

        self.show()

    def on_click(self):
        hostname = self.text.text()
        api_key = self.text.text()
        ip = self.text.text()

        if hostname == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(hostname)
            if res:
                self.label2.setText("Answer%s" % (res["Hello"]))
                self.label2.adjustSize()
                self.show()

        if api_key == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(api_key)
            if res:
                self.label3.setText("Answer%s" % (res["Hello"]))
                self.label3.adjustSize()
                self.show()

        if ip == "":
            QMessageBox.about(self, "Error", "Please fill the field")
        else:
            res = self.__query(ip)
            if res:
                self.label5.setText("Answer%s" % (res["Hello"]))
                self.label5.adjustSize()
                self.show()

    def __query(self, hostname, api_key, ip):
        url = "http://hostname=%sapi_key=%sip=%s" % (hostname,api_key,ip)
        r = requests.get(url)
        print(r.content[:1000])
        if r.status_code == requests.codes.NOT_FOUND:
            QMessageBox.about(self, "Error", "IP not found")
        if r.status_code == requests.codes.OK:
            return r.json()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    app.exec_()
