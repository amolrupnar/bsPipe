import os
import json

from bsPipe.bs_core import bs_pathGenerator

reload(bs_pathGenerator)


def bs_getAllAssets(astType, episode=None):
    """
    @ get asset type and return all asset names.
    Args:
        astType (str): asset types is only ['Character', 'Prop', 'Set', 'SetElement', 'Vehicle'].
        episode (str): episode number.

    Returns:
            all asset names from folder structure.
    """
    if bs_pathGenerator.bs_getEnv()['projectType'] == 'series':
        return bs_pathGenerator.bs_getAllAssetNames(astType, episode=episode)
    return bs_pathGenerator.bs_getAllAssetNames(astType)


def bs_assetDirPath(astType, astName, astDept):
    """
    @ return asset directory path.
    Args:
        astType (str): asset types is only ['Character', 'Prop', 'Set', 'SetElement', 'Vehicle'].
        astName (str): asset name
        astDept (str): asset category like (model, texture, rig etc.)

    Returns:
            asset directory path.
    """
    appJson = os.path.dirname(os.path.dirname(__file__)) + '/bs_app/configs/' + project + '/appConfig/appSetting.json'
    # get project root directory path from json.
    with open(appJson) as config_data:
        config = json.load(config_data)
    projectRootPath = config['projectRootPath']
    assetRootPath = projectRootPath + 'kicko_speedo/01_pre/'
    return assetRootPath + astType + '/' + astName + '/' + astDept


def bs_assetFileAndVersions(project, assetType, assetName, category):
    """
    @ return asset files and version file names
    @ parameters are passed for geting asset directory path.
    Args:

    Returns:
            mainFiles and version files.
    """
    fullPath = bs_assetDirPath(project, assetType, assetName, category)
    mainFiles = list()
    versionFiles = list()
    for each in os.listdir(fullPath):
        if each.endswith('.ma'):
            mainFiles.append(each)
    for each in os.listdir(fullPath + '/version'):
        if each.endswith('.ma'):
            versionFiles.append(each)
    return mainFiles, versionFiles
