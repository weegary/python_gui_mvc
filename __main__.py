# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 18:08:20 2022

@author: Gary
"""

from gui_model import *
from gui_view import *
from gui_controller import *
import tkinter as tk
from tkinter import ttk

class Application(tk.Tk):
    def __init__(self, master=None):
        super().__init__()
        self.master = master
        self.title('Tkinter MVC Demo')
        model = Model('hello@pythontutorial.net')
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)
        controller = Controller(model, view)
        view.set_controller(controller)

if __name__ == "__main__":
    app=Application()
    app.mainloop()