import os
import json


def bs_getAllAssets(project, assetType):
    """
    @ get asset type and return all asset names.
    Args:
        project: project name for example 'kns'
        assetType (str): asset type like ('chars', 'props', 'sets', 'vehicles')

    Returns:
            all asset names from folder structure.
    """
    # arrange asset type folder structure.
    assetTypeStructure = {'chars': '01_char', 'props': '02_props', 'sets': '03_set', 'vehicles': '04_vehicle', 'SetElement': '03_set/00_setElement'}
    appJson = os.path.dirname(os.path.dirname(__file__)) + '/bs_app/configs/' + project + '/appConfig/appSetting.json'
    # get project root directory path from json.
    with open(appJson) as config_data:
        config = json.load(config_data)
    projectRootPath = config['projectRootPath']
    assetRootPath = projectRootPath + 'kicko_speedo/01_pre/'
    return os.listdir(assetRootPath + assetTypeStructure[assetType])


def bs_assetDirPath(project, assetType, assetName, category):
    """
    @ return asset directory path.
    Args:
        project (str): project name (basically get it from environment variable)
        assetType (str): asset type for example ('char','props' etc)
        assetName (str): asset name
        category (str): asset category like (model, texture, rig etc.)

    Returns:
            asset directory path.
    """
    appJson = os.path.dirname(os.path.dirname(__file__)) + '/bs_app/configs/' + project + '/appConfig/appSetting.json'
    # get project root directory path from json.
    with open(appJson) as config_data:
        config = json.load(config_data)
    projectRootPath = config['projectRootPath']
    assetRootPath = projectRootPath + 'kicko_speedo/01_pre/'
    return assetRootPath + assetType + '/' + assetName + '/' + category


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
