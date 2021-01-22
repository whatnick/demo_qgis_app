# Sample Standalone QGIS App for windows
- This application shows how to build a custom windows application using QGIS as a library
- It is very bare bones and displays
  - Load OSM Maptiles using an XYZ Layer
  - Load static ecw raster data for Canberra 100K mapsheet form a hardcoded path
  - Load static vector data for Australian airports from a hardcoded path
- Launch the application from OSGeo4W CLI or standard cli using `C:\OSGeo4W64\bin\python-qgis qgis_demo.py`

## Developer Setup
- Launch VSCode and start a new python project
- Select Python3.7 that ships with Osgeo4W64 as the interpreter

![Developer Setup](doc/vscode_qgis.png)


## Packaging executable for Windows
[PyInstaller](https://www.pyinstaller.org/) is recommended for folder / single file based distribution of the QGIS application.
There is a nice tutorial / answer on [StackOverflow](https://gis.stackexchange.com/a/178615). This approach is included here for
distribution of the application. It involves 2 steps:
- Detecting the mode in which PyInstaller is running and setting paths accordingly
- A spec file to cleanly setup options to pack the binary

To get the packaging tooling install pyinstaller via pip into the OSGeo4W python 3.7 environment ( current as of 28-09-2020). Python3-pip must be installed as a package in the osgeo4w setup. It is safer to pack a heavier directory based version of the
application to avoid possible DLL hell due to different versions of QGIS being installed on the user machine compared to the
developers. Install pyinstaller from PyPI, `python3 -m pip install setuptools pyinstaller` should work on most platforms.

## Sample Data Attribution
- Sample airport data is obtained from [data.gov.au](https://data.gov.au/data/dataset/f1d9414d-7688-4289-9a63-d9e70036f07a)
- Sample Canberra Map sheet is obtained from [data.gov.au](https://data.gov.au/dataset/ds-ga-a05f7892-eaaf-7506-e044-00144fdd4fa6/distribution/dist-ga-a05f7892-eaaf-7506-e044-00144fdd4fa6-2/details?q=Ecw)

## Sample Code Attribution
- XYZ Raster Layer Sample from [GIS StackExchange](https://gis.stackexchange.com/a/315484)
- Vector Layer Sample from [PyQGIS Cookbook](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/loadlayer.html#vector-layers)

![Application Screenshot](doc/airport_show.png)