import tkinter as tk
import math as mt
import threading
        
class _3dpr:
    def __init__(self):
        self.nob=[[],'',[0,0]]
        self.ob=[[24,12],[24,12],[24,12],[24,12],[24,12],[24,12],[24,12],[24,12]]
        self.menu=tk.Tk()
        self.menu.geometry('960x540')
        self.mp=tk.Label(self.menu,text=self.nob[1])
        self.mp.pack(anchor='center')
        self.menu.bind('<Key>',self.__next__)

    
    def __next__(self,k):
        key=k.keycode
        cnt=0
        if key==65:self.nob[2][0]+=mt.pi*1/32;cnt+=1
        elif key==68:self.nob[2][0]+=mt.pi*(-1)/32;cnt+=1
        elif key==83:self.nob[2][1]+=mt.pi*1/32;cnt+=1
        elif key==87:self.nob[2][1]+=mt.pi*(-1)/32;cnt+=1
        elif cnt==0:key=0
        
        self.nob[0]=[]
        for i in range(26):
            self.nob[0].append([])
            for j in range(48):
                self.nob[0][i].append('□')

        self.nob[0][round(self.ob[0][1])][round(self.ob[0][0])]='1'
        self.ob[0]=[24+12*mt.sin(self.nob[2][0]+(mt.pi/4)),13+12*mt.sin(self.nob[2][1]+(mt.pi/4))]

        self.nob[0][round(self.ob[1][1])][round(self.ob[1][0])]='2'
        self.ob[1]=[24+12*mt.sin(self.nob[2][0]+(mt.pi/4)),13+12*mt.sin(self.nob[2][1]+(7*mt.pi/4))]

        self.nob[0][round(self.ob[2][1])][round(self.ob[2][0])]='3'
        self.ob[2]=[24+12*mt.sin(self.nob[2][0]+(3*mt.pi/4)),13+12*mt.sin(self.nob[2][1]+(3*mt.pi/4))]

        self.nob[0][round(self.ob[3][1])][round(self.ob[3][0])]='4'
        self.ob[3]=[24+12*mt.sin(self.nob[2][0]+(3*mt.pi/4)),13+12*mt.sin(self.nob[2][1]+(5*mt.pi/4))]



        self.nob[0][round(self.ob[4][1])][round(self.ob[4][0])]='5'
        self.ob[4]=[24+12*mt.sin(self.nob[2][0]+(5*mt.pi/4)),13+12*mt.sin(self.nob[2][1]+(3*mt.pi/4))]

        self.nob[0][round(self.ob[5][1])][round(self.ob[5][0])]='6'
        self.ob[5]=[24+12*mt.sin(self.nob[2][0]+(5*mt.pi/4)),13+12*mt.sin(self.nob[2][1]+(5*mt.pi/4))]

        self.nob[0][round(self.ob[6][1])][round(self.ob[6][0])]='7'
        self.ob[6]=[24+12*mt.sin(self.nob[2][0]+(7*mt.pi/4)),13+12*mt.sin(self.nob[2][1]+(mt.pi/4))]

        self.nob[0][round(self.ob[7][1])][round(self.ob[7][0])]='8'
        self.ob[7]=[24+12*mt.sin(self.nob[2][0]+(7*mt.pi/4)),13+12*mt.sin(self.nob[2][1]+(7*mt.pi/4))]

        self.nob[1]=''
        for i in range(26):
            for j in range(48):
                self.nob[1]+=self.nob[0][i][j]
            self.nob[1]+='\n'
        self.mp.config(text=self.nob[1])
pj=_3dpr()
