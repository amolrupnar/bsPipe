# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/bsw_programation/01_maya/Pipeline/bsPipe/bsPipe/bs_ui/bsui_asset/bsui_assetPublish.ui'
#
# Created: Thu Dec 14 17:34:44 2017
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AssetPublishMainWindow(object):
    def setupUi(self, AssetPublishMainWindow):
        AssetPublishMainWindow.setObjectName("AssetPublishMainWindow")
        AssetPublishMainWindow.resize(879, 550)
        self.centralwidget = QtGui.QWidget(AssetPublishMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bsap_publishLogo_lbl = QtGui.QLabel(self.centralwidget)
        self.bsap_publishLogo_lbl.setObjectName("bsap_publishLogo_lbl")
        self.horizontalLayout.addWidget(self.bsap_publishLogo_lbl)
        self.bsap_refresh_pb = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bsap_refresh_pb.sizePolicy().hasHeightForWidth())
        self.bsap_refresh_pb.setSizePolicy(sizePolicy)
        self.bsap_refresh_pb.setMinimumSize(QtCore.QSize(50, 50))
        self.bsap_refresh_pb.setMaximumSize(QtCore.QSize(50, 50))
        self.bsap_refresh_pb.setObjectName("bsap_refresh_pb")
        self.horizontalLayout.addWidget(self.bsap_refresh_pb)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.bsap_category_lbl = QtGui.QLabel(self.centralwidget)
        self.bsap_category_lbl.setText("")
        self.bsap_category_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.bsap_category_lbl.setObjectName("bsap_category_lbl")
        self.gridLayout.addWidget(self.bsap_category_lbl, 1, 0, 1, 1)
        self.bsap_assetType_lbl = QtGui.QLabel(self.centralwidget)
        self.bsap_assetType_lbl.setText("")
        self.bsap_assetType_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.bsap_assetType_lbl.setObjectName("bsap_assetType_lbl")
        self.gridLayout.addWidget(self.bsap_assetType_lbl, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.bsap_assetName_lbl = QtGui.QLabel(self.centralwidget)
        self.bsap_assetName_lbl.setText("")
        self.bsap_assetName_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.bsap_assetName_lbl.setObjectName("bsap_assetName_lbl")
        self.gridLayout.addWidget(self.bsap_assetName_lbl, 1, 2, 1, 1)
        self.bsap_episodeTag_lbl = QtGui.QLabel(self.centralwidget)
        self.bsap_episodeTag_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.bsap_episodeTag_lbl.setObjectName("bsap_episodeTag_lbl")
        self.gridLayout.addWidget(self.bsap_episodeTag_lbl, 0, 3, 1, 1)
        self.bsap_episode_lbl = QtGui.QLabel(self.centralwidget)
        self.bsap_episode_lbl.setText("")
        self.bsap_episode_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.bsap_episode_lbl.setObjectName("bsap_episode_lbl")
        self.gridLayout.addWidget(self.bsap_episode_lbl, 1, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 0, 1, 2)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.bsap_comment_TE = QtGui.QTextEdit(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(80)
        sizePolicy.setHeightForWidth(self.bsap_comment_TE.sizePolicy().hasHeightForWidth())
        self.bsap_comment_TE.setSizePolicy(sizePolicy)
        self.bsap_comment_TE.setMaximumSize(QtCore.QSize(16777215, 200))
        self.bsap_comment_TE.setObjectName("bsap_comment_TE")
        self.layoutWidget = QtGui.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.bsap_prevVers_tableWidget = QtGui.QTableWidget(self.layoutWidget)
        self.bsap_prevVers_tableWidget.setObjectName("bsap_prevVers_tableWidget")
        self.bsap_prevVers_tableWidget.setColumnCount(5)
        self.bsap_prevVers_tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.bsap_prevVers_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.bsap_prevVers_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.bsap_prevVers_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.bsap_prevVers_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.bsap_prevVers_tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout.addWidget(self.bsap_prevVers_tableWidget)
        self.gridLayout_2.addWidget(self.splitter, 4, 0, 1, 2)
        self.bsap_publish_pb = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bsap_publish_pb.sizePolicy().hasHeightForWidth())
        self.bsap_publish_pb.setSizePolicy(sizePolicy)
        self.bsap_publish_pb.setMinimumSize(QtCore.QSize(0, 40))
        self.bsap_publish_pb.setObjectName("bsap_publish_pb")
        self.gridLayout_2.addWidget(self.bsap_publish_pb, 5, 0, 1, 2)
        AssetPublishMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(AssetPublishMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 879, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        AssetPublishMainWindow.setMenuBar(self.menubar)
        self.actionFile = QtGui.QAction(AssetPublishMainWindow)
        self.actionFile.setObjectName("actionFile")
        self.actionExit = QtGui.QAction(AssetPublishMainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout = QtGui.QAction(AssetPublishMainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuMenu.addAction(self.actionFile)
        self.menuMenu.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(AssetPublishMainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL("triggered()"), AssetPublishMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(AssetPublishMainWindow)

    def retranslateUi(self, AssetPublishMainWindow):
        AssetPublishMainWindow.setWindowTitle(QtGui.QApplication.translate("AssetPublishMainWindow", "BSW Asset Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.bsap_publishLogo_lbl.setText(QtGui.QApplication.translate("AssetPublishMainWindow", "Logo", None, QtGui.QApplication.UnicodeUTF8))
        self.bsap_refresh_pb.setText(QtGui.QApplication.translate("AssetPublishMainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AssetPublishMainWindow", "Asset Department", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AssetPublishMainWindow", "Asset Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AssetPublishMainWindow", "Asset Name", None, QtGui.QApplication.UnicodeUTF8))
        self.bsap_episodeTag_lbl.setText(QtGui.QApplication.translate("AssetPublishMainWindow", "Episode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AssetPublishMainWindow", "Comment", None, QtGui.QApplication.UnicodeUTF8))
        self.bsap_comment_TE.setHtml(QtGui.QApplication.translate("AssetPublishMainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AssetPublishMainWindow", "Previous Versions", None, QtGui.QApplication.UnicodeUTF8))
        self.bsap_prevVers_tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("AssetPublishMainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.bsap_prevVers_tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("AssetPublishMainWindow", "Date Time", None, QtGui.QApplication.UnicodeUTF8))
        self.bsap_prevVers_tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("AssetPublishMainWindow", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.bsap_prevVers_tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("AssetPublishMainWindow", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.bsap_prevVers_tableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("AssetPublishMainWindow", "Comment", None, QtGui.QApplication.UnicodeUTF8))
        self.bsap_publish_pb.setText(QtGui.QApplication.translate("AssetPublishMainWindow", "Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMenu.setTitle(QtGui.QApplication.translate("AssetPublishMainWindow", "Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("AssetPublishMainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFile.setText(QtGui.QApplication.translate("AssetPublishMainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("AssetPublishMainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("AssetPublishMainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))

