import tkinter
import random
import sys
from tkinter import ttk
from tkinter import *
from tkinter import font
import tkinter as tk
import tkinter.ttk as ttk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):