from PySide import QtGui
import os

from bsPipe.bs_core import bs_mayaFile
from bsPipe.bs_core import bs_reference
from bsPipe.bs_ui import bs_qui
from bsPipe.bs_ui.bsui_asset import bsui_assetManager
from bsPipe.bs_core import bs_pathGenerator
from bsPipe.bs_core import bs_os
from bsPipe.bs_core import bs_database

reload(bs_mayaFile)
reload(bs_reference)
reload(bs_qui)
reload(bsui_assetManager)
reload(bs_pathGenerator)
reload(bs_os)
reload(bs_database)


class Bs_AssetManagerUIConn(QtGui.QMainWindow, bsui_assetManager.Ui_bs_assetManagerMainWin):
    def __init__(self, parent=None):
        super(Bs_AssetManagerUIConn, self).__init__(parent)
        self.imageRootPath = os.path.dirname(os.path.dirname(__file__))
        self.setupUi(self)
        self._initUiDesign()
        # fill episodes if project type is series.
        if self.projectType:
            self.fillAllEpisodeInComboBox()
            self.episode_cBox.currentIndexChanged.connect(self.refreshManager)
            # self.connections()
        self._getAllAssets()
        self.addAssetsInManager()
        self._searchEventAdd()
        self.fillFilesAndVersionOnChangeCommand()
        self.bsAm_refresh_pb.clicked.connect(self.refreshManager)
        self.bsAm_open_pb.clicked.connect(self._openFile)
        self.bsAm_import_pb.clicked.connect(self._importFile)
        self.bsAm_reference_pb.clicked.connect(self._referenceFile)
        self.bsAm_assetVersions_lw.itemSelectionChanged.connect(self.setScreenshot)
        self.bsAm_assetVersions_lw.itemSelectionChanged.connect(self.setVersionInfo)

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
        # set image map to logo.
        imageMap = self.imageRootPath + '/bs_images/bsw_assetManagerLogo.png'
        self.logo_lbl.setPixmap(imageMap)
        # hide episode fields if project type is series.
        if not self.projectType:
            self.episode_lbl.hide()
            self.episode_cBox.hide()

    def fillFilesAndVersionOnChangeCommand(self):
        # clear fields.
        self.bsAm_assetVersions_lw.clear()
        self.bsAm_versionInfo_TE.clear()
        self.bsAm_chars_lw.itemSelectionChanged.connect(self.addFileAndVersionsInAssetLw)
        self.bsAm_props_lw.itemSelectionChanged.connect(self.addFileAndVersionsInAssetLw)
        self.bsAm_sets_lw.itemSelectionChanged.connect(self.addFileAndVersionsInAssetLw)
        self.bsAm_setElems_lw.itemSelectionChanged.connect(self.addFileAndVersionsInAssetLw)
        self.bsAm_vehicles_lw.itemSelectionChanged.connect(self.addFileAndVersionsInAssetLw)

    @property
    def projectType(self):
        if bs_pathGenerator.bs_getEnv()['projectType'] == 'series':
            return 'series'
        else:
            return None

    @property
    def _getCheckedAssetDept(self):
        for each in [self.model_RB, self.texture_RB, self.rig_RB, self.light_RB, self.fx_RB]:
            if each.isChecked():
                return each.text()

    @property
    def _getAssetType(self):
        return self.bsAm_asset_tw.tabText(self.bsAm_asset_tw.currentIndex())

    def fillAllEpisodeInComboBox(self):
        if self.projectType:
            allEpisodes = bs_pathGenerator.bs_getAllAssetEpisodes(self._getAssetType)
            self.episode_cBox.addItems(allEpisodes)

    @property
    def selectedEpisode(self):
        if self.projectType:
            return str(self.episode_cBox.currentText())
        else:
            return None

    def _getAllAssets(self):
        # get all assets.
        self.allChars = bs_pathGenerator.bs_getAllAssetNames('Character', episode=self.selectedEpisode)
        self.allProps = bs_pathGenerator.bs_getAllAssetNames('Prop', episode=self.selectedEpisode)
        self.allSets = bs_pathGenerator.bs_getAllAssetNames('Set', episode=self.selectedEpisode)
        self.allSetElements = bs_pathGenerator.bs_getAllAssetNames('SetElement', episode=self.selectedEpisode)
        self.allVehicles = bs_pathGenerator.bs_getAllAssetNames('Vehicle', episode=self.selectedEpisode)

    def _searchEventAdd(self):
        self.bsAm_charSearch_LE.textChanged.connect(
            lambda: bs_qui.bs_filterListWidget(self.bsAm_chars_lw, self.bsAm_charSearch_LE, self.allChars))
        self.bsAm_propSearch_LE.textChanged.connect(
            lambda: bs_qui.bs_filterListWidget(self.bsAm_props_lw, self.bsAm_propSearch_LE, self.allProps))
        self.bsAm_setSearch_LE.textChanged.connect(
            lambda: bs_qui.bs_filterListWidget(self.bsAm_sets_lw, self.bsAm_setSearch_LE, self.allSets))
        self.bsAm_setElementSearch_LE.textChanged.connect(
            lambda: bs_qui.bs_filterListWidget(self.bsAm_setElems_lw, self.bsAm_setElementSearch_LE,
                                               self.allSetElements))
        self.bsAm_vehicleSearch_LE.textChanged.connect(
            lambda: bs_qui.bs_filterListWidget(self.bsAm_vehicles_lw, self.bsAm_vehicleSearch_LE, self.allVehicles))

    def refreshManager(self):
        self._getAllAssets()
        self.addAssetsInManager()

    def addAssetsInManager(self):
        self.bsAm_chars_lw.clear()
        self.bsAm_props_lw.clear()
        self.bsAm_sets_lw.clear()
        self.bsAm_setElems_lw.clear()
        self.bsAm_vehicles_lw.clear()
        self.bsAm_chars_lw.addItems(self.allChars)
        self.bsAm_props_lw.addItems(self.allProps)
        self.bsAm_sets_lw.addItems(self.allSets)
        self.bsAm_setElems_lw.addItems(self.allSetElements)
        self.bsAm_vehicles_lw.addItems(self.allVehicles)

    def addFileAndVersionsInAssetLw(self):
        assetType = self.bsAm_asset_tw.tabText(self.bsAm_asset_tw.currentIndex())
        # list widget dictionary.
        assetTypeFilterLw = {'Character': self.bsAm_chars_lw.currentItem, 'Prop': self.bsAm_props_lw.currentItem,
                             'Set': self.bsAm_sets_lw.currentItem, 'Vehicle': self.bsAm_vehicles_lw.currentItem,
                             'SetElement': self.bsAm_setElems_lw.currentItem}
        assetName = assetTypeFilterLw[assetType]().text()
        assetDept = self._getCheckedAssetDept
        # get main file and version file.
        mFiles, vFiles = bs_pathGenerator.bs_getAssetFileAndVersions(assetType, assetDept, assetName,
                                                                     episode=self.selectedEpisode)
        # clear list widget before adding.
        self.bsAm_assetVersions_lw.clear()
        # split name from full file path.
        mFiles = [each.split('/')[-1] for each in mFiles]
        vFiles = [each.split('/')[-1] for each in vFiles]
        # add files into list widget.
        self.bsAm_assetVersions_lw.addItems(mFiles)
        self.bsAm_assetVersions_lw.addItems(vFiles)

    def setScreenshot(self):
        self.imageView_lbl.setText('')
        assetName = self.bsAm_assetVersions_lw.currentItem().text()[:-3] + '.jpg'
        screenshotPath = os.path.dirname(self.getFilePath())
        if screenshotPath.endswith('version'):
            screenshotFilePath = screenshotPath + '/screenshot/' + assetName
        else:
            screenshotFilePath = screenshotPath + '/version/screenshot/' + assetName
        if os.path.exists(screenshotFilePath):
            self.imageView_lbl.setPixmap(screenshotFilePath)

    def setVersionInfo(self):
        assetName = self.bsAm_assetVersions_lw.currentItem().text()
        filePath = self.getFilePath()
        self.name_lbl.setText(assetName)
        self.type_lbl.setText('')
        self.owner_lbl.setText(bs_os.bs_getFileOwner(filePath))
        self.size_lbl.setText(bs_os.bs_getFileSize(filePath))
        self.time_lbl.setText(bs_os.bs_getFileDateTime(filePath))
        # get comment from the database.
        # get table name using split selection if file is version file so increase split numbers.
        if len(assetName.split('_')) == 6:
            tableName = assetName[:-8]
        else:
            tableName = assetName[:-3]
        try:
            addInfoDB = bs_database.Bs_Database()
            comment = addInfoDB.bs_databaseAssetComment(tableName, str(assetName))
            self.bsAm_versionInfo_TE.setText(comment)
        except:
            self.bsAm_versionInfo_TE.setText('comment not found\ndatabase connection error')

    def getFilePath(self):
        assetName = self.bsAm_assetVersions_lw.currentItem().text()
        assetDirPath = bs_pathGenerator.bs_getAssetPathFromFileName(assetName)
        return str(assetDirPath + assetName)

    def _importFile(self):
        bs_mayaFile.bs_importFile(self.getFilePath())
        self.close()

    def _openFile(self):
        bs_mayaFile.bs_openFile(self.getFilePath())
        self.close()

    def _referenceFile(self):
        bs_reference.bs_createReference(self.getFilePath(), prefixStyle='normal')


def main():
    winClass = Bs_AssetManagerUIConn(bs_qui.bs_mayaMainWindow())
    return winClass.show()
