from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')

py2exe_options = {
    "includes": ["sip"],
    "dll_excludes": ["MSVCP90.dll"],
    "compressed": 1,
    "optimize": 2,
    "ascii": 0,
    "bundle_files": 1,
}

setup(
      name = 'FabonacciClockPy34PyQt5',
      version = '1.0',
      windows = ['main.py',],
      data_files=[("",
                   [r"D:\Python34\Lib\site-packages\PyQt5\libEGL.dll"]),
                  ("platforms",
                   [r"D:\Python34\Lib\site-packages\PyQt5\plugins\platforms\qwindows.dll"])],
      zipfile = None,
      options = {'py2exe': py2exe_options}
      )