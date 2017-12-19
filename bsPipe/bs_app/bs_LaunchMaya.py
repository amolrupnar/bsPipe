import os
import subprocess
import json


def setEnvPaths(project):
    """
    @ set environment variables and project specific configurations.
    Args:
        project (str): project short name.

    Returns:
            project application path (str).
    """
    # set programation path and create new environment variable.
    pipelinePath = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    showConfigPath = os.path.dirname(__file__) + '/configs/' + project + '/showConfig'
    appConfigPath = os.path.dirname(__file__) + '/configs/' + project + '/appConfig'
    allPythonPaths = [pipelinePath + '/CoreScripts/PythonScripts',
                      pipelinePath + '/rigtools',
                      pipelinePath + '/bsPipe',
                      appConfigPath
                      ]

    appSetting = appConfigPath + '/appSetting.json'
    with open(appSetting) as config_data:
        config = json.load(config_data)
    # setx.
    # SET BSW ENVIRONMENTS.
    programDir = os.path.dirname(os.path.dirname(os.path.dirname(pipelinePath))) + 'bsw_programation/01_maya'
    sitePackagesPath = os.path.dirname(
        os.path.dirname(os.path.dirname(pipelinePath))) + 'bsw_programation/07_python/site-packages'
    os.environ['BSW_PROJECT_SHORT'] = project
    os.environ['BSW_PROJECT_NAME'] = config['project_name']
    os.environ['BSW_PROJECT_DIR'] = config['project_dir']
    os.environ['BSW_PROGRAM_DIR'] = programDir
    os.environ['BSW_PROJECT_TYPE'] = 'series'
    # SET APP PATH ENVIRONMENT.
    os.environ['MAYA_APP_PATH'] = config['project_app']
    # SET OTHER MAYA ENVIRONMENTS.
    os.environ['XBMLANGPATH'] = showConfigPath + '/icons'
    os.environ['MAYA_SHELF_PATH'] = showConfigPath + '/shelf'
    # add maya script paths core mel scripts and appConfig path for the purpose of "userSetup.mel"
    os.environ['MAYA_SCRIPT_PATH'] = pipelinePath + '/CoreScripts/MelScripts'
    os.environ['MAYA_SCRIPT_PATH'] = os.environ['MAYA_SCRIPT_PATH'] + ";" + appConfigPath
    # add python paths custom site packages and core scripts.
    os.environ['PYTHONPATH'] = sitePackagesPath
    os.environ['PYTHONPATH'] = os.environ['PYTHONPATH'] + ";" + showConfigPath + '/scriptPython'
    for each in allPythonPaths:
        os.environ['PYTHONPATH'] = os.environ['PYTHONPATH'] + ";" + each
    return config['project_app']


def launch_app():
    """
    @ launch project application.
    Returns:
            None.
    """
    mayaApplication = setEnvPaths('kns')
    cmd = [mayaApplication, ['-noAutoloadPlugins -command startupCmd;']]
    subprocess.Popen(cmd)


if __name__ == '__main__':
    launch_app()
