import tkinter as tk
import random
from tkinter import ttk
from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
import time
import sys

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        master.title("My application")
        master.geometry("600x600")
        self.pack()
        #フォント
        self.strfont=font.Font(size=25)
        self.framefont=font.Font(size=16)

        self.game()



    def one_more(self):
        self.textcomcard.set("")
        self.textyourcard.set("")
        self.textcomcard_sum.set("")
        self.textyourcard_sum.set("")
        self.info.set("")
        self.info2.set("")
        self.cont.destroy()
        self.exit.destroy()
        self.bhit.destroy()
        self.bstand.destroy()
        self.game()




    def battle(self):
        if sum(self.yourcard)>sum(self.comcard):
            self.info.set("あなたの勝ち")
            self.con()
        elif sum(self.yourcard)<sum(self.comcard):
            self.info.set("あなたの負け")
            self.con()
        else:
            self.info.set("引き分け")
            self.con()
    def con(self):
        self.bhit.destroy()
        self.bstand.destroy()
        self.info2.set("続けますか")
        self.cont=tk.Button(self,text="continue",command=self.one_more)
        self.cont.grid(row=3,column=0,padx=(200,50),sticky=tk.W+tk.N)
        self.exit=tk.Button(self,text="exit",command=lambda:root.destroy())
        self.exit.grid(row=3,column=1,sticky=tk.W+tk.N)

    def comturn(self):
        if sum(self.comcard)<=15:
            while True:
                self.comcard.append(random.randint(1,13))
                self.textyourcard.set("{}".format(self.comcard))
                self.textcomcard_sum.set("相手の合計{}".format(sum(self.comcard)))
                if sum(self.comcard)>21:
                    self.info.set("相手がバーストしました")
                    self.con()
                    break
                else:
                    self.battle()
                    break
        else:
            self.battle()

    def update_yourcard(self):
        self.yourcard.append(random.randint(1,13))
        self.textyourcard.set("{}".format(self.yourcard))
        self.textyourcard_sum.set("あなたの合計:{}".format(sum(self.yourcard)))
        if sum(self.yourcard)>21:
            self.info.set("バーストしました")
            #time.sleep(1)
            self.con()

    def game(self):

        #関数in関数
        #ここはオブジェクト指向だと少し楽かも同じ作業だし
        self.yourcard=[]
        self.comcard=[]


        for i in range(2):
            self.yourcard.append(random.randint(1,13))
            self.comcard.append(random.randint(1,13))

        #相手
        self.textcomcard=tk.StringVar()
        self.textcomcard.set("{}".format(self.comcard))
        self.textcomcard_sum=tk.StringVar()
        self.textcomcard_sum.set("相手の合計:{}".format(sum(self.comcard)))

        self.lcomcard=tk.Label(self,font=self.strfont,textvariable=self.textcomcard)
        self.lcomcard.grid(row=0,column=0,columnspan=10,sticky=tk.W+tk.N)
        self.lcomcard_sum=tk.Label(self,font=self.strfont,textvariable=self.textcomcard_sum)
        self.lcomcard_sum.grid(row=0,column=1,sticky=tk.E+tk.N,columnspan=10)
        #中央
        self.info=tk.StringVar()
        self.info.set("hit or stand")
        self.info2=tk.StringVar()
        self.info2.set("")
        self.linfo=tk.Label(self,textvariable=self.info,font=self.framefont)
        self.linfo.grid(row=1,column=0,padx=200,pady=(0,10),columnspan=10,rowspan=1,sticky=tk.W+tk.N)
        self.linfo2=tk.Label(self,textvariable=self.info2,font=self.framefont)
        self.linfo2.grid(row=2,column=0,padx=200,columnspan=10,sticky=tk.W)
        self.bhit=tk.Button(self,text="hit",command=self.update_yourcard)
        self.bhit.grid(row=5,column=0,padx=(200,50),sticky=tk.W+tk.N)
        self.bstand=tk.Button(self,text="stand",command=self.comturn)
        self.bstand.grid(row=5,column=1,sticky=tk.W+tk.N)
        #自分
        self.textyourcard=tk.StringVar()
        self.textyourcard.set("{}".format(self.yourcard))
        self.textyourcard_sum=tk.StringVar()
        self.textyourcard_sum.set("あなたの合計:{}".format(sum(self.yourcard)))

        self.lmycord=tk.Label(self,font=self.strfont,textvariable=self.textyourcard)
        self.lmycord.grid(row=6,column=0,sticky=tk.W+tk.S,columnspan=10)
        self.lmycord_sum=tk.Label(self,font=self.strfont,textvariable=self.textyourcard_sum)
        self.lmycord_sum.grid(row=6,column=1,sticky=tk.E+tk.S,columnspan=10)

        if sum(self.yourcard)>21:
            self.info.set("バーストしました")
            self.con()

#class Destroy:
#    def __init__(self):




root = tk.Tk()
app = Application(master=root)
app.mainloop()
