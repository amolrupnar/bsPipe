from PySide import QtGui
import os

from bsPipe.bs_asset import bs_assetManager
from bsPipe.bs_core import bs_mayaFile
from bsPipe.bs_core import bs_reference
from bsPipe.bs_ui import bs_qui
from bsPipe.bs_ui.bsui_asset import bsui_assetManager

reload(bs_assetManager)
reload(bs_mayaFile)
reload(bs_reference)
reload(bs_qui)
reload(bsui_assetManager)

imageRootPath = os.path.dirname(os.path.dirname(__file__))
project = os.environ['BSW_PROJECT']


class Bs_AssetManagerUIConn(QtGui.QMainWindow, bsui_assetManager.Ui_bs_assetManagerMainWin):
    def __init__(self, parent=None):
        super(Bs_AssetManagerUIConn, self).__init__(parent)
        self.setupUi(self)
        self.__getAllAssets()
        self.connections()
        self.addAssetsInManager()
        self._initUiDesign()
        self.bsAm_open_pb.clicked.connect(self.openFile)
        self.bsAm_import_pb.clicked.connect(self.importFile)
        self.bsAm_reference_pb.clicked.connect(self.referenceFile)
        self._searchEventAdd()

    def __getAllAssets(self):
        # get all assets.
        self.allChars = bs_assetManager.bs_getAllAssets(project, 'chars')
        self.allProps = bs_assetManager.bs_getAllAssets(project, 'props')
        self.allSets = bs_assetManager.bs_getAllAssets(project, 'sets')
        self.allSetElements = bs_assetManager.bs_getAllAssets(project, 'SetElement')
        self.allVehicles = bs_assetManager.bs_getAllAssets(project, 'vehicles')

    def _initUiDesign(self):
        # search line edits set with icon and placeholder text.
        bs_qui.bs_setSearchIconInLineEdit(self.bsAm_charSearch_LE)
        self.bsAm_charSearch_LE.setPlaceholderText('Search')
        bs_qui.bs_setSearchIconInLineEdit(self.bsAm_propSearch_LE)
        self.bsAm_propSearch_LE.setPlaceholderText('Search')
        bs_qui.bs_setSearchIconInLineEdit(self.bsAm_setSearch_LE)
        self.bsAm_setSearch_LE.setPlaceholderText('Search')
        bs_qui.bs_setSearchIconInLineEdit(self.bsAm_setElementSearch_LE)
        self.bsAm_setElementSearch_LE.setPlaceholderText('Search')
        bs_qui.bs_setSearchIconInLineEdit(self.bsAm_vehicleSearch_LE)
        self.bsAm_vehicleSearch_LE.setPlaceholderText('Search')

    def _searchEventAdd(self):
        self.bsAm_charSearch_LE.textChanged.connect(lambda: bs_qui.bs_filterListWidget(self.bsAm_chars_lw, self.bsAm_charSearch_LE, self.allChars))
        self.bsAm_propSearch_LE.textChanged.connect(lambda: bs_qui.bs_filterListWidget(self.bsAm_props_lw, self.bsAm_propSearch_LE, self.allProps))
        self.bsAm_setSearch_LE.textChanged.connect(lambda: bs_qui.bs_filterListWidget(self.bsAm_sets_lw, self.bsAm_setSearch_LE, self.allSets))
        self.bsAm_setElementSearch_LE.textChanged.connect(lambda: bs_qui.bs_filterListWidget(self.bsAm_setElems_lw, self.bsAm_setElementSearch_LE, self.allSetElements))
        self.bsAm_vehicleSearch_LE.textChanged.connect(lambda: bs_qui.bs_filterListWidget(self.bsAm_vehicles_lw, self.bsAm_vehicleSearch_LE, self.allVehicles))

    def refreshManager(self):
        self.__getAllAssets()
        self.addAssetsInManager()

    def connections(self):
        imageMap = imageRootPath + '/bs_images/bsw_assetManagerLogo.png'
        self.logo_lbl.setPixmap(imageMap)
        self.bsAm_refresh_pb.clicked.connect(self.refreshManager)
        self.bsAm_assetVersions_lw.clear()
        self.bsAm_versionInfo_lw.clear()
        self.bsAm_chars_lw.itemSelectionChanged.connect(self.addFileAndVersionsInAssetLw)
        self.bsAm_props_lw.itemSelectionChanged.connect(self.addFileAndVersionsInAssetLw)
        self.bsAm_sets_lw.itemSelectionChanged.connect(self.addFileAndVersionsInAssetLw)
        self.bsAm_setElems_lw.itemSelectionChanged.connect(self.addFileAndVersionsInAssetLw)
        self.bsAm_vehicles_lw.itemSelectionChanged.connect(self.addFileAndVersionsInAssetLw)

    def addAssetsInManager(self):
        self.bsAm_chars_lw.clear()
        self.bsAm_props_lw.clear()
        self.bsAm_sets_lw.clear()
        self.bsAm_vehicles_lw.clear()
        self.bsAm_chars_lw.addItems(self.allChars)
        self.bsAm_props_lw.addItems(self.allProps)
        self.bsAm_sets_lw.addItems(self.allSets)
        self.bsAm_setElems_lw.addItems(self.allSetElements)
        self.bsAm_vehicles_lw.addItems(self.allVehicles)

    def addFileAndVersionsInAssetLw(self):
        assetType = self.bsAm_asset_tw.tabText(self.bsAm_asset_tw.currentIndex())
        assetTypeFilterLw = {'Chars': self.bsAm_chars_lw.currentItem, 'Props': self.bsAm_props_lw.currentItem,
                             'Sets': self.bsAm_sets_lw.currentItem, 'Vehicles': self.bsAm_vehicles_lw.currentItem,
                             'SetElement': self.bsAm_setElems_lw.currentItem}
        assetTypeFilter = {'Chars': '01_char', 'Props': '02_props', 'Sets': '03_set', 'Vehicles': '04_vehicle',
                           'SetElement': '03_set/00_setElement'}
        categoryFilter = {'Model': '02_model', 'Texture': '03_texture', 'Rig': '05_rig', 'Light': '04_light'}
        astType = assetTypeFilter[assetType]
        assetName = assetTypeFilterLw[assetType]().text()
        category = self.bsAm_category_cBox.currentText()
        mFiles, vFiles = bs_assetManager.bs_assetFileAndVersions(project, astType, assetName, categoryFilter[category])
        self.bsAm_assetVersions_lw.clear()
        self.bsAm_assetVersions_lw.addItems(mFiles)
        self.bsAm_assetVersions_lw.addItems(vFiles)

    def getFilePath(self):
        assetType = self.bsAm_asset_tw.tabText(self.bsAm_asset_tw.currentIndex())
        assetTypeFilterLw = {'Chars': self.bsAm_chars_lw.currentItem, 'Props': self.bsAm_props_lw.currentItem,
                             'Sets': self.bsAm_sets_lw.currentItem, 'Vehicles': self.bsAm_vehicles_lw.currentItem,
                             'SetElement': self.bsAm_setElems_lw.currentItem}
        assetTypeFilter = {'Chars': '01_char', 'Props': '02_props', 'Sets': '03_set', 'Vehicles': '04_vehicle',
                           'SetElement': '03_set/00_setElement'}
        categoryFilter = {'Model': '02_model', 'Texture': '03_texture', 'Rig': '05_rig', 'Light': '04_light'}
        astType = assetTypeFilter[assetType]
        assetName = assetTypeFilterLw[assetType]().text()
        category = self.bsAm_category_cBox.currentText()
        fileRootPath = bs_assetManager.bs_assetDirPath(project, astType, assetName, categoryFilter[category])
        selectedFile = self.bsAm_assetVersions_lw.currentItem().text()
        nonVersionFile = None
        for each in os.listdir(fileRootPath):
            if each == selectedFile:
                nonVersionFile = True
        if nonVersionFile:
            filePath = fileRootPath + '/' + selectedFile
        else:
            filePath = fileRootPath + '/version/' + selectedFile
        return filePath

    def importFile(self):
        bs_mayaFile.bs_importFile(self.getFilePath())

    def openFile(self):
        bs_mayaFile.bs_openFile(self.getFilePath())
        self.close()

    def referenceFile(self):
        bs_reference.bs_createReference(self.getFilePath(), prefixStyle='normal')


def main():
    winClass = Bs_AssetManagerUIConn(bs_qui.bs_mayaMainWindow())
    return winClass.show()
