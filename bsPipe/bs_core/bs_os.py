import math
import os
import platform
import subprocess
import time
import getpass


def bs_getFileSize(filePath):
    """
    @ get file size.
    Args:
        filePath (str): file path.

    Returns:
            file size.
    """
    size_bytes = os.stat(filePath).st_size
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def bs_openDirInExplorer(path):
    """
    @ open path in os explorer.
    Args:
        path (str): path

    Returns:
            None.
    """
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


def bs_getFileDateTime(path):
    """
    @ get last modified date and time.
    Args:
        path (str): file path.

    Returns:
            date and time (str).
    """
    # get Date And Time.
    sDate = time.ctime(os.path.getmtime(path)).split(' ')
    fDate = sDate[2] + ' ' + sDate[1] + ' ' + sDate[4] + ' | ' + sDate[3]
    return fDate


def bs_getComputerName():
    """
    @ string identifying the currently active system user as name@node
    Returns:
            system Name (str).
    """
    return "%s@%s" % (getpass.getuser(), platform.node())


def bs_getFileOwner(path):
    """
    @ get file owner name
    Args:
        path (str): get file owner name.

    Returns:
            file owner name.
    """
    # TODO: get file owner name once server installation is done.
    if path:
        return 'NULL'
    else:
        return 'NULL'
