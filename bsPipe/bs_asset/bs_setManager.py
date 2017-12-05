import pymel.core as pm
import os

from bsPipe.bs_ui import bs_qui
from bsPipe.bs_core import bs_pathGenerator
from bsPipe.bs_batch.bs_createSetGPU import bs_runner

reload(bs_qui)
reload(bs_pathGenerator)
reload(bs_runner)


def bs_makeGpuCacheFile():
    """
    @ make a gpu cache file and if gpu maya file is not exist then auto run bs_makeGpuMayaFile method.
    Returns:
            None.
    """
    # query current set.
    dept, assetType, assetName, uid = bs_pathGenerator.bs_getAssetDetails()
    if dept == 'Not Exist' or assetType == 'Not Exist' or assetName == 'Not Exist':
        bs_qui.bs_displayMessage('error', 'No Set Found in Scene.....')
        return False
    pm.loadPlugin('gpuCache')
    ct = pm.currentTime()
    cacheDir = bs_pathGenerator.bs_getAssetDir(astType=assetType, astName=assetName, astDept=dept)['dept'] + 'gpu/'
    fileName = bs_pathGenerator.bs_getMainFileName().split('.')[0][:-3] + 'gpu'
    # create gpu directory if not exist.
    if not os.path.isdir(cacheDir):
        os.makedirs(cacheDir)
    # export gpu cache.
    pm.gpuCache(st=ct, et=ct, o=True, ot=40000, wm=True, df='ogawa', dir=cacheDir, fileName=fileName, ado=True)
    # check gpu maya file is exist or not.
    if not os.path.isfile(cacheDir + fileName + '.ma'):
        bs_makeGpuMayaFile()
        bs_qui.bs_displayMessage('success', 'Gpu Cache Exported And Gpu Maya File also Created..')
    else:
        bs_qui.bs_displayMessage('success', 'Gpu Cache Exported..')


def bs_makeGpuMayaFile():
    """
    @ make gpu maya file.
    Returns:

    """
    # Make Gpu File
    # query current set.
    dept, assetType, assetName, uid = bs_pathGenerator.bs_getAssetDetails()
    if dept == 'Not Exist' or assetType == 'Not Exist' or assetName == 'Not Exist':
        bs_qui.bs_displayMessage('error', 'No Set Found in Scene.....')
        return False
    # get asset grade in current scene
    geoGrp = pm.PyNode('geo')
    assetGrade = geoGrp.assetGrade.get()
    # create file path.
    cacheDir = bs_pathGenerator.bs_getAssetDir(astType=assetType, astName=assetName, astDept=dept)['dept'] + 'gpu/'
    fileName = bs_pathGenerator.bs_getMainFileName().split('.')[0][:-3] + 'gpu'
    # check gpu maya file is exist or not.
    filePath = cacheDir + fileName + '.ma'
    if os.path.isfile(cacheDir + fileName + '.ma'):
        return True
    bs_runner.bs_blast(astPath=filePath, astName=assetName, astGrade=assetGrade, astUID=uid)
