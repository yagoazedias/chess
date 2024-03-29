# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

added_files = [
    ( 'constants', 'constants' ),
    ( 'images', 'images' ),
    ( 'models', 'models' ),
    ( 'util', 'util' ),
    ( 'font', 'font' )
]

a = Analysis(['main.py'],
             pathex=['{changeme}/main.py'],
             binaries=[],
             datas=added_files,
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='chess',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
