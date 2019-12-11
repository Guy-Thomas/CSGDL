# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CSGDLDialog
                                 A QGIS plugin
 This Plugin will download the features of the currently selected ArcGIS Map Server Layer. the features to be downloaded are those that are within the current active extent of the map canvass. The features will be downloaded as a json file and stored int he current projects directory in a "/jsonDL" folder.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-11-01
        git sha              : $Format:%H$
        copyright            : (C) 2018 by Guy Thomas
        email                : guyrm.thomas13@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt5 import uic
from PyQt5 import QtWidgets

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'csgdl_dialog_base.ui'))


class CSGDLDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(CSGDLDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
