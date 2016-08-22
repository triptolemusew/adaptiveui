from PyQt4 import QtGui
import sys

imagePath = "C:/Users/danial/Desktop/project/adaptiveui/IG/"
print imagePath
class ImgWidget1(QtGui.QLabel):

    def __init__(self, parent=None):
        super(ImgWidget1, self).__init__(parent)
        pic = QtGui.QPixmap(imagePath)
        print imagePath
        self.setPixmap(pic)

class ImgWidget2(QtGui.QWidget):

    def __init__(self, parent=None):
        super(ImgWidget2, self).__init__(parent)
        print imagePath
        self.pic = QtGui.QPixmap(imagePath)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(0, 0, self.pic)


class Widget(QtGui.QWidget):

    def __init__(self):
        super(Widget, self).__init__()
        tableWidget = QtGui.QTableWidget(10, 2, self)
        tableWidget.setCellWidget(0, 1, ImgWidget1(self))
        tableWidget.setCellWidget(1, 1, ImgWidget2(self))

if __name__ == "__main__":
    app = QtGui.QApplication([])
    wnd = Widget()
    wnd.show()
    sys.exit(app.exec_())