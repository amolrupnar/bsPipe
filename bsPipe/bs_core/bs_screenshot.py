import pymel.core as pm
import os


def bs_getScreenShot(imageOutPath):
    """
    @ frame all views and get off screen screen shot using maya playblast.
    Args:
        imageOutPath (str): output path should be in '.jpg' format.

    Returns:
            image output path.
    """
    if pm.about(batch=True):
        return False
    # make screenshot dir if not exist.
    if not os.path.exists(os.path.dirname(imageOutPath)):
        os.makedirs(os.path.dirname(imageOutPath))
    perspCam = pm.PyNode('persp')
    perspCam.t.set(28.0, 21.0, 28.0)
    perspCam.r.set(-27.9383527296, 45.0, 0)
    pm.language.mel.eval('FrameAllInAllViews')
    return pm.playblast(frame=[pm.currentTime()], format="image", viewer=False, cf=imageOutPath, os=True, compression='jpg',
                        wh=[250, 250], quality=100, percent=100)
