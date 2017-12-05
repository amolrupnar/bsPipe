import pymel.core as pm
import os
from PySide import QtGui

from bsPipe.bs_ui import bs_qui
from bsPipe.bs_ui.bsui_sanity import bsui_sanityMod
from bsPipe.bs_sanity import bs_sanityCore
from bsPipe.bs_sanity import bs_sanityMod

reload(bs_qui)
reload(bsui_sanityMod)
reload(bs_sanityCore)
reload(bs_sanityMod)


class Bs_SanityMod(QtGui.QMainWindow, bsui_sanityMod.Ui_bs_san_MainWindow):
    def __init__(self, parent=None):
        super(Bs_SanityMod, self).__init__(parent)
        self.setupUi(self)
        # set fonts to label.
        objFont = QtGui.QFont("Verdana", 12, QtGui.QFont.DemiBold)
        self.label.setFont(objFont)
        self.label_2.setFont(objFont)
        self.label_3.setFont(objFont)
        # set logo image.
        imageRootPath = os.path.dirname(os.path.dirname(__file__))
        imageMap = imageRootPath + '/bs_images/bsw_modelSanityCheck.png'
        self.bs_san_logo_lbl.setPixmap(imageMap)
        self.actionExit.triggered.connect(self.close)
        self.connections()

    def connections(self):
        # check duplicates.
        self.bs_san_checkDuplicates_c_pb.clicked.connect(self.checkDuplicate)
        self.bs_san_checkDuplicates_s_pb.clicked.connect(lambda: self.checkDuplicate(select=True))
        # check display layers.
        self.bs_san_checkDisplayLayer_c_pb.clicked.connect(self.checkDisplayLayer)
        self.bs_san_checkDisplayLayer_s_pb.clicked.connect(lambda: self.checkDisplayLayer(select=True))
        # check render layers.
        self.bs_san_checkRenderLayer_c_pb.clicked.connect(self.checkRenderLayer)
        self.bs_san_checkRenderLayer_s_pb.clicked.connect(lambda: self.checkRenderLayer(select=True))
        # check namespace.
        self.bs_san_checkNamespaces_c_pb.clicked.connect(self.checkNamespaces)
        # self.bs_san_checkNamespaces_s_pb.clicked.connect(lambda: self.checkNamespaces(select=True))
        # check all transforms are freezed or not.
        self.bs_san_checkAllTransFreeze_c_pb.clicked.connect(self.checkNonFreezedTransforms)
        self.bs_san_checkAllTransFreeze_s_pb.clicked.connect(lambda: self.checkNonFreezedTransforms(select=True))
        # check all non freezed vertex.
        self.bs_san_checkAllVertFreeze_c_pb.clicked.connect(self.checkNonFreezeVertex)
        self.bs_san_checkAllVertFreeze_s_pb.clicked.connect(lambda: self.checkNonFreezeVertex(select=True))
        # check all geo endswith _geo in suffix.
        self.bs_san_checkAllGeoEndGeo_c_pb.clicked.connect(self.checkGeoSuffix)
        self.bs_san_checkAllGeoEndGeo_s_pb.clicked.connect(lambda: self.checkGeoSuffix(select=True))
        # check all groups endswith _grp in suffix.
        self.bs_san_checkAllGroupEndGrp_c_pb.clicked.connect(self.checkGrpSuffix)
        self.bs_san_checkAllGroupEndGrp_s_pb.clicked.connect(lambda: self.checkGrpSuffix(select=True))
        # check all shape naming.
        self.bs_san_checkShapeName_c_pb.clicked.connect(self.checkShapeName)
        self.bs_san_checkShapeName_s_pb.clicked.connect(lambda: self.checkShapeName(select=True))
        # check multiple shapes.
        self.bs_san_checkMoreThan1Shapes_c_pb.clicked.connect(self.checkMultiShapes)
        self.bs_san_checkMoreThan1Shapes_s_pb.clicked.connect(lambda: self.checkMultiShapes(select=True))
        # check naming case.
        self.bs_san_checkAllTransStartLowerCase_c_pb.clicked.connect(self.checkNameCasing)
        self.bs_san_checkAllTransStartLowerCase_s_pb.clicked.connect(lambda: self.checkNameCasing(select=True))

    def checkDuplicate(self, select=None):
        dupObjects = bs_sanityCore.bs_findDuplicates()
        if dupObjects:
            self.bs_san_checkDuplicates_c_pb.setStyleSheet("background-color: red")
            self.bs_san_checkDuplicates_s_pb.setStyleSheet("background-color: red")
        else:
            self.bs_san_checkDuplicates_c_pb.setStyleSheet("background-color: green")
            self.bs_san_checkDuplicates_s_pb.setStyleSheet("background-color: green")
        if select:
            if dupObjects:
                pm.select(dupObjects, r=True)

    def checkDisplayLayer(self, select=None):
        allLayers = bs_sanityCore.bs_sanityCheckDisplayLayer()
        if allLayers:
            self.bs_san_checkDisplayLayer_c_pb.setStyleSheet("background-color: red")
            self.bs_san_checkDisplayLayer_s_pb.setStyleSheet("background-color: red")
        else:
            self.bs_san_checkDisplayLayer_c_pb.setStyleSheet("background-color: green")
            self.bs_san_checkDisplayLayer_s_pb.setStyleSheet("background-color: green")
        if select:
            if allLayers:
                pm.select(allLayers, r=True)

    def checkRenderLayer(self, select=None):
        allLayers = bs_sanityCore.bs_sanityCheckRenderLayer()
        if allLayers:
            self.bs_san_checkRenderLayer_c_pb.setStyleSheet("background-color: red")
            self.bs_san_checkRenderLayer_s_pb.setStyleSheet("background-color: red")
        else:
            self.bs_san_checkRenderLayer_c_pb.setStyleSheet("background-color: green")
            self.bs_san_checkRenderLayer_s_pb.setStyleSheet("background-color: green")
        if select:
            if allLayers:
                pm.select(allLayers, r=True)

    def checkNamespaces(self):
        allLayers = bs_sanityCore.bs_sanityCheckNamespaces()
        if allLayers:
            self.bs_san_checkNamespaces_c_pb.setStyleSheet("background-color: red")
            self.bs_san_checkNamespaces_s_pb.setStyleSheet("background-color: red")
        else:
            self.bs_san_checkNamespaces_c_pb.setStyleSheet("background-color: green")
            self.bs_san_checkNamespaces_s_pb.setStyleSheet("background-color: green")

    def checkNonFreezedTransforms(self, select=None):
        checkFreezed = bs_sanityCore.bs_checkAllTransformFreezed()
        if checkFreezed:
            self.bs_san_checkAllTransFreeze_c_pb.setStyleSheet("background-color: red")
            self.bs_san_checkAllTransFreeze_s_pb.setStyleSheet("background-color: red")
        else:
            self.bs_san_checkAllTransFreeze_c_pb.setStyleSheet("background-color: green")
            self.bs_san_checkAllTransFreeze_s_pb.setStyleSheet("background-color: green")
        if select:
            if checkFreezed:
                pm.select(checkFreezed, r=True)

    def checkNonFreezeVertex(self, select=None):
        checker = bs_sanityMod.bs_checkNonFreezedVertex()
        if checker:
            self.bs_san_checkAllVertFreeze_c_pb.setStyleSheet("background-color: red")
            self.bs_san_checkAllVertFreeze_s_pb.setStyleSheet("background-color: red")
        else:
            self.bs_san_checkAllVertFreeze_c_pb.setStyleSheet("background-color: green")
            self.bs_san_checkAllVertFreeze_s_pb.setStyleSheet("background-color: green")
        if select:
            if checker:
                pm.select(checker[1], r=True)

    def checkMultiShapes(self, select=None):
        checks = bs_sanityMod.bs_sanityModCheckBasics()
        if checks['multiShapes']:
            self.bs_san_checkMoreThan1Shapes_c_pb.setStyleSheet("background-color: red")
            self.bs_san_checkMoreThan1Shapes_s_pb.setStyleSheet("background-color: red")
        else:
            self.bs_san_checkMoreThan1Shapes_c_pb.setStyleSheet("background-color: green")
            self.bs_san_checkMoreThan1Shapes_s_pb.setStyleSheet("background-color: green")
        if select:
            if checks['multiShapes']:
                pm.select(checks['multiShapes'], r=True)

    def checkGeoSuffix(self, select=None):
        checks = bs_sanityMod.bs_sanityModCheckBasics()
        if checks['geo']:
            self.bs_san_checkAllGeoEndGeo_c_pb.setStyleSheet("background-color: red")
            self.bs_san_checkAllGeoEndGeo_s_pb.setStyleSheet("background-color: red")
        else:
            self.bs_san_checkAllGeoEndGeo_c_pb.setStyleSheet("background-color: green")
            self.bs_san_checkAllGeoEndGeo_s_pb.setStyleSheet("background-color: green")
        if select:
            if checks['geo']:
                pm.select(checks['geo'], r=True)

    def checkGrpSuffix(self, select=None):
        checks = bs_sanityMod.bs_sanityModCheckBasics()
        if checks['grp']:
            self.bs_san_checkAllGroupEndGrp_c_pb.setStyleSheet("background-color: red")
            self.bs_san_checkAllGroupEndGrp_s_pb.setStyleSheet("background-color: red")
        else:
            self.bs_san_checkAllGroupEndGrp_c_pb.setStyleSheet("background-color: green")
            self.bs_san_checkAllGroupEndGrp_s_pb.setStyleSheet("background-color: green")
        if select:
            if checks['grp']:
                pm.select(checks['grp'], r=True)

    def checkShapeName(self, select=None):
        checks = bs_sanityMod.bs_sanityModCheckBasics()
        if checks['shapeNamingIssue']:
            self.bs_san_checkShapeName_c_pb.setStyleSheet("background-color: red")
            self.bs_san_checkShapeName_s_pb.setStyleSheet("background-color: red")
        else:
            self.bs_san_checkShapeName_c_pb.setStyleSheet("background-color: green")
            self.bs_san_checkShapeName_s_pb.setStyleSheet("background-color: green")
        if select:
            if checks['shapeNamingIssue']:
                pm.select(checks['shapeNamingIssue'], r=True)

    def checkNameCasing(self, select=None):
        checks = bs_sanityMod.bs_sanityModCheckBasics()
        if checks['case']:
            self.bs_san_checkAllTransStartLowerCase_c_pb.setStyleSheet("background-color: red")
            self.bs_san_checkAllTransStartLowerCase_s_pb.setStyleSheet("background-color: red")
        else:
            self.bs_san_checkAllTransStartLowerCase_c_pb.setStyleSheet("background-color: green")
            self.bs_san_checkAllTransStartLowerCase_s_pb.setStyleSheet("background-color: green")
        if select:
            if checks['case']:
                pm.select(checks['case'], r=True)


def main():
    winClass = Bs_SanityMod(bs_qui.bs_mayaMainWindow())
    winClass.show()
