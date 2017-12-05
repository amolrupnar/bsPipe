import pymel.core as pm
import os

from bsPipe.bs_ui import bs_qui
from bsPipe.bs_core import bs_mayaFile
from bsPipe.bs_core import bs_pathGenerator, bs_reference

reload(bs_qui)
reload(bs_mayaFile)
reload(bs_pathGenerator)
reload(bs_reference)


def bs_shotBuild(epi, seq, shot, startTime, endTime, assetPaths):
    """
    @
    Args:
        epi (str): episode name like "ep001"
        seq (str): sequence name like "sq001"
        shot (str): shot name like "sh001"
        startTime (int): animation start time.
        endTime (int): animation end time.
        assetPaths (list): all assets path in list.

    Returns:
            None.
    """
    # set current time and unit.
    pm.currentUnit(time='pal')
    pm.playbackOptions(ast=startTime, aet=endTime, maxTime=endTime, minTime=startTime)
    pm.currentTime(startTime)
    # create Hierarchy.
    shotGroup = pm.createNode('transform', n='shot_grp', ss=True)
    charGroup = pm.createNode('transform', n='char_grp', ss=True)
    propGroup = pm.createNode('transform', n='prop_grp', ss=True)
    setGroup = pm.createNode('transform', n='set_grp', ss=True)
    vehicleGroup = pm.createNode('transform', n='vehicle_grp', ss=True)
    fxGroup = pm.createNode('transform', n='fx_grp', ss=True)
    pm.parent(charGroup, propGroup, setGroup, vehicleGroup, fxGroup, shotGroup)
    # import camera.
    camFilePath = bs_pathGenerator.bs_getConfigPaths() + 'mayaFiles/shot_cam.ma'
    bs_mayaFile.bs_importFile(camFilePath)
    pm.parent('cam_grp', shotGroup)
    # add attributes.
    pm.addAttr(shotGroup, ln='bsw_episode', dt='string', k=True)
    pm.addAttr(shotGroup, ln='bsw_sequence', dt='string', k=True)
    pm.addAttr(shotGroup, ln='bsw_shot', dt='string', k=True)
    pm.addAttr(shotGroup, ln='bsw_stage', dt='string', k=True)
    # set Values.
    pm.setAttr(shotGroup + '.bsw_episode', epi)
    pm.setAttr(shotGroup + '.bsw_episode', l=True)
    pm.setAttr(shotGroup + '.bsw_sequence', seq)
    pm.setAttr(shotGroup + '.bsw_sequence', l=True)
    pm.setAttr(shotGroup + '.bsw_shot', shot)
    pm.setAttr(shotGroup + '.bsw_shot', l=True)
    pm.setAttr(shotGroup + '.bsw_stage', 'lay')
    pm.setAttr(shotGroup + '.bsw_stage', l=True)
    # add assets sets in one categorized set.
    pm.select(cl=True)
    mainSet = pm.sets(n='Assets_Set')
    charSet = pm.sets(n='Char_Set')
    propSet = pm.sets(n='Prop_Set')
    setSets = pm.sets(n='Set_Sets')
    vehicleSets = pm.sets(n='Vehicle_Sets')
    mainSet.addMembers([charSet, propSet, setSets, vehicleSets])
    bs_referenceAssetsInCurrentShot(assetPaths)


def bs_referenceAssetsInCurrentShot(assetPaths):
    """
    @ reference assets in the current shot.
    Args:
        assetPaths (list): assets path list.

    Returns:
            None.
    """
    # add assets sets in one categorized set.
    pm.select(cl=True)
    if not pm.objExists('Assets_Set'):
        pm.sets(n='Assets_Set')
    if not pm.objExists('Char_Set'):
        pm.sets(n='Char_Set')
    if not pm.objExists('Prop_Set'):
        pm.sets(n='Prop_Set')
    if not pm.objExists('Set_Sets'):
        pm.sets(n='Set_Sets')
    if not pm.objExists('Vehicle_Sets'):
        pm.sets(n='Vehicle_Sets')
    charSet = pm.PyNode('Char_Set')
    propSet = pm.PyNode('Prop_Set')
    setSets = pm.PyNode('Set_Sets')
    vehicleSets = pm.PyNode('Vehicle_Sets')
    # reference all assets.
    # and parent rig group in main shot hierarchy, also parent sets in set hierarchy.
    for each in assetPaths:
        if each.split('/')[-1].split('_')[1] == 'ch':
            ref = bs_reference.bs_createReference(each, prefixStyle='fileName')
            pm.parent(ref.namespace + ':rig_grp', 'char_grp')
            if pm.objExists(ref.namespace + ':Sets'):
                charSet.addMembers([ref.namespace + ':Sets'])
        elif each.split('/')[-1].split('_')[1] == 'pr':
            ref = bs_reference.bs_createReference(each, prefixStyle='fileName')
            pm.parent(ref.namespace + ':rig_grp', 'prop_grp')
            if pm.objExists(ref.namespace + ':Sets'):
                propSet.addMembers([ref.namespace + ':Sets'])
        elif each.split('/')[-1].split('_')[1] == 'bg':
            ref = bs_reference.bs_createReference(each, prefixStyle='fileName')
            pm.parent(ref.namespace + ':rig_grp', 'set_grp')
            if pm.objExists(ref.namespace + ':Sets'):
                setSets.addMembers([ref.namespace + ':Sets'])
        elif each.split('/')[-1].split('_')[1] == 'vh':
            ref = bs_reference.bs_createReference(each, prefixStyle='fileName')
            pm.parent(ref.namespace + ':rig_grp', 'vehicle_grp')
            if pm.objExists(ref.namespace + ':Sets'):
                vehicleSets.addMembers([ref.namespace + ':Sets'])


def bs_getItemsFromLwFilterAndReturnPath(allAssetsListWidget):
    """
    @ get all items from list widget and sort it with prefix ('ch_', 'pr_', 'bg_', 'vh_')
    Args:
        allAssetsListWidget (QtGui.QTabWidget): list widget who has a all types of assets sorted by ["ch_", "pr_"] etc.

    Returns:
            all assets paths with environment variable.
    """
    serverPath = bs_pathGenerator.bs_getEnvDetails()['rootPath']
    chars = list()
    props = list()
    sets = list()
    vehicles = list()
    for x in range(allAssetsListWidget.count()):
        assetName = allAssetsListWidget.item(x).text()
        if assetName.startswith('ch_'):
            astDict = bs_pathGenerator.bs_getAssetFileAndVersions('Character', 'Rig', assetName[3:])[0]
            if len(astDict.keys()) != 1:
                continue
            chars.append(astDict[astDict.keys()[0]]['path'])
        elif assetName.startswith('pr_'):
            astDict = bs_pathGenerator.bs_getAssetFileAndVersions('Prop', 'Rig', assetName[3:])[0]
            if len(astDict.keys()) != 1:
                continue
            props.append(astDict[astDict.keys()[0]]['path'])
        elif assetName.startswith('bg_'):
            astDict = bs_pathGenerator.bs_getAssetFileAndVersions('Set', 'Rig', assetName[3:])[0]
            if len(astDict.keys()) != 1:
                continue
            sets.append(astDict[astDict.keys()[0]]['path'])
        elif assetName.startswith('vh_'):
            astDict = bs_pathGenerator.bs_getAssetFileAndVersions('Vehicle', 'Rig', assetName[3:])[0]
            if len(astDict.keys()) != 1:
                continue
            vehicles.append(astDict[astDict.keys()[0]]['path'])
    mainList = chars + props + sets + vehicles
    environPaths = list()
    for each in mainList:
        newPath = each.replace(serverPath, '$BSW_PROD_SERVER/')
        environPaths.append(newPath)
    return environPaths
