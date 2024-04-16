from Tickable import Tickable
from PIL import Image, ImageTk
from csv import excel
from Drawable import Drawable
import tkinter as tk
import time
class Enemy(Tickable):
    '''
    classdocs
    
    This class provides the basic framework for enemies
    '''    
    enemy_image = None 
    @classmethod
    def _load_image(cls,filename):
        try:
            temp = Image.open(f"../img/{filename}.png")
            Enemy.enemy_image = temp  
        except FileNotFoundError:
            print(f"File '{filename}.png' is not found in the directory 'img'")
        except:
            print("Error occurred loading the image")
        return None
    
    def __init__(self, left = 0, top = 0, hp = 20, speed = 4, character = "BlueBoy", width = 0 , height = 0):
        super().__init__(left , top)
        self._bound = {"left":left , "top": top}
        if Enemy.enemy_image == None:
            Enemy._load_image("ActionF")

        self._face = character
        self._image = []
        self._character = {"right":[],"front":[],"back":[]}
        self._character2 = {"right":[],"front":[],"back":[]}
        self._character3 = {"right":[],"front":[],"back":[]}
        for i in range(3):
            #front
            temp = Enemy.enemy_image.crop((6 + (i * 76), 12, 66 + (i * 76), 112))
            tem = Enemy.enemy_image.crop((475 + (i * 76), 12, 554 + (i * 76), 112))
            te = Enemy.enemy_image.crop((241 + (i * 76), 447, 300 + (i * 76), 541))
            # temp = Enemy.enemy_image.crop((27+(i*130),35,116+(i*130),125))
            #right
            temp2 = Enemy.enemy_image.crop((6 + (i * 76), 230, 66 + (i*76), 325))
            tem2 = Enemy.enemy_image.crop((475 + (i * 76), 230, 554 + (i * 76), 325))
            te2 = Enemy.enemy_image.crop((241 + (i * 76), 661, 300 + (i * 76), 755))
            #back
            temp3 = Enemy.enemy_image.crop((6 + (i * 76), 338, 66 + (i * 76), 434))
            tem3 = Enemy.enemy_image.crop((475 + (i * 76), 338, 554 + (i * 76), 434))
            te3 = Enemy.enemy_image.crop((241 + (i * 76), 769, 300 + (i * 76), 863))

            resized_image = temp.resize((30, 30))
            resized_image2 = temp2.resize((30, 30))
            resized_image3 = temp3.resize((30, 30))

            resize_image = tem.resize((30, 30))
            resize_image2 = tem2.resize((30, 30))
            resize_image3 = tem3.resize((30, 30))

            resiz_image = te.resize((30, 30))
            resiz_image2 = te2.resize((30, 30))
            resiz_image3 = te3.resize((30, 30))
            
            self._character["front"].append(ImageTk.PhotoImage(resized_image))
            self._character["right"].append(ImageTk.PhotoImage(resized_image2))
            self._character["back"].append(ImageTk.PhotoImage(resized_image3))

            self._character2["front"].append(ImageTk.PhotoImage(resize_image))
            self._character2["right"].append(ImageTk.PhotoImage(resize_image2))
            self._character2["back"].append(ImageTk.PhotoImage(resize_image3))

            self._character3["front"].append(ImageTk.PhotoImage(resiz_image))
            self._character3["right"].append(ImageTk.PhotoImage(resiz_image2))
            self._character3["back"].append(ImageTk.PhotoImage(resiz_image3))

        self._image.append(self._character)
        self._image.append(self._character2)
        self._image.append(self._character3)

        self._hp = hp
        self._speed = speed
        self._currentImage = 0
        self._interval = 0.1
        self._last_frame_time = time.time()
        self._current_frame = 0
        self._direction = "right"

    def _getframe(self):
        current_time = time.time()
        elapsed_time = current_time - self._last_frame_time
        if elapsed_time > self._interval:
            self._last_frame_time = current_time
            self._current_frame = (self._current_frame + 1) % len(self._image[0])  # Loop back to the first image if at the end
        return self._current_frame

    def getDirection(self):
        return self._direction
    def setDirection(self, direction):
        self._direction = direction
    def moveTo(self, newLeft, newTop):


        Current_cord = self.getCoords()

        if newLeft >= Current_cord[0] and newTop == Current_cord[1]:
            self.setDirection("right")
        elif newLeft == Current_cord[0] and newTop >= Current_cord[1]:
            self.setDirection("front")
        elif newLeft == Current_cord[0] and newTop <= Current_cord[1]:
            self.setDirection("back")

        self._left = newLeft
        self._top = newTop


    def render(self, cvs):
        frame = self._getframe()
        direction = self.getDirection()

        self.unrender(cvs)
        t = self._top - 25
        L = self._left - 17

        index = 0
        if self._face == "BlueGirl":
            index = 1
        if self._face == "GreyHat":
            index = 2

        if self._image is not None:
            self._drawings.append(cvs.create_image(self._bound["left"]+L, self._bound["top"]+t, image=self._image[index][direction][frame], anchor = "nw"))


    # def render(self, cvs):
    #     self.unrender(cvs)
    #     t = self._top
    #     L = self._left
    #     s = self._hp
    #     if self._image is not None:
    #         self.render(cvs)
    #     else:
    #         self._drawings.append(cvs.create_oval(L - s/2, t - s/2, L + s/2, t + s/2, fill='red'))
    #         self._drawings.append(cvs.create_text(L, t, text = f"{self._hp}"))
    #

    def take_damage(self, amt):
        self._hp -= amt
        
    def get_hp(self):
        return self._hp
    
    def tic(self, step = 1):
        super().tic(step * self._speed)
