import os
# import sys
# from pymel import core as pm

import project_pathGen

reload(project_pathGen)


# from bsPipe.bs_core import bs_os
# from bsPipe.bs_ui import bs_qui
#
# reload(bs_os)
# reload(bs_qui)


def bs_getEnv():
    """
    @ get our own selected environ details.
    Returns:
            env details.
    """
    bsw_getEnv = dict()
    # get environments.
    bsw_getEnv['projectShort'] = os.environ['BSW_PROJECT_SHORT']
    bsw_getEnv['projectName'] = os.environ['BSW_PROJECT_NAME']
    bsw_getEnv['projectDir'] = os.environ['BSW_PROJECT_DIR']
    bsw_getEnv['programDir'] = os.environ['BSW_PROGRAM_DIR']
    bsw_getEnv['projectType'] = os.environ['BSW_PROJECT_TYPE']
    return bsw_getEnv


def bs_createAssetDirectories(astType, astName):
    """
    @ create asset directories of all department.
    Args:
        astType (str): asset Type Character, Prop, Set, SetElement, Vehicle.
        astName (str): assetName.

    Returns:
            bool.
    """
    return project_pathGen.bsw_createAssetDirectories(astType, astName)


def bs_getAllAssetNames(astType):
    """
    @ just replace function with project path generator.
    @ get all asset names of asset types from directory.
    Args:
        astType (str): asset types is only ['Character', 'Prop', 'Set', 'SetElement', 'Vehicle'].

    Returns:
            all asset names.
    """
    return project_pathGen.bsw_getAllAssetNames(astType)


def bs_getAssetDeptDirs(astType, astName):
    """
    @ just replace function with project path generator.
    @ get passed asset all department directories.
    Args:
        astType (str): asset types is only ['Character', 'Prop', 'Set', 'SetElement', 'Vehicle'].
        astName (str): asset name.

    Returns:
            selected asset all department directory (dict).
    """
    return project_pathGen.bsw_getAssetDeptDirs(astType, astName)


def bs_getAssetFileAndVersions(astType, astDept, astName):
    """
    @ getting input from passed arguments and return a two dictionaries.
    @ each dictionary having keys(file name used as a key).
    @ also value is a dictionary.
    @ value dictionary keys are detail types like ('path','size','owner',etc.).
    Args:
        astType (str): asset Type Character, Prop, Set, Vehicle.
        astDept (str): Design, Model, Texture, Rig, Light or etc.
        astName (str): assetName.

    Returns:
            mainFiles and version files (Both return type is dict.)
    """
    return project_pathGen.bsw_getAssetFileAndVersions(astType, astDept, astName)


def bs_getValidDeptAssetNames(astType, astDept):
    """
    @ return all department wise asset return name if file is exist.
    Args:
        astType (str): asset type for example('Character', 'Prop', 'Set', 'Vehicle').
        astDept (str): asset department like ('Design', 'Model', 'Texture', 'Rig', 'Light' or etc.)

    Returns:
            department wise asset names list.
    """
    return project_pathGen.bsw_getValidDeptAssetNames(astType, astDept)


def bs_versionUpPath(versionDir):
    """
    @ get version directory the query all maya version files and retun new file name.
    Args:
        versionDir (str): version directory path.

    Returns:
            newVersionFile Name.
    """
    return project_pathGen.bsw_versionUpPath(versionDir)


def bs_getAssetDetails(rootGrpName=None):
    """
    @ get asset details from root group entries which created in asset generation time.
    Args:
        rootGrpName: root group name, three group is currently [Texture_Group,Group,geo].
    Returns:
            asset details.
    """
    if rootGrpName:
        return project_pathGen.bsw_getAssetDetails(rootGrpName=rootGrpName)
    else:
        return project_pathGen.bsw_getAssetDetails()


def bs_getCurrentAssetMainFileName():
    """
    @ get main file name of current scene.
    Returns:
            main file name (str).
    """
    return project_pathGen.bsw_getCurrentAssetMainFileName()


def bs_getOnlyFinalFileOfDept(astType, astDept, astName):
    """
    @ get only final file of required department.
    Args:
        astType (str): asset Type Character, Prop, Set, Vehicle.
        astDept (str): Design, Model, Texture, Rig, Light or etc.
        astName (str): assetName.

    Returns:

    """
    return project_pathGen.bsw_getOnlyFinalFileOfDept(astType, astDept, astName)

# def bs_animFilePath(epi, seq, shot):
#     """
#     @ generate animation path with it stages by using following arguments.
#     Args:
#         epi (str): episode Number like ("ep001")
#         seq (str): sequence Number like ("sq001")
#         shot (str): shot Number like ("sh001")
#
#     Returns:
#             all animation path. (dict).
#     """
#     projectName = bs_getEnvDetails()['projectName']
#     # check episode, sequence and shot is sorting correct.
#     if not epi.startswith('ep'):
#         return False
#     if not seq.startswith('sq'):
#         return False
#     if not shot.startswith('sh'):
#         return False
#     # get environment details.
#     prodPath = bs_getEnvDetails()['rootPath'] + bs_getEnvDetails()['projectFolder'] + '/02_prod/'
#     animStage = {'lay': '01_layout/', 'cam': '02_camera/', 'ani': '03_animation/', 'cah': '04_cache/',
#                  'shf': '05_shotFinalize/', 'acy': '06_animationCycles/'}
#     fileName = projectName.lower() + '_' + epi + '_' + seq + '_' + shot
#     lay = prodPath + animStage['lay'] + epi + '/' + seq + '/' + shot + '/' + fileName + '_lay.ma'
#     cam = prodPath + animStage['cam'] + epi + '/' + seq + '/' + shot + '/' + fileName + '_cam.ma'
#     ani = prodPath + animStage['ani'] + epi + '/' + seq + '/' + shot + '/' + fileName + '_ani.ma'
#     cah = prodPath + animStage['cah'] + epi + '/' + seq + '/' + shot + '/' + fileName + '_cah.ma'
#     shf = prodPath + animStage['shf'] + epi + '/' + seq + '/' + shot + '/' + fileName + '_shf.ma'
#     return {'lay': lay, 'cam': cam, 'ani': ani, 'cah': cah, 'shf': shf}


# def bs_getVersionDirAndFiles(filePath):
#     """
#     @ get full file path and return file version directory path.
#     Args:
#         filePath (str): file path.
#
#     Returns:
#             version directory path (str).
#     """
#     projectName = bs_getEnvDetails()['projectName']
#     dirPath = str()
#     for each in filePath.split('/')[:-1]:
#         dirPath += each + '/'
#     versionDir = dirPath + 'versions/'
#     versionFilePaths = list()
#     versionFileNames = list()
#     print versionDir
#     for each in os.listdir(versionDir):
#         if each.startswith(projectName.lower() + '_') and each[-8:-6] == '_v' and each.endswith('.ma'):
#             versionFileNames.append(each)
#             versionFilePaths.append(versionDir + each)
#     return {'dir': versionDir, 'fileNames': versionFileNames, 'filePaths': versionFilePaths}


# def bs_getConfigPaths():
#     """
#     @ return project config path.
#     Returns:
#             None.
#     """
#     return os.environ['BSW_PROGRAM_SERVER'] + '/Pipeline/bsPipe/bsPipe/bs_app/configs/' + os.environ[
#         'BSW_PROJECT'] + '/'


# def bs_shotDetailsCheckAndReturn():
#     """
#     @ get shot details from current scene.
#     Returns:
#             episode, sequence, shot, stage.
#     """
#     if not pm.objExists('shot_grp'):
#         bs_qui.bs_displayMessage('error', 'Valid shot is not found')
#         return False
#     shotGroup = pm.PyNode('shot_grp')
#     epi = shotGroup.bsw_episode.get()
#     seq = shotGroup.bsw_sequence.get()
#     shot = shotGroup.bsw_shot.get()
#     stage = shotGroup.bsw_stage.get()
#
#     # check episode name.
#     if not epi.startswith('ep'):
#         bs_qui.bs_displayMessage('error', 'enter ep at the start.')
#         return False
#     # check sequence name.
#     if not seq.startswith('sq'):
#         bs_qui.bs_displayMessage('error', 'enter sq at the start.')
#         return False
#     # check shot name.
#     if not shot.startswith('sh'):
#         bs_qui.bs_displayMessage('error', 'enter sh at the start.')
#         return False
#     # return animation stage.
#     if not (stage == 'lay' or stage == 'ani'):
#         bs_qui.bs_displayMessage('error', 'animation stage is not valid.')
#         return False
#     return epi, seq, shot, stage


# def bs_saveAnimFile(shotStage=None):
#     """
#     @ save animation file according to its file stage.
#     Args:
#         shotStage (str): shot stage like ('lay', 'ani', 'cam').
#
#     Returns:
#             None.
#     """
#     bsDrive = bs_getEnvDetails()['rootPath']
#     projectFolder = bs_getEnvDetails()['projectFolder']
#     projectName = bs_getEnvDetails()['projectName'].lower()
#     animStage = {'lay': '01_layout/', 'cam': '02_camera/', 'ani': '03_animation/', 'cac': '04_cache/',
#                  'shf': '05_shotFinalize/'}
#     epi, seq, shot, stage = bs_shotDetailsCheckAndReturn()
#     # add condition if something is wrong in episode sequence or shot.
#     if not (epi and seq and shot):
#         return False
#     # if shot stage is passed from parameter then reassign to stage variable.
#     if shotStage:
#         stage = shotStage
#     basePath = bsDrive + projectFolder + '/02_prod/' + animStage[stage] + epi + '/' + seq + '/' + shot + '/'
#     shotName = '{0}_{1}_{2}_{3}_{4}.ma'.format(projectName, epi, seq, shot, stage)
#     versionDir = basePath + 'versions/'
#     # make directory is not exist.
#     bs_makeAnimDirStructure(epi, seq, shot)
#     # save as file version.
#     versionFile = bs_versionUpPath(versionDir)
#     if not versionFile:
#         versionFile = shotName[:-3] + '_v001.ma'
#     # change entry.
#     shotGroup = pm.PyNode('shot_grp')
#     shotGroup.bsw_stage.unlock()
#     shotGroup.bsw_stage.set(shotStage)
#     shotGroup.bsw_stage.lock()
#     pm.saveAs(versionDir + versionFile)
#     # save as a main final file.
#     pm.saveAs(basePath + shotName)
#     bs_qui.bs_displayMessage('success', '{0} file and its next version successfully saved.'.format(stage))


# def bs_makeAnimDirStructure(epi, seq, shot):
#     """
#     @ create complete animation folder structure, using episode sequence and shot.
#     Args:
#         epi (str): episode, input like this ('ep001')
#         seq (str): sequence, input like this ('sq001')
#         shot (str): shot, input like this ('sh001')
#
#     Returns:
#             None.
#     """
#     bsDrive = bs_getEnvDetails()['rootPath']
#     projectFolder = bs_getEnvDetails()['projectFolder']
#     animStage = {'lay': '01_layout/', 'cam': '02_camera/', 'ani': '03_animation/', 'cac': '04_cache/',
#                  'shf': '05_shotFinalize/'}
#     newDirs = list()
#     existDirs = list()
#     for each in animStage.keys():
#         basePath = bsDrive + projectFolder + '/02_prod/' + animStage[each] + epi + '/' + seq + '/' + shot + '/'
#         versionPath = basePath + 'versions/'
#         if not os.path.exists(versionPath):
#             os.makedirs(versionPath)
#             newDirs.append(versionPath)
#         else:
#             existDirs.append(versionPath)
#     if newDirs:
#         bs_qui.bs_displayMessage('success', '{0} directory newly created'.format(str(len(newDirs))))
#     else:
#         bs_qui.bs_displayMessage('success', 'all directories are already exist.')


# def bs_getAllEpisodeList():
#     """
#     @ get all valid episodes from layout directory.
#     Returns:
#             validEpisodes (list).
#     """
#     # get basic directory.
#     rootPath = bs_getEnvDetails()['rootPath']
#     projectPath = bs_getEnvDetails()['projectFolder']
#     layBasePath = rootPath + projectPath + '/02_prod/01_layout/'
#     validEpisodes = list()
#     for each in os.listdir(layBasePath):
#         if each.startswith('ep') and os.path.isdir(layBasePath + each):
#             validEpisodes.append(each)
#     return validEpisodes


# def bs_getAllSequenceList(episode):
#     """
#     @ get all valid sequence from layout directory.
#     Args:
#         episode (str): episode name.
#
#     Returns:
#             validSequence (list).
#     """
#     # get basic directory.
#     rootPath = bs_getEnvDetails()['rootPath']
#     projectPath = bs_getEnvDetails()['projectFolder']
#     layBasePath = rootPath + projectPath + '/02_prod/01_layout/' + episode + '/'
#     validSeq = list()
#     for each in os.listdir(layBasePath):
#         if each.startswith('sq') and os.path.isdir(layBasePath + each):
#             validSeq.append(each)
#     return validSeq


# def bs_getAllShotList(episode, sequence):
#     """
#     @ get all valid shot names from layout directory.
#     Args:
#         episode (str): episode name.
#         sequence (str): sequence name.
#
#     Returns:
#             valid shots (list).
#     """
#     # get basic directory.
#     rootPath = bs_getEnvDetails()['rootPath']
#     projectPath = bs_getEnvDetails()['projectFolder']
#     layBasePath = rootPath + projectPath + '/02_prod/01_layout/' + episode + '/' + sequence + '/'
#     validShot = list()
#     for each in os.listdir(layBasePath):
#         if each.startswith('sh') and os.path.isdir(layBasePath + each):
#             validShot.append(each)
#     return validShot


# def bs_getShotFiles(episode, sequence, shot):
#     """
#     @ get valid shot files and its version.
#     Args:
#         episode (str):
#         sequence (str):
#         shot (str):
#         stage (str):
#
#     Returns:
#             dict.
#     """
#     layoutDict = dict()
#     animDict = dict()
#     shotDict = {'layout': layoutDict, 'animation': animDict}
#     # get basic directory.
#     rootPath = bs_getEnvDetails()['rootPath']
#     projectPath = bs_getEnvDetails()['projectFolder']
#     projectName = bs_getEnvDetails()['projectName']
#     # ------------------------------------------------------------
#     # layout details fetch.
#     # ------------------------------------------------------------
#     layoutMainFile = None
#     layoutPlayblastFile = None
#     layoutVersionFiles = list()
#     # list files,
#     layBasePath = rootPath + projectPath + '/02_prod/01_layout/' + episode + '/' + sequence + '/' + shot + '/'
#     if os.listdir(layBasePath):
#         allMainFiles = os.listdir(layBasePath)
#         for each in allMainFiles:
#             if each == projectName.lower() + '_' + episode + '_' + sequence + '_' + shot + '_lay.ma':
#                 layoutMainFile = layBasePath + each
#             elif each == projectName.lower() + '_' + episode + '_' + sequence + '_' + shot + '_lay.avi':
#                 layoutPlayblastFile = layBasePath + each
#         # get version files.
#         if os.listdir(layBasePath + 'versions/'):
#             allVersionFiles = os.listdir(layBasePath + 'versions/')
#             for each in allVersionFiles:
#                 if each.startswith(projectName.lower() + '_' + episode + '_' + sequence + '_' + shot + '_lay_v'):
#                     layoutVersionFiles.append(layBasePath + 'versions/' + each)
#     layoutDict['mainFile'] = layoutMainFile
#     layoutDict['playblast'] = layoutPlayblastFile
#     layoutDict['versions'] = layoutVersionFiles
#     # ------------------------------------------------------------
#     # animation details fetch.
#     # ------------------------------------------------------------
#     animMainFile = None
#     animPlayblastFile = None
#     animVersionFiles = list()
#     # list files,
#     animBasePath = rootPath + projectPath + '/02_prod/03_animation/' + episode + '/' + sequence + '/' + shot + '/'
#     if os.listdir(animBasePath):
#         allMainFiles = os.listdir(animBasePath)
#         for each in allMainFiles:
#             if each == projectName.lower() + '_' + episode + '_' + sequence + '_' + shot + '_ani.ma':
#                 animMainFile = animBasePath + each
#             elif each == projectName.lower() + '_' + episode + '_' + sequence + '_' + shot + '_ani.avi':
#                 animPlayblastFile = animBasePath + each
#         # get version files.
#         if os.listdir(animBasePath + 'versions/'):
#             allVersionFiles = os.listdir(animBasePath + 'versions/')
#             for each in allVersionFiles:
#                 if each.startswith(projectName.lower() + '_' + episode + '_' + sequence + '_' + shot + '_ani_v'):
#                     animVersionFiles.append(animBasePath + 'versions/' + each)
#     animDict['mainFile'] = animMainFile
#     animDict['playblast'] = animPlayblastFile
#     animDict['versions'] = animVersionFiles
#     # ------------------------------------------------------------
#     return shotDict
