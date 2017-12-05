# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'S:/bsw_programation/01_maya/Pipeline/bsPipe/bsPipe/bs_ui/bsui_asset/bsui_blendshapeMaker.ui'
#
# Created: Thu Aug 24 16:41:41 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_bswBlendMaker_MW(object):
    def setupUi(self, bswBlendMaker_MW):
        bswBlendMaker_MW.setObjectName("bswBlendMaker_MW")
        bswBlendMaker_MW.resize(367, 369)
        self.centralwidget = QtGui.QWidget(bswBlendMaker_MW)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(35, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.bsm_geometries_LW = QtGui.QListWidget(self.centralwidget)
        self.bsm_geometries_LW.setObjectName("bsm_geometries_LW")
        self.gridLayout.addWidget(self.bsm_geometries_LW, 1, 0, 1, 1)
        self.bsm_load_PB = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bsm_load_PB.sizePolicy().hasHeightForWidth())
        self.bsm_load_PB.setSizePolicy(sizePolicy)
        self.bsm_load_PB.setMinimumSize(QtCore.QSize(11, 278))
        self.bsm_load_PB.setMaximumSize(QtCore.QSize(35, 16777215))
        self.bsm_load_PB.setObjectName("bsm_load_PB")
        self.gridLayout.addWidget(self.bsm_load_PB, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.bsm_make_PB = QtGui.QPushButton(self.centralwidget)
        self.bsm_make_PB.setObjectName("bsm_make_PB")
        self.verticalLayout.addWidget(self.bsm_make_PB)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        bswBlendMaker_MW.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(bswBlendMaker_MW)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 367, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        bswBlendMaker_MW.setMenuBar(self.menubar)
        self.actionExit = QtGui.QAction(bswBlendMaker_MW)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtGui.QAction(bswBlendMaker_MW)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(bswBlendMaker_MW)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), bswBlendMaker_MW.close)
        QtCore.QMetaObject.connectSlotsByName(bswBlendMaker_MW)

    def retranslateUi(self, bswBlendMaker_MW):
        bswBlendMaker_MW.setWindowTitle(QtGui.QApplication.translate("bswBlendMaker_MW", "BSW Blendshape Maker", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("bswBlendMaker_MW", "Load Items to duplicate for blendshape", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("bswBlendMaker_MW", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.bsm_load_PB.setText(QtGui.QApplication.translate("bswBlendMaker_MW", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.bsm_make_PB.setText(QtGui.QApplication.translate("bswBlendMaker_MW", "Make Blendshape Hierarchy", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("bswBlendMaker_MW", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("bswBlendMaker_MW", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("bswBlendMaker_MW", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("bswBlendMaker_MW", "About", None, QtGui.QApplication.UnicodeUTF8))

