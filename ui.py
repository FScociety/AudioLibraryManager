from PyQt5.QtWidgets import QWidget, QLineEdit, QTableWidget, QFrame, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QColor
import sys
import numpy as np
from pydub import AudioSegment
from WaveFormWiget import WaveForm
import time


class Ui(QtWidgets.QMainWindow):

    lineEdit = None
    fileView = None
    searchFrame = None

    def ploting(self, file):
        file_complete = file.file_path + "/" + file.file_name
        file_extension = file.file_extension[1:]  # '1:' for removing the '.' from Bsp: '.mp3'
        _time = time.time()
        audio = AudioSegment.from_file(file_complete, format=file_extension)

        print("Audio was loaded in", time.time() - _time)

        data = audio.get_array_of_samples()
        samplerate = audio.frame_rate

        duration = len(data)/samplerate  # frames / samples per second
        timex = np.arange(0, duration, 1/samplerate)  # timestep array for duration

        #print(data, len(data))
        #print("-------------------------------------------")
        #print(timex, len(data))

        self.waveform.plot(data)
        #self.plot.plot(timex, data)

    def initUI(self):
        self.ui = uic.loadUi("main.ui", self)

        # adding the plot
        self.waveform = WaveForm()
        self.ui.verticalLayout_2.addWidget(self.waveform)

        self.lineEdit = self.ui.findChild(QLineEdit, "search")
        self.searchFrame = self.ui.findChild(QFrame, "searchframe")

        self.fileView = self.ui.findChild(QTableWidget, "fileview")
        horizontalHeader = self.fileView.horizontalHeader()
        horizontalHeader.setSectionResizeMode(1, QtWidgets.QHeaderView.Fixed)

        libaryFrame = self.ui.findChild(QFrame, "libraryframe")
        libraryShadow = QGraphicsDropShadowEffect(enabled=True, blurRadius=30)
        libraryShadow.setXOffset(0)
        libraryShadow.setYOffset(0)
        libraryShadow.setColor(QColor(0, 0, 0))
        libaryFrame.setGraphicsEffect(libraryShadow)

        waveformFrame = self.ui.findChild(QFrame, "waveformframe")
        waveformShadow = QGraphicsDropShadowEffect(enabled=True, blurRadius=30)
        waveformShadow.setXOffset(0)
        waveformShadow.setYOffset(0)
        waveformShadow.setColor(QColor(0, 0, 0))
        waveformFrame.setGraphicsEffect(waveformShadow)

        # QApplication.instance().focusChanged.connect(print)

    def __init__(self):
        super(Ui, self).__init__()
        self.initUI()
