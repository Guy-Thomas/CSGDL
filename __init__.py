# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CSGDL
                                 A QGIS plugin
 This Plugin will download the features of the currently selected ArcGIS Map Server Layer. the features to be downloaded are those that are within the current active extent of the map canvass. The features will be downloaded as a json file and stored int he current projects directory in a "/jsonDL" folder.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2018-11-01
        copyright            : (C) 2018 by Guy Thomas
        email                : guyrm.thomas13@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CSGDL class from file CSGDL.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .csgdl import CSGDL
    return CSGDL(iface)
