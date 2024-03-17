import pygame as pg
import random
import time

size=[1000,1000]
positions=[[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]

class Screen():
    def __init__(self):
        pg.init()
        self.screen=pg.display.set_mode((size[0],size[1]))
        
        self.random_pick()
        running=True
        while running==True:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    running=False
            self.screen.fill((0,0,0))
            self.list_display()
            self.list_update()
            time.sleep(0.1)
            pg.display.update()  
            
    def random_pick(self):
        self.screen_size=200
        self.bit_size=size[0]/self.screen_size
        self.bytes_list=[[0] * self.screen_size for _ in range(self.screen_size)]
        for i in range(30000):
            self.bytes_list[random.randrange(self.screen_size)][random.randrange(self.screen_size)]=1
   
    def list_display(self):
        for i in range(self.screen_size):
            for j in range(self.screen_size):
                if self.bytes_list[i][j]==1:
                    pg.draw.rect(self.screen,(255,255,255),(i*self.bit_size,j*self.bit_size,self.bit_size,self.bit_size))
                    
    def list_update(self):
        next_gen=[[0] * self.screen_size for _ in range(self.screen_size)]
        for i in range(self.screen_size):
            for j in range(self.screen_size):
                count=0
                for position in positions:
                    if i+position[0]>=0 and i+position[0]<self.screen_size and j+position[1]>=0 and j+position[1]<self.screen_size:
                        if self.bytes_list[i+position[0]][j+position[1]]:
                            count+=1
                if self.bytes_list[i][j]==1 and (count==2 or count==3):
                    next_gen[i][j]=1
                if self.bytes_list[i][j]==0 and count==3:
                    next_gen[i][j]=1
        self.bytes_list=next_gen           
Screen()