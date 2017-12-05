import os
from subprocess import Popen, PIPE
import tempfile
import json


def bs_blast(astPath='', astName='', astGrade='', astUID=''):
    """
    @ set environ paths and get raw file from this dir and save as path getting from json file. (using popen)
    @ popen process in this function.
    Args:
        astPath (str): asset path.
        astName (str): asset name.
        astGrade (str): asset grade.
        astUID (str): asset uid.

    Returns:
            None.
    """
    mayaApp = "C:/Program Files/Autodesk/Maya2015/bin/mayabatch.exe"
    pipelinePath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    os.environ['PYTHONPATH'] = os.path.dirname(__file__)
    os.environ['PYTHONPATH'] = os.environ['PYTHONPATH'] + ";" + pipelinePath
    scriptPath = os.path.dirname(__file__) + '/startupCmd.mel'
    tempJson = tempfile.gettempdir() + '\\zSetAssetData.json'
    dataDict = {'name': astName, 'grade': astGrade, 'uid': astUID, 'path': astPath}
    # dump data in temp directory as json file.
    with open(tempJson, 'w') as jsFile:
        json.dump(dataDict, jsFile)
    # raw gpu file path.
    gpuFilePath = os.path.dirname(__file__) + '/kns_bg_rawGPU_ep000_gpu.ma'
    # run p open.
    process = Popen([mayaApp, "-batch", "-file", gpuFilePath, "-script", scriptPath], stdout=PIPE)
    stdout, stderr = process.communicate()
    print stdout
    print stderr
