import sys
import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r"C:\Users\Sasha\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Sasha\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6"

includes      = ["tkinter"]
include_files = [r"C:\Users\Sasha\AppData\Local\Programs\Python\Python36-32\DLLs\tcl86t.dll", \
                 r"C:\Users\Sasha\AppData\Local\Programs\Python\Python36-32\DLLs\tk86t.dll",
                 r"C:\Users\Sasha\AppData\Local\Programs\Python\Python36-32\DLLs\sqlite3.dll",
                 r"C:\Users\Sasha\Desktop\DebiaTranslator-master\zoom_logo.jpg"]
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"includes": ["tkinter", "os", "platform"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Devia Translator",
        version = "0.1",
        description = "Devia Translator application!",
        options = {"build_exe": {"includes": includes, "include_files": include_files}},
        executables = [Executable("devia_translator.py", base=base)])
