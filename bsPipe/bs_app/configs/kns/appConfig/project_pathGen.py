import os
from pymel import core as pm

# make basic paths.
os.environ['BSW_PROJECT_SHORT'] = 'kns'
os.environ['BSW_PROJECT_NAME'] = 'kicko_speedo'
os.environ['BSW_PROJECT_DIR'] = 'D:/zTempDir'
os.environ['BSW_PROGRAM_DIR'] = 'D:/'
os.environ['BSW_PROJECT_TYPE'] = 'series'


class ProjectNamingInputs(object):
    def __init__(self):
        self.projectShortName = os.environ['BSW_PROJECT_SHORT']
        self.projectName = os.environ['BSW_PROJECT_NAME']
        self.basePath = os.environ['BSW_PROJECT_DIR']
        self.projectType = os.environ['BSW_PROJECT_TYPE']

    @property
    def assetType(self):
        astType = \
            {
                'Input': '00_inputs',
                'Character': '01_char',
                'Prop': '02_props',
                'Set': '03_set',
                'SetElement': '04_setElement',
                'Vehicle': '05_vehicle'
            }
        return astType

    @property
    def assetDept(self):
        astDept = \
            {
                'Design': '01_design',
                'Model': '02_model',
                'Texture': '03_texture',
                'Light': '04_light',
                'Rig': '05_rig'
            }
        return astDept


def bsw_getAllAssetEpisodes(astType):
    """
    @ get all episodes in selected asset type, and if project type is not series then return None.
    Args:
        astType (str): asset types is only ['Character', 'Prop', 'Set', 'SetElement', 'Vehicle'].

    Returns:
            all asset episode numbers (list) if project type is not series then return None.
    """
    # get basic inputs.
    basePath = ProjectNamingInputs().basePath
    projectName = ProjectNamingInputs().projectName
    assetType = ProjectNamingInputs().assetType
    projectType = ProjectNamingInputs().projectType
    if projectType == 'series':
        episodeDir = '{basePath}/{projectName}/01_pre/{assetType}/' \
            .format(basePath=basePath, projectName=projectName, assetType=assetType[astType])
        return [each for each in os.listdir(episodeDir) if os.path.isdir(os.path.join(episodeDir, each))]
    else:
        return None


def bsw_getAllAssetNames(astType, episode=None):
    """
    @ get all asset names of asset types from directory.
    Args:
        astType (str): asset types is only ['Character', 'Prop', 'Set', 'SetElement', 'Vehicle'].
        episode (str): episode number.

    Returns:
            all asset names.
    """
    # get basic inputs.
    basePath = ProjectNamingInputs().basePath
    projectName = ProjectNamingInputs().projectName
    assetType = ProjectNamingInputs().assetType
    projectType = ProjectNamingInputs().projectType
    if projectType == 'series':
        assetDirectory = '{basePath}/{projectName}/01_pre/{assetType}/{episode}/' \
            .format(basePath=basePath, projectName=projectName, assetType=assetType[astType], episode=episode)
    else:
        assetDirectory = '{basePath}/{projectName}/01_pre/{assetType}/' \
            .format(basePath=basePath, projectName=projectName, assetType=assetType[astType])
    # if asset directory is not found then return message.
    if os.path.exists(assetDirectory):
        allAstNames = [each for each in os.listdir(assetDirectory) if os.path.isdir(os.path.join(assetDirectory, each))]
    else:
        allAstNames = ['asset is not found']
    return allAstNames


def bsw_getAssetDeptDirs(astType, astName, episode=None):
    """
    @ get template of passed asset all department directory paths.
    Args:
        astType (str): asset types is only ['Character', 'Prop', 'Set', 'SetElement', 'Vehicle'].
        astName (str): asset name.
        episode (str): episode number.

    Returns:
            selected asset all department directory (dict).
    """
    basePath = ProjectNamingInputs().basePath
    projName = ProjectNamingInputs().projectName
    assetType = ProjectNamingInputs().assetType
    projectType = ProjectNamingInputs().projectType
    allDeptDirs = dict()
    if projectType == 'series':
        baseAssetDir = '{basePath}/{projectName}/01_pre/{assetType}/{episode}/{assetName}/' \
            .format(basePath=basePath, projectName=projName, assetType=assetType[astType],
                    assetName=astName, episode=episode)
    else:
        baseAssetDir = '{basePath}/{projectName}/01_pre/{assetType}/{assetName}/' \
            .format(basePath=basePath, projectName=projName, assetType=assetType[astType], assetName=astName)
    allDeptDirs['Design'] = baseAssetDir + '01_design'
    allDeptDirs['DesignVersion'] = baseAssetDir + '01_design/version/'
    allDeptDirs['Model'] = baseAssetDir + '02_model/'
    allDeptDirs['ModelVersion'] = baseAssetDir + '02_model/version/'
    allDeptDirs['Blendshape'] = baseAssetDir + '02_model/blendshape/'
    allDeptDirs['BlendshapeVersion'] = baseAssetDir + '02_model/blendshape/version/'
    allDeptDirs['Texture'] = baseAssetDir + '03_texture/'
    allDeptDirs['TextureVersion'] = baseAssetDir + '03_texture/version/'
    allDeptDirs['SourceimagesHigh'] = baseAssetDir + '03_texture/sourceimages/high/'
    allDeptDirs['SourceimagesMid'] = baseAssetDir + '03_texture/sourceimages/mid/'
    allDeptDirs['SourceimagesLow'] = baseAssetDir + '03_texture/sourceimages/low/'
    allDeptDirs['Light'] = baseAssetDir + '04_light/'
    allDeptDirs['LightVersion'] = baseAssetDir + '04_light/version/'
    allDeptDirs['Rig'] = baseAssetDir + '05_rig/'
    allDeptDirs['RigVersion'] = baseAssetDir + '05_rig/version/'
    return allDeptDirs


def bsw_createAssetDirectories(astType, astName, episode=None):
    """
    @ create asset directories of all department.
    Args:
        astType (str): asset Type Character, Prop, Set, SetElement, Vehicle.
        astName (str): assetName.
        episode (str): episode number.

    Returns:
            bool.
    """
    # get all asset department directory template.
    projectType = ProjectNamingInputs().projectType
    if projectType == 'series':
        assetDeptDir = bsw_getAssetDeptDirs(astType, astName, episode=episode)
    else:
        assetDeptDir = bsw_getAssetDeptDirs(astType, astName)
    for each in assetDeptDir.keys():
        if not os.path.exists(assetDeptDir[each]):
            os.makedirs(assetDeptDir[each])
    return True


def bsw_getAssetFileAndVersions(astType, astDept, astName, episode=None):
    """
    @ get main file and version files, and create directory if not exist.
    Args:
        astType (str): asset Type Character, Prop, Set, SetElement, Vehicle.
        astDept (str): Design, Model, Texture, Rig, Light or etc.
        astName (str): assetName.
        episode (str): episode number.

    Returns:
            mainFiles and version file paths (list, list).
    """
    projectShortName = ProjectNamingInputs().projectShortName
    projectType = ProjectNamingInputs().projectType
    if projectType == 'series':
        assetDeptDir = bsw_getAssetDeptDirs(astType, astName, episode=episode)
    else:
        assetDeptDir = bsw_getAssetDeptDirs(astType, astName)
    mainAssetFile = list()
    versionFiles = list()
    # get main Files.
    # make directory if not exist.
    if projectType == 'series':
        bsw_createAssetDirectories(astType, astName, episode)
    else:
        bsw_createAssetDirectories(astType, astName)
    # add all main files in list main file is need only one but this is wrong.
    for each in os.listdir(assetDeptDir[astDept]):
        if each.startswith(projectShortName + '_') and each.endswith('.ma'):
            mainAssetFile.append(os.path.join(assetDeptDir[astDept], each))

    # get version files, returns in to list.
    # add all version files in list.
    for each in os.listdir(assetDeptDir[astDept + 'Version']):
        if each.startswith(projectShortName + '_') and each.endswith('.ma') and each[-8:-6] == '_v':
            versionFiles.append(os.path.join(assetDeptDir[astDept + 'Version'], each))
    return mainAssetFile, versionFiles


def bsw_getValidDeptAssetNames(astType, astDept, episode=None):
    """
    @ return all department wise asset return name if file is exist.
    Args:
        astType (str): asset type for example('Character', 'Prop', 'Set', 'Vehicle').
        astDept (str): asset department like ('Design', 'Model', 'Texture', 'Rig', 'Light' or etc.)
        episode (str): episode number.

    Returns:
            department wise asset names list.
    """
    # get all asset names.
    projectShortName = ProjectNamingInputs().projectShortName
    projectType = ProjectNamingInputs().projectType
    if projectType == 'series':
        assetNames = bsw_getAllAssetNames(astType, episode=episode)
    else:
        assetNames = bsw_getAllAssetNames(astType)
    validDeptAsset = list()
    # go to each asset directory and check there is any file with our project naming structure is exist or not.
    for eachName in assetNames:
        if projectType == 'series':
            assetDeptDir = bsw_getAssetDeptDirs(astType, eachName, episode=episode)[astDept]
        else:
            assetDeptDir = bsw_getAssetDeptDirs(astType, eachName)[astDept]
        # return if directory is not found.
        if not os.path.exists(assetDeptDir):
            continue
        # get valid file if naming is matched with our naming structure.
        for each in os.listdir(assetDeptDir):
            if each.startswith(projectShortName + '_') and each.endswith('.ma'):
                validDeptAsset.append(eachName)
    return list(set(validDeptAsset))


def bsw_versionUpPath(versionDir):
    """
    @ get version directory the query all maya version files and return new file name.
    Args:
        versionDir (str): version directory path.

    Returns:
            newVersionFile Name.
    """
    projectShortName = ProjectNamingInputs().projectShortName
    if not os.path.exists(versionDir):
        return False
    # get all files from version directory.
    if os.listdir(versionDir):
        filteredVersionFiles = list()
        # check and add every files from version directory if naming is correct in filteredVersionFiles list.
        for each in os.listdir(versionDir):
            if each.startswith(projectShortName + '_') and each.endswith('.ma') and each[-8:-6] == '_v':
                filteredVersionFiles.append(each)
        # version up.
        if filteredVersionFiles:
            # split only version numbers from each filtered file, and add in allNumbers list.
            allNumbers = list()
            for num in filteredVersionFiles:
                fileNumber = num[-6:-3]
                allNumbers.append(int(fileNumber))
            upNumber = str(max(allNumbers) + 1).zfill(3)
            upVersionFileName = filteredVersionFiles[0]
            return upVersionFileName[:-6] + upNumber + '.ma'
        else:
            return False
    else:
        return False


def bsw_getAssetDetails(rootGrpName=None):
    """
    @ get asset details from root group entries which created in asset generation time.
    Args:
        rootGrpName: root group name, three group is currently [Texture_Group,Group,geo].
    Returns:
            asset details (assetDepartment, assetType, assetName, assetUID, episode).
    """
    if not rootGrpName:
        if pm.objExists('Texture_Group'):
            rootGrpName = 'Texture_Group'
        elif pm.objExists('rig_grp'):
            rootGrpName = 'rig_grp'
        elif pm.objExists('geo'):
            rootGrpName = 'geo'
        else:
            rootGrpName = 'None'
    astDept = {'Texture_Group': 'Texture', 'rig_grp': 'Rig', 'geo': 'Model', 'None': 'None'}
    if rootGrpName == 'None':
        return 'Not Exist', 'Not Exist', 'Not Exist', 'Not Exist', 'NotExist'
    rootGrp = pm.PyNode(rootGrpName)
    # get episode if environment is series, else return "Not Exist" string.
    episode = 'NotExist'
    if os.environ['BSW_PROJECT_TYPE'] == 'series':
        episode = rootGrp.assetEpisode.get()
    return astDept[rootGrpName], rootGrp.assetType.get(), rootGrp.assetName.get(), rootGrp.assetUID.get(), episode


def bsw_getCurrentAssetMainFileName():
    """
    @ get main file name of current scene.
    Returns:
            main file name (str).
    """
    projectShortName = ProjectNamingInputs().projectShortName
    # get asset UID from the kns_getAssetDetails function (second last return is assetUID).
    assetUID = bsw_getAssetDetails()[-2]
    if os.environ['BSW_PROJECT_TYPE'] == 'series':
        return projectShortName + '_' + assetUID.split('_')[1] + '_' + assetUID.split('_')[2] + '_' + \
               assetUID.split('_')[-1] + '_' + assetUID.split('_')[-2] + '.ma'
    else:
        return projectShortName + '_' + assetUID.split('_')[1] + '_' + assetUID.split('_')[2] + '_' + \
               assetUID.split('_')[-1] + '.ma'


def bsw_getOnlyFinalFileOfDept(astType, astDept, astName, episode=None):
    """
    @ get only final file of required department.
    Args:
        astType (str): asset Type Character, Prop, Set, Vehicle.
        astDept (str): Design, Model, Texture, Rig, Light or etc.
        astName (str): assetName.
        episode (str): episode number.

    Returns:
            filePath if exist else return False.
    """
    projectShortName = ProjectNamingInputs().projectShortName
    astTypShortCode = {'Character': 'ch', 'Prop': 'pr', 'Set': 'bg', 'Vehicle': 'vh', 'SetElement': 'se'}
    astDeptShortCode = {'Model': 'mod', 'Rig': 'rig', 'Texture': 'tex', 'Light': 'lit'}
    projectType = ProjectNamingInputs().projectType
    if projectType == 'series':
        mainFiles, versionFiles = bsw_getAssetFileAndVersions(astType, astDept, astName, episode)
    else:
        mainFiles, versionFiles = bsw_getAssetFileAndVersions(astType, astDept, astName)
    for each in mainFiles:
        fileDir = os.path.dirname(each)
        splitFile = each.split('/')[-1]
        startName = '{0}_{1}_{2}'.format(projectShortName, astTypShortCode[astType], astName)
        endName = '_{0}.ma'.format(astDeptShortCode[astDept])
        if splitFile.startswith(startName) and splitFile.endswith(endName):
            return fileDir + '/' + splitFile
    else:
        return False


def bsw_getAssetPathFromFileName(fileName):
    """
    @ get asset dir from file name.
    Args:
        fileName (str): fileName

    Returns:
            filePath(str).
    """
    projectType = ProjectNamingInputs().projectType
    assetType = {'ch': 'Character', 'pr': 'Prop', 'bg': 'Set', 'vh': 'Vehicle', 'se': 'SetElement'}
    assetDept = {'mod': 'Model', 'tex': 'Texture', 'rig': 'Rig', 'lit': 'Light'}
    astType = fileName.split('_')[1]
    astName = fileName.split('_')[2]
    versionFile = False
    if len(fileName.split('_')) == 6:
        versionFile = True
    if projectType == 'series':
        episode = fileName.split('_')[3]
        # use 3 digit after splitting because main file dept has no "_" after dept.
        astDept = fileName.split('_')[4][:3]
        if versionFile:
            return bsw_getAssetDeptDirs(assetType[astType], astName, episode=episode)[assetDept[astDept] + 'Version']
        return bsw_getAssetDeptDirs(assetType[astType], astName, episode=episode)[assetDept[astDept]]
    else:
        astDept = fileName.split('_')[3][:3]
        if versionFile:
            return bsw_getAssetDeptDirs(assetType[astType], astName)[assetDept[astDept] + 'Version']
        return bsw_getAssetDeptDirs(assetType[astType], astName)[assetDept[astDept]]
