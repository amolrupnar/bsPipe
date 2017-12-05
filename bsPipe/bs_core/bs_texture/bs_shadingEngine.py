import pymel.core as pm
import json

from bsPipe.bs_ui import bs_qui
from bsPipe.bs_core import bs_mayaFile

reload(bs_qui)
reload(bs_mayaFile)


def bs_exportShaders(shaderExpPath, jsonPath):
    """
    @ export shaders on shader exp path.
    @ export shader applied details on json file.
    Args:
        shaderExpPath (str): path where shader will be exported.
        jsonPath (str): path where shader information will store.

    Returns:
            exported Shader path. (str)
    """
    # get all shading engines.
    allShdEngines = pm.ls(type='shadingEngine')
    allShdEng = list()
    [allShdEng.append(each.name()) for each in allShdEngines]
    filtShdEng = list(set(allShdEng) - {'initialParticleSE', 'initialShadingGroup'})
    # convert shading engines in PyNode.
    shadingEngines = list()
    [shadingEngines.append(pm.PyNode(each)) for each in filtShdEng]
    # get geometries where shading engine is applied.
    shadingInformation = dict()
    for each in shadingEngines:
        appliedMesh = list()
        [appliedMesh.append(x.name()) for x in each.listConnections(type='mesh')]
        shadingInformation[each.name()] = appliedMesh
    # export applied data in json file.
    with open(jsonPath, 'w') as outfile:
        json.dump(shadingInformation, outfile, indent=4)
    # select and export all shading engines.
    pm.select(shadingInformation.keys(), r=True, ne=True)
    pm.cmds.file(shaderExpPath, op="v=0;", typ='mayaAscii', pr=False, es=True)
    bs_qui.bs_displayMessage('success', 'Shaders exported successful')


def bs_getShaders(obj):
    """
    @ get shader of object.
    Args:
        obj (str): object with shader.

    Returns:
            shader.
    """
    pm.select(obj)
    pm.windows.hyperShade(shaderNetworksSelectMaterialNodes=True)
    return pm.ls(sl=True)  # Returns all shaders associated with the object (shape, face etc)


def bs_getShadersPerFace(geoShape):
    """
    @ get per face shader of passed geometry shape.
    Args:
        geoShape (str): geometry shape name.

    Returns:
            perFaceShader information (dict).
    """
    perFaceShaders = {}
    for f in range(pm.modeling.polyEvaluate(geoShape, f=True)):
        face = geoShape + '.f[' + str(f) + ']'
        try:
            shader = bs_getShaders(face)
            perFaceShaders[face] = shader
        except RuntimeError:
            print 'Error: could not fetch shader for ' + face

    return perFaceShaders


def bs_recordShaderAssignment(shape, shaders):
    print type(shaders)
    # TODO: shader assignment per face.
    if str(type(shaders)) == '<type \'list\'>':
        print 'To do: Store assignment of shader per shape'
    if str(type(shaders)) == '<type \'dict\' > ':
        print 'To do: Store assignment of shaders per face'
        print shape


def bs_importShaders(shaderPath, jsonPath):
    """
    @ import shaders and apply on geometries.
    @ apply data read from json file.
    Args:
        shaderPath (str): shader path where shaders are stored.
        jsonPath (str): json path where all information about shaders is stored.

    Returns:
            bool.
    """
    # import shaders.
    bs_mayaFile.bs_importFile(shaderPath)
    # read shader data from json file.
    with open(jsonPath) as json_data:
        shaderData = json.load(json_data)
        print shaderData
    # apply shaders.
    for each in shaderData.keys():
        # for x in shaderData[each]:
        # pm.select(shaderData[each][x],r=True)
        pm.select(shaderData[each], r=True)
        pm.windows.hyperShade(a=each)
    bs_qui.bs_displayMessage('success', 'shader import success.')
    return True
