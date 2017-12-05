from PySide import QtGui
import os

from bsPipe.bs_core.bs_animation import bs_shot
from bsPipe.bs_core import bs_pathGenerator
from bsPipe.bs_ui.bsui_anim import bsui_shotBuilder
from bsPipe.bs_ui import bs_qui

reload(bs_shot)
reload(bs_pathGenerator)
reload(bsui_shotBuilder)
reload(bs_qui)


class Bs_ShotBuilder(QtGui.QMainWindow, bsui_shotBuilder.Ui_bssb_shotBuilderMainWindow):
    def __init__(self, parent=None):
        super(Bs_ShotBuilder, self).__init__(parent)
        self.setupUi(self)
        self.actionExit.triggered.connect(self.close)
        self.uiDesignInit()
        self.validatorConnections()
        # get all Assets.
        self.chars = bs_pathGenerator.bs_getValidDeptAssetNames('Character', 'Rig')
        self.props = bs_pathGenerator.bs_getValidDeptAssetNames('Prop', 'Rig')
        self.sets = bs_pathGenerator.bs_getValidDeptAssetNames('Set', 'Rig')
        self.vehicle = bs_pathGenerator.bs_getValidDeptAssetNames('Vehicle', 'Rig')
        self.addAllAssetsInListWidget()
        self.bssb_add_PB.clicked.connect(self.addAssetsInSelectedListWidget)
        self.bssb_build_PB.clicked.connect(self.buildShot)

        # search line edit connection.
        self.bssb_charSearch_LE.textChanged.connect(
            lambda: bs_qui.bs_filterListWidget(self.bssb_chars_LW, self.bssb_charSearch_LE, self.chars))
        self.bssb_propSearch_LE.textChanged.connect(
            lambda: bs_qui.bs_filterListWidget(self.bssb_props_LW, self.bssb_propSearch_LE, self.props))
        self.bssb_setSearch_LE.textChanged.connect(
            lambda: bs_qui.bs_filterListWidget(self.bssb_set_LW, self.bssb_setSearch_LE, self.sets))
        self.bssb_vehicleSearch_LE.textChanged.connect(
            lambda: bs_qui.bs_filterListWidget(self.bssb_vehicles_LW, self.bssb_vehicleSearch_LE, self.vehicle))

    def validatorConnections(self):
        self.bssb_episode_LE.setText('ep')
        self.bssb_sequence_LE.setText('sq')
        self.bssb_shot_LE.setText('sh')

    def uiDesignInit(self):
        imageRootPath = os.path.dirname(os.path.dirname(__file__))
        imageMap = imageRootPath + '/bs_images/bsw_search.png'
        logoImageMap = imageRootPath + '/bs_images/bsw_shotBuilder.png'
        self.bssb_charSearch_lbl.setPixmap(imageMap)
        self.bssb_propSearch_lbl.setPixmap(imageMap)
        self.bssb_setSearch_lbl.setPixmap(imageMap)
        self.bssb_vehicleSearch_lbl.setPixmap(imageMap)
        self.bssb_logo_lbl.setPixmap(logoImageMap)
        # set list widget as extended selection.
        self.bssb_chars_LW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.bssb_props_LW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.bssb_set_LW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.bssb_vehicles_LW.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        # add Fonts.
        subObjFont = QtGui.QFont("Times", 12)
        self.bssb_riggedAsset_lbl.setFont(subObjFont)
        self.bssb_selectedAsset_lbl.setFont(subObjFont)
        self.bssb_startFrame_spinBox.setValue(101)
        self.bssb_endFrame_spinBox.setValue(102)

    def addAllAssetsInListWidget(self):
        self.bssb_chars_LW.addItems(self.chars)
        self.bssb_props_LW.addItems(self.props)
        self.bssb_set_LW.addItems(self.sets)
        self.bssb_vehicles_LW.addItems(self.vehicle)

    def addAssetsInSelectedListWidget(self):
        bs_qui.bs_getSelectedItemsFromTabWidgetAndAddInDestLW(self.bssb_assets_tabWidget, self.bssb_chars_LW,
                                                              self.bssb_props_LW, self.bssb_set_LW,
                                                              self.bssb_vehicles_LW, self.bssb_selectedAsset_LW)

    def buildShot(self):
        getEpi = self.bssb_episode_LE.text()
        getSeq = self.bssb_sequence_LE.text()
        getShot = self.bssb_shot_LE.text()
        if not getEpi.startswith('ep'):
            bs_qui.bs_displayMessage('error', 'wrong episode entered')
            return False
        if not getSeq.startswith('sq'):
            bs_qui.bs_displayMessage('error', 'wrong sequence entered')
            return False
        if not getShot.startswith('sh'):
            bs_qui.bs_displayMessage('error', 'wrong shot entered')
            return False
        startTime = self.bssb_startFrame_spinBox.value()
        endTime = self.bssb_endFrame_spinBox.value()
        # get all paths.
        environPaths = bs_shot.bs_getItemsFromLwFilterAndReturnPath(self.bssb_selectedAsset_LW)
        bs_shot.bs_shotBuild(getEpi, getSeq, getShot, startTime, endTime, environPaths)
        self.close()
        bs_qui.bs_displayMessage('success', 'Shot Created..')


def main():
    winClass = Bs_ShotBuilder(bs_qui.bs_mayaMainWindow())
    winClass.show()
