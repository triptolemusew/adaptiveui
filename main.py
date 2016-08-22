import json
import sys

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QLabel


class myWindow(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(0)
        self.setMaximumSize(1280, 720)
        self.setMinimumSize(1280, 720)
        self.setWindowTitle('App Test 1.0')
        self.setObjectName("asd")

        # Buttons
        self.Button = QtGui.QPushButton('Button 1', self)
        self.Button.setGeometry(1020, 680, 110, 30)
        self.Button2 = QtGui.QPushButton('Button 2', self)
        self.Button2.setGeometry(1150, 680, 110, 30)
        self.Button3 = QtGui.QPushButton('Change to different settings!', self)
        self.Button3.setGeometry(10, 10, 170, 30)
        self.Button3.setMinimumWidth(200)
        self.Button4 = QtGui.QPushButton('Change background color', self)
        self.Button4.setGeometry(540, 10, 170, 30)

        # ComboBox
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.addItem('Settings 1')
        self.comboBox.addItem('Settings 2')
        self.comboBox.addItem('Settings 3')
        self.comboBox.setGeometry(240, 10, 170, 30)
        # self.comboBox.activated[str].connect(self.settingsChoice) # For instant select in QComboBox

        # TextEdit box
        self.textEdit = QtGui.QLineEdit(self)
        self.textEdit.setGeometry(50, 685, 950, 20)
        self.setGeometry(200, 200, 300, 100)

        self.Button2.setAutoRepeat(True)
        self.Button2.setAutoRepeatDelay(1000)
        self.Button2.setAutoRepeatInterval(1000)

        # Color

        hbox.addWidget(self.Button)
        hbox.addWidget(self.Button2)
        hbox.addWidget(self.Button3)
        hbox.addWidget(self.comboBox)
        hbox.addWidget(self.textEdit)

        self.Button2.clicked.connect(self.onChanged)
        self.Button3.clicked.connect(self.settingsChoice)
        self.Button4.clicked.connect(self.changeBackground)

        vbox = QtGui.QVBoxLayout()
        vbox.addStretch(0)
        vbox.addLayout(hbox)

        self.setLayout(hbox)
        self._state = 0
        self._background_clicked = 0

        # self.Button3 = QtGui.QPushButton('Add Json thingy')
        # self.Button4 = QtGui.QPushButton('Add JSON file')
        # myLayout.addStretch(1)
        # self.Button.move(1100, 600)

        # myLayout.addWidget(self.Button2)
        # myLayout.addWidget(self.Button3)
        # myLayout.addWidget(self.Button4)
        # Button.setMinimumWidth(200)
        # self.Button2.setMinimumWidth(200)
        # self.Button3.setMinimumWidth(200)
        # self.Button4.setMinimumWidth(200)
        # Button.clicked.connect(self.resizeDialog)
        # self.Button2.clicked.connect(self.resizeButton)
        # self.Button3.clicked.connect(self.addJSON)
        # self.Button4.clicked.connect(self.selectFile)
    def getBackColor(self):
        return self.palette().color(QtGui.QPalette.Background)

    def setBackColor(self, color):
        pal = self.palette()
        pal.setColor(QtGui.QPalette.Background, color)
        self.setPalette(pal)

    def changeBackground(self):
        color1 = QtGui.QColor(255, 0, 0)
        color2 = QtGui.QColor(0, 255, 0)

        self.color = QtCore.QPropertyAnimation(self, 'backColor')
        self.color.setStartValue(color1)
        self.color.setKeyValueAt(0.5, color2)
        self.color.setEndValue(color1)
        self.color.setDuration(1000)
        self.color.setLoopCount(-1)
        self.color.start()

    def settingsChoice(self):
        # self.style_choice.setText(text)
        # QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))
        if str(self.comboBox.currentText()) == 'Settings 1':
            self.settings(1)
        elif str(self.comboBox.currentText()) == 'Settings 2':
            self.settings(2)
        else:
            print "No input"

    def settings(self, choice):
        if choice == 1:
            self.resizeButton(self.Button, 300, 500, 200, 200)
        elif choice == 2:
            self.resizeButton(self.Button2, 1000, 0, 300, 100)
        else:
            print "No input"

    def resizeDialog(self):
        self.animation = QtCore.QPropertyAnimation(self, "size")
        # self.animation.setDuration(1000) #Default 250ms
        if self.size().width() == 200:
            self.animation.setEndValue(QtCore.QSize(600, 300))
        else:
            self.animation.setEndValue(QtCore.QSize(200, 100))
        self.animation.start()

    def onChanged(self):
        print self.textEdit.text()
        if self.Button2.isDown():
            if self._state == 0:
                self._state = 1
                self.Button2.setAutoRepeatInterval(100)
                print 'press'
            else:
                print 'repeat'
        elif self._state == 1:
            self._state = 0
            self.Button2.setAutoRepeatInterval(1000)
            print 'release'
        else:
            print 'click'

    def resizeButton(self, button, location_x, location_y, width, height):
        self.animation = QtCore.QPropertyAnimation(button, "geometry")
        # self.animation.setDuration(10000)
        # self.animation.setStartValue(QtCore.QSize(100, 30))
        self.animation.setEndValue(QtCore.QRect(location_x, location_y, width, height))
        self.animation.start()

    # Below is for importing profiles
    def selectFile(self):
        self.fileDialog = QtGui.QFileDialog.getOpenFileName(self)
        # self.fileDialog.show()
        # print x
        print self.fileDialog
        with open(self.fileDialog) as data_file:
            data_json = json.load(data_file)
        f = open(self.fileDialog, 'r')
        data = f.read()
        print data_json["maps"]
        print type(data)

    def addJSON(self):
        with open('file.json') as data_file:
            data = json.load(data_file)

        # pprint(data)
        print data["maps"]

    def mousePressEvent(self, QMouseEvent):
        print QMouseEvent.pos()
        self._background_clicked += 1
        print self._background_clicked

    def mouseReleaseEvent(self, QMouseEvent):
        cursor = QtGui.QCursor()
        print cursor.pos()

    backColor = QtCore.pyqtProperty(QtGui.QColor, getBackColor, setBackColor)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('myApp')
    dialog = myWindow()

    # TODO: Need to make another separate file for driver
    dialog.show()
    sys.exit(app.exec_())
