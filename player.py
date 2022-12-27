# player program

import pygame as py
import math
import numpy as np
import time

#colors
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (235, 25, 25)
Green = (25, 235, 25)
Blue = (25, 25, 235)
Yellow = (255, 255, 0)
Steel = (176, 196, 222)

# game surface
Window = py.display.set_mode(1000, 380)

# variables
player_pos = (0, 0) #temporary

# player image
player_im = py.image.load("sprites/Cannon.png")
Player = py.draw.circle(Window, False, player_pos, player_im)