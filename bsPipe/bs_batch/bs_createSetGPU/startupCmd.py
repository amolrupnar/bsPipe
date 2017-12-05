import pymel.core as pm
import json
import tempfile
import os

from bsPipe.bs_core import bs_pathGenerator

reload(bs_pathGenerator)


def runInitialStartup():
    """
    @ run this function on maya start.
    Returns:
            None.
    """
    pm.select(cl=True)
    # make groups.
    topGrp = pm.PyNode('geo')
    modelGrp = pm.PyNode('test_grp')
    # get asset data from temp directory using json.
    jsonFilePath = tempfile.gettempdir() + '\\zSetAssetData.json'
    with open(os.path.join(tempfile.gettempdir(), jsonFilePath)) as fd:
        astData = json.load(fd)
    # set Values.
    pm.setAttr(topGrp + '.assetName', astData['name'])
    pm.setAttr(topGrp + '.assetName', l=True)
    pm.setAttr(topGrp + '.assetGrade', astData['grade'])
    pm.setAttr(topGrp + '.assetGrade', l=True)
    pm.setAttr(topGrp + '.assetUID', astData['uid'])
    pm.setAttr(topGrp + '.assetUID', l=True)
    modelGrp.rename(astData['name'])
    # get back to gpu folder.
    gpuPath = str()
    for each in astData['path'].split('.')[0].split('/')[:-1]:
        gpuPath += each + '/'
    if not os.path.isdir(gpuPath):
        os.makedirs(gpuPath)
        print 'path created.'
    # change gpu cache path.
    cacheFilePath = astData['path'].replace('.ma', '.abc')
    cacheNode = pm.PyNode('gpuCache')
    serverPath = bs_pathGenerator.bs_getEnvDetails()['rootPath']
    cacheFilePath = cacheFilePath.replace(serverPath, '$BSW_PROD_SERVER/')
    cacheNode.cacheFileName.set(cacheFilePath)
    # save as file.
    pm.saveAs(astData['path'])
    return topGrp
