import pymel.core as pm
import maya.cmds as cmds


def bs_sanityCheckNamespaces():
    """
    @ get all namespaces in the scene.
    Returns:
            namespaces (list).
    """
    return pm.listNamespaces()


def bs_sanityCheckDisplayLayer():
    """
    @ get and return all display layers except default layer in the scene.
    Returns:
            display layer (list).
    """
    allLayers = cmds.ls(typ='displayLayer')
    filtLayers = list(set(allLayers) - {'defaultLayer'})
    if filtLayers:
        return filtLayers
    else:
        return False


def bs_sanityCheckRenderLayer():
    """
    @ get and return all render layers except default layer in the scene.
    Returns:
            render layer (list).
    """
    allLayers = cmds.ls(typ='renderLayer')
    filtLayers = list(set(allLayers) - {'defaultRenderLayer'})
    if filtLayers:
        return filtLayers
    else:
        return False


def bs_findDuplicates():
    """
    @ brief Check for nodes with duplicate name and add them to errors node.
    Returns:
            duplicated objects.
    """
    duplicateNames = list()
    for node in pm.ls():
        if "|" in str(node):
            if not node.isInstanced():
                duplicateNames.append(str(node))
            else:
                if len(pm.ls(node)) > 1:
                    duplicateNames.append(str(node))
    if not duplicateNames:
        return False
    return duplicateNames


def bs_checkAllTransformFreezed():
    """
    @ check all transforms are freezed
    @ if not freezed transform found return the list of non freezed transforms.
    Returns:
            nonFreezed transform.
    """
    allTransform = cmds.ls(typ='transform')
    avoidTransform = ['front', 'side', 'top', 'persp']
    filtTransform = list(set(allTransform) - set(avoidTransform))
    nonFreezed = list()
    for each in filtTransform:
        obj = pm.PyNode(each)
        if obj.getShape():
            if pm.nodeType(obj.getShape()) == 'lattice' or pm.nodeType(obj.getShape()) == 'baseLattice':
                continue
        tx, ty, tz = obj.getAttr('tx'), obj.getAttr('ty'), obj.getAttr('tz')
        rx, ry, rz = obj.getAttr('rx'), obj.getAttr('ry'), obj.getAttr('rz')
        sx, sy, sz = obj.getAttr('sx'), obj.getAttr('sy'), obj.getAttr('sz')
        if tx != 0 or ty != 0 or tz != 0 or rx != 0 or ry != 0 or rz != 0 or sx != 1 or sy != 1 or sz != 1:
            nonFreezed.append(obj)
    if nonFreezed:
        return nonFreezed
    else:
        return False
