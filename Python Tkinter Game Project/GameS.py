'''
Created on Feb 28, 2024

@author: andri
'''
from BlackJack_GUI import BlackJackG
from Poker_GUI import PokerG
from War_GUI import WarGUI
import tkinter as tk
import random
'''
description: 

this is a main window that will execute all the games in one option window.
it is simple 
it just contains the games in a button option you click and it will open the game
but the down side is that it will destroy the main window making your run it again if you want to choose another game

the things that stands out is the buttons color change while you hover in and out of them 
it just uses two more functions and bind widget to make it. 
'''
def warGame():
    wn.withdraw()
    win = tk.Toplevel(wn)
    theWar = WarGUI(parent=win)
    win.protocol("WM_DELETE_WINDOW", lambda: on_closing(win))
    win.wait_window(win)
    wn.deiconify()

def on_closing(win):
    # Destroy the game window
    win.destroy()
    
def pokerGame():
    wn.withdraw()
    win = tk.Toplevel(wn)
    thePoker = PokerG(parent=win)
    win.protocol("WM_DELETE_WINDOW", lambda: on_closing(win))
    win.wait_window(win)
    wn.deiconify()
    
    
def BlackGame():
    wn.withdraw()
    win = tk.Toplevel(wn)
    theBlack = BlackJackG(parent=win)
    win.protocol("WM_DELETE_WINDOW", lambda: on_closing(win))
    win.wait_window(win)
    wn.deiconify()
    
def exit():
    wn.destroy()
    
def on_enter(e):
    colors=["darkslategray","darkorange", "darkgoldenrod4","chartreuse2"]
    selected_color = random.choice(colors)
    e.widget['background'] = selected_color

def on_leave(e):
    colors=["purple","green", "red","indigo","lightcoral","lightsteelblue3"]
    selected_color = random.choice(colors)
    e.widget['background'] = selected_color  
if __name__ == '__main__':
    wn = tk.Tk()
    wn.title("Fun Games")
    wn.configure(background = "snow4")
    
    queLabel = tk.Label(wn, text="WELCOME, Whoever you are😒!",font=("Consolas", 25 ,"bold"))
    queLabel.config(background = "snow4")
    queLabel.grid(row = 0, column = 0, padx=5, pady = 5)
    op1 = tk.Button(wn, text="Card War⚔️",bg="tan1",activebackground="red4",borderwidth = 5,font=("Consolas", 15,"bold"), command= warGame)
    op1.grid(row = 1, column = 0,padx=5, pady = 5)
    
    op2 = tk.Button(wn, text="Black-Jack🃏",bg="tan1",activebackground="green",borderwidth = 5,font=("Consolas", 15,"bold"), command= BlackGame)
    op2.grid(row = 2, column = 0,padx=5, pady = 5)
    
    op3= tk.Button(wn, text="Card Poker💰",bg="tan1",activebackground="blue",borderwidth = 5,font=("Consolas", 15,"bold"), command= pokerGame)
    op3.grid(row = 3, column = 0,padx=5, pady = 5)
    
    op4= tk.Button(wn, text="Quit🛑",font=("Consolas", 15,"bold"),bg="tan1",activebackground="orange",borderwidth = 5, command= exit)
    op4.grid(row = 4, column = 0,padx=5, pady = 5)
    
    ##############################################
    ##############################################
    #New function called bind, which attaches a function with the cursors placement##
    #<Enter> means when the cursor is in the place where the button occupies, it will run on_enter function
    #<Leave> means where the cursor is not in the button occupied place, it will run on_leave function
    
    op1.bind("<Enter>", on_enter)
    op1.bind("<Leave>", on_leave)
    op2.bind("<Enter>", on_enter)
    op2.bind("<Leave>", on_leave)
    op3.bind("<Enter>", on_enter)
    op3.bind("<Leave>", on_leave)
    op4.bind("<Enter>", on_enter)
    op4.bind("<Leave>", on_leave)
    
    wn.mainloop()

    
    