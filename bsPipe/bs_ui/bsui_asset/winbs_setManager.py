import os
import pymel.core as pm
from PySide import QtGui

from bsPipe.bs_ui import bs_qui
from bsPipe.bs_ui.bsui_asset import bsui_setManager
from bsPipe.bs_core import bs_pathGenerator, bs_os
from bsPipe.bs_core import bs_reference
from bsPipe.bs_asset import bs_setManager
from bsPipe.bs_batch.bs_createSetGPU import startupCmd

reload(bs_qui)
reload(bsui_setManager)
reload(bs_pathGenerator)
reload(bs_reference)
reload(bs_setManager)
reload(startupCmd)
reload(bs_os)


class Bs_SetManager(QtGui.QMainWindow, bsui_setManager.Ui_bssm_setManager_MW):
    def __init__(self, parent=None):
        super(Bs_SetManager, self).__init__(parent)
        self.setupUi(self)
        # fill asset entries and set fonts.
        assetCategory, assetType, assetName, uid = bs_pathGenerator.bs_getAssetDetails()
        self.bssm_category_lbl.setText(assetCategory)
        self.bssm_assetType_lbl.setText(assetType)
        self.bssm_assetName_lbl.setText(assetName)
        # change current font.
        headerFont = QtGui.QFont("Times", 12, QtGui.QFont.Bold)
        objFont = QtGui.QFont("Verdana", 10, QtGui.QFont.StyleItalic)
        self.label_2.setFont(headerFont)
        self.label_4.setFont(headerFont)
        self.label_5.setFont(headerFont)
        self.bssm_category_lbl.setFont(objFont)
        self.bssm_assetName_lbl.setFont(objFont)
        self.bssm_assetType_lbl.setFont(objFont)
        # ui changes.
        self.actionExit.triggered.connect(self.close)
        self.bssm_setElementLib_LW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.bssm_selectedItems_LW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.bssm_currentSetElem_LW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.addGpuPath()
        # ui connections
        self.addAllSetElements()
        self.addReferencedElem()
        self.bssm_addElem_PB.clicked.connect(self.addItemsInSelectedLW)
        self.bssm_remElem_PB.clicked.connect(lambda: bs_qui.bs_removeSelectedItemsFromQLW(self.bssm_selectedItems_LW))
        self.bssm_addElemInScene_PB.clicked.connect(self.referenceElements)
        self.bssm_removeRef_PB.clicked.connect(self.removeSelectedReferences)
        self.bssm_refresh_PB.clicked.connect(self.refresh)
        self.bssm_exportGPU_PB.clicked.connect(self.exportGPU)
        self.bssm_GPUfilePath_PB.clicked.connect(self.openGpuDirectory)
        self.bssm_GPUcachePath_PB.clicked.connect(self.openGpuDirectory)

    def addAllSetElements(self):
        self.bssm_setElementLib_LW.clear()
        # add only rigged set elements.
        allElementNames = bs_pathGenerator.bs_getAssetNames('SetElement')
        riggedElements = list()
        for each in allElementNames:
            mainFile, verFiles = bs_pathGenerator.bs_getAssetFileAndVersions('SetElement', 'Rig', each)
            if len(mainFile.keys()) == 1:
                riggedElements.append(each)
        self.bssm_setElementLib_LW.addItems(riggedElements)

    def addItemsInSelectedLW(self):
        selectedItems = list()
        [selectedItems.append(each.text()) for each in self.bssm_setElementLib_LW.selectedItems()]
        self.bssm_selectedItems_LW.addItems(selectedItems)

    def addReferencedElem(self):
        self.bssm_currentSetElem_LW.clear()
        allRef = pm.listReferences()
        referencedNodes = list()
        for each in allRef:
            path = str(each.unresolvedPath())
            if path.startswith('$BSW_PROD_SERVER/kicko_speedo/01_pre/03_set/00_setElement/'):
                referencedNodes.append(each.refNode.name())
        referencedNodes.sort()
        self.bssm_currentSetElem_LW.addItems(referencedNodes)

    def removeSelectedReferences(self):
        removeRef = bs_qui.bs_removeSelectedReferenceFromQLW(self.bssm_currentSetElem_LW)
        self.refresh()
        bs_qui.bs_displayMessage('success', '%d set elements removed from scene...' % removeRef)

    def referenceElements(self):
        # get environments.
        serverPath = bs_pathGenerator.bs_getEnvDetails()['rootPath']
        # query current set.
        dept, assetType, assetName, uid = bs_pathGenerator.bs_getAssetDetails()
        if dept == 'Not Exist' or assetType == 'Not Exist' or assetName == 'Not Exist':
            bs_qui.bs_displayMessage('error', 'No Set Found in Scene.....')
            return False
        elements = list()
        for x in range(self.bssm_selectedItems_LW.count()):
            elements.append(self.bssm_selectedItems_LW.item(x).text())
        # reference and parent all selected setElements.
        for each in elements:
            mainFile, verFiles = bs_pathGenerator.bs_getAssetFileAndVersions('SetElement', 'Rig', each)
            if len(mainFile.keys()) == 1:
                filePath = mainFile[mainFile.keys()[0]]['path']
                filePath = filePath.replace(serverPath, '$BSW_PROD_SERVER/')
                ns = bs_reference.bs_createReference(filePath, prefixStyle='fileName')
                pm.parent(ns.namespace + ':rig_grp', 'setElements_grp')
        self.refresh()

    def exportGPU(self):
        # query current set.
        dept, assetType, assetName, uid = bs_pathGenerator.bs_getAssetDetails()
        if dept == 'Not Exist' or assetType == 'Not Exist' or assetName == 'Not Exist':
            bs_qui.bs_displayMessage('error', 'No Set Found in Scene.....')
            return False
        bs_setManager.bs_makeGpuCacheFile()
        self.addGpuPath()

    def addGpuPath(self):
        # query current set.
        dept, assetType, assetName, uid = bs_pathGenerator.bs_getAssetDetails()
        if dept == 'Not Exist' or assetType == 'Not Exist' or assetName == 'Not Exist':
            bs_qui.bs_displayMessage('error', 'No Set Found in Scene.....')
            return False
        cacheDir = bs_pathGenerator.bs_getAssetDir(astType=assetType, astName=assetName, astDept=dept)['dept'] + 'gpu/'
        fileName = bs_pathGenerator.bs_getMainFileName().split('.')[0][:-3] + 'gpu'
        if os.path.isfile(cacheDir + fileName + '.ma'):
            self.bssm_GPUfilePath_LE.setText(cacheDir + fileName + '.ma')
        else:
            self.bssm_GPUfilePath_LE.setText('gpu maya file is not found...')
        if os.path.isfile(cacheDir + fileName + '.abc'):
            self.bssm_GPUcachePath_LE.setText(cacheDir + fileName + '.abc')
        else:
            self.bssm_GPUcachePath_LE.setText('gpu cache file is not found...')

    def openGpuDirectory(self):
        path = self.bssm_GPUfilePath_LE.text()
        if not path.startswith('gpu '):
            gpuDir = str()
            for each in path.split('/')[:-1]:
                gpuDir += each + '/'
            bs_os.bs_openDirInExplorer(gpuDir)
        else:
            bs_qui.bs_displayMessage('error', 'not valid directory...')

    def refresh(self):
        self.addAllSetElements()
        self.addReferencedElem()


def main():
    winClass = Bs_SetManager(bs_qui.bs_mayaMainWindow())
    winClass.show()
