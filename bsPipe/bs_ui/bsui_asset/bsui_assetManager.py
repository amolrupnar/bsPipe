# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/bsw_programation/01_maya/Pipeline/bsPipe/bsPipe/bs_ui/bsui_asset/bsui_assetManager.ui'
#
# Created: Tue Dec 19 12:41:12 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_bs_assetManagerMainWin(object):
    def setupUi(self, bs_assetManagerMainWin):
        bs_assetManagerMainWin.setObjectName("bs_assetManagerMainWin")
        bs_assetManagerMainWin.resize(882, 740)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(bs_assetManagerMainWin.sizePolicy().hasHeightForWidth())
        bs_assetManagerMainWin.setSizePolicy(sizePolicy)
        bs_assetManagerMainWin.setMinimumSize(QtCore.QSize(882, 740))
        bs_assetManagerMainWin.setMaximumSize(QtCore.QSize(882, 740))
        self.centralwidget = QtGui.QWidget(bs_assetManagerMainWin)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 11, 871, 118))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.logo_lbl = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.logo_lbl.sizePolicy().hasHeightForWidth())
        self.logo_lbl.setSizePolicy(sizePolicy)
        self.logo_lbl.setMinimumSize(QtCore.QSize(0, 50))
        self.logo_lbl.setMaximumSize(QtCore.QSize(16777215, 50))
        self.logo_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_lbl.setObjectName("logo_lbl")
        self.verticalLayout_4.addWidget(self.logo_lbl)
        self.line_3 = QtGui.QFrame(self.layoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_4.addWidget(self.line_3)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.episode_lbl = QtGui.QLabel(self.layoutWidget)
        self.episode_lbl.setObjectName("episode_lbl")
        self.horizontalLayout_3.addWidget(self.episode_lbl)
        self.episode_cBox = QtGui.QComboBox(self.layoutWidget)
        self.episode_cBox.setObjectName("episode_cBox")
        self.horizontalLayout_3.addWidget(self.episode_cBox)
        self.line_5 = QtGui.QFrame(self.layoutWidget)
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_3.addWidget(self.line_5)
        self.label_7 = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)
        self.model_RB = QtGui.QRadioButton(self.layoutWidget)
        self.model_RB.setChecked(True)
        self.model_RB.setObjectName("model_RB")
        self.horizontalLayout_3.addWidget(self.model_RB)
        self.texture_RB = QtGui.QRadioButton(self.layoutWidget)
        self.texture_RB.setObjectName("texture_RB")
        self.horizontalLayout_3.addWidget(self.texture_RB)
        self.rig_RB = QtGui.QRadioButton(self.layoutWidget)
        self.rig_RB.setObjectName("rig_RB")
        self.horizontalLayout_3.addWidget(self.rig_RB)
        self.light_RB = QtGui.QRadioButton(self.layoutWidget)
        self.light_RB.setObjectName("light_RB")
        self.horizontalLayout_3.addWidget(self.light_RB)
        self.fx_RB = QtGui.QRadioButton(self.layoutWidget)
        self.fx_RB.setObjectName("fx_RB")
        self.horizontalLayout_3.addWidget(self.fx_RB)
        self.line_2 = QtGui.QFrame(self.layoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_3.addWidget(self.line_2)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.bsAm_refresh_pb = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bsAm_refresh_pb.sizePolicy().hasHeightForWidth())
        self.bsAm_refresh_pb.setSizePolicy(sizePolicy)
        self.bsAm_refresh_pb.setMinimumSize(QtCore.QSize(0, 40))
        self.bsAm_refresh_pb.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bsAm_refresh_pb.setObjectName("bsAm_refresh_pb")
        self.horizontalLayout_3.addWidget(self.bsAm_refresh_pb)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.line_4 = QtGui.QFrame(self.layoutWidget)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_4.addWidget(self.line_4)
        self.layoutWidget1 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(1, 140, 871, 511))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.bsAm_asset_tw = QtGui.QTabWidget(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bsAm_asset_tw.sizePolicy().hasHeightForWidth())
        self.bsAm_asset_tw.setSizePolicy(sizePolicy)
        self.bsAm_asset_tw.setMinimumSize(QtCore.QSize(310, 425))
        self.bsAm_asset_tw.setMaximumSize(QtCore.QSize(300, 500))
        self.bsAm_asset_tw.setObjectName("bsAm_asset_tw")
        self.chars_tab = QtGui.QWidget()
        self.chars_tab.setObjectName("chars_tab")
        self.bsAm_chars_lw = QtGui.QListWidget(self.chars_tab)
        self.bsAm_chars_lw.setGeometry(QtCore.QRect(0, 40, 300, 425))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bsAm_chars_lw.sizePolicy().hasHeightForWidth())
        self.bsAm_chars_lw.setSizePolicy(sizePolicy)
        self.bsAm_chars_lw.setMinimumSize(QtCore.QSize(300, 425))
        self.bsAm_chars_lw.setMaximumSize(QtCore.QSize(300, 425))
        self.bsAm_chars_lw.setObjectName("bsAm_chars_lw")
        self.bsAm_charSearch_LE = QtGui.QLineEdit(self.chars_tab)
        self.bsAm_charSearch_LE.setGeometry(QtCore.QRect(0, 10, 300, 21))
        self.bsAm_charSearch_LE.setMinimumSize(QtCore.QSize(300, 21))
        self.bsAm_charSearch_LE.setMaximumSize(QtCore.QSize(300, 21))
        self.bsAm_charSearch_LE.setObjectName("bsAm_charSearch_LE")
        self.bsAm_asset_tw.addTab(self.chars_tab, "")
        self.props_tab = QtGui.QWidget()
        self.props_tab.setObjectName("props_tab")
        self.bsAm_props_lw = QtGui.QListWidget(self.props_tab)
        self.bsAm_props_lw.setGeometry(QtCore.QRect(0, 40, 300, 425))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bsAm_props_lw.sizePolicy().hasHeightForWidth())
        self.bsAm_props_lw.setSizePolicy(sizePolicy)
        self.bsAm_props_lw.setMinimumSize(QtCore.QSize(300, 425))
        self.bsAm_props_lw.setMaximumSize(QtCore.QSize(300, 425))
        self.bsAm_props_lw.setObjectName("bsAm_props_lw")
        self.bsAm_propSearch_LE = QtGui.QLineEdit(self.props_tab)
        self.bsAm_propSearch_LE.setGeometry(QtCore.QRect(0, 10, 300, 21))
        self.bsAm_propSearch_LE.setMinimumSize(QtCore.QSize(300, 21))
        self.bsAm_propSearch_LE.setMaximumSize(QtCore.QSize(300, 21))
        self.bsAm_propSearch_LE.setObjectName("bsAm_propSearch_LE")
        self.bsAm_asset_tw.addTab(self.props_tab, "")
        self.sets_tab = QtGui.QWidget()
        self.sets_tab.setObjectName("sets_tab")
        self.bsAm_sets_lw = QtGui.QListWidget(self.sets_tab)
        self.bsAm_sets_lw.setGeometry(QtCore.QRect(0, 40, 300, 425))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bsAm_sets_lw.sizePolicy().hasHeightForWidth())
        self.bsAm_sets_lw.setSizePolicy(sizePolicy)
        self.bsAm_sets_lw.setMinimumSize(QtCore.QSize(300, 425))
        self.bsAm_sets_lw.setMaximumSize(QtCore.QSize(300, 425))
        self.bsAm_sets_lw.setObjectName("bsAm_sets_lw")
        self.bsAm_setSearch_LE = QtGui.QLineEdit(self.sets_tab)
        self.bsAm_setSearch_LE.setGeometry(QtCore.QRect(0, 10, 300, 21))
        self.bsAm_setSearch_LE.setMinimumSize(QtCore.QSize(300, 21))
        self.bsAm_setSearch_LE.setMaximumSize(QtCore.QSize(300, 21))
        self.bsAm_setSearch_LE.setObjectName("bsAm_setSearch_LE")
        self.bsAm_asset_tw.addTab(self.sets_tab, "")
        self.setElements_tab = QtGui.QWidget()
        self.setElements_tab.setObjectName("setElements_tab")
        self.bsAm_setElems_lw = QtGui.QListWidget(self.setElements_tab)
        self.bsAm_setElems_lw.setGeometry(QtCore.QRect(0, 40, 300, 425))
        self.bsAm_setElems_lw.setMinimumSize(QtCore.QSize(300, 425))
        self.bsAm_setElems_lw.setMaximumSize(QtCore.QSize(300, 425))
        self.bsAm_setElems_lw.setObjectName("bsAm_setElems_lw")
        self.bsAm_setElementSearch_LE = QtGui.QLineEdit(self.setElements_tab)
        self.bsAm_setElementSearch_LE.setGeometry(QtCore.QRect(0, 10, 300, 21))
        self.bsAm_setElementSearch_LE.setMinimumSize(QtCore.QSize(300, 21))
        self.bsAm_setElementSearch_LE.setMaximumSize(QtCore.QSize(300, 21))
        self.bsAm_setElementSearch_LE.setObjectName("bsAm_setElementSearch_LE")
        self.bsAm_asset_tw.addTab(self.setElements_tab, "")
        self.vehicles_tab = QtGui.QWidget()
        self.vehicles_tab.setObjectName("vehicles_tab")
        self.bsAm_vehicles_lw = QtGui.QListWidget(self.vehicles_tab)
        self.bsAm_vehicles_lw.setGeometry(QtCore.QRect(0, 40, 300, 425))
        self.bsAm_vehicles_lw.setMinimumSize(QtCore.QSize(300, 425))
        self.bsAm_vehicles_lw.setMaximumSize(QtCore.QSize(300, 425))
        self.bsAm_vehicles_lw.setObjectName("bsAm_vehicles_lw")
        self.bsAm_vehicleSearch_LE = QtGui.QLineEdit(self.vehicles_tab)
        self.bsAm_vehicleSearch_LE.setGeometry(QtCore.QRect(0, 10, 300, 21))
        self.bsAm_vehicleSearch_LE.setMinimumSize(QtCore.QSize(300, 21))
        self.bsAm_vehicleSearch_LE.setMaximumSize(QtCore.QSize(300, 21))
        self.bsAm_vehicleSearch_LE.setObjectName("bsAm_vehicleSearch_LE")
        self.bsAm_asset_tw.addTab(self.vehicles_tab, "")
        self.verticalLayout.addWidget(self.bsAm_asset_tw)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.bsAm_assetVersions_lw = QtGui.QListWidget(self.layoutWidget1)
        self.bsAm_assetVersions_lw.setObjectName("bsAm_assetVersions_lw")
        self.verticalLayout_3.addWidget(self.bsAm_assetVersions_lw)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.imageView_lbl = QtGui.QLabel(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageView_lbl.sizePolicy().hasHeightForWidth())
        self.imageView_lbl.setSizePolicy(sizePolicy)
        self.imageView_lbl.setMinimumSize(QtCore.QSize(250, 250))
        self.imageView_lbl.setMaximumSize(QtCore.QSize(250, 250))
        self.imageView_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.imageView_lbl.setObjectName("imageView_lbl")
        self.verticalLayout_2.addWidget(self.imageView_lbl)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.owner_lbl = QtGui.QLabel(self.layoutWidget1)
        self.owner_lbl.setText("")
        self.owner_lbl.setObjectName("owner_lbl")
        self.gridLayout.addWidget(self.owner_lbl, 2, 1, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.name_lbl = QtGui.QLabel(self.layoutWidget1)
        self.name_lbl.setText("")
        self.name_lbl.setObjectName("name_lbl")
        self.gridLayout.addWidget(self.name_lbl, 0, 1, 1, 1)
        self.type_lbl = QtGui.QLabel(self.layoutWidget1)
        self.type_lbl.setText("")
        self.type_lbl.setObjectName("type_lbl")
        self.gridLayout.addWidget(self.type_lbl, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.size_lbl = QtGui.QLabel(self.layoutWidget1)
        self.size_lbl.setText("")
        self.size_lbl.setObjectName("size_lbl")
        self.gridLayout.addWidget(self.size_lbl, 3, 1, 1, 1)
        self.time_lbl = QtGui.QLabel(self.layoutWidget1)
        self.time_lbl.setText("")
        self.time_lbl.setObjectName("time_lbl")
        self.gridLayout.addWidget(self.time_lbl, 4, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.bsAm_versionInfo_TE = QtGui.QTextEdit(self.layoutWidget1)
        self.bsAm_versionInfo_TE.setObjectName("bsAm_versionInfo_TE")
        self.verticalLayout_2.addWidget(self.bsAm_versionInfo_TE)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.layoutWidget2 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 660, 871, 42))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bsAm_open_pb = QtGui.QPushButton(self.layoutWidget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bsAm_open_pb.sizePolicy().hasHeightForWidth())
        self.bsAm_open_pb.setSizePolicy(sizePolicy)
        self.bsAm_open_pb.setMinimumSize(QtCore.QSize(0, 30))
        self.bsAm_open_pb.setMaximumSize(QtCore.QSize(16777215, 30))
        self.bsAm_open_pb.setObjectName("bsAm_open_pb")
        self.horizontalLayout.addWidget(self.bsAm_open_pb)
        self.bsAm_import_pb = QtGui.QPushButton(self.layoutWidget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bsAm_import_pb.sizePolicy().hasHeightForWidth())
        self.bsAm_import_pb.setSizePolicy(sizePolicy)
        self.bsAm_import_pb.setMinimumSize(QtCore.QSize(0, 30))
        self.bsAm_import_pb.setMaximumSize(QtCore.QSize(16777215, 30))
        self.bsAm_import_pb.setObjectName("bsAm_import_pb")
        self.horizontalLayout.addWidget(self.bsAm_import_pb)
        self.bsAm_reference_pb = QtGui.QPushButton(self.layoutWidget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bsAm_reference_pb.sizePolicy().hasHeightForWidth())
        self.bsAm_reference_pb.setSizePolicy(sizePolicy)
        self.bsAm_reference_pb.setMinimumSize(QtCore.QSize(0, 30))
        self.bsAm_reference_pb.setMaximumSize(QtCore.QSize(16777215, 30))
        self.bsAm_reference_pb.setObjectName("bsAm_reference_pb")
        self.horizontalLayout.addWidget(self.bsAm_reference_pb)
        bs_assetManagerMainWin.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(bs_assetManagerMainWin)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 882, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        bs_assetManagerMainWin.setMenuBar(self.menubar)
        self.actionExit = QtGui.QAction(bs_assetManagerMainWin)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(bs_assetManagerMainWin)
        self.bsAm_asset_tw.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), bs_assetManagerMainWin.close)
        QtCore.QMetaObject.connectSlotsByName(bs_assetManagerMainWin)

    def retranslateUi(self, bs_assetManagerMainWin):
        bs_assetManagerMainWin.setWindowTitle(QtGui.QApplication.translate("bs_assetManagerMainWin", "Bioscopewala Asset Manager", None, QtGui.QApplication.UnicodeUTF8))
        self.logo_lbl.setStatusTip(QtGui.QApplication.translate("bs_assetManagerMainWin", "ui logo", None, QtGui.QApplication.UnicodeUTF8))
        self.logo_lbl.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "logo", None, QtGui.QApplication.UnicodeUTF8))
        self.episode_lbl.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "Episode:-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "   Asset Type:-", None, QtGui.QApplication.UnicodeUTF8))
        self.model_RB.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "Model", None, QtGui.QApplication.UnicodeUTF8))
        self.texture_RB.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "Texture", None, QtGui.QApplication.UnicodeUTF8))
        self.rig_RB.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "Rig", None, QtGui.QApplication.UnicodeUTF8))
        self.light_RB.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "Light", None, QtGui.QApplication.UnicodeUTF8))
        self.fx_RB.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "FX", None, QtGui.QApplication.UnicodeUTF8))
        self.bsAm_refresh_pb.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.bsAm_asset_tw.setTabText(self.bsAm_asset_tw.indexOf(self.chars_tab), QtGui.QApplication.translate("bs_assetManagerMainWin", "Character", None, QtGui.QApplication.UnicodeUTF8))
        self.bsAm_asset_tw.setTabText(self.bsAm_asset_tw.indexOf(self.props_tab), QtGui.QApplication.translate("bs_assetManagerMainWin", "Prop", None, QtGui.QApplication.UnicodeUTF8))
        self.bsAm_asset_tw.setTabText(self.bsAm_asset_tw.indexOf(self.sets_tab), QtGui.QApplication.translate("bs_assetManagerMainWin", "Set", None, QtGui.QApplication.UnicodeUTF8))
        self.bsAm_asset_tw.setTabText(self.bsAm_asset_tw.indexOf(self.setElements_tab), QtGui.QApplication.translate("bs_assetManagerMainWin", "SetElement", None, QtGui.QApplication.UnicodeUTF8))
        self.bsAm_asset_tw.setTabText(self.bsAm_asset_tw.indexOf(self.vehicles_tab), QtGui.QApplication.translate("bs_assetManagerMainWin", "Vehicle", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "All Versions", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "Screenshot", None, QtGui.QApplication.UnicodeUTF8))
        self.imageView_lbl.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "screenshot", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "Name:-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "Type:-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "Owner:-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "Size:-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "Time:-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "Version Comment", None, QtGui.QApplication.UnicodeUTF8))
        self.bsAm_open_pb.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.bsAm_import_pb.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.bsAm_reference_pb.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "Reference", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("bs_assetManagerMainWin", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("bs_assetManagerMainWin", "Exit", None, QtGui.QApplication.UnicodeUTF8))

