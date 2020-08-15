import sys
from qgis.core import (
    QgsVectorLayer,
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

vlayer = QgsVectorLayer('testdata/Leased Federal Airports.gdb', "Airports layer", "ogr")
if not vlayer.isValid():
    print("Layer failed to load!")

# add layer to the registry
QgsProject.instance().addMapLayer(vlayer)

# set extent to the extent of our layer
canvas.setExtent(vlayer.extent())

# set the map canvas layer set
canvas.setLayers([vlayer])

qgs.exec_()

# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()