import pymel.core as pm
import getpass
import time

from bsPipe.bs_core import bs_pathGenerator
from bsPipe.bs_ui import bs_qui

reload(bs_pathGenerator)
reload(bs_qui)


def bspb_getCurrentCam():
    """
    @ get camera name from scene according to focused model panel.
    Returns:
            camera name (str).
    """
    curPanel = pm.windows.getPanel(wf=True)
    if curPanel.startswith('modelPanel'):
        currentCamera = str(pm.windows.modelEditor(curPanel, q=True, camera=True))
        if currentCamera == 'shot_cam' or currentCamera == 'shot_camShape':
            return 'shot_cam'
        else:
            return 'Valid Camera is not selected.'
    else:
        return 'Please Select shot_cam viewport.'


def bspb_sceneName():
    """
    @ query and return scene name from current scene.
    Returns:
            scene name.
    """
    projectName = bs_pathGenerator.bs_getEnvDetails()['projectName'].lower()
    # get shot details.
    epi, seq, shot, stage = bs_pathGenerator.bs_shotDetailsCheckAndReturn()
    return '{0}_{1}_{2}_{3}_{4}'.format(projectName, epi, seq, shot, stage)


def bspb_artistName():
    """
    @ get and return username
    Returns:
            username.
    """
    return getpass.getuser()


def bspb_dateTime():
    """
    @ return current time and date.
    Returns:
            time and date.
    """
    return time.strftime("%c")


def bspb_frameCounter():
    """
    @ count current frame.
    Returns:
            Current time and max time.
    """
    curTime = int(pm.currentTime())
    maxTime = int(pm.playbackOptions(q=True, maxTime=True))
    return '{0} / {1}'.format(curTime, maxTime)


def bspb_frameCounterUpdate():
    """
    @ update frame counter using heads up display refresh flag.
    Returns:
            frame counter update using headsUpDisplay.
    """
    if pm.windows.headsUpDisplay('frameCounterUpdateEXP', q=True, ex=True):
        pm.delete('frameCounterUpdateEXP')
    pm.expression(s='headsUpDisplay -r "frameCounterHUD";', n='frameCounterUpdateEXP', ae=1, uc='all')


def bspb_focalLength():
    """
    @ get and return shot camera focal length.
    Returns:
            focal length.
    """
    shotCam = pm.PyNode('shot_cam').getShape()
    return str(shotCam.focalLength.get())


def bspb_focalLengthUpdate():
    """
    @ update focal length using headsUpDisplay refresh command.
    Returns:
            update focal length.
    """
    if pm.windows.headsUpDisplay('focalLengthUpdateEXP', q=True, ex=True):
        pm.delete('focalLengthUpdateEXP')
    pm.expression(s='headsUpDisplay -r "focalLengthHUD";', n='focalLengthUpdateEXP', ae=1, uc='all')


def bs_addHeadsUpDisplay():
    """
    @ add headsUpDisplay and add expressions.
    Returns:
            headsUpDisplay.
    """
    # remove all headsUpDisplay.
    if pm.windows.headsUpDisplay(lh=True):
        for each in pm.windows.headsUpDisplay(lh=True):
            pm.windows.headsUpDisplay(each, rem=True)
    # add new heads up displays.
    pm.windows.headsUpDisplay('sceneNameHUD', l='Scene Name:- ', allowOverlap=True, b=0, s=4, dataFontSize='small',
                              command=bspb_sceneName)
    pm.windows.headsUpDisplay('artistNameHUD', l='Artist Name:- ', allowOverlap=True, b=1, s=5, dataFontSize='small',
                              command=bspb_artistName)
    pm.windows.headsUpDisplay('dateTimeHUD', l='Date And Time:- ', allowOverlap=True, b=0, s=5, dataFontSize='small',
                              command=bspb_dateTime)
    pm.windows.headsUpDisplay('frameCounterHUD', l='Frame Number:- ', allowOverlap=True, b=1, s=9, dataFontSize='small',
                              command=bspb_frameCounter)
    pm.windows.headsUpDisplay('focalLengthHUD', l='Focal Length:- ', allowOverlap=True, b=0, s=9, dataFontSize='small',
                              command=bspb_focalLength)
    pm.windows.headsUpDisplay('camNameHUD', l='Cam :- ', allowOverlap=True, b=0, s=7, dataFontSize='small',
                              command=bspb_getCurrentCam)
    # add colors in heads up display.
    # pm.mel.eval("displayColor -dormant headsUpDisplayLabels 19")
    # pm.mel.eval("displayColor -dormant headsUpDisplayValues 14")
    # add expressions.
    bspb_frameCounterUpdate()
    bspb_focalLengthUpdate()


def bs_removeHeadsUpDisplay():
    """
    @ remove headsUpDisplay and also delete expressions.
    Returns:
            None.
    """
    # remove all headsUpDisplay.
    if pm.windows.headsUpDisplay(lh=True):
        for each in pm.windows.headsUpDisplay(lh=True):
            pm.windows.headsUpDisplay(each, rem=True)
    # remove resolution gates.
    shotCam = pm.PyNode('shot_cam')
    # add resolution gates.
    pm.camera(shotCam, e=True, dsa=False, dfc=False, displayFilmGate=False, displayResolution=False,
              displaySafeTitle=False)
    pm.setAttr(shotCam + '.displayGateMaskOpacity', 0)
    pm.setAttr(shotCam + '.displayGateMaskColor', [0, 0, 0], type='double3')
    pm.setAttr(shotCam + '.displayGateMask', 0)
    # delete expression.
    pm.delete('focalLengthUpdateEXP')
    pm.delete('frameCounterUpdateEXP')


def bs_playblast():
    """
    @ create playblast with headsUpDisplays.
    Returns:
            playblastPath.
    """
    bs_addHeadsUpDisplay()
    epi, seq, shot, stage = bs_pathGenerator.bs_shotDetailsCheckAndReturn()
    outPath = bs_pathGenerator.bs_animFilePath(epi, seq, shot)[stage][:-3]
    shotCam = pm.PyNode('shot_cam')
    # add resolution gates.
    pm.camera(shotCam, e=True, filmFit='overscan')
    pm.camera(shotCam, e=True, dsa=True, dfc=False, displayFilmGate=False, displayResolution=True,
              displaySafeTitle=False)
    pm.setAttr(shotCam + '.displayGateMaskOpacity', 1)
    pm.setAttr(shotCam + '.displayGateMaskColor', [0, 0, 0], type='double3')
    pm.setAttr(shotCam + '.displayGateMask', 1)
    # get Sound File.
    soundFile = pm.windows.timeControl('timeControl1', q=True, s=True)
    # playblast.
    if soundFile:
        vidPath = pm.playblast(f=outPath, format='avi', s=soundFile, sequenceTime=0, forceOverwrite=True, clearCache=1,
                               viewer=1,
                               showOrnaments=1, fp=4, percent=100, quality=70, widthHeight=[960, 540])
    else:
        vidPath = pm.playblast(f=outPath, format='avi', sequenceTime=0, forceOverwrite=True, clearCache=1, viewer=1,
                               showOrnaments=1, fp=4, percent=100, quality=70, widthHeight=[960, 540])
    bs_removeHeadsUpDisplay()
    bs_qui.bs_displayMessage('success', '{0}'.format(vidPath))
    return vidPath
