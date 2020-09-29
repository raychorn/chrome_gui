import tkinter as tk
import pygubu

import os


class HelloWorldApp:

    def __init__(self):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file(os.path.abspath('gui/helloworld.ui'))

        #3: Create the mainwindow
        self.mainwindow = builder.get_object('mainwindow')

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    app = HelloWorldApp()
    app.run()
