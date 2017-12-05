import pymel.core as pm
import os

from bsPipe.bs_core import bs_screenshot
from bsPipe.bs_core import bs_pathGenerator
from bsPipe.bs_ui import bs_qui

reload(bs_screenshot)
reload(bs_pathGenerator)
reload(bs_qui)


def bs_publishCurrentAsset():
    """
    @ publish current opened asset.
    @ get details from top group and find path and then take a snapshot and saveAs main file and Version File.
    Returns:
            mainFilePath And versionFilePath.
    """
    # get environments.
    projectName = bs_pathGenerator.bs_getEnvDetails()['projectName']
    assetCategory, assetType, assetName, uid = bs_pathGenerator.bs_getAssetDetails()
    if assetCategory == 'Not Exist' or assetType == 'Not Exist' or assetName == 'Not Exist' or uid == 'Not Exist':
        bs_qui.bs_displayMessage('error', 'No Asset To Publish.....')
        return False
    mainDir = bs_pathGenerator.bs_getAssetDir(astName=assetName, astType=assetType, astDept=assetCategory)['dept']
    verDir = bs_pathGenerator.bs_getAssetDir(astName=assetName, astType=assetType, astDept=assetCategory)['ver']
    if not os.path.isdir(verDir):
        os.makedirs(verDir)
        fileName = projectName.lower() + '_' + uid.split('_')[1] + '_' + uid.split('_')[2] + '_' + uid.split('_')[
            4] + '_' + uid.split('_')[3] + '_v001.ma'
        filePath = verDir + fileName
    else:
        fileName = bs_pathGenerator.bs_versionUpPath(verDir)
        if fileName:
            filePath = verDir + fileName
        else:
            fileName = projectName.lower() + '_' + uid.split('_')[1] + '_' + uid.split('_')[2] + '_' + uid.split('_')[
                4] + '_' + uid.split('_')[3] + '_v001.ma'
            filePath = verDir + fileName
    # get screenshot.
    imageFilePath = verDir + 'snapshot/' + fileName[:-3] + '.iff'
    bs_screenshot.bs_getScreenShot(imageFilePath)
    # save version File.
    pm.saveAs(filePath)
    # save main File.
    pm.saveAs(mainDir + fileName[:-8] + '.ma')
    bs_qui.bs_displayMessage('success', 'Asset Publish Successfully...')
    return mainDir + fileName[:-8] + '.ma', filePath
