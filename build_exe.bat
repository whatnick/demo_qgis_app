@echo off
SET "VIEWER_DIR=%cd%"
python3 -m pip install setuptools pyinstaller
set PATH=C:\OSGeo4W64\apps\qgis\bin;%PATH%
set PYTHONPATH=C:\OSGeo4W64\bin;C:\OSGeo4W64\apps\qgis\python;C:\OSGeo4W64\apps\qgis\python\plugins;C:\OSGeo4W64\apps\Python37\lib\site-packages;
pyinstaller --clean -F -d all AirportViewer.spec
