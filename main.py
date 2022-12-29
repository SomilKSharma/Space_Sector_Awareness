import os
import pygame as pyg
import math
import random


W=(255,255,255)
Bk=(0,0,0)
Rd=(255,0,0)
Gr=(0,255,0)
B=(173,216,230)




class Satellite(pyg.sprite.Sprite):
    """Object to control the satellite"""
    
    
    
    def __init__(self, background):
        
        super().__init__()
        self.background=background
        
        self.image_sat=pyg.image.load("s.png").convert()
        self.image_crash=pyg.image.load("s_crash_.png").convert()
        self.image=self.image_sat
        self.image=self.image.get_rect()
        self.image.set_colorkey(B)
        
        self.x=random.randrange(200,425)
        self.y=random.randrange(60,190)
        self.dx=random.choice([-3,3])
        self.dy=0
        
        self.heading=0
        self.fuel=100
        self.mass=1
        self.distance=0
        
        self.thrust=pyg.mixer.Sound('thrust_audio.ogg')
        self.thrust.set_volume(0.07)
        
        
    def thrusters(self,dx,dy):
        """Fire the Thrusters!!"""
        
        self.dx=self.dx+dx
        self.dy=self.dy+dy
        self.duel=self.fuel-2
        self.thrust.play()
        
    
    def check_keys(self):
        """check if user presses keys"""
        
        keys=pyg.key.get_pressed()
        
            
            