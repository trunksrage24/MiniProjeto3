# player program

import pygame as py
import sys
import math
import numpy as np
import time

#init py
py.init()

#colors
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (235, 25, 25)
Green = (25, 235, 25)
Blue = (25, 25, 235)
Yellow = (255, 255, 0)
Steel = (176, 196, 222)

# game surface
Window = py.display.set_mode((1000, 380))

# Cannon class
class Cannon:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.image = py.image.load("sprites/Cannon.png")
    
    def aim(self, mouse_x, mouse_y):
        # Set the cannon's velocity based on the mouse position
        self.dx = mouse_x - self.x
        self.dy = mouse_y - self.y
    
    def fire(self):
        # Create a new projectile and set its velocity based on the cannon's velocity
        projectile = Projectile(self.x, self.y)
        projectile.dx = self.dx
        projectile.dy = self.dy
        return projectile

# Projectile class
class Projectile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0
        self.image = py.image.load('projectile.png')
    
    def move(self):
        self.x += self.dx
        self.y += self.dy

# Create an instance of the cannon
cannon = Cannon(100, 100)

# Set up a list to store the projectiles
projectiles = []

# Set the gravity constant
gravity = 0.1

# Set up the walls as rectangles
wall1 = py.Rect(200, 200, 100, 100)
wall2 = py.Rect(400, 400, 100, 100)

# Set score and timer text
font = py.font.Font(None, 36)

# Set the starting score and time
score = 0
time = 60

# Main game loop
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
        # Check for mouse movement
        elif event.type == py.MOUSEMOTION:
            mouse_x, mouse_y = event.pos
            cannon.aim(mouse_x, mouse_y)
        # Check for mouse clicks
        elif event.type == py.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            cannon.aim(mouse_x, mouse_y)
            # Fire a projectile when the mouse is clicked
            projectile = cannon.fire()
            projectiles.append(projectile)

    # Move and check for collisions for each projectile
    for projectile in projectiles:
        # Check for collisions with the walls
        if projectile.rect.colliderect(wall1) or projectile.rect.colliderect(wall2):
            # Increase the score if the projectile hits wall 1
            score += 1
            # Reverse the projectile's velocity if it hits a wall
            projectile.dx *= -1
            projectile.dy *= -1
        
    # Apply gravity to the projectile's motion
    projectile.dy += gravity

    # Move the projectile
    projectile.move()

    # Draw the cannon and projectile
    Window.blit(cannon.image, (cannon.x, cannon.y))
    Window.blit(projectile.image, (projectile.x, projectile.y))

    py.display.flip()

