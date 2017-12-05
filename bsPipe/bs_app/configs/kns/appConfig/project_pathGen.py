import os
from pymel import core as pm

# make basic paths.
os.environ['BSW_PROJECT_SHORT'] = 'kns'
os.environ['BSW_PROJECT_NAME'] = 'kicko_speedo'
os.environ['BSW_PROJECT_DIR'] = 'D:/zTempDir'
os.environ['BSW_PROGRAM_DIR'] = 'D:/'
os.environ['BSW_PROJECT_TYPE'] = 'series'

projectShortName = os.environ['BSW_PROJECT_SHORT']
projectName = os.environ['BSW_PROJECT_NAME']
basePath = os.environ['BSW_PROJECT_DIR']


class TestClass(object):
    def __init__(self, *args):
        self.assetType()

    def __call__(self, *args, **kwargs):
        print args
        self.assetType()

    # def __enter__(self):
    #     self.assetType()

    # @property
    def assetType(self):
        assetTyper = \
            {
                'Input': '00_inputs',
                'Character': '01_char',
                'Prop': '02_props',
                'Set': '03_set',
                'SetElement': '04_setElement',
                'Vehicle': '05_vehicle'
            }
        return assetTyper


a = TestClass('amol', 'rupnar')
print a
# print a.assetType

assetType = \
    {
        'Input': '00_inputs',
        'Character': '01_char',
        'Prop': '02_props',
        'Set': '03_set',
        'SetElement': '04_setElement',
        'Vehicle': '05_vehicle'
    }
assetDept = \
    {
        'Design': '01_design',
        'Model': '02_model',
        'Texture': '03_texture',
        'Light': '04_light',
        'Rig': '05_rig'
    }


def bsw_getAllAssetNames(astType):
    """
    @ get all asset names of asset types from directory.
    Args:
        astType (str): asset types is only ['Character', 'Prop', 'Set', 'SetElement', 'Vehicle'].

    Returns:
            all asset names.
    """
    assetDirectory = '{basePath}/{projectName}/01_pre/{assetType}/'.format(basePath=basePath,
                                                                           projectName=projectName,
                                                                           assetType=assetType[astType])
    allAssetNames = [each for each in os.listdir(assetDirectory) if os.path.isdir(os.path.join(assetDirectory, each))]
    return allAssetNames


def bsw_getAssetDeptDirs(astType, astName):
    """
    @ get template of passed asset all department directory paths.
    Args:
        astType (str): asset types is only ['Character', 'Prop', 'Set', 'SetElement', 'Vehicle'].
        astName (str): asset name.

    Returns:
            selected asset all department directory (dict).
    """
    allDeptDirs = dict()
    baseAssetDir = '{basePath}/{projectName}/01_pre/{assetType}/{assetName}/'.format(basePath=basePath,
                                                                                     projectName=projectName,
                                                                                     assetType=assetType[astType],
                                                                                     assetName=astName)
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


def bsw_createAssetDirectories(astType, astName):
    """
    @ create asset directories of all department.
    Args:
        astType (str): asset Type Character, Prop, Set, SetElement, Vehicle.
        astName (str): assetName.

    Returns:
            bool.
    """
    # get all asset department directory template.
    assetDeptDir = bsw_getAssetDeptDirs(astType, astName)
    for each in assetDeptDir.keys():
        if not os.path.exists(assetDeptDir[each]):
            os.makedirs(assetDeptDir[each])
    return True


def bsw_getAssetFileAndVersions(astType, astDept, astName):
    """
    @ get main file and version files, and create directory if not exist.
    Args:
        astType (str): asset Type Character, Prop, Set, Vehicle.
        astDept (str): Design, Model, Texture, Rig, Light or etc.
        astName (str): assetName.

    Returns:
            mainFiles and version file paths (list, list).
    """
    assetDeptDir = bsw_getAssetDeptDirs(astType, astName)
    mainAssetFile = list()
    versionFiles = list()
    # get main Files.
    # make directory if not exist.
    bsw_createAssetDirectories(astType, astName)
    # add all main files in list main file is need only one but this is wrong.
    for each in os.listdir(assetDeptDir[astDept]):
        if each.startswith(projectShortName + '_') and each.endswith('.ma'):
            mainAssetFile.append(os.path.join(assetDeptDir[astDept], each))

    # get version files, returns in to list.
    # add all version files in list.
    for each in os.listdir(assetDeptDir[astDept + 'Version']):
        if each.startswith(projectShortName + '_') and each.endswith('.ma') and each[-8:-6] == '_v':
            versionFiles.append(os.path.join(assetDeptDir[astDept], each))
    return mainAssetFile, versionFiles


def bsw_getValidDeptAssetNames(astType, astDept):
    """
    @ return all department wise asset return name if file is exist.
    Args:
        astType (str): asset type for example('Character', 'Prop', 'Set', 'Vehicle').
        astDept (str): asset department like ('Design', 'Model', 'Texture', 'Rig', 'Light' or etc.)

    Returns:
            department wise asset names list.
    """
    # get all asset names.
    assetNames = bsw_getAllAssetNames(astType)
    validDeptAsset = list()
    # go to each asset directory and check there is any file with our project naming structure is exist or not.
    for eachName in assetNames:
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
    # get asset UID from the kns_getAssetDetails function (second last return is assetUID).
    assetUID = bsw_getAssetDetails()[-2]
    if os.environ['BSW_PROJECT_TYPE'] == 'series':
        return projectShortName + '_' + assetUID.split('_')[1] + '_' + assetUID.split('_')[2] + '_' + \
               assetUID.split('_')[-1] + '_' + assetUID.split('_')[-2] + '.ma'
    else:
        return projectShortName + '_' + assetUID.split('_')[1] + '_' + assetUID.split('_')[2] + '_' + \
               assetUID.split('_')[-1] + '.ma'


def bsw_getOnlyFinalFileOfDept(astType, astDept, astName):
    """
    @ get only final file of required department.
    Args:
        astType (str): asset Type Character, Prop, Set, Vehicle.
        astDept (str): Design, Model, Texture, Rig, Light or etc.
        astName (str): assetName.

    Returns:

    """
    astTypShortCode = {'Character': 'ch', 'Prop': 'pr', 'Set': 'bg', 'Vehicle': 'vh', 'SetElement': 'se'}
    astDeptShortCode = {'Model': 'mod', 'Rig': 'rig', 'Texture': 'tex', 'Light': 'lit'}
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


# if __name__ == '__main__':
#     a = bsw_getOnlyFinalFileOfDept('Character', 'Model', 'dodo')
#     print a
