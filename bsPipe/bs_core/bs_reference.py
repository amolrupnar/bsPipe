import pymel.core as pm

from bsPipe.bs_core import bs_pathGenerator

reload(bs_pathGenerator)


def bs_getReference():
    """
    @ get all references from the scene and check if it came from valid directory.
    @ and filter it with asset type like (char, prop, set, vehicle.)
    Returns:
            dict.
            # return dictionary format.
            mainDict = {
            'char':{refNode: {'node':'', 'path':'', 'name':''}, refNode1: {'node':'', 'path':'', 'name':''}},
            'prop':{refNode: {'node':'', 'path':'', 'name':''}, refNode1: {'node':'', 'path':'', 'name':''}},
            'set':{refNode: {'node':'', 'path':'', 'name':''}, refNode1: {'node':'', 'path':'', 'name':''}},
            'vehicle':{refNode: {'node':'', 'path':'', 'name':''}, refNode1: {'node':'', 'path':'', 'name':''}},
                        }
    """
    allRef = pm.getReferences()
    # Declare dictionary.
    mainDict = dict()
    charDict = dict()
    propDict = dict()
    setDict = dict()
    vehicleDict = dict()
    for each in allRef.keys():
        eachRef = pm.getReferences()[each]
        projectFolder = bs_pathGenerator.bs_getEnvDetails()['projectFolder']
        basePath = '$BSW_PROD_SERVER/' + projectFolder + '/01_pre/'
        if str(eachRef.unresolvedPath()).startswith(basePath):
            astDict = dict()
            astDict['node'] = eachRef.refNode.name()
            astDict['path'] = str(eachRef.path)
            astDict['name'] = str(eachRef.path.name)
            if str(eachRef.path.name).split('_')[1] == 'ch':
                charDict[eachRef.refNode.name()] = astDict
            elif str(eachRef.path.name).split('_')[1] == 'pr':
                propDict[eachRef.refNode.name()] = astDict
            elif str(eachRef.path.name).split('_')[1] == 'bg':
                setDict[eachRef.refNode.name()] = astDict
            elif str(eachRef.path.name).split('_')[1] == 'vh':
                vehicleDict[eachRef.refNode.name()] = astDict
    mainDict['char'] = charDict
    mainDict['prop'] = propDict
    mainDict['set'] = setDict
    mainDict['vehicle'] = vehicleDict
    return mainDict


def bs_createReference(filePath, prefixStyle='normal', prefixName='MSH'):
    """
    @ reference file using three different style naming prefix.
    Args:
        filePath (str): full file path.
        prefixStyle (str): prefix type 3 supported (normal, namespace, prefix).
        prefixName (str): prefix name.

    Returns:
            bool.
    """
    if prefixStyle == 'normal':
        pm.createReference(filePath)
        return True
    elif prefixStyle == 'fileName':
        namespace = filePath.split('/')[-1].split('.')[0]
        return pm.createReference(filePath, gl=True, namespace=namespace)
    elif prefixStyle == 'namespace':
        pm.createReference(filePath, namespace=prefixName)
        return True
    elif prefixStyle == 'prefix':
        pm.createReference(filePath, rpr=prefixName)
        return True
    elif prefixStyle == 'withoutNamespace':
        pm.createReference(filePath, namespace=':')
    return False
