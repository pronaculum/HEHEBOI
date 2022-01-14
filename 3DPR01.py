import tkinter as tk
import math as mt
import threading
        
class _3dpr:
    def __init__(self):
        self.nob=[[],'',(0,0,0)]
        self.ob=[[-8,-8,-8],[-8,-8,8],[-8,8,-8],[-8,8,8],[8,-8,-8],[8,-8,8],[8,8,-8],[8,8,8]]
        self.menu=tk.Tk()
        self.menu.geometry('960x540')
        self.mp=tk.Label(self.menu,text=self.nob[1])
        self.mp.pack(anchor='center')
        self.menu.bind('<Key>',self.__next__)

    
    def __next__(self,k):
        key=k.keycode
        cnt=0
        if key==65:self.nob[2][0]+=1
        elif key==68:self.nob[2][0]-=1
        elif key==83:self.nob[2][1]+=1
        elif key==87:self.nob[2][1]-=1
        elif cnt==0:key=0
        
        self.nob[0]=[]
        for i in range(26):
            self.nob[0].append([])
            for j in range(48):
                self.nob[0][i].append('■')


        self.ob[0]=[self.ob[0][0]+self.nob[2][0]
        self.ob[0][1]=[self.ob[0][1][0]+self.nob[2][0],self.ob[0][1][1]+self.nob[2][1],self.ob[0][1][2]+self.nob[2][2]]
        self.ob[0][2]=[self.ob[0][2][0]+self.nob[2][0],self.ob[0][2][1]+self.nob[2][1],self.ob[0][2][2]+self.nob[2][2]]
        self.ob[0][3]=[self.ob[0][3][0]+self.nob[2][0],self.ob[0][3][1]+self.nob[2][1],self.ob[0][3][2]+self.nob[2][2]]
        self.ob[0][4]=[self.ob[0][4][0]+self.nob[2][0],self.ob[0][4][1]+self.nob[2][1],self.ob[0][4][2]+self.nob[2][2]]
        self.ob[0][5]=[self.ob[0][5][0]+self.nob[2][0],self.ob[0][5][1]+self.nob[2][1],self.ob[0][5][2]+self.nob[2][2]]
        self.ob[0][6]=[self.ob[0][6][0]+self.nob[2][0],self.ob[0][6][1]+self.nob[2][1],self.ob[0][6][2]+self.nob[2][2]]
        self.ob[0][7]=[self.ob[0][7][0]+self.nob[2][0],self.ob[0][7][1]+self.nob[2][1],self.ob[0][7][2]+self.nob[2][2]]

        self.nob[0][13+round(self.ob[0][1])][24+round(self.ob[0][0])]='①'
        self.nob[0][13+round(self.ob[1][1])][24+round(self.ob[1][0])]='②'
        self.nob[0][13+round(self.ob[2][1])][24+round(self.ob[2][0])]='③'
        self.nob[0][13+round(self.ob[3][1])][24+round(self.ob[3][0])]='④'
        self.nob[0][13+round(self.ob[4][1])][24+round(self.ob[4][0])]='⑤'
        self.nob[0][13+round(self.ob[5][1])][24+round(self.ob[5][0])]='⑥'
        self.nob[0][13+round(self.ob[6][1])][24+round(self.ob[6][0])]='⑦'
        self.nob[0][13+round(self.ob[7][1])][24+round(self.ob[7][0])]='⑧'

        print(self.ob,end='\n\n')
        
        self.nob[1]=''
        for i in range(26):
            for j in range(48):
                self.nob[1]+=self.nob[0][i][j]
            self.nob[1]+='\n'
        self.mp.config(text=self.nob[1])
pj=_3dpr()
