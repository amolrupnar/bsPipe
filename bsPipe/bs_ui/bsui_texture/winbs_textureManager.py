import os
from PySide import QtGui

from bsPipe.bs_ui import bs_qui
from bsPipe.bs_ui.bsui_texture import bsui_textureManager
from bsPipe.bs_core import bs_pathGenerator, bs_os
from bsPipe.bs_core.bs_texture import bs_shadingEngine, bs_fileTexture

reload(bs_qui)
reload(bsui_textureManager)
reload(bs_pathGenerator)
reload(bs_shadingEngine)
reload(bs_os)
reload(bs_fileTexture)


class Bs_TextureManager(QtGui.QMainWindow, bsui_textureManager.Ui_bstm_mainWindow_MW):
    def __init__(self, parent=None):
        super(Bs_TextureManager, self).__init__(parent)
        self.setupUi(self)
        # set logo image.
        imageRootPath = os.path.dirname(os.path.dirname(__file__))
        imageMap = imageRootPath + '/bs_images/bsw_textureManger.png'
        self.bstm_logo_lbl.setPixmap(imageMap)
        # change current font.
        headerFont = QtGui.QFont("Times", 12, QtGui.QFont.Bold)
        objFont = QtGui.QFont("Verdana", 10, QtGui.QFont.StyleItalic)
        self.label_2.setFont(headerFont)
        self.label_4.setFont(headerFont)
        self.bstm_assetName_lbl.setFont(objFont)
        self.bstm_assetType_lbl.setFont(objFont)
        # fill asset details.
        assetCategory, assetType, assetName, uid = bs_pathGenerator.bs_getAssetDetails()
        self.bstm_assetName_lbl.setText(assetName)
        self.bstm_assetType_lbl.setText(assetType)
        # set button clicked commands.
        self.bstm_exportShader_pb.clicked.connect(self.exportShaders)
        self.bstm_importShader_pb.clicked.connect(self.importShaders)
        # exported shader path line edit fill and set read only.
        self.addShaderPathInLineEdit()
        self.bstm_exportPath_le.setReadOnly(True)
        self.bstm_exportedPath_pb.clicked.connect(self.openExportedShaderPathDir)
        # get and set all file texture root path.
        if bs_fileTexture.bs_getAllFileTexturePathIfValid():
            if bs_fileTexture.bs_checkAllFileTexturePathIsComingFromEnv():
                self.bstm_currentRootPath_le.setText(bs_fileTexture.bs_checkAllFileTexturePathIsComingFromEnv())
                self.bstm_convertPath_le.setText(bs_fileTexture.bs_checkAllFileTexturePathIsComingFromEnv())
            else:
                self.bstm_currentRootPath_le.setText('all path are not coming with environment variable.')
        else:
            self.bstm_currentRootPath_le.setText('file texture path not from valid directory...')
        self.bstm_currentRootPath_pb.clicked.connect(self.openSourceImageDir)
        self.bstm_convertPath_pb.clicked.connect(self.convertPath)
        self.bstm_refresh_pb.clicked.connect(self.refresh)
        self.bstm_currentRootPath_le.setReadOnly(True)
        self.bstm_convertPath_le.setReadOnly(True)

    def convertPath(self):
        bs_fileTexture.bs_convertAllFileTexturePathInEnvVariable()
        self.refresh()

    def refresh(self):
        # get and set all file texture root path.
        if bs_fileTexture.bs_getAllFileTexturePathIfValid():
            if bs_fileTexture.bs_checkAllFileTexturePathIsComingFromEnv():
                self.bstm_currentRootPath_le.setText(bs_fileTexture.bs_checkAllFileTexturePathIsComingFromEnv())
                self.bstm_convertPath_le.setText(bs_fileTexture.bs_checkAllFileTexturePathIsComingFromEnv())
            else:
                self.bstm_currentRootPath_le.setText('all path are not coming with environment variable.')
        else:
            self.bstm_currentRootPath_le.setText('file texture path not from valid directory...')
        self.addShaderPathInLineEdit()

    def openSourceImageDir(self):
        urp = self.bstm_convertPath_le.text()
        if urp.startswith('$BSW_PROD_SERVER/'):
            resolvedPath = urp.replace('$BSW_PROD_SERVER/', bs_pathGenerator.bs_getEnvDetails()['rootPath'])
            bs_os.bs_openDirInExplorer(resolvedPath)
            bs_qui.bs_displayMessage('success', 'sourceimage directory opened in your os explorer.')
            return True
        bs_qui.bs_displayMessage('error', 'directory not found..')
        return False

    def openExportedShaderPathDir(self):
        exportedPath = self.bstm_exportPath_le.text()
        expDir = str()
        for each in exportedPath.split('/')[:-1]:
            expDir += each + '/'
        if os.path.isdir(expDir):
            bs_os.bs_openDirInExplorer(expDir)
            bs_qui.bs_displayMessage('success', 'Shader directory opened in your os explorer.')
            return True
        bs_qui.bs_displayMessage('error', 'Invalid Shader Directory.')
        return False

    def addShaderPathInLineEdit(self):
        assetCategory, assetType, assetName, uid = bs_pathGenerator.bs_getAssetDetails()
        if assetType == 'Not Exist' or assetName == 'Not Exist':
            self.bstm_exportPath_le.setText('asset not found in scene.')
            return False
        deptDir = bs_pathGenerator.bs_getAssetDir(astType=assetType, astDept='Texture', astName=assetName)['dept']
        shaderFileName = bs_pathGenerator.bs_getMainFileName().replace('_tex.', '_shd.')
        if os.path.isfile(deptDir + 'shaders/' + shaderFileName):
            self.bstm_exportPath_le.setText(deptDir + 'shaders/' + shaderFileName)
        else:
            self.bstm_exportPath_le.setText('shaders not found')

    def exportShaders(self):
        # get shader directory.
        assetCategory, assetType, assetName, uid = bs_pathGenerator.bs_getAssetDetails()
        deptDir = bs_pathGenerator.bs_getAssetDir(astType=assetType, astDept='Texture', astName=assetName)[
            'dept']
        if not os.path.isdir(deptDir + 'shaders'):
            os.makedirs(deptDir + 'shaders')
        shaderDir = deptDir + 'shaders/'
        shaderFileName = bs_pathGenerator.bs_getMainFileName().replace('_tex.', '_shd.')
        jsonFileName = bs_pathGenerator.bs_getMainFileName().replace('_tex.ma', '_shd.json')
        bs_shadingEngine.bs_exportShaders(shaderDir + shaderFileName, shaderDir + jsonFileName)
        self.refresh()

    def importShaders(self):
        # get shader directory.
        assetCategory, assetType, assetName, uid = bs_pathGenerator.bs_getAssetDetails()
        deptDir = bs_pathGenerator.bs_getAssetDir(astType=assetType, astDept='Texture', astName=assetName)[
            'dept']
        if not os.path.isdir(deptDir + 'shaders'):
            os.makedirs(deptDir + 'shaders')
        shaderDir = deptDir + 'shaders/'
        shaderFileName = bs_pathGenerator.bs_getMainFileName().replace('_tex.', '_shd.')
        jsonFileName = bs_pathGenerator.bs_getMainFileName().replace('_tex.ma', '_shd.json')
        bs_shadingEngine.bs_importShaders(shaderDir + shaderFileName, shaderDir + jsonFileName)
        self.refresh()


def main():
    winClass = Bs_TextureManager(bs_qui.bs_mayaMainWindow())
    winClass.show()
