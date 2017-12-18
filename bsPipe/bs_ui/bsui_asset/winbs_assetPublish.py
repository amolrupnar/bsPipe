import os
from PySide import QtGui

from bsPipe.bs_ui.bsui_asset import bsui_assetPublish
from bsPipe.bs_core import bs_pathGenerator, bs_os
from bsPipe.bs_asset import bs_assetPublish
from bsPipe.bs_ui import bs_qui

reload(bsui_assetPublish)
reload(bs_pathGenerator)
reload(bs_assetPublish)
reload(bs_qui)
reload(bs_os)

imageRootPath = os.path.dirname(os.path.dirname(__file__))


class Bs_AssetPublish(QtGui.QMainWindow, bsui_assetPublish.Ui_AssetPublishMainWindow):
    def __init__(self, parent=None):
        super(Bs_AssetPublish, self).__init__(parent)
        # get environments.
        self.projectType = bs_pathGenerator.bs_getEnv()['projectType']
        self.setupUi(self)
        self.connections()
        self.bsap_publish_pb.clicked.connect(self.publishAsset)
        self.addItemInTable()
        self.bsap_prevVers_tableWidget.resizeColumnsToContents()
        self.bsap_refresh_pb.clicked.connect(self.addItemInTable)
        # hide episode fields if environment is movie.
        if not self.projectType == 'series':
            self.bsap_episode_lbl.hide()
            self.bsap_episodeTag_lbl.hide()

    def connections(self):
        imageMap = imageRootPath + '/bs_images/bsw_assetPublishLogo.png'
        self.bsap_publishLogo_lbl.setPixmap(imageMap)
        assetCategory, assetType, assetName, uid, episode = bs_pathGenerator.bs_getAssetDetails()

        self.bsap_category_lbl.setText(assetCategory)
        self.bsap_assetType_lbl.setText(assetType)
        self.bsap_assetName_lbl.setText(assetName)
        if self.projectType == 'series':
            self.bsap_episode_lbl.setText(episode)
        # change current font.
        headerFont = QtGui.QFont("Times", 12, QtGui.QFont.Bold)
        objFont = QtGui.QFont("Verdana", 10, QtGui.QFont.StyleItalic)
        self.label.setFont(headerFont)
        self.label_4.setFont(headerFont)
        self.label_5.setFont(headerFont)
        self.bsap_category_lbl.setFont(objFont)
        self.bsap_assetType_lbl.setFont(objFont)
        self.bsap_assetName_lbl.setFont(objFont)
        if self.projectType == 'series':
            self.bsap_episodeTag_lbl.setFont(headerFont)
            self.bsap_episode_lbl.setFont(objFont)

    def addItemInTable(self):
        self.bsap_prevVers_tableWidget.setRowCount(0)
        dept, assetType, assetName, uid, episode = bs_pathGenerator.bs_getAssetDetails()
        if dept == 'Not Exist' or assetType == 'Not Exist' or assetName == 'Not Exist':
            bs_qui.bs_displayMessage('warning', 'No Assets Found in Scene.....')
            return False
        if self.projectType == 'series':
            mainFi, verFi = bs_pathGenerator.bs_getAssetFileAndVersions(assetType, dept, assetName, episode=episode)
        else:
            mainFi, verFi = bs_pathGenerator.bs_getAssetFileAndVersions(assetType, dept, assetName)
        # add version details in table widget.
        for each in mainFi:
            rowPosition = self.bsap_prevVers_tableWidget.rowCount()
            self.bsap_prevVers_tableWidget.insertRow(rowPosition)
            fileName = each.split('/')[-1]
            fileTime = bs_os.bs_getFileDateTime(each)
            fileOwner = bs_os.bs_getFileOwner(each)
            fileSize = bs_os.bs_getFileSize(each)
            fileComment = 'NUll'
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 0, QtGui.QTableWidgetItem(fileName))
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 1, QtGui.QTableWidgetItem(fileTime))
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 2, QtGui.QTableWidgetItem(fileOwner))
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 3, QtGui.QTableWidgetItem(fileSize))
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 4, QtGui.QTableWidgetItem(fileComment))
        for each in verFi:
            rowPosition = self.bsap_prevVers_tableWidget.rowCount()
            self.bsap_prevVers_tableWidget.insertRow(rowPosition)
            fileName = each.split('/')[-1]
            fileTime = bs_os.bs_getFileDateTime(each)
            fileOwner = bs_os.bs_getFileOwner(each)
            fileSize = bs_os.bs_getFileSize(each)
            fileComment = 'NUll'
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 0, QtGui.QTableWidgetItem(fileName))
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 1, QtGui.QTableWidgetItem(fileTime))
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 2, QtGui.QTableWidgetItem(fileOwner))
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 3, QtGui.QTableWidgetItem(fileSize))
            self.bsap_prevVers_tableWidget.setItem(rowPosition, 4, QtGui.QTableWidgetItem(fileComment))
        self.bsap_prevVers_tableWidget.resizeColumnsToContents()

    def publishAsset(self):
        commentText = str(self.bsap_comment_TE.toPlainText())
        bs_assetPublish.bs_publishCurrentAsset(comment=commentText)
        self.addItemInTable()


def main():
    winClass = Bs_AssetPublish(bs_qui.bs_mayaMainWindow())
    winClass.show()
