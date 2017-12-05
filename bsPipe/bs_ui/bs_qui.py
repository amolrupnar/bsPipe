import pymel.core as pm
import maya.cmds as cmds
import maya.OpenMayaUI as omui
import os
from PySide import QtGui
from shiboken import wrapInstance


class bs_undoChunkOpen(object):
    def __init__(self, chunkName=''):
        self._name = chunkName

    def __enter__(self):
        pm.undoInfo(chunkName=self._name, openChunk=True)

    def __exit__(self, *_):
        pm.undoInfo(chunkName=self._name, closeChunk=True)


def bs_mayaMainWindow():
    """
    This is to get the maya window QT pointer.
    :return:
    :rtype:
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtGui.QWidget)


def bs_displayMessage(status, message):
    """
    display message with different color in maya according to status.
    :param status: string
    :param message: string
    :return: message
    """
    # exit if this function run in batch mode.
    if pm.about(batch=True):
        return False
    # Base color    Text Color.
    statusColors = {
        'error': ((255, 40, 20), (0, 0, 0)),
        'warning': ((255, 177, 86), (0, 0, 0)),
        'success': ((140, 230, 140), (0, 0, 0))}
    # commandLine1 will be unique in maya in all cases.
    commandLinePtr = omui.MQtUtil.findControl('commandLine1')
    commandLine = wrapInstance(long(commandLinePtr), QtGui.QWidget)
    # get result Line.
    resultLine = commandLine.findChildren(QtGui.QLineEdit)[0]
    palette = resultLine.palette()
    palette.setBrush(QtGui.QPalette.Base, QtGui.QColor(*statusColors[status][0]))
    palette.setColor(QtGui.QPalette.Text, QtGui.QColor(*statusColors[status][1]))
    resultLine.setPalette(palette)
    resultLine.setText('[ ' + status + ' ] ' + message)
    pm.refresh()


def bs_displayDialogue(status, message, detailMessage=None):
    """
    create qt QMessageBox according to status.
    :param status: string
    :param message: string
    :param detailMessage: string
    :return: None
    """
    # exit if this function run in batch mode.
    if pm.about(batch=True):
        return False
    # set icon according to status mode.
    if status == 'warning':
        statusIcon = QtGui.QMessageBox.Warning
    elif status == 'error':
        statusIcon = QtGui.QMessageBox.Critical
    else:
        statusIcon = QtGui.QMessageBox.NoIcon
    # create QMessageBox.
    msgBox = QtGui.QMessageBox(bs_mayaMainWindow())
    msgBox.setIcon(statusIcon)
    msgBox.setText(status)
    msgBox.setInformativeText(message)
    msgBox.setWindowTitle(status)
    # set additional text.
    if detailMessage:
        msgBox.setDetailedText("The details are as follows:\n" + detailMessage)
    else:
        msgBox.setDetailedText("The details are as follows:")
    msgBox.setStandardButtons(QtGui.QMessageBox.Ok | QtGui.QMessageBox.Cancel)
    msgBox.exec_()


def bs_fillLineEdit(lineEdit, sel=None):
    """
    @ add selection in window line edit.
    Args:
        lineEdit (str): line edit name.
        sel (list): object has to be add in line edit.

    Returns:
            bool.
    """
    if not sel:
        sel = pm.ls(sl=True)
    if not sel:
        bs_displayMessage('error', 'Please select only one object')
        return False
    elif len(sel) > 1:
        bs_displayMessage('error', 'more than one objects selected.')
        return False
    lineEdit.setText(str(sel[0]))
    return True


def bs_fillListInLineEdit(lineEdit, sel=None):
    """
    @ add selection list in line edit.
    Args:
        lineEdit (str): line edit name.
        sel (list): object has to be add in line edit.

    Returns:
            bool.
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if not sel:
        bs_displayMessage('error', 'Please select only one object')
        return False
    lineText = ",".join(sel)
    lineEdit.setText(lineText)
    return True


def bs_extractLineEditList(lineEdit):
    """
    @ extract multiple objects from line edit and return it to list.
    Args:
        lineEdit (str): line edit name.

    Returns:
            objList.
    """
    strObj = lineEdit.text()
    objList = strObj.split(',')
    return objList


def bs_fillListWidget(listWidget, sel=None):
    """
    @ fill item in list widget.
    Args:
        listWidget (str): name of list widget.
        sel (list): item to add in list widget.

    Returns:
            sel.
    """
    if not sel:
        sel = cmds.ls(sl=True)
    if not sel:
        bs_displayMessage('error', 'Please select minimum one object')
        return False
    listWidget.clear()
    listWidget.addItems(sel)
    return sel


def bs_filterListWidget(listWidget, lineEdit, defaultList):
    """
    @ filter QListwidget with QLineedit text.
    Args:
        listWidget (QListWidget): QListWidget.
        lineEdit (QLineedit): QLineedit.
        defaultList (list): default item list.

    Returns:
            None.
    """
    # get keyword for filter.
    searchKey = lineEdit.text()
    if not searchKey:
        listWidget.clear()
        listWidget.addItems(defaultList)
        return True
    listWidget.clear()
    filteredList = list()
    for each in defaultList:
        if each.find(searchKey) != -1 or each.capitalize().find(searchKey) != -1:
            filteredList.append(each)
    listWidget.addItems(filteredList)


def bs_getSelectedItemsFromTabWidgetAndAddInDestLW(tabWidget, charLW, propLW, setLW, vehicleLW, destLW):
    """
    @ get selected Items From asset tab widget,
    @ restrictions for tab widget "tabText" = ['Character', 'Prop', 'Set', 'Vehicle']
    Args:
        tabWidget (QtGui.QTabWidget): tab widget (4 list widget inside the tab widget.)
        charLW (QtGui.QListWidget): character list widget.
        propLW (QtGui.QListWidget): prop list widget.
        setLW (QtGui.QListWidget): set list widget.
        vehicleLW (QtGui.QListWidget): vehicle list widget.
        destLW (QtGui.QListWidget): destination list widget, where we add selected items.

    Returns:
            None.
    """
    # get current tab.
    assetType = tabWidget.tabText(tabWidget.currentIndex())
    # choose list widget according to current tab.
    astType = {'Character': charLW, 'Prop': propLW, 'Set': setLW,
               'Vehicle': vehicleLW}
    # add short prefix to identify asset type.
    typeShort = {'Character': 'ch_', 'Prop': 'pr_', 'Set': 'bg_', 'Vehicle': 'vh_'}
    # get and set selected items from asset tab widget.
    selectedItems = list()
    for each in astType[assetType].selectedItems():
        selectedItems.append(typeShort[assetType] + each.text())
    destLW.addItems(selectedItems)


def bs_removeSelectedItemsFromQLW(listWidget):
    """
    @ remove selected items from QListWidget of same list widget.
    Args:
        listWidget (QtGui.QListWidget): list widget.

    Returns:
            None.
    """
    listItems = listWidget.selectedItems()
    if not listItems:
        return False
    for item in listItems:
        listWidget.takeItem(listWidget.row(item))


def bs_removeSelectedReferenceFromQLW(listWidget):
    """
    @ get selected assets from list widget and remove its reference.
    Args:
        listWidget (QtGui.QListWidget): list widget has a reference node.

    Returns:
            numberOfRemovedReference (int).
    """
    selectedRef = list()
    [selectedRef.append(each.text()) for each in listWidget.selectedItems()]
    for eachRN in selectedRef:
        allRef = pm.listReferences()
        for each in allRef:
            if eachRN == each.refNode.name():
                each.remove()
    return len(selectedRef)


def bs_setSearchIconInLineEdit(myLineEdit, iconPath=None, padding=17):
    """
    @ set search icon in qLineEdit.
    Args:
        myLineEdit (QtGui.QLineEdit): qline edit where search icon need to be place.
        iconPath (str): search icon path.
        padding (int): width of search icon.

    Returns:
            None.
    """
    if not iconPath:
        imageRootPath = os.path.dirname(__file__)
        iconPath = imageRootPath + '/bs_images/bsw_search.png'
    button = QtGui.QToolButton(myLineEdit)
    myLineEdit.setStyleSheet('QLineEdit {padding-left: %dpx; }' % padding)
    button.setIcon(QtGui.QIcon(iconPath))
    button.setStyleSheet('border: 0px; padding: 0px;')


def bs_qListWidgetSelectionChangeUsingCheckBox(selCBox, clearCBox, myListWidget, selMode=True):
    """
    @ qListWidget item select all items or clear all items, using check box state.
    Args:
        selCBox (QCheckBox): select all items check box.
        clearCBox (QCheckBox): clear all selection check box.
        myListWidget (QListWidget): list widget who had all items.
        selMode (bool): set selection mode.

    Returns:
            None.
    """
    # select all items.
    if selMode:
        if selCBox.isChecked():
            clearCBox.setChecked(False)
            for x in range(myListWidget.count()):
                myListWidget.selectAll()
    # clear all selection when if condition getting false.
    else:
        if clearCBox.isChecked():
            selCBox.setChecked(False)
            myListWidget.clearSelection()
