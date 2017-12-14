from PySide import QtGui

from bsPipe.bs_ui import bs_qui
from bsPipe.bs_ui.bsui_asset import bsui_assetCreate
from bsPipe.bs_asset import bs_assetCreate
from bsPipe.bs_core import bs_pathGenerator

reload(bs_qui)
reload(bsui_assetCreate)
reload(bs_assetCreate)
reload(bs_pathGenerator)


class Bs_AssetCreate(QtGui.QMainWindow, bsui_assetCreate.Ui_bsag_assetGenerate_MW):
    def __init__(self, parent=None):
        super(Bs_AssetCreate, self).__init__(parent)
        # get environments.
        self.projectType = bs_pathGenerator.bs_getEnv()['projectType']
        self.setupUi(self)
        # add restrictions in ui.
        self.bsag_epNumber_LE.setValidator(QtGui.QIntValidator(self.bsag_epNumber_LE))
        self.bsag_epNumber_LE.setMaxLength(3)
        self.bsag_ep_LE.setReadOnly(True)
        # hide episode fields if environment is movie.
        if not self.projectType == 'series':
            self.bsag_epNumber_LE.hide()
            self.bsag_ep_LE.hide()
            self.label_3.hide()
        # add crete command in button.
        self.bsag_createAsset_pb.clicked.connect(self.connections)

    def connections(self):
        assetName = self.bsag_assetName_LE.text()
        assetGrade = self.bsag_assetGrade_comboBox.currentText()
        assetType = self.bsag_assetType_comboBox.currentText()
        episode = self.bsag_ep_LE.text() + self.bsag_epNumber_LE.text()
        if self.projectType == 'series':
            bs_assetCreate.bs_createModelBase('geo', assetName, assetGrade, assetType, episode=episode)
        else:
            bs_assetCreate.bs_createModelBase('geo', assetName, assetGrade, assetType)


def main():
    winClass = Bs_AssetCreate(bs_qui.bs_mayaMainWindow())
    winClass.show()
