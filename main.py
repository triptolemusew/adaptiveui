# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fusemuse_4.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore, QtGui
from PyQt4 import phonon
from PyQt4.phonon import Phonon
from facerec.model import PredictableModel
from facerec.feature import Fisherfaces
from facerec.distance import EuclideanDistance
from facerec.classifier import NearestNeighbor
from facerec.validation import KFoldCrossValidation
from facerec.serialization import save_model, load_model
# for face detection (you can also use OpenCV2 directly):
from facedet.detector import CascadedDetector
import cv2
import sys
import glob, os

from helper.common import *
from helper.video import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self._state = 0
        self.gender = ""
        self._background_clicked = 0
        self.setObjectName(_fromUtf8("MainWindow"))
        self.resize(1254, 872)
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.page_3)
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.music_list_scrollArea = QtGui.QScrollArea(self.page_3)
        self.music_list_scrollArea.setWidgetResizable(True)
        self.music_list_scrollArea.setObjectName(_fromUtf8("music_list_scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 940, 728))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_4 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.music_table = QtGui.QTableWidget(self.scrollAreaWidgetContents_2)
        self.music_table.setObjectName(_fromUtf8("music_table"))
        self.music_table.setColumnCount(5)
        self.music_table.setRowCount(0)
        self.gridLayout_4.addWidget(self.music_table, 0, 0, 1, 1)
        self.music_list_scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.addWidget(self.music_list_scrollArea)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_2)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.seekSlider = phonon.Phonon.SeekSlider(self.centralwidget)
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.verticalLayout_3.addWidget(self.seekSlider)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.play_button = QtGui.QPushButton(self.centralwidget)
        self.play_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.play_button.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Buttons/play-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play_button.setIcon(icon)
        self.play_button.setIconSize(QtCore.QSize(20, 20))
        self.play_button.setFlat(True)
        self.play_button.setObjectName(_fromUtf8("play_button"))
        self.horizontalLayout.addWidget(self.play_button)
        self.pause_button = QtGui.QPushButton(self.centralwidget)
        self.pause_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pause_button.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Buttons/pause (1).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_button.setIcon(icon1)
        self.pause_button.setIconSize(QtCore.QSize(20, 20))
        self.pause_button.setFlat(True)
        self.pause_button.setObjectName(_fromUtf8("pause_button"))
        self.horizontalLayout.addWidget(self.pause_button)
        self.fast_forward_button = QtGui.QPushButton(self.centralwidget)
        self.fast_forward_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.fast_forward_button.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Buttons/fast-forward.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fast_forward_button.setIcon(icon2)
        self.fast_forward_button.setIconSize(QtCore.QSize(20, 20))
        self.fast_forward_button.setFlat(True)
        self.fast_forward_button.setObjectName(_fromUtf8("fast_forward_button"))
        self.horizontalLayout.addWidget(self.fast_forward_button)
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout.addWidget(self.label_12)
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setMaximumSize(QtCore.QSize(70, 30))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.horizontalLayout.addWidget(self.lcdNumber)
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.horizontalLayout.addWidget(self.line_3)
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.centralwidget)
        self.volumeSlider.setMinimumSize(QtCore.QSize(150, 0))
        self.volumeSlider.setMaximumSize(QtCore.QSize(150, 16777215))
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.horizontalLayout.addWidget(self.volumeSlider)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1254, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.setStatusBar(self.statusbar)
        self.Dock_Settings = QtGui.QDockWidget(self)
        self.Dock_Settings.setMinimumSize(QtCore.QSize(194, 386))
        self.Dock_Settings.setMaximumSize(QtCore.QSize(524287, 524287))
        self.Dock_Settings.setObjectName(_fromUtf8("Dock_Settings"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.likes_button = QtGui.QPushButton(self.dockWidgetContents)
        self.likes_button.setStyleSheet(_fromUtf8("text-align:left;"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Buttons/music-player (2).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.likes_button.setIcon(icon3)
        self.likes_button.setIconSize(QtCore.QSize(23, 23))
        self.likes_button.setFlat(True)
        self.likes_button.setObjectName(_fromUtf8("likes_button"))
        self.horizontalLayout_6.addWidget(self.likes_button)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.saved_settings_box = QtGui.QGroupBox(self.dockWidgetContents)
        self.saved_settings_box.setAlignment(QtCore.Qt.AlignCenter)
        self.saved_settings_box.setObjectName(_fromUtf8("saved_settings_box"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.saved_settings_box)
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.list_settings = QtGui.QListWidget(self.saved_settings_box)
        self.list_settings.setTabKeyNavigation(True)
        self.list_settings.setDragEnabled(True)
        self.list_settings.setDragDropOverwriteMode(True)
        self.list_settings.setObjectName(_fromUtf8("list_settings"))
        item = QtGui.QListWidgetItem()
        self.list_settings.addItem(item)
        item = QtGui.QListWidgetItem()
        self.list_settings.addItem(item)
        item = QtGui.QListWidgetItem()
        self.list_settings.addItem(item)
        item = QtGui.QListWidgetItem()
        self.list_settings.addItem(item)
        self.horizontalLayout_10.addWidget(self.list_settings)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
        self.verticalLayout.addWidget(self.saved_settings_box)
        self.gridLayout_3.addLayout(self.verticalLayout, 8, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.currently_playing_button = QtGui.QPushButton(self.dockWidgetContents)
        self.currently_playing_button.setStyleSheet(_fromUtf8("text-align:left;"))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Buttons/speakers.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.currently_playing_button.setIcon(icon4)
        self.currently_playing_button.setIconSize(QtCore.QSize(23, 23))
        self.currently_playing_button.setFlat(True)
        self.currently_playing_button.setObjectName(_fromUtf8("currently_playing_button"))
        self.horizontalLayout_7.addWidget(self.currently_playing_button)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 6, 0, 1, 1)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.collections_button = QtGui.QPushButton(self.dockWidgetContents)
        self.collections_button.setStyleSheet(_fromUtf8("text-align:left;"))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("Buttons/music-player (1).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.collections_button.setIcon(icon5)
        self.collections_button.setIconSize(QtCore.QSize(23, 23))
        self.collections_button.setFlat(True)
        self.collections_button.setObjectName(_fromUtf8("collections_button"))
        self.horizontalLayout_5.addWidget(self.collections_button)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.notifications_button = QtGui.QPushButton(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.notifications_button.setFont(font)
        self.notifications_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.notifications_button.setStyleSheet(_fromUtf8("text-align:left;\n"
                                                          ""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("Buttons/alarm (2).png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notifications_button.setIcon(icon6)
        self.notifications_button.setIconSize(QtCore.QSize(23, 23))
        self.notifications_button.setAutoRepeat(False)
        self.notifications_button.setAutoDefault(False)
        self.notifications_button.setDefault(False)
        self.notifications_button.setFlat(True)
        self.notifications_button.setObjectName(_fromUtf8("notifications_button"))
        self.horizontalLayout_3.addWidget(self.notifications_button)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.line = QtGui.QFrame(self.dockWidgetContents)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_3.addWidget(self.line, 3, 0, 1, 1)
        self.line_2 = QtGui.QFrame(self.dockWidgetContents)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.gridLayout_3.addWidget(self.line_2, 7, 0, 1, 1)
        self.Dock_Settings.setWidget(self.dockWidgetContents)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.Dock_Settings)
        self.actionExit = QtGui.QAction("E&xit", self, shortcut="Ctrl+X",
                                        triggered=self.close)

        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.triggered[QtGui.QAction].connect(self.processTrigger)
        self.actionAdd_Folder = QtGui.QAction("Add &Folder", self,
                                              shortcut="Ctrl+W", triggered=self.addFolder)
        self.actionAdd_Folder.setObjectName(_fromUtf8("actionAdd_Folder"))
        self.actionAdd_File = QtGui.QAction("Add &Files", self,
                                            shortcut="Ctrl+F", triggered=self.addFiles)

        self.actionAdd_File.setObjectName(_fromUtf8("actionAdd_File"))
        self.actionPreference = QtGui.QAction(self)
        self.actionPreference.setObjectName(_fromUtf8("actionPreference"))
        self.menuFile.addAction(self.actionAdd_Folder)
        self.menuFile.addAction(self.actionAdd_File)
        self.menuFile.addAction(self.actionPreference)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(self)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.notifications_button.setAutoRepeat(True)
        self.notifications_button.setAutoRepeatDelay(1000)
        self.notifications_button.setAutoRepeatInterval(1000)

        self.collections_button.setAutoRepeat(True)
        self.collections_button.setAutoRepeatDelay(1000)
        self.collections_button.setAutoRepeatInterval(1000)

        self.likes_button.setAutoRepeat(True)
        self.likes_button.setAutoRepeatDelay(1000)
        self.likes_button.setAutoRepeatInterval(1000)

        # self.notifications_button.clicked.connect(lambda: self.onChanged(self.notifications_button))
        # self.collections_button.clicked.connect(lambda: self.onChanged(self.collections_button))
        self.notifications_button.clicked.connect(self.cameraStack)
        self.collections_button.clicked.connect(self.filterCollections)
        self.likes_button.clicked.connect(self.filterLike)

        self.currently_playing_button.clicked.connect(self.changeSetting)

        # Media stuff starts here
        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory, self)
        self.mediaObject = Phonon.MediaObject(self)
        self.metaInformationResolver = Phonon.MediaObject(self)

        self.mediaObject.setTickInterval(1000)

        self.mediaObject.tick.connect(self.tick)
        self.mediaObject.stateChanged.connect(self.stateChanged)
        self.metaInformationResolver.stateChanged.connect(self.metaStateChanged)
        self.mediaObject.currentSourceChanged.connect(self.sourceChanged)
        self.mediaObject.aboutToFinish.connect(self.aboutToFinish)

        Phonon.createPath(self.mediaObject, self.audioOutput)

        self.setupActions()  # first method
        # self.setupMenus()  # second method
        self.setupUi()  # third method
        self.lcdNumber.display("00:00")

        self.sources = []
        self.retrieveMusicList()
        # self.cameraStack()


    def tick(self, time):
        displayTime = QtCore.QTime(0, (time / 60000) % 60, (time / 1000) % 60)
        self.lcdNumber.display(displayTime.toString('mm:ss'))

    def sourceChanged(self, source):
        self.music_table.selectRow(self.sources.index(source))
        self.lcdNumber.display('00:00')

    def aboutToFinish(self):
        index = self.sources.index(self.mediaObject.currentSource()) + 1
        if len(self.sources) > index:
            self.mediaObject.enqueue(self.sources[index])

    # def setupMenus(self):

    def metaStateChanged(self, newState, oldState):
        if newState == Phonon.ErrorState:
            QtGui.QMessageBox.warning(self, "Error opening files",
                                      self.metaInformationResolver.errorString())

            while self.sources and self.sources.pop() != self.metaInformationResolver.currentSource():
                pass

        if newState != Phonon.StoppedState and newState != Phonon.PausedState:
            return

        if self.metaInformationResolver.currentSource().type() == Phonon.MediaSource.Invalid:
            return

        metaData = self.metaInformationResolver.metaData()

        title = metaData.get('TITLE', [''])[0]
        print title
        if not title:
            title = self.metaInformationResolver.currentSource().fileName()

        titleItem = QtGui.QTableWidgetItem(title)
        print titleItem
        titleItem.setFlags(titleItem.flags() ^ QtCore.Qt.ItemIsEditable)

        artist = metaData.get('ARTIST', [''])[0]
        print artist
        artistItem = QtGui.QTableWidgetItem(artist)
        artistItem.setFlags(artistItem.flags() ^ QtCore.Qt.ItemIsEditable)

        album = metaData.get('ALBUM', [''])[0]
        print album
        albumItem = QtGui.QTableWidgetItem(album)
        albumItem.setFlags(albumItem.flags() ^ QtCore.Qt.ItemIsEditable)

        year = metaData.get('DATE', [''])[0]
        print year
        yearItem = QtGui.QTableWidgetItem(year)
        yearItem.setFlags(yearItem.flags() ^ QtCore.Qt.ItemIsEditable)

        currentRow = self.music_table.rowCount()
        print currentRow
        self.music_table.insertRow(currentRow)
        self.music_table.setItem(currentRow, 0, titleItem)
        self.music_table.setItem(currentRow, 1, artistItem)
        self.music_table.setItem(currentRow, 2, albumItem)
        self.music_table.setItem(currentRow, 3, yearItem)

        if not self.music_table.selectedItems():
            self.music_table.selectRow(0)
            self.mediaObject.setCurrentSource(self.metaInformationResolver.currentSource())

        source = self.metaInformationResolver.currentSource()
        index = self.sources.index(self.metaInformationResolver.currentSource()) + 1

        if len(self.sources) > index:
            self.metaInformationResolver.setCurrentSource(self.sources[index])
        else:
            self.music_table.resizeColumnsToContents()
            if self.music_table.columnWidth(0) > 300:
                self.music_table.setColumnWidth(0, 300)

    def handleButton(self, button):
        if button == self.play_button:
            print "play"
            self.mediaObject.play()
        elif button == self.pause_button:
            print "pause"
            self.mediaObject.pause()
        elif button == self.fast_forward_button:
            print "stop"
            self.mediaObject.stop()

    def stateChanged(self, newState, oldState):
        if newState == Phonon.ErrorState:
            if self.mediaObject.errorType() == Phonon.FatalError:
                QtGui.QMessageBox.warning(self, "Fatal Error",
                                          self.mediaObject.errorString())
            else:
                QtGui.QMessageBox.warning(self, "Error",
                                          self.mediaObject.errorString())
        elif newState == Phonon.PlayingState:
            self.play_button.setEnabled(False)
            self.pause_button.setEnabled(True)
            self.fast_forward_button.setEnabled(True)

        elif newState == Phonon.StoppedState:
            self.fast_forward_button.setEnabled(False)
            self.play_button.setEnabled(True)
            self.pause_button.setEnabled(False)
            self.lcdNumber.display("00:00")

        elif newState == Phonon.PausedState:
            self.pause_button.setEnabled(False)
            self.fast_forward_button.setEnabled(True)
            self.play_button.setEnabled(True)

    def setupActions(self):
        self.play_button.clicked.connect(lambda: self.handleButton(self.play_button))
        self.pause_button.clicked.connect(lambda: self.handleButton(self.pause_button))
        self.fast_forward_button.clicked.connect(lambda: self.handleButton(self.fast_forward_button))

        self.nextAction = QtGui.QAction(
            self.style().standardIcon(QtGui.QStyle.SP_MediaSkipForward),
            "Next", self, shortcut="Ctrl+N"
        )

        self.previousAction = QtGui.QAction(
            self.style().standardIcon(QtGui.QStyle.SP_MediaSkipBackward),
            "Previous", self, shortcut="Ctrl+R"
        )

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.menuFile.setTitle(_translate("MainWindow", "asdasdsad", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.Dock_Settings.setWindowTitle(_translate("MainWindow", "asdasd Item", None))
        self.likes_button.setText(_translate("MainWindow", "Likes", None))
        self.saved_settings_box.setTitle(_translate("MainWindow", "Saved settings", None))
        __sortingEnabled = self.list_settings.isSortingEnabled()
        self.list_settings.setSortingEnabled(False)
        item = self.list_settings.item(0)
        item.setText(_translate("MainWindow", "Settings 1", None))
        item = self.list_settings.item(1)
        item.setText(_translate("MainWindow", "Settings 2", None))
        item = self.list_settings.item(2)
        item.setText(_translate("MainWindow", "Settings 3", None))
        item = self.list_settings.item(3)
        item.setText(_translate("MainWindow", "Settings 4", None))
        self.list_settings.setSortingEnabled(__sortingEnabled)
        self.currently_playing_button.setText(_translate("MainWindow", "Currently Playing", None))
        self.collections_button.setText(_translate("MainWindow", "Collections", None))
        self.notifications_button.setText(_translate("MainWindow", "Notifications", None))
        self.notifications_button.setShortcut(_translate("MainWindow", "Return", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionAdd_Folder.setText(_translate("MainWindow", "Add Folder", None))
        self.actionAdd_File.setText(_translate("MainWindow", "Add File", None))
        self.actionPreference.setText(_translate("MainWindow", "Preference", None))

    def processTrigger(self, q):
        if q.text() == 'Exit':
            sys.exit()

    def onChanged(self, button):
        if button.isDown():
            if self._state == 0:
                self._state = 1
                button.setAutoRepeatInterval(100)
                print 'press'
            else:
                print 'repeat'
        elif self._state == 1:
            self._state = 0
            button.setAutoRepeatInterval(1000)
            print 'release'
        else:
            print 'click'

    def getBackColor(self):
        return self.palette().color(QtGui.QPalette.Background)

    def setBackColor(self, color):
        pal = self.palette()
        pal.setColor(QtGui.QPalette.Background, color)
        self.setPalette(pal)

    def addFiles(self):
        files = QtGui.QFileDialog.getOpenFileNames(self, "Select Music Files",
                                                   QtGui.QDesktopServices.storageLocation(
                                                       QtGui.QDesktopServices.MusicLocation))
        if not files:
            return

        index = len(self.sources)

        print files
        file = QtCore.QFile('musiclist.txt')
        file.open(QtCore.QFile.Append | QtCore.QFile.Text)
        if not file.open(QtCore.QIODevice.WriteOnly):
            QtGui.QMessageBox.information(None, 'info', file.errorString())

        for string in files:
            stream = QtCore.QTextStream(file)
            stream << string
            stream << '\n'
            self.sources.append(Phonon.MediaSource(string))

        print index
        if self.sources:
            self.metaInformationResolver.setCurrentSource(self.sources[index])

    def addFolder(self):
        dialog = FileDialog()
        if dialog.exec_() == QtGui.QDialog.Accepted:
            print(dialog.selectedFiles())

            # TODO: implementing the add folder function

    def retrieveMusicList(self):
        file = QtCore.QFile('musiclist.txt')
        file.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text)
        index = len(self.sources)

        # if not file.open(QtCore.QIODevice.WriteOnly):
        #     QtGui.QMessageBox.information(None, 'info', file.errorString())

        stream = QtCore.QTextStream(file)
        while not stream.atEnd():
            self.sources.append(Phonon.MediaSource(stream.readLine()))

        print index
        if self.sources:
            self.metaInformationResolver.setCurrentSource(self.sources[0])

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

    def setupUi(self):
        self.seekSlider.setMediaObject(self.mediaObject)
        self.volumeSlider.setAudioOutput(self.audioOutput)
        self.volumeSlider.setSizePolicy(QtGui.QSizePolicy.Maximum,
                                        QtGui.QSizePolicy.Maximum)
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Light, QtCore.Qt.darkGray)

        self.lcdNumber.setPalette(palette)

        headers = ("Title", "Artist", "Album", "Year", "Liked?")
        self.music_table.setHorizontalHeaderLabels(headers)
        self.music_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.music_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.music_table.cellPressed.connect(self.tableClicked)

    def tableClicked(self, row, column):
        wasPlaying = (self.mediaObject.state() == Phonon.PlayingState)

        self.mediaObject.stop()
        self.mediaObject.clearQueue()

        self.mediaObject.setCurrentSource(self.sources[row])

        if wasPlaying:
            self.mediaObject.play()
        else:
            self.mediaObject.stop()

    def contextMenuEvent(self, QContextMenuEvent):
        self.menu = QtGui.QMenu(self)
        renameAction = QtGui.QAction('Like/Unlike', self)
        renameAction.triggered.connect(self.likeSlot)
        self.menu.addAction(renameAction)
        self.menu.popup(QtGui.QCursor.pos())

    def likeSlot(self):
        print self.music_table.currentRow()
        print self.sources[self.music_table.currentRow()]
        item = QtGui.QTableWidgetItem(str("Yes"))
        item_list = self.music_table.item(self.music_table.currentRow(), 4)
        if not item_list:
            self.music_table.setItem(self.music_table.currentRow(), 4, item)
        else:
            self.music_table.setItem(self.music_table.currentRow(), 4, None)

    def filterLike(self):
        for i in range(0, self.music_table.rowCount()):
            item = self.music_table.item(i, 4)
            if not item:
                self.music_table.setRowHidden(i, True)

    def filterCollections(self):
        for i in range(0, self.music_table.rowCount()):
            self.music_table.setRowHidden(i, False)

    # TODO: Finish the face/detection function
    def cameraStack(self):
        # layout = QtGui.QFormLayout()
        # layout.addRow("Name", QtGui.QLineEdit())
        # layout.addRow("Address", QtGui.QLineEdit())
        # self.page_4.setLayout(layout)
        model_filename = "model.pkl"
        image_size = (200,200)
        [images, labels, subject_names] = read_images("gender/", image_size)
        list_of_labels = list(xrange(max(labels)+1))
        subject_dictionary = dict(zip(list_of_labels, subject_names))
        model = get_model(image_size=image_size, subject_names=subject_dictionary)
        model.compute(images, labels)
        print "save model"
        save_model(model_filename, model)


        self.model = load_model(model_filename)
        # self.model = load_model("model.pkl")
        faceCascade = 'haarcascade_frontalface_alt2.xml'
        print self.model.image_size
        print "Starting the face detection"

        self.detector = CascadedDetector(cascade_fn=faceCascade, minNeighbors=5, scaleFactor=1.1)
        video_capture = cv2.VideoCapture(0)

        while True:
            ret, frame = video_capture.read()

            img = cv2.resize(frame, (frame.shape[1] / 2, frame.shape[0] / 2), interpolation=cv2.INTER_CUBIC)
            imgout = img.copy()
            for i, r in enumerate(self.detector.detect(img)):
                x0, y0, x1, y1 = r
                # (1) Get face, (2) Convert to grayscale & (3) resize to image_size:
                face = img[y0:y1, x0:x1]
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                face = cv2.resize(face, self.model.image_size, interpolation=cv2.INTER_CUBIC)
                # Get a prediction from the model:
                prediction = self.model.predict(face)[0]
                # Draw the face area in image:
                cv2.rectangle(imgout, (x0, y0), (x1, y1), (0, 255, 0), 2)
                # Draw the predicted name (folder name...):
                draw_str(imgout, (x0 - 20, y0 - 20), self.model.subject_names[prediction])
                self.gender =  self.model.subject_names[prediction]
                self.changeSetting()
            cv2.imshow('videofacerec', imgout)

            ch = cv2.waitKey(10)
            if ch == 27:
                break



        # ret, frame = video_capture.read()
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #
        # faces = faceCascade.detectMultiScale(
        #     gray,
        #     scaleFactor=1.1,
        #     minNeighbors=5,
        #     minSize=(30, 30),
        #     flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        # )
        #
        # # Draw a rectangle around the faces
        # for (x, y, w, h) in faces:
        #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #
        # # Display the resulting frame
        # cv2.imshow('Video', frame)
        #
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     sys.exit()
    def changeSetting(self):
        if self.gender == "male":
            print "ayys!"
            animation = QtCore.QPropertyAnimation(self.currently_playing_button, "color")
            animation.setDuration(200)
            animation.setStartValue(QtGui.QColor(0, 0, 0))
            animation.setEndValue(QtGui.QColor(240, 240, 240))
            animation.start()
        elif self.gender == "female":
            print "d'oh"


    def displayStack(self):
        if self.stackedWidget.currentIndex() == 1:
            self.stackedWidget.setCurrentIndex(0)
        else:
            self.stackedWidget.setCurrentIndex(1)

    backColor = QtCore.pyqtProperty(QtGui.QColor, getBackColor, setBackColor)


class FileDialog(QtGui.QFileDialog):
    def __init__(self, *args, **kwargs):
        super(FileDialog, self).__init__(*args, **kwargs)
        self.setOption(QtGui.QFileDialog.DontUseNativeDialog, True)
        self.setFileMode(QtGui.QFileDialog.ExistingFiles)

    def accept(self):
        super(FileDialog, self).accept(self)

def read_images(path, image_size=None):
    """Reads the images in a given folder, resizes images on the fly if size is given.

    Args:
        path: Path to a folder with subfolders representing the subjects (persons).
        sz: A tuple with the size Resizes

    Returns:
        A list [X, y, folder_names]

            X: The images, which is a Python list of numpy arrays.
            y: The corresponding labels (the unique number of the subject, person) in a Python list.
            folder_names: The names of the folder, so you can display it in a prediction.
    """
    c = 0
    X = []
    y = []
    folder_names = []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            folder_names.append(subdirname)
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                try:
                    im = cv2.imread(os.path.join(subject_path, filename), cv2.IMREAD_GRAYSCALE)
                    # resize to given size (if given)
                    if (image_size is not None):
                        im = cv2.resize(im, image_size)
                    X.append(np.asarray(im, dtype=np.uint8))
                    y.append(c)
                except IOError, (errno, strerror):
                    print "I/O error({0}): {1}".format(errno, strerror)
                except:
                    print "Unexpected error:", sys.exc_info()[0]
                    raise
            c = c+1
    return [X,y,folder_names]

def get_model(image_size, subject_names):
    """ This method returns the PredictableModel which is used to learn a model
        for possible further usage. If you want to define your own model, this
        is the method to return it from!
    """
    # Define the Fisherfaces Method as Feature Extraction method:
    feature = Fisherfaces()
    # Define a 1-NN classifier with Euclidean Distance:
    classifier = NearestNeighbor(dist_metric=EuclideanDistance(), k=1)
    # Return the model as the combination:
    return ExtendedPredictableModel(feature=feature, classifier=classifier, image_size=image_size, subject_names=subject_names)

class ExtendedPredictableModel(PredictableModel):
    """ Subclasses the PredictableModel to store some more
        information, so we don't need to pass the dataset
        on each program call...
    """

    def __init__(self, feature, classifier, image_size, subject_names):
        PredictableModel.__init__(self, feature=feature, classifier=classifier)
        self.image_size = image_size
        self.subject_names = subject_names

if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    # MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    ui.show()
    sys.exit(app.exec_())
