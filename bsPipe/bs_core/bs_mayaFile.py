import pymel.core as pm


def bs_importFile(filePath, namespace=None, fileType='ma'):
    """
    @ import file in the scene using passed parameters.
    Args:
        filePath (str): full file path is must in string.
        namespace (str): namespace for import file.
        fileType (str): there is only two types of files to be import ('ma' or 'mb').

    Returns:
            bool.
    """
    fileTypeFilter = {'ma': 'mayaAscii', 'mb': 'mayaBinary'}
    if namespace:
        pm.importFile(filePath, type=fileTypeFilter[fileType], pr=True, namespace=namespace,
                      mergeNamespacesOnClash=False)
    else:
        pm.importFile(filePath, type=fileTypeFilter[fileType], pr=True, mergeNamespacesOnClash=False)
    return True


def bs_openFile(filePath):
    """
    @ open file
    Args:
        filePath (str): full file path.

    Returns:
            bool
    """
    pm.openFile(filePath, f=True)
    return True
