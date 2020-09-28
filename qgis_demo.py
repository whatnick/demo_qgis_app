import os
import sys
from qgis.core import (
    QgsVectorLayer,
    QgsRasterLayer,
    QgsPoint,
    QgsPointXY,
    QgsProject,
    QgsGeometry,
    QgsMapRendererJob,
    QgsApplication,
    QgsProviderRegistry,
)
from qgis.gui import (
    QgsMapCanvas,
    QgsVertexMarker,
    QgsMapCanvasItem,
    QgsRubberBand,
)
from PyQt5 import QtGui

# Supply the path to the qgis install location
# This is supplied by the environment variable
# Invoke this script using "C:\OSGeo4W64\bin\python-qgis"
# QgsApplication.setPrefixPath("C:\\OSGeo4W64\\apps\\qgis", True)
APP_ICON = "graphics/airports.ico"


def setup_qgis(qgs_app):
    """ Set QGIS paths based on whether running as a bundled application or not """
    if getattr(sys, "frozen", False):
        print("Running In An Application Bundle")
        bundle_dir = sys._MEIPASS
        qgis_prefix_path = bundle_dir
        qgis_plugin_path = bundle_dir + "\qgis_plugins"
        qgis_proj_dir = bundle_dir + "\proj_db"
        os.environ["PROJ_LIB"] = qgis_proj_dir
        os.environ["TEST_DATA"] = bundle_dir + "/testdata/Australia_Airports.geojson"
        os.environ["APP_ICON"] = os.path.join(bundle_dir, APP_ICON)
    else:
        print("Running In A Normal Python Environment")
        bundle_dir = os.path.dirname(os.path.abspath(__file__))
        qgis_prefix_path = os.getenv("QGIS_PREFIX_PATH")
        qgis_plugin_path = qgis_prefix_path + "\plugins"
    qgs_app.setPrefixPath(qgis_prefix_path, True)
    qgs_app.setPluginPath(qgis_plugin_path)
    qgs_app.initQgis()
    registry = QgsProviderRegistry.instance()
    if not "ogr" in registry.providerList():
        print("ERROR: Missing OGR provider")


# Create a reference to the QgsApplication.
# Setting the second argument to True enables the GUI.  We need
# this since this is a custom application.
qgs = QgsApplication([], True)

# load providers
setup_qgis(qgs)

# setup icon in bundle mode
icon_path = os.getenv("APP_ICON", APP_ICON)
qgs.setWindowIcon(QtGui.QIcon(icon_path))

# Write your code here to load some layers, use processing
# algorithms, etc.
canvas = QgsMapCanvas()
canvas.setWindowTitle("Airport Viewer")
canvas.show()

vlayer = QgsVectorLayer(
    os.getenv("TEST_DATA", "testdata/Australia_Airports.geojson"),
    "Airports layer",
    "ogr",
)
if not vlayer.isValid():
    print("Vector layer failed to load!")

urlWithParams = "type=xyz&url=https://a.tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=19&zmin=0&crs=EPSG3857"
rlayer = QgsRasterLayer(urlWithParams, "OpenStreetMap", "wms")

if rlayer.isValid():
    QgsProject.instance().addMapLayer(rlayer)
else:
    print("Raster layer failed to load!")

# add layer to the registry
QgsProject.instance().addMapLayer(rlayer)
QgsProject.instance().addMapLayer(vlayer)

# set extent to the extent of our layer
canvas.setExtent(vlayer.extent())

# set the map canvas layer set
canvas.setLayers([vlayer, rlayer])

# set canvas icon
canvas.setWindowIcon(QtGui.QIcon(icon_path))

qgs.exec_()

# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()
