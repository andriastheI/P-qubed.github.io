'''
NAME
    drawable

DESCRIPTION
    This module provides classes for a simple Tower Defense demo game.
          
PROVIDES
    Drawable
    BG_Tile
    Tickable
    Enemy
    Defender
    Projectile
    
Dependencies
    tkinter
    
Created by: Ted Wendt
Created on: March 24, 2024
Modified by: Andrias Zelele
Modified on: 
'''

import tkinter as tk
from Defender import Defender
from BG_Tile import BG_Tile
from Enemy import Enemy
import random
if __name__ == '__main__':

    
    def pp(t):
        '''
        Function used to force enemies to follow the road.
        '''
        # Follow the center of the parameterized path.
        # (  0,  90) -> (150,  90)     150 units
        # (150,  90) -> (150, 510)     420 units
        # (150, 510) -> (270, 510)     120 units
        # (270, 510) -> (270, 150)     360 units
        # (270, 150) -> (450, 150)     180 units
        # (450, 150) -> (450, 390)     240 units
        # (450, 390) -> (600, 390)     150 units
        path = [(0,90), (150,90), (150,510), (270,510), (270,150), (450,150), (450,390), (600,390)]
        x = 0
        y = 0
        
        current_node = 0
        dist_travelled = 0
        this_point = path[current_node]
        next_point = path[current_node + 1]
        next_dist = max(abs(next_point[0] - this_point[0]), abs(next_point[1] - this_point[1]))
        while current_node < len(path) - 1 and t > next_dist:
            current_node += 1
            dist_travelled += next_dist
            t -= next_dist
            this_point = path[current_node]
            next_point = path[current_node + 1]
            next_dist = max(abs(next_point[0] - this_point[0]), abs(next_point[1] - this_point[1]))
        
        # If the enemy hasn't completed the path, calculate their new position.
        # Otherwise, return the default position.
        if current_node < len(path) - 1:
            if next_point[0] == this_point[0]:
                # X coordinate has not changed.  Character is not moving horizontally
                x = this_point[0]
            else:
                # X coordinate has changed.  Character is moving horizontally.
                # Determine if they're moving left or right. 
                direction = (next_point[0] - this_point[0]) / abs((next_point[0] - this_point[0]))
                x = path[current_node][0] + direction * t
            if next_point[1] == this_point[1]:
                # Y coordinate has not changed.  Character is not moving vertically
                y = this_point[1]
            else:
                # Y coordinate has changed.  Character is moving vertically.
                # Determine if they're moving up or down. 
                direction = (next_point[1] - this_point[1]) / abs((next_point[1] - this_point[1]))
                y = path[current_node][1] + direction * t
    
        else:
            x = 0
            y = 90 
        
        return (x,y)
    
    wn = tk.Tk()
    wn.geometry("600x600")
    wn.title("Tower Defense")
    
    enemies = []
    enemies.append(Enemy(hp = 40, speed = 8))
    
    defenders = []
    # Create a defender in row 7 column 3
    d1 = Defender()
    d1.moveTo(3*BG_Tile._base_size, 7*BG_Tile._base_size)
    # Create a defender in row 2 column 1
    d2 = Defender()
    d2.moveTo(1*BG_Tile._base_size, 2*BG_Tile._base_size)
    # Create a defender in row 3 column 6
    d3 = Defender()
    d3.moveTo(6*BG_Tile._base_size, 3*BG_Tile._base_size)
    # Create a defender in row 4 column 3
    d4 = Defender()
    d4.moveTo(3*BG_Tile._base_size, 4*BG_Tile._base_size)
    
    defenders.append(d1)
    defenders.append(d2)
    defenders.append(d3)
    defenders.append(d4)
    
    # Empty collection to store projectiles when they're 'in flight'
    projectiles = []

    step = 1

    names = ["BlueBoy", "BlueGirl", "GreyHat"]
    def update():
        global step, global_time, running
        if running:
            global_time += 1
            
            # Spawn a new enemy every 50 tics
            if global_time > 50:
                global_time = 0
                enemies.append(Enemy(character=random.choice(names)))
                
            # Update the positions of all of the enemies
            for elem in enemies:
                elem.tic(step)
                t = elem.get_count()
                
                # If an enemy reaches the end of the path, remove them.
                if t > 1620:
                    enemies.remove(elem)
                    elem.unrender(cvsMain)
                else:
                    x,y = pp(t)
                    elem.moveTo(x,y)
                    elem.render(cvsMain)
            
            # Update the actions of all of the defenders
            for elem in defenders:
                elem.tic(step)
                
                closest = None
                if elem.can_fire():
                    # Find a target.  We will choose the target who is in range AND farthest along the path.
                    for enemy in enemies:
                        if elem.dist_to_target(enemy) < elem.get_range():
                            if closest == None or enemy.get_count() > closest.get_count():
                                closest = enemy
                                
                    if closest is not None:
                        # Create a projectile
                        p = elem.fire(closest)
                        projectiles.append(p)
                elem.render(cvsMain)
            
            # Update the locations of all of the projectiles
            for elem in projectiles:
                elem.tic(step)
                
                # If a projectile is within 10 pixels of the target, count it as a 'hit'
                if elem.dist_to_target() < 10:
                    elem.hit_target()
                    projectiles.remove(elem)
                    elem.unrender(cvsMain)
                    
                    # If the projecile hit kills teh target, remove it from the screen.
                    if elem.get_target().get_hp() <= 0 and elem.get_target() in enemies:
                        enemies.remove(elem.get_target())
                        elem.get_target().unrender(cvsMain)
                else:
                    elem.render(cvsMain)
            
            # Redraw after 40 ms.  (i.e. 200 frames per second.)
            wn.after(40, update)
        

    # Create the main canvas
    cvsMain = tk.Canvas(wn, bg = 'white', width = 600, height = 600)
    cvsMain.grid(row = 0, column=0)
    
    # "Map" for where the path should run.
    data = [[ "Empty",  "Empty",   "Empty",  "Empty",   "Empty",  "Empty",  "Empty",   "Empty",  "Empty",  "Empty"],
            ["Road-H", "Road-H", "Road-L4",  "Empty",   "Empty",  "Empty",  "Empty",   "Empty",  "Empty",  "Empty"],
            [ "Empty",  "Empty",  "Road-V",  "Empty", "Road-L3", "Road-H", "Road-H", "Road-L4",  "Empty",  "Empty"],
            [ "Empty",  "Empty",  "Road-V",  "Empty",  "Road-V",  "Empty",  "Empty",  "Road-V",  "Empty",  "Empty"],
            [ "Empty",  "Empty",  "Road-V",  "Empty",  "Road-V",  "Empty",  "Empty",  "Road-V",  "Empty",  "Empty"],
            [ "Empty",  "Empty",  "Road-V",  "Empty",  "Road-V",  "Empty",  "Empty",  "Road-V",  "Empty",  "Empty"],
            [ "Building",  "Empty",  "Road-V",  "Empty",  "Road-V",  "Empty",  "Empty", "Road-L2", "Road-H", "Road-H"],
            [ "Empty",  "Empty",  "Road-V",  "Empty",  "Road-V",  "Empty",  "Empty",   "Empty",  "Empty",  "Empty"],
            [ "Empty",  "Empty", "Road-L2", "Road-H", "Road-L1",  "Empty",  "Building",   "Empty",  "Empty",  "Empty"],
            [ "Empty",  "Empty",   "Empty",  "Empty",   "Empty",  "Empty",  "Empty",   "Empty",  "Building",  "Empty"]]
    
    
    # Create each of the required background elements.
    draws = []
    for i in range(len(data)):
        temp = []
        for j in range(len(data[i])):
            tile_type = BG_Tile._types[data[i][j]]
            temp.append(BG_Tile(BG_Tile._base_size*j, BG_Tile._base_size*i, tile_type))
        draws.append(temp)
    
    # Draw each of the background elements.
    for row in draws:
        for elem in row:
            elem.render(cvsMain)    
    global_time = 0
    running = True
    
    # Trigger the game to start when the user clicks the mouse button.
    cvsMain.bind("<Button>", lambda x: update())
    wn.mainloop()