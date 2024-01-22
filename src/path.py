import os
import sys

PATH_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(PATH_ROOT)
PATH_SRC = os.path.join(PATH_ROOT, "src")

if sys.path[0] != PATH_ROOT:
    sys.path.insert(0, PATH_ROOT)
if sys.path[1] != PATH_SRC:
    sys.path.insert(1, PATH_SRC)

PATH_DATA = os.path.join(PATH_ROOT, "data")
PATH_DATA_SETTING = os.path.join(PATH_ROOT, "data\\setting")
PATH_DATA_IMGRES = os.path.join(PATH_ROOT, "data\\imgresource")

# print(PATH_ROOT, PATH_DATA, PATH_SRC, PATH_DATA_SETTING)
# print(sys.path)
