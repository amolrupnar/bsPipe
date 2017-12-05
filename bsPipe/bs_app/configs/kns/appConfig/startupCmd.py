import pymel.core as pm

from bsPipe.bs_ui import bs_qui


def runInitialStartup():
    """
    @ run this function on maya start.
    Returns:
            None.
    """
    # load plugings.
    # pm.loadPlugin('mtoa')
    # set fps.
    pm.currentUnit(time='pal')
    print('SUCCESS MAYA OPEN WITH PRE LOADED SETTING...............'),
    bs_qui.bs_displayMessage('success', 'SUCCESS MAYA OPEN WITH PRE LOADED SETTING...............')
