# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['CompareImages.py'],
             pathex=['/Users/dderooy/Projects/image_comparison'],
             binaries=[],
             datas=[],
             hiddenimports=["cv2", "csv", "time", "pyimod03_importers", "pkg_resources", "setuptools", "nt", "os2", "_emx_link", "ce",
             "riscos", "riscospath", "riscosenviron", "msvcrt", "_subprocess", "org", "_sha", "_md5", "_sha256", "_sha512"],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='CompareImages',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='CompareImages')
