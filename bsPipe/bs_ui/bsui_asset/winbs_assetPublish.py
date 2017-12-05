import os
from PySide import QtGui

from bsPipe.bs_ui.bsui_asset import bsui_assetPublish
from bsPipe.bs_core import bs_pathGenerator
from bsPipe.bs_asset import bs_assetPublish
from bsPipe.bs_ui import bs_qui

reload(bsui_assetPublish)
reload(bs_pathGenerator)
reload(bs_assetPublish)
reload(bs_qui)

imageRootPath = os.path.dirname(os.path.dirname(__file__))


class Bs_AssetPublish(QtGui.QMainWindow, bsui_assetPublish.Ui_AssetPublishMainWindow):
    def __init__(self, parent=None):
        super(Bs_AssetPublish, self).__init__(parent)
        self.setupUi(self)
        self.connections()
        self.bsap_publish_pb.clicked.connect(self.publishAsset)
        self.addItemInTable()
        self.bsap_prevVers_tableWidget.resizeColumnsToContents()
        self.bsap_refresh_pb.clicked.connect(self.addItemInTable)

    def connections(self):
        imageMap = imageRootPath + '/bs_images/bsw_assetPublishLogo.png'
        self.bsap_publishLogo_lbl.setPixmap(imageMap)
        assetCategory, assetType, assetName, uid = bs_pathGenerator.bs_getAssetDetails()

        self.bsap_category_lbl.setText(assetCategory)
        self.bsap_assetType_lbl.setText(assetType)
        self.bsap_assetName_lbl.setText(assetName)
        # change current font.
        headerFont = QtGui.QFont("Times", 12, QtGui.QFont.Bold)
        objFont = QtGui.QFont("Verdana", 10, QtGui.QFont.StyleItalic)
        self.label.setFont(headerFont)
        self.label_4.setFont(headerFont)
        self.label_5.setFont(headerFont)
        self.bsap_category_lbl.setFont(objFont)
        self.bsap_assetType_lbl.setFont(objFont)
        self.bsap_assetName_lbl.setFont(objFont)

    def addItemInTable(self):
        self.bsap_prevVers_tableWidget.setRowCount(0)
        dept, assetType, assetName, uid = bs_pathGenerator.bs_getAssetDetails()
        if dept == 'Not Exist' or assetType == 'Not Exist' or assetName == 'Not Exist':
            bs_qui.bs_displayMessage('warning', 'No Assets Found in Scene.....')
            return False
        mainFile, verFiles = bs_pathGenerator.bs_getAssetFileAndVersions(assetType, dept, assetName)
        verKeys = verFiles.keys()
        verKeys.sort()
        for each in mainFile.keys():
            rowPosition = self.bsap_prevVers_tableWidget.rowCount()
            self.bsap_prevVers_tableWidget.insertRow(rowPosition)
            fileName = mainFile[each]['path'].split('/')[-1]
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 0, QtGui.QTableWidgetItem(fileName))
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 1, QtGui.QTableWidgetItem(mainFile[each]['time']))
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 2, QtGui.QTableWidgetItem(mainFile[each]['owner']))
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 3, QtGui.QTableWidgetItem(mainFile[each]['size']))
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 4, QtGui.QTableWidgetItem('None'))
        for each in verKeys:
            rowPosition = self.bsap_prevVers_tableWidget.rowCount()
            self.bsap_prevVers_tableWidget.insertRow(rowPosition)
            fileName = verFiles[each]['path'].split('/')[-1]
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 0, QtGui.QTableWidgetItem(fileName))
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 1, QtGui.QTableWidgetItem(verFiles[each]['time']))
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 2, QtGui.QTableWidgetItem(verFiles[each]['owner']))
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 3, QtGui.QTableWidgetItem(verFiles[each]['size']))
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 4, QtGui.QTableWidgetItem('None'))
        self.bsap_prevVers_tableWidget.resizeColumnsToContents()

    def publishAsset(self):
        bs_assetPublish.bs_publishCurrentAsset()
        self.addItemInTable()


def main():
    winClass = Bs_AssetPublish(bs_qui.bs_mayaMainWindow())
    winClass.show()
