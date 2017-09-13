# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\Lukas\\PycharmProjects\\LukasPlatformer'],
             binaries=[],
             datas=[
                ( 'sprites\\enemy\\*.png', 'sprites\\enemy' ),
                ( 'sprites\\player\\p1\\duck\\*.png', 'sprites\\player\\p1\\duck' ),
                ( 'sprites\\player\\p1\\hurt\\*.png', 'sprites\\player\\p1\\hurt' ),
                ( 'sprites\\player\\p1\\idle\\*.png', 'sprites\\player\\p1\\idle' ),
                ( 'sprites\\player\\p1\\jump\\*.png', 'sprites\\player\\p1\\jump' ),
                ( 'sprites\\player\\p1\\walk\\*.png', 'sprites\\player\\p1\\walk' ),
                ( 'sounds\\*.wav', 'sounds' ),
                ( 'backgrounds\\*.png', 'backgrounds' ),
                ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='cafeetje',
          debug=False,
          strip=False,
          upx=True,
          console=True )
