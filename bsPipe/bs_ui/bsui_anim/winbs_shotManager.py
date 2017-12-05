from PySide import QtGui
import os

from bsPipe.bs_ui import bs_qui
from bsPipe.bs_ui.bsui_anim import bsui_shotManager
from bsPipe.bs_core import bs_pathGenerator
from bsPipe.bs_core import bs_reference
from bsPipe.bs_core.bs_animation import bs_shot, bs_playblast

reload(bs_qui)
reload(bsui_shotManager)
reload(bs_reference)
reload(bs_pathGenerator)
reload(bs_shot)
reload(bs_playblast)


class Bs_ShotManager(QtGui.QMainWindow, bsui_shotManager.Ui_bsshm_shotManager_MainWindow):
    def __init__(self, parent=None):
        super(Bs_ShotManager, self).__init__(parent)
        self._getInitialDetails()
        # set Ui Connections.
        self.setupUi(self)
        self._initUiDesign()
        self._fillShotDetails()
        self._fillElementsInCurrentAsset()
        self._fillAllAssetFromServer()
        self.uiSearchEventAdded()
        self._listWidgetSelectionWithCheckBoxState()
        self.bsshm_add_PB.clicked.connect(self._addSelectedAssetsInSelectedLW)
        self.bsshm_addSelectedAssetInScene_PB.clicked.connect(self._addNewAssets)
        # remove selected items from list widget.
        self.bsshm_remove_PB.clicked.connect(lambda: bs_qui.bs_removeSelectedItemsFromQLW(self.bsshm_selectedAsset_LW))
        self._addCurrentReference()
        self.bsshm_removeSelectedAssets_PB.clicked.connect(self._removeReference)
        # file save as button click command added.
        self.bsshm_CA_layout_PB.clicked.connect(lambda: self._saveAsShot('lay'))
        self.bsshm_CA_animation_PB.clicked.connect(lambda: self._saveAsShot('ani'))
        # add buttons command.
        self.bsshm_CA_playblast_PB.clicked.connect(bs_playblast.bs_playblast)

    def _listWidgetSelectionWithCheckBoxState(self):
        # select all and clear all check box connections.
        self.bsshm_CA_charSelAll_cBox.stateChanged.connect(
            lambda: bs_qui.bs_qListWidgetSelectionChangeUsingCheckBox(self.bsshm_CA_charSelAll_cBox,
                                                                      self.bsshm_CA_charClearAll_cBox,
                                                                      self.bsshm_CA_char_LW, selMode=True))
        self.bsshm_CA_charClearAll_cBox.stateChanged.connect(
            lambda: bs_qui.bs_qListWidgetSelectionChangeUsingCheckBox(self.bsshm_CA_charSelAll_cBox,
                                                                      self.bsshm_CA_charClearAll_cBox,
                                                                      self.bsshm_CA_char_LW, selMode=False))
        self.bsshm_CA_propSelAll_cBox.stateChanged.connect(
            lambda: bs_qui.bs_qListWidgetSelectionChangeUsingCheckBox(self.bsshm_CA_propSelAll_cBox,
                                                                      self.bsshm_CA_propClearAll_cBox,
                                                                      self.bsshm_CA_prop_LW, selMode=True))
        self.bsshm_CA_propClearAll_cBox.stateChanged.connect(
            lambda: bs_qui.bs_qListWidgetSelectionChangeUsingCheckBox(self.bsshm_CA_propSelAll_cBox,
                                                                      self.bsshm_CA_propClearAll_cBox,
                                                                      self.bsshm_CA_prop_LW, selMode=False))
        self.bsshm_CA_setSelAll_cBox.stateChanged.connect(
            lambda: bs_qui.bs_qListWidgetSelectionChangeUsingCheckBox(self.bsshm_CA_setSelAll_cBox,
                                                                      self.bsshm_CA_setClearAll_cBox,
                                                                      self.bsshm_CA_set_LW, selMode=True))
        self.bsshm_CA_setClearAll_cBox.stateChanged.connect(
            lambda: bs_qui.bs_qListWidgetSelectionChangeUsingCheckBox(self.bsshm_CA_setSelAll_cBox,
                                                                      self.bsshm_CA_setClearAll_cBox,
                                                                      self.bsshm_CA_set_LW, selMode=False))
        self.bsshm_CA_vehicleSelAll_cBox.stateChanged.connect(
            lambda: bs_qui.bs_qListWidgetSelectionChangeUsingCheckBox(self.bsshm_CA_vehicleSelAll_cBox,
                                                                      self.bsshm_CA_vehicleClearAll_cBox,
                                                                      self.bsshm_CA_vehicle_LW, selMode=True))
        self.bsshm_CA_vehicleClearAll_cBox.stateChanged.connect(
            lambda: bs_qui.bs_qListWidgetSelectionChangeUsingCheckBox(self.bsshm_CA_vehicleSelAll_cBox,
                                                                      self.bsshm_CA_vehicleClearAll_cBox,
                                                                      self.bsshm_CA_vehicle_LW, selMode=False))

    def _fillShotDetails(self):
        epi, seq, shot, stage = bs_pathGenerator.bs_shotDetailsCheckAndReturn()
        if epi and shot and seq and stage:
            self.bsshm_fileType_lbl.setText(stage)
            self.bsshm_episode_lbl.setText(epi)
            self.bsshm_sequence_lbl.setText(seq)
            self.bsshm_shot_lbl.setText(shot)

    def _getInitialDetails(self):
        # get references category wise list.
        self.refChars = bs_reference.bs_getReference()['char'].keys()
        self.refProps = bs_reference.bs_getReference()['prop'].keys()
        self.refSets = bs_reference.bs_getReference()['set'].keys()
        self.refVehicles = bs_reference.bs_getReference()['vehicle'].keys()
        self.refChars.sort()
        self.refProps.sort()
        self.refSets.sort()
        self.refVehicles.sort()
        # get all rigged assets from server.
        self.allChars = bs_pathGenerator.bs_getValidDeptAssetNames('Character', 'Rig')
        self.allProps = bs_pathGenerator.bs_getValidDeptAssetNames('Prop', 'Rig')
        self.allSets = bs_pathGenerator.bs_getValidDeptAssetNames('Set', 'Rig')
        self.allVehicles = bs_pathGenerator.bs_getValidDeptAssetNames('Vehicle', 'Rig')

    def _initUiDesign(self):
        # disabled codes.
        self.bsshm_CA_playblastBatch_cBox.setVisible(False)
        self.bsshm_fixFrameRange_PB.setDisabled(True)
        self.bsshm_CA_exportCache_PB.setDisabled(True)
        self.bsshm_CA_exportAnim_PB.setDisabled(True)
        self.bsshm_CA_exportCamera_PB.setDisabled(True)
        # working codes.
        self.actionExit.triggered.connect(self.close)
        imageRootPath = os.path.dirname(os.path.dirname(__file__))
        logoImageMap = imageRootPath + '/bs_images/bsw_shotManager.png'
        self.bsshm_logo_lbl.setPixmap(logoImageMap)
        bs_qui.bs_setSearchIconInLineEdit(self.bsshm_CA_charSearch_LE)
        bs_qui.bs_setSearchIconInLineEdit(self.bsshm_CA_propSearch_LE)
        bs_qui.bs_setSearchIconInLineEdit(self.bsshm_CA_setSearch_LE)
        bs_qui.bs_setSearchIconInLineEdit(self.bsshm_CA_vehicleSearch_LE)
        bs_qui.bs_setSearchIconInLineEdit(self.bsshm_charSearch_LE)
        bs_qui.bs_setSearchIconInLineEdit(self.bsshm_propSearch_LE)
        bs_qui.bs_setSearchIconInLineEdit(self.bsshm_setSearch_LE)
        bs_qui.bs_setSearchIconInLineEdit(self.bsshm_vehicleSearch_LE)

        # set list widget as extended selection.
        self.bsshm_chars_LW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.bsshm_props_LW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.bsshm_set_LW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.bsshm_vehicles_LW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.bsshm_currentAsset_LW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.bsshm_selectedAsset_LW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.bsshm_CA_char_LW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.bsshm_CA_prop_LW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.bsshm_CA_set_LW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.bsshm_CA_vehicle_LW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        # add Fonts.
        headObjFont = QtGui.QFont("Times", 12)
        subObjFont = QtGui.QFont("Times", 12)
        self.bsshm_episode_lblHeader.setFont(headObjFont)
        self.bsshm_sequence_lblHeader.setFont(headObjFont)
        self.bsshm_shot_lblHeader.setFont(headObjFont)
        self.bsshm_fileType_lblHeader.setFont(headObjFont)
        self.bsshm_fixFrameRange_lbl.setFont(headObjFont)
        self.bsshm_episode_lbl.setFont(subObjFont)
        self.bsshm_sequence_lbl.setFont(subObjFont)
        self.bsshm_shot_lbl.setFont(subObjFont)
        self.bsshm_fileType_lbl.setFont(subObjFont)

    def uiSearchEventAdded(self):
        self.bsshm_CA_charSearch_LE.textChanged.connect(
            lambda: bs_qui.bs_filterListWidget(self.bsshm_CA_char_LW, self.bsshm_CA_charSearch_LE, self.refChars))
        self.bsshm_CA_propSearch_LE.textChanged.connect(
            lambda: bs_qui.bs_filterListWidget(self.bsshm_CA_prop_LW, self.bsshm_CA_propSearch_LE, self.refProps))
        self.bsshm_CA_setSearch_LE.textChanged.connect(
            lambda: bs_qui.bs_filterListWidget(self.bsshm_CA_set_LW, self.bsshm_CA_setSearch_LE, self.refSets))
        self.bsshm_CA_vehicleSearch_LE.textChanged.connect(
            lambda: bs_qui.bs_filterListWidget(self.bsshm_CA_vehicle_LW, self.bsshm_CA_vehicleSearch_LE,
                                               self.refVehicles))
        # add search events in server asset library.
        self.bsshm_charSearch_LE.textChanged.connect(
            lambda: bs_qui.bs_filterListWidget(self.bsshm_chars_LW, self.bsshm_charSearch_LE, self.allChars))
        self.bsshm_propSearch_LE.textChanged.connect(
            lambda: bs_qui.bs_filterListWidget(self.bsshm_props_LW, self.bsshm_propSearch_LE, self.allProps))
        self.bsshm_setSearch_LE.textChanged.connect(
            lambda: bs_qui.bs_filterListWidget(self.bsshm_set_LW, self.bsshm_setSearch_LE, self.allSets))
        self.bsshm_vehicleSearch_LE.textChanged.connect(
            lambda: bs_qui.bs_filterListWidget(self.bsshm_vehicles_LW, self.bsshm_vehicleSearch_LE, self.allVehicles))

    def _fillElementsInCurrentAsset(self):
        # get references category wise list.
        refChars = bs_reference.bs_getReference()['char'].keys()
        refProps = bs_reference.bs_getReference()['prop'].keys()
        refSets = bs_reference.bs_getReference()['set'].keys()
        refVehicles = bs_reference.bs_getReference()['vehicle'].keys()
        refChars.sort()
        refProps.sort()
        refSets.sort()
        refVehicles.sort()
        # clear all list widgets.
        self.bsshm_CA_char_LW.clear()
        self.bsshm_CA_prop_LW.clear()
        self.bsshm_CA_set_LW.clear()
        self.bsshm_CA_vehicle_LW.clear()
        # add it in list widget.
        self.bsshm_CA_char_LW.addItems(refChars)
        self.bsshm_CA_prop_LW.addItems(refProps)
        self.bsshm_CA_set_LW.addItems(refSets)
        self.bsshm_CA_vehicle_LW.addItems(refVehicles)

    def _fillAllAssetFromServer(self):
        self.bsshm_chars_LW.addItems(self.allChars)
        self.bsshm_props_LW.addItems(self.allProps)
        self.bsshm_set_LW.addItems(self.allSets)
        self.bsshm_vehicles_LW.addItems(self.allVehicles)

    def _addSelectedAssetsInSelectedLW(self):
        bs_qui.bs_getSelectedItemsFromTabWidgetAndAddInDestLW(self.bsshm_assets_tabWidget, self.bsshm_chars_LW,
                                                              self.bsshm_props_LW, self.bsshm_set_LW,
                                                              self.bsshm_vehicles_LW, self.bsshm_selectedAsset_LW)

    def _addNewAssets(self):
        assetsPath = bs_shot.bs_getItemsFromLwFilterAndReturnPath(self.bsshm_selectedAsset_LW)
        bs_shot.bs_referenceAssetsInCurrentShot(assetsPath)
        bs_qui.bs_displayMessage('success', 'new assets added success')
        self._addCurrentReference()
        self._fillElementsInCurrentAsset()
        self.bsshm_selectedAsset_LW.clear()

    def _addCurrentReference(self):
        allRef = bs_reference.bs_getReference()
        refChar = allRef['char']
        refProp = allRef['prop']
        refSet = allRef['set']
        refVehicle = allRef['vehicle']
        refList = refChar.keys() + refProp.keys() + refSet.keys() + refVehicle.keys()
        self.bsshm_currentAsset_LW.clear()
        self.bsshm_currentAsset_LW.addItems(refList)

    def _removeReference(self):
        bs_qui.bs_removeSelectedReferenceFromQLW(self.bsshm_currentAsset_LW)
        self._addCurrentReference()
        self._fillElementsInCurrentAsset()

    def _saveAsShot(self, shotStage):
        # shotStage currently ('lay', 'ani').
        bs_pathGenerator.bs_saveAnimFile(shotStage=shotStage)
        self._fillShotDetails()


def main():
    winClass = Bs_ShotManager(bs_qui.bs_mayaMainWindow())
    winClass.show()
