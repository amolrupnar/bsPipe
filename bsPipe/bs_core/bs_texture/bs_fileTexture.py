import pymel.core as pm
from bsPipe.bs_core import bs_pathGenerator
from bsPipe.bs_ui import bs_qui

reload(bs_pathGenerator)
reload(bs_qui)


def bs_getAllFileTexturePathIfValid():
    """
    @ query all file texture path and,
    @ return if all are coming from same valid path.
    Returns:
            sourceimages directory (str).
    """
    # get env details and sourceimage directory.
    envRoot = bs_pathGenerator.bs_getEnvDetails()['rootPath']
    assetDept, assetType, assetName, uid = bs_pathGenerator.bs_getAssetDetails()
    sourceImageDir = bs_pathGenerator.bs_getAssetDir(astType=assetType, astDept=assetDept, astName=assetName)[
                         'dept'] + 'sourceimages/'

    allFileTextures = pm.ls(type='file')
    validPath = list()
    invalidPath = list()
    for each in allFileTextures:
        ftn = each.ftn.get()
        filtSourceImageDir = sourceImageDir.replace(envRoot, '')
        if ftn.find(filtSourceImageDir) != -1:
            validPath.append(each)
        else:
            invalidPath.append(each)
    if not invalidPath:
        return sourceImageDir
    bs_qui.bs_displayMessage('error', 'all path not from same path..')
    return False


def bs_checkAllFileTexturePathIsComingFromEnv():
    """
    @ check all file texture path is coming from environment.
    @ run this function if all path are same.
    Returns:
            bool.
    """
    # get env details and sourceimage directory.
    envRoot = bs_pathGenerator.bs_getEnvDetails()['rootPath']
    assetDept, assetType, assetName, uid = bs_pathGenerator.bs_getAssetDetails()
    sourceImageDir = bs_pathGenerator.bs_getAssetDir(astType=assetType, astDept=assetDept, astName=assetName)[
                         'dept'] + 'sourceimages/'
    sourceImageEnvDir = None
    notEnvPath = list()
    allFileTextures = pm.ls(type='file')
    for each in allFileTextures:
        ftn = each.ftn.get()
        if ftn.find('$') != -1:
            sourceImageEnvDir = '$BSW_PROD_SERVER/' + sourceImageDir.replace(envRoot, '')
    if sourceImageEnvDir:
        for each in allFileTextures:
            ftn = each.ftn.get()
            filtSourceImageDir = sourceImageEnvDir
            if not ftn.find(filtSourceImageDir) != -1:
                notEnvPath.append(each)
    if notEnvPath:
        return False
    return sourceImageEnvDir


def bs_convertAllFileTexturePathInEnvVariable():
    """
    @ convert all file texture path in environment variable.
    @ it is run if all path is valid.
    Returns:
            None.
    """
    if bs_getAllFileTexturePathIfValid():
        allFileTextures = pm.ls(type='file')
        for each in allFileTextures:
            ftn = each.ftn.get()
            if not ftn.startswith('$'):
                newPath = '$BSW_PROD_SERVER/'
                for x in ftn.split('/')[1:-2]:
                    newPath += x + '/'
                splitPath = ''
                for x in ftn.split('/')[1:-2]:
                    splitPath += x + '/'
                finalPath = newPath + ftn.split(splitPath)[-1]
                each.ftn.set(finalPath)
        bs_qui.bs_displayMessage('success', 'all paths converted success..')
    else:
        bs_qui.bs_displayMessage('error', 'all file texture root directory is not same....')
