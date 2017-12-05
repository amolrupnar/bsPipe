from PySide import QtGui
import os

from bsPipe.bs_ui.bsui_asset import bsui_createRig
from bsPipe.bs_ui import bs_qui
from bsPipe.bs_core import bs_pathGenerator
from bsPipe.bs_asset import bs_assetCreate

reload(bsui_createRig)
reload(bs_qui)
reload(bs_pathGenerator)
reload(bs_assetCreate)


class Bs_CreateRig(QtGui.QMainWindow, bsui_createRig.Ui_bscr_createRig_MW):
    def __init__(self, parent=None):
        super(Bs_CreateRig, self).__init__(parent)
        self.setupUi(self)
        self.connection()
        imageRootPath = os.path.dirname(os.path.dirname(__file__))
        imageMap = imageRootPath + '/bs_images/bsw_assetCreateRigBase.png'
        self.bscr_icon_lbl.setPixmap(imageMap)
        self.bscr_refresh_pb.clicked.connect(self.fillAssetNames)
        self.bscr_createBase_pb.clicked.connect(self.createRigBaseHierarchy)
        self.bscr_assetTypes_lw.currentItemChanged.connect(self.fillAssetNames)
        self.bscr_assetNames_lw.currentItemChanged.connect(self.fillAssetModelFiles)
        self.bscr_assetFilesAndVer_lw.currentItemChanged.connect(self.fillFileDetails)

    def connection(self):
        # set fonts to label.
        objFont = QtGui.QFont("Verdana", 10, QtGui.QFont.StyleItalic)
        assetTypeFont = QtGui.QFont("Times", 12)
        self.label.setFont(objFont)
        self.label_6.setFont(objFont)
        self.label_7.setFont(objFont)
        self.bscr_assetTypes_lw.setFont(assetTypeFont)

    def fillAssetNames(self):
        assetType = self.bscr_assetTypes_lw.currentItem().text()
        assetNames = bs_pathGenerator.bs_getAssetNames(assetType)
        # clear other filled objects.
        self.bscr_assetNames_lw.clear()
        self.bscr_assetFilesAndVer_lw.clear()
        self.bscr_assetName_lbl.setText('None')
        self.bscr_assetShort_lbl.setText('None')
        self.bscr_assetType_lbl.setText('None')
        self.bscr_assetGrade_lbl.setText('None')
        # add all asset names in list widget.
        self.bscr_assetNames_lw.addItems(assetNames)

    def fillAssetModelFiles(self):
        # clear all asset details label.
        self.bscr_assetName_lbl.setText('None')
        self.bscr_assetShort_lbl.setText('None')
        self.bscr_assetType_lbl.setText('None')
        self.bscr_assetGrade_lbl.setText('None')
        # fill details.
        assetType = self.bscr_assetTypes_lw.currentItem().text()
        assetName = self.bscr_assetNames_lw.currentItem().text()
        mainFiles, versionFiles = bs_pathGenerator.bs_getAssetFileAndVersions(assetType, 'Model', assetName)
        self.bscr_assetFilesAndVer_lw.clear()
        # sort main files and version files as a ascending order.
        sortedMainFiles = mainFiles.keys()
        sortedMainFiles.sort()
        sortedVersionFiles = versionFiles.keys()
        sortedVersionFiles.sort()
        # add sorted names inb list widget.
        self.bscr_assetFilesAndVer_lw.addItems(sortedMainFiles)
        self.bscr_assetFilesAndVer_lw.addItems(sortedVersionFiles)

    def fillFileDetails(self):
        assetType = self.bscr_assetTypes_lw.currentItem().text()
        assetName = self.bscr_assetNames_lw.currentItem().text()
        mainFiles, versionFiles = bs_pathGenerator.bs_getAssetFileAndVersions(assetType, 'Model', assetName)
        selectedFile = self.bscr_assetFilesAndVer_lw.currentItem().text()
        if selectedFile in mainFiles.keys():
            filePath = mainFiles[selectedFile]['path']
        else:
            filePath = versionFiles[selectedFile]['path']
        assetName = None
        assetShortName = None
        assetType = None
        assetGrade = None
        with open(filePath, 'r') as fi:
            for line in fi.readlines():
                strippedLine = line.strip()
                if strippedLine.startswith('setAttr -l on -k on ".assetGrade" -type "string"'):
                    assetGrade = strippedLine.split(' ')[-1].split('"')[1]
                elif strippedLine.startswith('setAttr -l on -k on ".assetName" -type "string"'):
                    assetName = strippedLine.split(' ')[-1].split('"')[1]
                elif strippedLine.startswith('setAttr -l on -k on ".assetType" -type "string"'):
                    assetType = strippedLine.split(' ')[-1].split('"')[1]
                elif strippedLine.startswith('setAttr -l on -k on ".assetUID" -type "string"'):
                    assetShortName = strippedLine.split(' ')[-1].split('"')[1].split('_')[-1]
        self.bscr_assetName_lbl.setText(assetName)
        self.bscr_assetShort_lbl.setText(assetShortName)
        self.bscr_assetType_lbl.setText(assetType)
        self.bscr_assetGrade_lbl.setText(assetGrade)

    def createRigBaseHierarchy(self):
        assetName = self.bscr_assetName_lbl.text()
        assetShortName = self.bscr_assetShort_lbl.text()
        assetType = self.bscr_assetType_lbl.text()
        assetGrade = self.bscr_assetGrade_lbl.text()
        bs_assetCreate.bs_createRigBase(assetName, assetGrade, assetType, assetShortName)
        self.close()


def main():
    winClass = Bs_CreateRig(bs_qui.bs_mayaMainWindow())
    winClass.show()
