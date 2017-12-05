import pymel.core as pm


def bs_getScreenShot(imageOutPath):
    """
    @ frame all views and get screen shot using maya playblast.
    Args:
        imageOutPath (str): output path should be in '.iff' format.

    Returns:
            image output path.
    """
    if pm.about(batch=True):
        return False
    perspCam = pm.PyNode('persp')
    perspCam.t.set(28.0, 21.0, 28.0)
    perspCam.r.set(-27.9383527296, 45.0, 0)
    pm.mel.eval('FrameAllInAllViews')
    return pm.playblast(frame=[1], format="image", viewer=False, cf=imageOutPath)
