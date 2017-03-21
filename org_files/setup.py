import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
#build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}
build_exe_options= {"packages":["os"]}


# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "File Organizator",
        version = "0.1",
        description = "Simple File Organizator made with python 3" ,
        options = {"build_exe": build_exe_options},
        executables = [Executable("File_Organizator.py", base=base)])






#http://cx-freeze.readthedocs.io/en/latest/distutils.html#cx-freeze-executable
