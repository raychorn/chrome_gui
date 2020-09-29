import os
import sys

if (__name__ == '__main__'):
    py_version = float(sys.version_info.major)+(float(sys.version_info.minor)/10)+(float(sys.version_info.micro)/100)
    if (py_version < 3.9):
        print('ERROR: Requires Python 3.9.x rather than {}. Please use the correct Python version.'.format(py_version))
    
    # minimal Launcher for Web-based systems
    import webbrowser 
    webbrowser.open('http://127.0.0.1:8888') 
