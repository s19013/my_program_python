import tkinter as tk
import tkinter
import random
import sys
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mbox
from tkinter import font
import tkinter.ttk as ttk

win=tk.Tk()
win.geometry("600x600")

#フレーム
comside=tk.LabelFrame(win,bd=2,relief="ridge",text="相手",)
comside.pack(fill="x")
etcside=tk.Frame(win)
etcside.pack(fill="x")
myside=tk.LabelFrame(win,bd=2,relief="ridge",text="あなた",)
myside.pack(fill="x")
#部品
#-----------------------------
#関数
def game():
    yourcard=[]
    comcard=[]
    for i in range(2):
        yourcard.append(random.randint(1,13))
        comcard.append(random.randint(1,13))
    lcomcard=tk.Label(comside,text="{}".format(comcard)).pack(side="left",padx=(100,10))
    lcomcard_sum=tk.Label(comside,text="相手の合計{}".format(sum(comcard))).pack(side="left",padx=10)
#実行
game()
win.mainloop()
