'''
Created on Feb 14, 2024

@author: twendt
'''

from Project_1.Resource.DeckOfCards import DeckOfCards as DC
from Project_1.Projects.War_Player import WP
import tkinter as tk

class WarGUI(object):
    '''
    classdocs
    '''

    def __init__(self, parent = None):
        '''
        Constructor
        '''
        
        # Game Data
        
        self.__p1Spoils = WP("Player 1 Spoils")
        self.__p2Spoils = WP("Spoils for Player 2 it doesn't matter anyway cause we wont use this")
        self.__deck = DC("deck_of_cards.png")
        self.__player1 = WP("Ghengis", back = self.__deck.backOfCard, parent= parent)
        self.__player2 = WP("Shaka", back = self.__deck.backOfCard, parent= parent)
        self.__winner = None
        
        # GUI Information
        self.__parent = parent
        self.__parent.geometry('885x480')
        self.__parent.configure(background = "red")
        
        ## Add in the frames for player 1 and 2
        self.__player1.getFrame().grid(row = 0, column = 0, padx = 5, pady = 5)
        self.__player2.getFrame().grid(row = 0, column = 2, padx = 5, pady = 5)
        self.__player2.getFrame().config(background = "red")
        
        self.__warZoneFrame = tk.LabelFrame(self.__parent, text = "Battle Field")
        self.__warZoneFrame.grid(row = 0, column = 1, padx = 5, pady = 5)
        self.__warZoneFrame.config(background = "red")
        
        self.__warCanvas = tk.Canvas(self.__warZoneFrame, width = 400, height = 300)
        self.__warCanvas.grid(row = 0, column = 0, padx = 5, pady = 5)
        
        self.__controlFrame = tk.LabelFrame(self.__parent,highlightbackground = "black",  highlightthickness = 2)
        self.__controlFrame.grid(row = 1, column = 1)
        self.__controlFrame.config(background = "red")
        
        self.__flipButton = tk.Button(self.__controlFrame, text = "Flip Card",bg="red4",activebackground="blue",borderwidth = 5, command = self.flipCard)
        self.__flipButton.grid(row = 0, column = 0, padx = 5, pady = 5)
        
        self.__restartButton = tk.Button(self.__controlFrame, text = "New Game",bg="red4",activebackground="blue",borderwidth = 5, command = self.newGame)
        self.__restartButton.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.__Exitbutton = tk.Button(self.__controlFrame, text = "Exit",bg="red4",activebackground="blue",borderwidth = 5, command = self.exit)
        self.__Exitbutton.grid(row = 2, column = 0, padx = 5, pady = 5)
        
        self.newGame()
        
        self.__player1.render()
        self.__player2.render()
    
    def newGame(self):
        self.__deck.reset()
        self.__deck.shuffle()
        self.__player1.emptyCard()
        self.__player2.emptyCard()
        self.__warCanvas.delete(tk.ALL)
        
        while self.__player1.hasCard():
            self.__player1.playCard()
            
        while self.__player2.hasCard():
            self.__player2.playCard()     
 
        # FOr testing only
        
        while self.__deck.hasNext():
            self.__player1.addCard(self.__deck.dealCard())
            self.__player2.addCard(self.__deck.dealCard())
            
        self.__player1.getCanvas().delete("all")
        self.__player2.getCanvas().delete("all")
        
        self.__player1.render()
        self.__player2.render() 
        self.__player1.getCanvas().create_text(100, 170, text = f"{self.__player1.numberCard()} Cards Left!")
        self.__player2.getCanvas().create_text(100, 170, text = f"{self.__player2.numberCard()} Cards Left!")
        self.__flipButton["text"] = "Flip Card"
        self.__flipButton["command"] = self.flipCard
           
    
    def exit(self):
        self.__parent.destroy()
    
    def nothing(self):
        return None 
    
    def render(self):
        self.__player1.render()
        self.__player2.render()
        
        self.__warCanvas.delete(tk.ALL)
        if self.__winner is not None:
            self.__warCanvas.create_text(200, 20, text = f"{self.__winner.getName()} wins!")
        # Now render the spoils
        temp1 = []
        temp2 = []
        while self.__p1Spoils.hasCard():
            temp1.append(self.__p1Spoils.playCard())
            temp2.append(self.__p2Spoils.playCard())
        
        for i in range(len(temp1)):
            if i % 4 == 0:
                temp1[i].draw(self.__warCanvas, 20, 20 + 20*i)
                temp2[i].draw(self.__warCanvas, 300, 20 + 20*i)             
            else:
                self.__deck.backOfCard.draw(self.__warCanvas, 20, 20 + 20*i)
                self.__deck.backOfCard.draw(self.__warCanvas, 300, 20 + 20*i)
        
        for i in range(len(temp1)):
            self.__p1Spoils.addCard(temp1[i])
            self.__p2Spoils.addCard(temp2[i])
        
    def flipCard(self):
        
        if self.__player1.numberCard()==0:
            self.__warCanvas.delete(tk.ALL)
            self.__warCanvas.create_text(200, 20, text = f"{self.__player2.getName()} wins the whole Game!")
            self.__flipButton["text"] = ""
            self.__flipButton["command"] = self.nothing
        elif self.__player2.numberCard()==0:
            self.__warCanvas.delete(tk.ALL)
            self.__warCanvas.create_text(200, 20, text = f"{self.__player1.getName()} wins the whole Game!")
            self.__flipButton["text"] = ""
            self.__flipButton["command"] = self.nothing
        
        if self.__winner is not None:
            while self.__p1Spoils.hasCard():
                self.__winner.addCard(self.__p1Spoils.playCard())
            while self.__p2Spoils.hasCard():
                self.__winner.addCard(self.__p2Spoils.playCard())
                
    # Get a card from each player
        c1 = self.__player1.playCard()
        c2 = self.__player2.playCard()
        
        self.__player1.getCanvas().delete("all")
        self.__player2.getCanvas().delete("all") 
        
        self.__player1.getCanvas().create_text(100, 170, text = f"{self.__player1.numberCard()} Cards Left!")
        self.__player2.getCanvas().create_text(100, 170, text = f"{self.__player2.numberCard()} Cards Left!")
     
        # Put those cards in the spoils
        self.__p1Spoils.addCard(c1)
        self.__p2Spoils.addCard(c2)
        
        # Determine if there is a winner.
        if c1 > c2:
            self.__winner = self.__player1
        elif c1 < c2:
            self.__winner = self.__player2
        else:
            # WAR!!!!!
            L1 = self.__player1.prepareWar()
            L2 = self.__player2.prepareWar()   
            for c in L1:
                self.__p1Spoils.addCard(c)
            for c in L2:
                self.__p2Spoils.addCard(c)
            self.__winner = None
        
        # Tell the cards to draw themselves
        self.render()
    
if __name__ == "__main__":
    win = tk.Tk()
    theWar = WarGUI(parent=win)
    win.mainloop()
        
        
        
        
        