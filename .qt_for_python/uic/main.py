# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1191, 766)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 100))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.centralframe = QFrame(self.centralwidget)
        self.centralframe.setObjectName(u"centralframe")
        self.centralframe.setStyleSheet(u"background-color: rgb(40, 42, 54);")
        self.centralframe.setFrameShape(QFrame.StyledPanel)
        self.centralframe.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.centralframe)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalsplitter = QSplitter(self.centralframe)
        self.verticalsplitter.setObjectName(u"verticalsplitter")
        sizePolicy.setHeightForWidth(self.verticalsplitter.sizePolicy().hasHeightForWidth())
        self.verticalsplitter.setSizePolicy(sizePolicy)
        self.verticalsplitter.setLineWidth(0)
        self.verticalsplitter.setOrientation(Qt.Vertical)
        self.verticalsplitter.setHandleWidth(0)
        self.horizontalsplitter = QSplitter(self.verticalsplitter)
        self.horizontalsplitter.setObjectName(u"horizontalsplitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalsplitter.sizePolicy().hasHeightForWidth())
        self.horizontalsplitter.setSizePolicy(sizePolicy1)
        self.horizontalsplitter.setMinimumSize(QSize(0, 200))
        self.horizontalsplitter.setLineWidth(0)
        self.horizontalsplitter.setOrientation(Qt.Horizontal)
        self.horizontalsplitter.setHandleWidth(0)
        self.libraryframe = QFrame(self.horizontalsplitter)
        self.libraryframe.setObjectName(u"libraryframe")
        self.libraryframe.setMaximumSize(QSize(200, 16777215))
        self.libraryframe.setStyleSheet(u"background-color: rgb(35,39,42);\n"
"border: None")
        self.libraryframe.setFrameShape(QFrame.Panel)
        self.libraryframe.setFrameShadow(QFrame.Raised)
        self.horizontalsplitter.addWidget(self.libraryframe)
        self.top = QFrame(self.horizontalsplitter)
        self.top.setObjectName(u"top")
        self.top.setStyleSheet(u"background-color: rgb(44,47,51);\n"
"border: None;")
        self.top.setFrameShape(QFrame.StyledPanel)
        self.top.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.top)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setContentsMargins(10, 10, 10, 0)
        self.searchframe = QFrame(self.top)
        self.searchframe.setObjectName(u"searchframe")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.searchframe.sizePolicy().hasHeightForWidth())
        self.searchframe.setSizePolicy(sizePolicy2)
        self.searchframe.setMinimumSize(QSize(0, 25))
        self.searchframe.setMaximumSize(QSize(16777215, 25))
        self.searchframe.setStyleSheet(u"QFrame {\n"
"background-color: rgb(35,39,42);\n"
"border-radius: 12px;\n"
"border: 2px solid rgb(122, 255, 110);\n"
"}")
        self.searchframe.setFrameShape(QFrame.StyledPanel)
        self.searchframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.searchframe)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(7, 0, 0, 0)
        self.search = QLineEdit(self.searchframe)
        self.search.setObjectName(u"search")
        self.search.setEnabled(True)
        sizePolicy.setHeightForWidth(self.search.sizePolicy().hasHeightForWidth())
        self.search.setSizePolicy(sizePolicy)
        self.search.setMinimumSize(QSize(0, 0))
        self.search.setMaximumSize(QSize(16777215, 16777215))
        self.search.setStyleSheet(u"background-color: rgb(0,0,0,0);\n"
"color: rgb(122, 138, 153);")
        self.search.setMaxLength(1024)
        self.search.setCursorPosition(0)
        self.search.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.search.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.search.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.search)


        self.gridLayout_3.addWidget(self.searchframe, 0, 0, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(50, 0, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.fileview = QTableWidget(self.top)
        if (self.fileview.columnCount() < 4):
            self.fileview.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.fileview.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.fileview.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.fileview.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.fileview.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.fileview.setObjectName(u"fileview")
        sizePolicy.setHeightForWidth(self.fileview.sizePolicy().hasHeightForWidth())
        self.fileview.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(9)
        self.fileview.setFont(font)
        self.fileview.setMouseTracking(False)
        self.fileview.setFocusPolicy(Qt.StrongFocus)
        self.fileview.setStyleSheet(u"	QTableView {\n"
"		alternate-background-color: rgb(35,39,42);\n"
"		border: None;	\n"
"		border-left: 0.5px solid rgb(35,39,42);\n"
"	}\n"
"\n"
"	QTableWidget::item {\n"
"        color: rgb(122, 138, 153);\n"
"		border-color: rgb(100, 0, 0);\n"
"    }\n"
"\n"
"    QTableWidget::item:selected {\n"
"        color: rgb(153,170,181);\n"
"		background-color: rgb(52, 68, 83);\n"
"    }\n"
"	QScrollBar::handle {\n"
"		background-color: rgb(52, 68, 83);\n"
"		border-radius:5px;\n"
"	}\n"
"	QHeaderView::section {\n"
"    	background-color: rgb(44,47,51);\n"
"		color: rgb(153,170,181);\n"
"		border-style: None;\n"
"		border-bottom: 0.5px solid rgb(35,39,42);\n"
"		border-right: 0.5px solid rgb(35,39,42);\n"
"		border-top: 0.5px solid rgb(35,39,42);\n"
"		font-size: 12px;\n"
"	}")
        self.fileview.setLineWidth(0)
        self.fileview.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.fileview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.fileview.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.fileview.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.fileview.setDefaultDropAction(Qt.MoveAction)
        self.fileview.setAlternatingRowColors(True)
        self.fileview.setSelectionMode(QAbstractItemView.SingleSelection)
        self.fileview.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.fileview.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.fileview.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.fileview.setShowGrid(True)
        self.fileview.setGridStyle(Qt.SolidLine)
        self.fileview.setSortingEnabled(False)
        self.fileview.horizontalHeader().setVisible(True)
        self.fileview.horizontalHeader().setCascadingSectionResizes(False)
        self.fileview.horizontalHeader().setMinimumSectionSize(50)
        self.fileview.horizontalHeader().setDefaultSectionSize(200)
        self.fileview.horizontalHeader().setHighlightSections(False)
        self.fileview.horizontalHeader().setProperty("showSortIndicator", False)
        self.fileview.horizontalHeader().setStretchLastSection(True)
        self.fileview.verticalHeader().setVisible(False)
        self.fileview.verticalHeader().setCascadingSectionResizes(False)
        self.fileview.verticalHeader().setHighlightSections(False)
        self.fileview.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.fileview, 1, 0, 1, 3)

        self.horizontalsplitter.addWidget(self.top)
        self.verticalsplitter.addWidget(self.horizontalsplitter)
        self.waveformframe = QFrame(self.verticalsplitter)
        self.waveformframe.setObjectName(u"waveformframe")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.waveformframe.sizePolicy().hasHeightForWidth())
        self.waveformframe.setSizePolicy(sizePolicy3)
        self.waveformframe.setMinimumSize(QSize(0, 100))
        self.waveformframe.setMaximumSize(QSize(16777215, 16777215))
        self.waveformframe.setStyleSheet(u"background-color:  rgb(26,29,31);\n"
"border: None;")
        self.waveformframe.setFrameShape(QFrame.StyledPanel)
        self.waveformframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.waveformframe)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalsplitter.addWidget(self.waveformframe)

        self.gridLayout_2.addWidget(self.verticalsplitter, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.centralframe, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.search.setText("")
        self.search.setPlaceholderText("")
        ___qtablewidgetitem = self.fileview.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.fileview.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Length", None));
        ___qtablewidgetitem2 = self.fileview.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Format", None));
        ___qtablewidgetitem3 = self.fileview.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Path", None));
    # retranslateUi

