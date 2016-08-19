import sys, os
from PyQt4 import QtCore, QtGui


class userList(QtGui.QListWidget):
    def Clicked(self, item):
        QtGui.QMessageBox.information(self, "ListWidget", "You clicked: " + item.text())


class mainWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(0)
        self.name = ''
        self.setMaximumSize(600, 480)
        self.setMinimumSize(600, 480)

        self.list = QtGui.QListWidget(self)
        self.select_user = QtGui.QPushButton('Select User', self)
        self.enter_button = QtGui.QPushButton('ENTER', self)
        self.userName = QtGui.QLineEdit(self)
        self.userPass = QtGui.QLineEdit(self)
        self.userLabel = QtGui.QLabel('Enter Username:', self)
        self.passLabel = QtGui.QLabel('Enter Password:', self)
        self.user_selected_label = QtGui.QLabel('You are ', self)
        self.userPass.setEchoMode(QtGui.QLineEdit.Password)

        self.userName.setPlaceholderText("Enter username here")
        self.userPass.setPlaceholderText("Enter password here")
        self.list.addItem("Item 1")
        self.list.addItem("Item 2")
        self.list.addItem("Item 3")
        self.list.addItem("Item 4")
        self.select_user.clicked.connect(self.select_user_clicked)

        # Layout management
        self.list.setGeometry(10, 10, 100, 400)
        self.select_user.setGeometry(10, 430, 100, 30)
        self.userLabel.move(200, 420)
        self.passLabel.move(200, 450)
        self.user_selected_label.setGeometry(200, 390, 100, 10)
        self.userName.setGeometry(300, 415, 150, 25)
        self.userPass.setGeometry(300, 445, 150, 25)
        self.enter_button.setGeometry(490, 400, 100, 80)

        hbox.addWidget(self.list)
        hbox.addWidget(self.select_user)
        hbox.addWidget(self.userName)
        hbox.addWidget(self.userPass)
        hbox.addWidget(self.userLabel)
        hbox.addWidget(self.passLabel)
        hbox.addWidget(self.enter_button)
        hbox.addWidget(self.user_selected_label)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(0)
        vbox.addLayout(hbox)
        self.setLayout(hbox)
        self.show()

    def select_user_clicked(self):
        self.name = self.list.currentItem().text()
        print self.list.currentItem().text()
        self.user_selected_label.setText('You are ' + self.name)

def main():
    app = QtGui.QApplication(sys.argv)
    loginDialog = mainWindow()
    loginDialog.setWindowTitle("User Login")
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
