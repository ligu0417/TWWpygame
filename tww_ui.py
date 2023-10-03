"""
======================================================================
TWW_UI --- 

UI surface of the whole game.
    Author: Zi Liang <liangzid@stu.xjtu.edu.cn>
    Copyright © 2023, ZiLiang, all rights reserved.
    Created:  3 十月 2023
======================================================================
"""

import pygame
from pygame import gfxdraw, freetype

# for HP and MP
class progressBar:
    def __init__(self,
        # the (0,0) represents the left-top corner of the whole canvas.
                 x=0, # left
        y=0, # top
        width=300,
        height=30,
        current_alpha=1.0,
        history_alpha=1.0,
        color_tuple=(0,255,0),
        red=(192, 57, 43),
        value=100.0,
        text=f"HP:",
                 ):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.current_alpha=current_alpha
        self.history_alpha=history_alpha
        self.color_tuple=color_tuple
        self.red=red
        black=(255,255,255)
        self.black=black
        self.value=value
        self.text=text
        
    
    def build(self,screen):
        self.current_alpha=max(0,self.current_alpha)
        current_value=round(self.current_alpha*self.value,2)
        text=f"{self.text}{current_value}/{self.value}"
        gfxdraw.box(screen,(self.x,self.y,
                            int(self.current_alpha*self.width,),
                            self.height),
                    self.color_tuple)
        gfxdraw.box(screen,(self.x+int(self.current_alpha*self.width,)
                            ,self.y,
                            int((self.history_alpha-self.current_alpha)
                                *self.width,),
                            self.height),
                    self.red)

        gfxdraw.rectangle(screen,(self.x,self.y,int(self.width,),
                            self.height),
                    (230, 126, 34))

        ## add text
        font=freetype.Font("./ttfs/code-style.ttf",16)
        font.render_to(screen,
            (self.x+3,self.y+self.height/3),text,self.black)
        
        import time
        time.sleep(0.08) # hack: to show the bloody animation
        self.history_alpha=self.current_alpha
        

