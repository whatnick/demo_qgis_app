REM --SET VIEWER_DIR to working directory--
REM --Run from Osgeo4W Shell--
@echo off
python3 -m pip install setuptools pyinstaller
set PATH=C:\OSGeo4W64\apps\qgis\bin;%PATH%
set PYTHONPATH=C:\OSGeo4W64\bin;C:\OSGeo4W64\apps\qgis\python;C:\OSGeo4W64\apps\qgis\python\plugins;C:\OSGeo4W64\apps\Python37\lib\site-packages;
pyinstaller --clean -F -d all AirportViewer.spec
