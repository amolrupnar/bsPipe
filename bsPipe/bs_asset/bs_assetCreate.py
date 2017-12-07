import pymel.core as pm

from bsPipe.bs_core import bs_pathGenerator
from bsPipe.bs_core import bs_reference
from bsPipe.bs_ui import bs_qui

reload(bs_pathGenerator)
reload(bs_reference)
reload(bs_qui)


def bs_createModelBase(topGroup, assetName, assetGrade, assetType, episode=None, makeGroups=True):
    """
    @ create asset model
    @ make modeling base hierarchy and add attributes on top group for query purpose.
    Args:
        topGroup (str): Hierarchy Top Group Name.
        assetName (str): Asset Name.
        assetGrade (str): Character Grade (Primary, Secondary, Tertiary).
        assetType (str): Asset Type Character, Prop, Set, Vehicle.
        episode (str): episode number like (ep000,ep001,ep002) format.
        makeGroups (bool): make groups if value is True

    Returns:
            topGrp.
    """
    # raise popup window for current scene will be discarded if maya is not in batch mode.
    if not pm.about(batch=True):
        confirmation = pm.windows.confirmDialog(title='Confirm',
                                                message="Don't Save Current Scene\nAnd Load New Scene?",
                                                button=['Yes', 'No'], defaultButton='Yes')
        if confirmation == 'Yes':
            pm.newFile(f=True)
        else:
            print 'process cancelled',
            return False
    # create group if make hierarchy is True.
    astTypShortCode = {'Character': 'ch', 'Prop': 'pr', 'Set': 'bg', 'Vehicle': 'vh', 'SetElement': 'se'}
    if bs_pathGenerator.bs_getEnv()['projectType'] == 'series':
        uid = 'bsw_' + astTypShortCode[assetType] + '_' + assetName + '_mod_' + episode
    else:
        uid = 'bsw_' + astTypShortCode[assetType] + '_' + assetName + '_mod'
    pm.select(cl=True)
    if makeGroups:
        # make groups.
        topGrp = pm.createNode('transform', n=topGroup, ss=True)
        modelGrp = pm.createNode('transform', n=assetName + '_grp', ss=True)
        if assetType == 'Character':
            bodyGrp = pm.createNode('transform', n='body_grp', ss=True)
            eyeGrp = pm.createNode('transform', n='eye_grp', ss=True)
            eyeBrowGrp = pm.createNode('transform', n='eyeBrow_grp', ss=True)
            innerMouthGrp = pm.createNode('transform', n='innerMouth_grp', ss=True)
            hairGrp = pm.createNode('transform', n='hair_grp', ss=True)
            clothGrp = pm.createNode('transform', n='cloth_grp', ss=True)
            propsGrp = pm.createNode('transform', n='props_grp', ss=True)
            shoeGrp = pm.createNode('transform', n='shoe_grp', ss=True)
            # make parent.
            pm.parent(bodyGrp, clothGrp, propsGrp, shoeGrp, modelGrp)
            pm.parent(eyeGrp, eyeBrowGrp, innerMouthGrp, hairGrp, bodyGrp)
        elif assetType == 'Set':
            setElementGrp = pm.createNode('transform', n='setElements_grp')
            pm.parent(modelGrp, setElementGrp, topGrp)
        pm.parent(modelGrp, topGrp)
    else:
        topGrp = topGroup
    # add attributes for query asset details purpose.
    pm.addAttr(topGrp, ln='assetBase', dt='string', k=True)
    pm.addAttr(topGrp, ln='assetType', dt='string', k=True)
    pm.addAttr(topGrp, ln='assetName', dt='string', k=True)
    pm.addAttr(topGrp, ln='assetGrade', dt='string', k=True)
    if bs_pathGenerator.bs_getEnv()['projectType'] == 'series':
        pm.addAttr(topGrp, ln='assetEpisode', dt='string', k=True)
    pm.addAttr(topGrp, ln='assetUID', dt='string', k=True)
    # add asset details in top group attributes.
    pm.setAttr(topGrp + '.assetBase', 'Asset')
    pm.setAttr(topGrp + '.assetBase', l=True)
    pm.setAttr(topGrp + '.assetType', assetType)
    pm.setAttr(topGrp + '.assetType', l=True)
    pm.setAttr(topGrp + '.assetName', assetName)
    pm.setAttr(topGrp + '.assetName', l=True)
    pm.setAttr(topGrp + '.assetGrade', assetGrade)
    pm.setAttr(topGrp + '.assetGrade', l=True)
    if bs_pathGenerator.bs_getEnv()['projectType'] == 'series':
        pm.setAttr(topGrp + '.assetEpisode', episode)
        pm.setAttr(topGrp + '.assetEpisode', l=True)
    pm.setAttr(topGrp + '.assetUID', uid)
    pm.setAttr(topGrp + '.assetUID', l=True)
    pm.select(topGrp, r=True)
    bs_pathGenerator.bs_createAssetDirectories(assetType, assetName)
    bs_qui.bs_displayMessage('success', 'Asset Created Successfully....')
    return topGrp


def bs_createRigBase(assetName, assetGrade, assetType, episode=None):
    """
    @ create Rig Base group in reference model file in rig.
    Args:
        assetName (str): Model Name.
        assetGrade (str): Character Grade (Primary, Secondary, Tertiary).
        assetType (str): Asset Type Character, Prop, Set, Vehicle
        episode (str): asset Name dodo is like (dod).

    Returns:
            top rig group.
    """
    # raise popup window for current scene will be discarded if maya is not in batch mode.
    if not pm.about(batch=True):
        confirmation = pm.windows.confirmDialog(title='Confirm',
                                                message="Don't Save Current Scene\nAnd Load New Scene?",
                                                button=['Yes', 'No'], defaultButton='Yes')
        if confirmation == 'Yes':
            pm.newFile(f=True)
        else:
            print 'process cancelled',
            return False
    # get environments.
    serverPath = bs_pathGenerator.bs_getEnv()['projectDir']
    # get model directory.
    if bs_pathGenerator.bs_getEnv()['projectType'] == 'series':
        modelFile = bs_pathGenerator.bs_getOnlyFinalFileOfDept(assetType, 'Model', assetName, episode=episode)
    else:
        modelFile = bs_pathGenerator.bs_getOnlyFinalFileOfDept(assetType, 'Model', assetName)
    # create path using environment variable.
    modelFile = modelFile.replace(serverPath, '$BSW_PROJECT_DIR')
    print modelFile
    bs_reference.bs_createReference(modelFile, prefixStyle='withoutNamespace', prefixName='')
    # create Rig Group.
    topGrp = pm.createNode('transform', n='rig_grp', ss=True)
    # add asset uid.
    astTypShortCode = {'Character': 'ch', 'Prop': 'pr', 'Set': 'bg', 'Vehicle': 'vh', 'SetElement': 'se'}
    if bs_pathGenerator.bs_getEnv()['projectType'] == 'series':
        uid = 'bsw_' + astTypShortCode[assetType] + '_' + assetName + '_rig_' + episode
    else:
        uid = 'bsw_' + astTypShortCode[assetType] + '_' + assetName + '_rig'
    # add attributes.
    pm.addAttr(topGrp, ln='assetBase', dt='string', k=True)
    pm.addAttr(topGrp, ln='assetType', dt='string', k=True)
    pm.addAttr(topGrp, ln='assetName', dt='string', k=True)
    pm.addAttr(topGrp, ln='assetGrade', dt='string', k=True)
    if bs_pathGenerator.bs_getEnv()['projectType'] == 'series':
        pm.addAttr(topGrp, ln='assetEpisode', dt='string', k=True)
    pm.addAttr(topGrp, ln='assetUID', dt='string', k=True)
    # set Values.
    pm.setAttr(topGrp + '.assetBase', 'Asset')
    pm.setAttr(topGrp + '.assetBase', l=True)
    pm.setAttr(topGrp + '.assetType', assetType)
    pm.setAttr(topGrp + '.assetType', l=True)
    pm.setAttr(topGrp + '.assetName', assetName)
    pm.setAttr(topGrp + '.assetName', l=True)
    pm.setAttr(topGrp + '.assetGrade', assetGrade)
    pm.setAttr(topGrp + '.assetGrade', l=True)
    if bs_pathGenerator.bs_getEnv()['projectType'] == 'series':
        pm.setAttr(topGrp + '.assetEpisode', episode)
        pm.setAttr(topGrp + '.assetEpisode', l=True)
    pm.setAttr(topGrp + '.assetUID', uid)
    pm.setAttr(topGrp + '.assetUID', l=True)
    # parent referenced model top group in rig group.
    pm.parent('geo', topGrp)
    pm.select(topGrp, r=True)
    if bs_pathGenerator.bs_getEnv()['projectType'] == 'series':
        bs_pathGenerator.bs_createAssetDirectories(assetType, assetName, episode=episode)
    else:
        bs_pathGenerator.bs_createAssetDirectories(assetType, assetName)
    return topGrp


def bs_createTextureBase(assetName, assetGrade, assetType, episode=None):
    """
    @ create Texture Base group in reference model file in rig.
    Args:
        assetName (str): Model Name.
        assetGrade (str): Character Grade (Primary, Secondary, Tertiary).
        assetType (str): Asset Type Character, Prop, Set, Vehicle
        episode (str): asset Name dodo is like (dod).

    Returns:
            top Texture group.
    """
    # raise popup window for current scene will be discarded if maya is not in batch mode.
    if not pm.about(batch=True):
        confirmation = pm.windows.confirmDialog(title='Confirm',
                                                message="Don't Save Current Scene\nAnd Load New Scene?",
                                                button=['Yes', 'No'], defaultButton='Yes')
        if confirmation == 'Yes':
            pm.newFile(f=True)
        else:
            print 'process cancelled',
            return False
    # get environments.
    serverPath = bs_pathGenerator.bs_getEnv()['projectDir']
    # get model directory.
    if bs_pathGenerator.bs_getEnv()['projectType'] == 'series':
        modelFile = bs_pathGenerator.bs_getOnlyFinalFileOfDept(assetType, 'Model', assetName, episode=episode)
    else:
        modelFile = bs_pathGenerator.bs_getOnlyFinalFileOfDept(assetType, 'Model', assetName)
    # create path using environment variable.
    modelFile = modelFile.replace(serverPath, '$BSW_PROJECT_DIR')
    bs_reference.bs_createReference(modelFile, prefixStyle='withoutNamespace', prefixName='')
    # create Texture Group.
    topGrp = pm.createNode('transform', n='Texture_Group', ss=True)
    # add asset uid.
    astTypShortCode = {'Character': 'ch', 'Prop': 'pr', 'Set': 'bg', 'Vehicle': 'vh', 'SetElement': 'se'}
    if bs_pathGenerator.bs_getEnv()['projectType'] == 'series':
        uid = 'bsw_' + astTypShortCode[assetType] + '_' + assetName + '_tex_' + episode
    else:
        uid = 'bsw_' + astTypShortCode[assetType] + '_' + assetName + '_tex'
    # add attributes.
    pm.addAttr(topGrp, ln='assetBase', dt='string', k=True)
    pm.addAttr(topGrp, ln='assetType', dt='string', k=True)
    pm.addAttr(topGrp, ln='assetName', dt='string', k=True)
    pm.addAttr(topGrp, ln='assetGrade', dt='string', k=True)
    if bs_pathGenerator.bs_getEnv()['projectType'] == 'series':
        pm.addAttr(topGrp, ln='assetEpisode', dt='string', k=True)
    pm.addAttr(topGrp, ln='assetUID', dt='string', k=True)
    # set Values.
    pm.setAttr(topGrp + '.assetBase', 'Asset')
    pm.setAttr(topGrp + '.assetBase', l=True)
    pm.setAttr(topGrp + '.assetType', assetType)
    pm.setAttr(topGrp + '.assetType', l=True)
    pm.setAttr(topGrp + '.assetName', assetName)
    pm.setAttr(topGrp + '.assetName', l=True)
    pm.setAttr(topGrp + '.assetGrade', assetGrade)
    pm.setAttr(topGrp + '.assetGrade', l=True)
    if bs_pathGenerator.bs_getEnv()['projectType'] == 'series':
        pm.setAttr(topGrp + '.assetEpisode', episode)
        pm.setAttr(topGrp + '.assetEpisode', l=True)
    pm.setAttr(topGrp + '.assetUID', uid)
    pm.setAttr(topGrp + '.assetUID', l=True)
    # parent referenced model top group in texture group.
    pm.parent('geo', topGrp)
    bs_pathGenerator.bs_createAssetDirectories(assetType, assetName)
    bs_qui.bs_displayMessage('success', 'asset Created success and created sourceimages directory')
    return topGrp
