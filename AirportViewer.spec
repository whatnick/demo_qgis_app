# -*- mode: python -*-
import os
block_cipher = None
workdir = os.getenv('VIEWER_DIR')
a = Analysis(['qgis_demo.py'],
         pathex=[workdir],
         binaries=None,
         datas=[('c:/OSGeo4W64/apps/qgis/plugins/*.dll','qgis_plugins'),
                ('c:/OSGeo4W64/bin/*.dll','DLLs'),
                ('c:/OSGeo4W64/bin/gdalplugins/*.dll', 'gdalplugins'),
                ('c:/OSGeo4W64/share/proj/*','proj_db'),
                (os.path.join(workdir,'testdata/*'),'testdata'),
                (os.path.join(workdir,'graphics/*'),'graphics'),],
         hiddenimports=['PyQt5.QtSql','PyQt5.QtNetwork','PyQt5.QtXml','PyQt5.Qsci','PyQt5.QtPrintSupport'],
         hookspath=None,
         runtime_hooks=None,
         excludes=None,
         win_no_prefer_redirects=None,
         win_private_assemblies=None,
         cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
         cipher=block_cipher)
exe = EXE(pyz,
      a.scripts,
      a.binaries,
      a.zipfiles,
      a.datas,
      name='Airport Viewer',
      debug=False,
      strip=None,
      upx=True,
      icon='graphics/airports.ico',
      console=False)