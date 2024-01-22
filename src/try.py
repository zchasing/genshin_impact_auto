qt_versions = [
    ["6", "PyQt6"],
    ["side6", "PySide6"],
]
qt_version = 'side6'
qt_module = 'PySide6'
for qt_version, qt_module in qt_versions:
    qt_is_installed = True
    break
else:
    qt_is_installed = False
    qt_version = None

print(qt_is_installed)