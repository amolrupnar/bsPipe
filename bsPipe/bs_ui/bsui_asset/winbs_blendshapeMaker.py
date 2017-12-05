from PySide import QtGui

from bsPipe.bs_ui import bs_qui
from bsPipe.bs_ui.bsui_asset import bsui_blendshapeMaker
from bsPipe.bs_core.bs_mod import bs_blendshapeMaker

reload(bs_qui)
reload(bsui_blendshapeMaker)
reload(bs_blendshapeMaker)


class Bs_BlendshapeMakerUIConn(QtGui.QMainWindow, bsui_blendshapeMaker.Ui_bswBlendMaker_MW):
    def __init__(self, parent=None):
        super(Bs_BlendshapeMakerUIConn, self).__init__(parent)
        self.setupUi(self)
        self.connections()

    def connections(self):
        self.bsm_load_PB.clicked.connect(lambda: bs_qui.bs_fillListWidget(self.bsm_geometries_LW))
        self.bsm_make_PB.clicked.connect(self.makeBlendshape)

    def makeBlendshape(self):
        allGeometries = list()
        for i in range(self.bsm_geometries_LW.count()):
            allGeometries.append(self.bsm_geometries_LW.item(i).text())
        bs_blendshapeMaker.bswExtract(allGeometries)


def main():
    winClass = Bs_BlendshapeMakerUIConn(bs_qui.bs_mayaMainWindow())
    return winClass.show()
