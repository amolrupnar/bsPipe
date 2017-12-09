import pymel.core as pm
import shutil

from bsPipe.bs_core import bs_pathGenerator, bs_screenshot
from bsPipe.bs_ui import bs_qui

reload(bs_pathGenerator)
reload(bs_screenshot)
reload(bs_qui)


def bs_publishCurrentAsset():
    """
    @ publish current opened asset.
    Returns:
            mainFilePath And versionFilePath.
    """
    # get environments.
    projectType = bs_pathGenerator.bs_getEnv()['projectType']
    assetDept, assetType, assetName, uid, episode = bs_pathGenerator.bs_getAssetDetails()
    if assetDept == 'Not Exist' or assetType == 'Not Exist' or assetName == 'Not Exist' or uid == 'Not Exist':
        bs_qui.bs_displayMessage('error', 'Asset not found To Publish.....')
        return False
    # get asset directories and create directories if not exist.
    if projectType == 'series':
        mainDir = bs_pathGenerator.bs_getAssetDeptDirs(assetType, assetName, episode=episode)[assetDept]
        verDir = bs_pathGenerator.bs_getAssetDeptDirs(assetType, assetName, episode=episode)[assetDept + 'Version']
        bs_pathGenerator.bs_createAssetDirectories(assetType, assetName, episode=episode)
    else:
        mainDir = bs_pathGenerator.bs_getAssetDeptDirs(assetType, assetName)[assetDept]
        verDir = bs_pathGenerator.bs_getAssetDeptDirs(assetType, assetName)[assetDept + 'Version']
        bs_pathGenerator.bs_createAssetDirectories(assetType, assetName)
    # get file paths to save the file.
    mainFilePath = mainDir + bs_pathGenerator.bs_getCurrentAssetMainFileName()
    versionFileName = bs_pathGenerator.bs_versionUpPath(verDir)
    # create new version file name if no version exist.
    if not versionFileName:
        versionFileName = bs_pathGenerator.bs_getCurrentAssetMainFileName()[:-3] + '_v001.ma'
    versionFilePath = verDir + versionFileName
    # get version screenshot.
    imageFilePath = verDir + 'snapshot/' + versionFileName[:-3] + '.jpg'
    bs_screenshot.bs_getScreenShot(imageFilePath)
    # save version File.
    pm.saveAs(versionFilePath)
    # copy main version file and save as main File if fail then save manually.
    try:
        shutil.copy2(versionFilePath, mainFilePath)
    except OSError:
        pm.saveAs(mainFilePath)
    # print message.
    bs_qui.bs_displayMessage('success', 'Asset Publish Successfully...')
    return mainFilePath, versionFilePath
