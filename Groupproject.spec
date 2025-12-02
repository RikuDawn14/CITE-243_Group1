# -*- mode: python ; coding: utf-8 -*-
import sys
from PyInstaller.utils.hooks import collect_all, collect_submodules
from PyInstaller.building.build_main import Analysis, PYZ, EXE

# Collect PySide6 binaries/datas/hiddenimports
binaries, datas, hiddenimports = collect_all("PySide6")

# Add your theme file
datas += [('steampunk_theme.py', '.')]

# Add your modules folder manually (no Tree in PyInstaller 6)
datas += [
    ('modules/port_scanner.py', 'modules'),
    ('modules/vuln_scanner.py', 'modules'),
    ('modules/Website_Scanner.py', 'modules'),
    ('modules/Vulnerabilitiy_Recommendations.py', 'modules')
]

hiddenimports += [
    'modules.port_scanner',
    'modules.vuln_scanner',
    'modules.Website_Scanner',
    'modules.Vulnerabilitiy_Recommendations'
]

block_cipher = None

a = Analysis(
    ['Groupproject.py'],
    pathex=['.'],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='Groupproject',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    exclude_binaries=False,
    onefile=True,
)
