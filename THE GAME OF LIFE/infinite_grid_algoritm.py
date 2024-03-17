import pygame as pg
import random
import time

size=[1000,1000]
positions=[[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]

class Screen():
    def __init__(self):
        pg.init()
        self.screen=pg.display.set_mode((size[0],size[1]))
        self.screen=pg.display.set_mode(size,pg.RESIZABLE)
        
        self.bytes_list=self.random_pick()
        
        running=True
        while running==True:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    running=False
            self.screen.fill((0,0,0))
            self.list_display()
            self.list_update()
            time.sleep(0.4)
            pg.display.update()  
            
    def random_pick(self):
        bytes_list=[]
        i=0
        while i<500:
            byte=[random.randrange(50),random.randrange(50)]
            if byte not in bytes_list:
                bytes_list.append(byte)
                i+=1

            
        return bytes_list
    
    def list_display(self):
        for block in self.bytes_list:
            pg.draw.rect(self.screen,(255,255,255),(block[0]*20,block[1]*20,20,20))
            
    def list_update(self):
        bytes_list_new=[]
        for block in self.bytes_list:
            count=0
            for position in positions:
                found=0
                for block1 in self.bytes_list:
                    if block[0]==block1[0]+position[0] and block[1]==block1[1]+position[1]:
                        found=1
                        count+=1
                if found==0:
                    x=[block[0]+position[0],block[1]+position[1]]
                    count1=0
                    for position1 in positions:
                        for block2 in self.bytes_list:
                            if x[0]==block2[0]+position1[0] and x[1]==block2[1]+position1[1]:
                                count1+=1
                    if count1==3 and x not in bytes_list_new:
                        bytes_list_new.append(x)

            if count==2  or count==3:
                bytes_list_new.append(block) 
        self.bytes_list=bytes_list_new
        
            
            
Screen()