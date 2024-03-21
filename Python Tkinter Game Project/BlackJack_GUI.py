'''
Created on Feb 25, 2024

@author: Andrias
'''
from DeckOfCards import DeckOfCards as DC
from Gambler import GB
import tkinter as tk
from tkinter.simpledialog import askstring, askinteger
'''

Description: 

This is a Black jack GUI game where a players is allowed 
to choose their name and the amount of money they want to bet against the dealer.
the value of A's in the game will vary depending on the cards given. they will have the value
of 11 if the first two given cards have the sum less than or equal to 10, or it will be 1.

the down side of this game is if have 21 you win the game no matter what. 
you can play the game with 0 money on bet not less. 


the thing that stands out of this game is maybe the money flow is organized and
its simple.

'''
#this is a black jack GUI, managed by BlackJackG class
class BlackJackG(object):
    '''
    classdocs
    '''


    def __init__(self, parent = None):
        '''
        Constructor
        '''
        self.__player = GB(parent= parent)
        self.__handler = GB("50 Cent", parent= parent)
        self.__pile = GB("Pile", status=True, parent= parent)
        self.__deck = DC("deck_of_cards.png")
        self.__callHit = None 
        self.__callStay = None 
        self.value = None
        self.__askbet = 0
        
        #assigning the windows to the object
        self.__parent = parent
        self.__parent.configure(background = "green")
        self.__parent.geometry("760x500")
        
        #ask the player their name and the amount of money they want to change to chips.
        self.__ask = askstring("Name", "What is your name?")
        self.__player.setName(self.__ask)
        self.__askmoney = askinteger("Money", "How much money do you want Change?")
        self.__player.setMoney(self.__askmoney)
        self.__handler.setMoney("None Of your business")

        
        self.__player.getFrame().grid(row = 1, column = 1, padx = 5, pady = 5)
        self.__player.getFrame().config(background = "green")
        
        self.__handler.getFrame().grid(row = 0, column = 1, padx = 5, pady = 5)
        self.__handler.getFrame().config(background = "green")
        self.__pile.getFrame().grid(row = 0, column = 0,rowspan=2, padx = 5, pady = 5)
        self.__pile.getFrame().config(background = "green")
        
        self.__moneyFrame = tk.LabelFrame(self.__parent)
        self.__moneyFrame.grid(row = 1, column = 2,rowspan =2)
        
        self.__moneyleft = tk.Label(self.__moneyFrame, text= f"Balance = ${self.__player.getMoney()}")
        self.__moneyleft.grid(row = 0, column = 0)
        self.__betleft = tk.Label(self.__moneyFrame, text= f"Ante bet= ${self.__askbet}")
        self.__betleft.grid(row = 1, column = 0)
        
        self.__controlFrame = tk.LabelFrame(self.__parent)
        self.__controlFrame.grid(row = 0, column = 2,rowspan =2)
        

        self.__playhit = tk.Button(self.__controlFrame, text = "Play",bg="dark green",activebackground="blue",borderwidth = 5, command= self.Play)
        self.__playhit.grid(row = 0, column = 0, padx = 5, pady = 5)
      
        
        self.__newButton = tk.Button(self.__controlFrame, text = "Exit",bg="dark green",activebackground="blue",borderwidth = 5, command= self.exit)
        self.__newButton.grid(row = 1, column = 0, padx = 5, pady = 5)
    
        
        self.__restartButton = tk.Button(self.__controlFrame, text = "Restart",bg="dark green",activebackground="blue",borderwidth = 5, command= self.newGame)
        self.__restartButton.grid(row = 2, column = 0, padx = 5, pady = 5)
        
        #runs the new game function 
        self.newGame()
        
    
    #used to exit the whole window    
    def exit(self):
        self.__parent.destroy()  
 
    def setHit(self):
        if self.value <21:
            new_card = self.__pile.PlayCard()
            self.__player.addCard(new_card)
            temp = self.__player.get_newValue(new_card)
            self.value += temp  
            self.__player.render()
        if self.value ==21:
            self.__player.addMoney(self.__askbet*2)
            self.__player.getCanvas().create_text(150, 10, text=f"{self.__player.getName()} wins!!!(${self.__player.getMoney()} left)")    
            self.__newButton["text"] = "Exit"
            self.__newButton["command"] = self.exit
            self.__playhit["text"] = "-"
            self.__playhit["command"] = self.Nothing 
        elif self.value > 21:
            self.__player.getCanvas().create_text(150, 10, text=f"{self.__player.getName()} BUST!!!(${self.__player.getMoney()} left)")
            self.__newButton["text"] = "Exit"
            self.__newButton["command"] = self.exit
            self.__playhit["text"] = "-"
            self.__playhit["command"] = self.Nothing 
                    
    def getHit(self):
        return self.__callHit
    
    def Nothing(self):
        return None
        
    def setStay(self):
        self.__newButton["text"] = "Exit"
        self.__newButton["command"] = self.exit
        self.__playhit["text"] = "-"
        self.__playhit["command"] = self.Nothing 
        
        self.__handler.setStatus(False)
        self.__handler.render()
        
        checker = 0
        for cards in self.__handler.getCard():                        
            temp = self.__player.get_newValue(cards)
            checker += temp 
        for card in self.__handler.getCard():
            if card.getFace() == "A" and checker <=11:
                checker+=10
                
        while checker <= 16:
            new_cards = self.__pile.PlayCard()
            self.__handler.addCard(new_cards)
            temp = self.__player.get_newValue(new_cards)
            checker += temp 
            
        self.__handler.render()
        
        if checker > 21:
            self.__player.addMoney(self.__askbet*2)
            self.__handler.getCanvas().create_text(150, 10, text=f"{self.__handler.getName()} BUST!!!")
            self.__player.getCanvas().create_text(150, 10, text=f"{self.__player.getName()} Wins!!!(${self.__player.getMoney()} left)")
        elif checker > 16:
            if self.value >= checker :
                self.__player.addMoney(self.__askbet*2)
                self.__player.getCanvas().create_text(150, 10, text=f"{self.__player.getName()} Wins!!! (${self.__player.getMoney()} left)") 
            elif self.value < checker:
                self.__handler.getCanvas().create_text(150, 10, text=f"{self.__handler.getName()} Wins!!!")
                self.__player.getCanvas().create_text(150, 10, text=f"{self.__player.getName()} (${self.__player.getMoney()} left)")

        
           
        
    def newGame(self):
        
        if self.__player.getMoney() <= 0:
            self.__askmoney = askinteger("Money", "How much money do you want Change?")
            self.__player.setMoney(self.__askmoney)
        
        self.__askbet = askinteger("Money", "How much money do you want bet?")
        
        while self.__askbet > self.__player.getMoney():
            self.__askbet = askinteger("Money", "How much money do you want bet(make to have that money)?")
        
        
        self.__player.giveMoney(self.__askbet)
        self.__moneyleft["text"]= f"Balance = ${self.__player.getMoney()}"
        self.__betleft["text"]= f"Ante bet= ${self.__askbet}"
        self.value = 0
        self.__deck.reset()
        self.__deck.shuffle()
        
        self.__pile.getCard().clear()
        self.__handler.getCard().clear()
        self.__player.getCard().clear()
        
        
        self.__handler.render()
        self.__player.render()
        
        
        
        while self.__deck.hasNext():
            self.__pile.addCard(self.__deck.dealCard())
            
        self.__pile.setBack(self.__deck.backOfCard)  
        self.__pile.render()
        self.__playhit["text"]= "Play"
        self.__newButton["text"] = "Exit"
        self.__playhit["command"]= self.Play
        self.__newButton["command"] = self.exit
        

        
    def Play(self):
        
        for _ in range(2):
            c1 = self.__pile.PlayCard()
            c2 = self.__pile.PlayCard()
            self.__player.addCard(c1)
            self.__handler.addCard(c2)
            
        self.__player.render()
        
        self.__handler.setStatus(True)
        self.__handler.setBack(self.__deck.backOfCard)
        self.__handler.render()
        
        for cards in self.__player.getCard():
            temp = self.__player.get_newValue(cards)
            self.value += temp                
        for card in self.__player.getCard():
            if card.getFace() == "A" and self.value <=11:
                self.value +=10
        if self.value == 21:
            self.__player.addMoney(self.__askbet*2+(self.__askbet*0.5))
            self.__player.getCanvas().create_text(150, 10, text=f"{self.__player.getName()} BlackJack!!!(${self.__player.getMoney()} left)")
            self.__newButton["text"] = "Exit"
            self.__newButton["command"] = self.exit
            self.__playhit["text"] = "-"
            self.__playhit["command"] = self.Nothing 
        elif self.value > 21:
            self.__player.getCanvas().create_text(150, 10, text=f"{self.__player.getName()} BUST!!!(${self.__player.getMoney()} left)")
            self.__newButton["text"] = "Exit"
            self.__newButton["command"] = self.exit
            self.__playhit["text"] = "-"
            self.__playhit["command"] = self.Nothing
        elif self.value < 21:
            self.__playhit["text"]= "Hit"
            self.__newButton["text"] = "Stay"
            self.__playhit["command"]= self.setHit
            self.__newButton["command"] = self.setStay
                
    
        
if __name__ == "__main__":
    win = tk.Tk()
    theBlack = BlackJackG(parent=win)
    win.mainloop()
        
        
        
        
        
        
        
        
        
        
        
        
        