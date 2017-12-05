from PySide import QtGui
import os

from bsPipe.bs_ui.bsui_anim import bsui_shotBrowser
from bsPipe.bs_core import bs_pathGenerator
from bsPipe.bs_ui import bs_qui
from bsPipe.bs_core import bs_os, bs_mayaFile

reload(bsui_shotBrowser)
reload(bs_qui)
reload(bs_pathGenerator)
reload(bs_os)
reload(bs_mayaFile)


class Bs_ShotBrowser(QtGui.QMainWindow, bsui_shotBrowser.Ui_bsbr_ShotBrowser_MW):
    def __init__(self, parent=None):
        super(Bs_ShotBrowser, self).__init__(parent)
        self.setupUi(self)
        self._uiDesignInit()
        self._updateEpisodes()
        self.bsbr_episode_LW.currentItemChanged.connect(self._updateSequences)
        self.bsbr_sequence_LW.currentItemChanged.connect(self._updateShots)
        self.bsbr_shot_LW.currentItemChanged.connect(self._updateShotFile)
        self.bsbr_shotVersion_LW.currentItemChanged.connect(self._updateFileDetails)
        self.bsbr_animation_RB.toggled.connect(self._updateShotFile)
        self.bsbr_open_PB.clicked.connect(self._openShot)
        self.bsbr_import_PB.clicked.connect(self._importShot)

    def _uiDesignInit(self):
        # set close ui action to action exit.
        self.actionExit.triggered.connect(self.close)
        self.bsbr_animation_RB.setChecked(True)
        # add logo image.
        imageRootPath = os.path.dirname(os.path.dirname(__file__))
        logoImageMap = imageRootPath + '/bs_images/bsw_shotOpen.png'
        self.bsbr_logo_lbl.setPixmap(logoImageMap)
        # set fonts.
        subObjFont = QtGui.QFont("Times", 12)
        tagFont = QtGui.QFont("Times", 10)
        self.bsbr_episode_lbl.setFont(subObjFont)
        self.bsbr_sequence_lbl.setFont(subObjFont)
        self.bsbr_shot_lbl.setFont(subObjFont)
        self.bsbr_fileNameTag_lbl.setFont(tagFont)
        self.bsbr_sizeTag_lbl.setFont(tagFont)
        self.bsbr_ownerTag_lbl.setFont(tagFont)
        self.bsbr_lastModifiedTag_lbl.setFont(tagFont)
        # add search icon in the line edit.
        bs_qui.bs_setSearchIconInLineEdit(self.bsbr_episodeSearch_LE)
        bs_qui.bs_setSearchIconInLineEdit(self.bsbr_sequenceSearch_LE)
        bs_qui.bs_setSearchIconInLineEdit(self.bsbr_shotSearch_LE)
        # set placeholder text to search line edit.
        self.bsbr_episodeSearch_LE.setPlaceholderText('Search')
        self.bsbr_sequenceSearch_LE.setPlaceholderText('Search')
        self.bsbr_shotSearch_LE.setPlaceholderText('Search')
        # -----------------------------------------------
        # set stylesheet to labels and radio button.
        # -----------------------------------------------
        shotVersionStyleSheet = "QLabel { color : #E74C3C; }"
        tagStyleSheet = "QLabel { color : #85C1E9; }"
        lblStyleSheet = "QLabel { color : orange; }"
        stageStyleSheet = "QRadioButton { color : #85C1E9; }"
        self.bsbr_shotVersion_lbl.setStyleSheet(shotVersionStyleSheet)
        self.bsbr_shotDetails_lbl.setStyleSheet(shotVersionStyleSheet)
        self.bsbr_episode_lbl.setStyleSheet(shotVersionStyleSheet)
        self.bsbr_sequence_lbl.setStyleSheet(shotVersionStyleSheet)
        self.bsbr_shot_lbl.setStyleSheet(shotVersionStyleSheet)
        self.bsbr_animation_RB.setStyleSheet(stageStyleSheet)
        self.bsbr_layout_RB.setStyleSheet(stageStyleSheet)
        self.bsbr_fileNameTag_lbl.setStyleSheet(tagStyleSheet)
        self.bsbr_ownerTag_lbl.setStyleSheet(tagStyleSheet)
        self.bsbr_sizeTag_lbl.setStyleSheet(tagStyleSheet)
        self.bsbr_lastModifiedTag_lbl.setStyleSheet(tagStyleSheet)
        self.bsbr_fileName_lbl.setStyleSheet(lblStyleSheet)
        self.bsbr_owner_lbl.setStyleSheet(lblStyleSheet)
        self.bsbr_size_lbl.setStyleSheet(lblStyleSheet)
        self.bsbr_lastModified_lbl.setStyleSheet(lblStyleSheet)

    def _getCheckedRadioButton(self):
        layoutRB = self.bsbr_layout_RB
        if layoutRB.isChecked():
            return 'layout'
        else:
            return 'animation'

    def _updateEpisodes(self):
        self.bsbr_episode_LW.clear()
        self.bsbr_episode_LW.addItems(bs_pathGenerator.bs_getAllEpisodeList())

    def _updateSequences(self):
        self._clearFileDetails()
        selectedEpisode = self.bsbr_episode_LW.currentItem().text()
        sequences = bs_pathGenerator.bs_getAllSequenceList(selectedEpisode)
        self.bsbr_sequence_LW.clear()
        self.bsbr_sequence_LW.addItems(sequences)

    def _updateShots(self):
        self._clearFileDetails()
        selectedEpisode = self.bsbr_episode_LW.currentItem().text()
        selectedSequence = self.bsbr_sequence_LW.currentItem().text()
        shot = bs_pathGenerator.bs_getAllShotList(selectedEpisode, selectedSequence)
        self.bsbr_shot_LW.clear()
        self.bsbr_shot_LW.addItems(shot)

    def _updateShotFile(self):
        self._clearFileDetails()
        selectedEpisode = self.bsbr_episode_LW.currentItem().text()
        selectedSequence = self.bsbr_sequence_LW.currentItem().text()
        selectedShot = self.bsbr_shot_LW.currentItem().text()
        stage = self._getCheckedRadioButton()
        # get files.
        mainFile = bs_pathGenerator.bs_getShotFiles(selectedEpisode, selectedSequence, selectedShot)[stage]['mainFile']
        versions = bs_pathGenerator.bs_getShotFiles(selectedEpisode, selectedSequence, selectedShot)[stage]['versions']
        self.bsbr_shotVersion_LW.clear()
        # add main file and set color.
        if mainFile:
            mainFileItem = QtGui.QListWidgetItem()
            mainFileItem.setText(str(mainFile))
            self.bsbr_shotVersion_LW.addItem(mainFileItem)
            QtGui.QListWidgetItem.setForeground(mainFileItem, (QtGui.QColor(140, 255, 0)))
        if versions:
            self.bsbr_shotVersion_LW.addItems(versions)
            for each in range(self.bsbr_shotVersion_LW.count()):
                if self.bsbr_shotVersion_LW.item(each).text().find('/versions/') != -1:
                    verItem = self.bsbr_shotVersion_LW.item(each)
                    QtGui.QListWidgetItem.setForeground(verItem, (QtGui.QColor(255, 200, 0)))

    def _updateFileDetails(self):
        fileName = self.bsbr_shotVersion_LW.currentItem().text().split('/')[-1]
        fileSize = bs_os.bs_getFileSize(self.bsbr_shotVersion_LW.currentItem().text())
        dateModified = bs_os.bs_getFileDateTime(self.bsbr_shotVersion_LW.currentItem().text())
        self.bsbr_fileName_lbl.setText(fileName)
        self.bsbr_size_lbl.setText(fileSize)
        self.bsbr_lastModified_lbl.setText(dateModified)

    def _clearFileDetails(self):
        self.bsbr_fileName_lbl.setText('Not Exist')
        self.bsbr_size_lbl.setText('Not Exist')
        self.bsbr_lastModified_lbl.setText('Not Exist')

    def _openShot(self):
        selectedFile = self.bsbr_shotVersion_LW.currentItem().text()
        bs_mayaFile.bs_openFile(str(selectedFile))
        self.close()

    def _importShot(self):
        selectedFile = self.bsbr_shotVersion_LW.currentItem().text()
        bs_mayaFile.bs_importFile(str(selectedFile))
        self.close()


def main():
    winClass = Bs_ShotBrowser(bs_qui.bs_mayaMainWindow())
    winClass.show()
