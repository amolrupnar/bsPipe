import maya.cmds as cmds
import pymel.core as pm


def bs_sanityModBasic():
    """
    @ modeling basic sanity check.
    Returns:
            None.
    """
    sel = cmds.ls(typ='transform')
    avoidNames = ['front', 'persp', 'side', 'top', 'geo']
    filteredNames = list(set(sel) - set(avoidNames))
    # list of errors.
    grpMissing = []
    geoMissing = []
    caseProblem = []
    multiShapes = []
    shapeNamingIssue = []

    # check namings.
    for each in filteredNames:
        pyObj = pm.PyNode(each)
        if pyObj.getShapes():
            if not pyObj.endswith('_geo'):
                if not (pm.nodeType(pyObj.getShape()) == 'lattice' or pm.nodeType(pyObj.getShape()) == 'baseLattice'):
                    geoMissing.append(pyObj)
            if len(pyObj.getShapes()) > 1:
                multiShapes.append(pyObj)
            else:
                if not pyObj.getShape().name().endswith('Shape'):
                    shapeNamingIssue.append(pyObj)
        else:
            if not pyObj.endswith('_grp'):
                grpMissing.append(pyObj)
        # check character in small case.
        for x in pyObj.split('_'):
            if x:
                if x[0].isupper():
                    caseProblem.append(pyObj)

    setsDict = {'grp': grpMissing, 'geo': geoMissing, 'case': caseProblem, 'multiShapes': multiShapes,
                'shapeNamingIssue': shapeNamingIssue}

    for x in setsDict.keys():
        if pm.objExists('SET_Missmatch_' + x):
            pm.delete('SET_Missmatch_' + x)
        if setsDict[x]:
            pm.sets(n='SET_Missmatch_' + x, em=True).union(setsDict[x])


def bs_checkNonFreezedVertex(sel=None):
    """
    @ check non freezed vertex of selected geometries.
    Args:
        sel (str): geometries have to check.

    Returns:
            nonFreezedVertexGeometry, nonFreezedVertex.
    """
    if not sel:
        allMesh = pm.ls(typ='mesh')
        allGeoTrans = list()
        for each in allMesh:
            allGeoTrans.append(each.getParent())
        # set all transforms.
        sel = list(set(allGeoTrans))
    nonVertFreezedGeo = []
    nonFreezedVert = []
    newSel = []
    for each in sel:
        latticeGeo = False
        for eachHist in pm.listHistory(each, pdo=True):
            if pm.nodeType(eachHist) == 'ffd':
                latticeGeo = True
        if not latticeGeo:
            newSel.append(each)
    for each in newSel:
        allVertNumbers = pm.modeling.polyEvaluate(each, v=True)
        for v in xrange(allVertNumbers):
            xPoint = pm.getAttr('{0}.vtx[{1}].pntx'.format(each, v))
            yPoint = pm.getAttr('{0}.vtx[{1}].pnty'.format(each, v))
            zPoint = pm.getAttr('{0}.vtx[{1}].pntz'.format(each, v))
            if xPoint == 0 and yPoint == 0 and zPoint == 0:
                pass
            else:
                nonVertFreezedGeo.append(each)
                nonFreezedVert.append('{0}.vtx[{1}]'.format(each, v))
    print nonVertFreezedGeo
    print nonFreezedVert
    if nonVertFreezedGeo:
        return list(set(nonVertFreezedGeo)), nonFreezedVert
    else:
        return False


def bs_sanityModCheckBasics():
    """
        @ modeling basic sanity check.
        Returns:
                None.
        """
    sel = cmds.ls(typ='transform')
    avoidNames = ['front', 'persp', 'side', 'top', 'geo']
    filteredNames = list(set(sel) - set(avoidNames))
    # list of errors.
    grpMissing = []
    geoMissing = []
    caseProblem = []
    multiShapes = []
    shapeNamingIssue = []

    # check namings.
    for each in filteredNames:
        pyObj = pm.PyNode(each)
        if pyObj.getShapes():
            if not pyObj.endswith('_geo'):
                if not (pm.nodeType(pyObj.getShape()) == 'lattice' or pm.nodeType(pyObj.getShape()) == 'baseLattice'):
                    geoMissing.append(pyObj)
            if len(pyObj.getShapes()) > 1:
                latticeGeo = False
                for eachHist in pm.listHistory(pyObj, pdo=True):
                    if pm.nodeType(eachHist) == 'ffd':
                        latticeGeo = True
                if not latticeGeo:
                    multiShapes.append(pyObj)
            else:
                if not pyObj.getShape().name().endswith('Shape'):
                    shapeNamingIssue.append(pyObj)
        else:
            if not pyObj.endswith('_grp'):
                grpMissing.append(pyObj)
        # check character in small case.
        for x in pyObj.split('_'):
            if x:
                if x[0].isupper():
                    caseProblem.append(pyObj)
    return {'grp': grpMissing, 'geo': geoMissing, 'case': caseProblem, 'multiShapes': multiShapes,
            'shapeNamingIssue': shapeNamingIssue}
