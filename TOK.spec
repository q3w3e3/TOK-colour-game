# -*- mode: python -*-
a = Analysis(['TOK.py'],
             pathex=['/Users/jackwoodrow/GitHub/TOK-colour-game'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='TOK',
          debug=False,
          strip=None,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='TOK')
app = BUNDLE(coll,
             name='TOK.app',
             icon=None)
