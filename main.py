import os
import sys

from vyperlogix import _utils
from vyperlogix.sockets import checkhosts

launcher_address = 'http://127.0.0.1:8888'

def normalize_port(addr, default=80):
    try:
        ret_val = int(addr.split('://')[-1].split(':')[-1])
    except:
        ret_val = default
    return ret_val

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

if (__name__ == '__main__'):
    py_version = _utils.getVersionFloat() # float(sys.version_info.major)+(float(sys.version_info.minor)/10)+(float(sys.version_info.micro)/100)
    if (py_version < 3.9):
        print('ERROR: Requires Python 3.9.x rather than {}. Please use the correct Python version.'.format(py_version))

    root = tk.Tk()
    app = Application(master=root)
    app.master.title("Hacker's Toolbox v0.1")
    app.master.maxsize(1920, 1080)
    app.master.geometry("800x600+300+300")
    app.mainloop()

    if (0):
        # minimal Launcher for Web-based systems
        __is__ = checkhosts.checkHost(launcher_address.split('://')[-1].split(':')[0], normalize_port(launcher_address), retries=3)
        if (__is__):
            import webbrowser 
            webbrowser.open(launcher_address)
        else:
            import ctypes
            WS_EX_TOPMOST = 0x40000
            ctypes.windll.user32.MessageBoxW(None, u"Cannot connect to the online toolbox api.", u"Hacker's Toolbox Startup Error", WS_EX_TOPMOST)
        
