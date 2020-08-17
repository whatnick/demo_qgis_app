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
)
from qgis.gui import (
    QgsMapCanvas,
    QgsVertexMarker,
    QgsMapCanvasItem,
    QgsRubberBand,
)

# Supply the path to the qgis install location
# This is supplied by the environment variable
# Invoke this script using "C:\OSGeo4W64\bin\python-qgis"
# QgsApplication.setPrefixPath("C:\\OSGeo4W64\\apps\\qgis", True)

# Create a reference to the QgsApplication.
# Setting the second argument to True enables the GUI.  We need
# this since this is a custom application.
qgs = QgsApplication([], True)

# load providers
qgs.initQgis()

# Write your code here to load some layers, use processing
# algorithms, etc.
canvas = QgsMapCanvas()
canvas.setWindowTitle("Airport Viewer")
canvas.show()

vlayer = QgsVectorLayer('testdata/Australia_Airports.geojson', "Airports layer", "ogr")
if not vlayer.isValid():
    print("Vector layer failed to load!")

urlWithParams = 'type=xyz&url=https://a.tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=19&zmin=0&crs=EPSG3857'
rlayer = QgsRasterLayer(urlWithParams, 'OpenStreetMap', 'wms')  

if rlayer.isValid():
    QgsProject.instance().addMapLayer(rlayer)
else:
    print('Raster layer failed to load!')

# add layer to the registry
QgsProject.instance().addMapLayer(rlayer)
QgsProject.instance().addMapLayer(vlayer)

# set extent to the extent of our layer
canvas.setExtent(vlayer.extent())

# set the map canvas layer set
canvas.setLayers([vlayer,rlayer])

qgs.exec_()

# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()