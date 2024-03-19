'''
Created on Mar 2, 2024

@author: andri
'''
from Project_1.Resource.DeckOfCards import DeckOfCards as DC
from Project_1.Projects.Hustler import HL
import tkinter as tk
from tkinter.simpledialog import askstring, askinteger

'''
Description:
  
'''
class PokerG(object):


    def __init__(self, parent = None):
        '''
        Constructor
        '''
        self.__deck = DC("deck_of_cards.png")
        self.__player = HL("Godzilla", parent= parent)
        self.__dealer = HL("Kong", parent= parent)
        self.__collector = HL("Draw Card", status=True, parent= parent)
        self.Antebet = 0
        self.Pairbet = 0
        
        self.__parent = parent
        self.__parent.configure(background = "blue")
        self.__parent.geometry("760x500")
        
        self.__ask = askstring("Name", "What is your name?")
        self.__player.setName(self.__ask)
        self.__askmoney = askinteger("Money", "How much money do you want Change?")
        self.__player.setMoney(self.__askmoney)
        



        self.__dealer.setMoney("None Of your business")

        
        self.__player.getFrame().grid(row = 1, column = 1, padx = 5, pady = 5)
        self.__player.getFrame().config(background = "blue")
        
        self.__dealer.getFrame().grid(row = 0, column = 1, padx = 5, pady = 5)
        self.__dealer.getFrame().config(background = "blue")
        self.__collector.getFrame().grid(row = 0, column = 0,rowspan=2, padx = 5, pady = 5)
        self.__collector.getFrame().config(background = "blue")
        
        self.__moneyFrame = tk.LabelFrame(self.__parent)
        self.__moneyFrame.grid(row = 1, column = 2,rowspan =2)
        
        self.__moneyleft = tk.Label(self.__moneyFrame, text= f"Balance = ${self.__player.getMoney()}")
        self.__moneyleft.grid(row = 0, column = 0)
        self.__betleft = tk.Label(self.__moneyFrame, text= f"Ante bet= ${self.Antebet}")
        self.__betleft.grid(row = 1, column = 0)
        self.__betpairleft = tk.Label(self.__moneyFrame, text= f"Pair bet= ${self.Pairbet}")
        self.__betpairleft.grid(row = 2, column = 0)
        self.__betplayleft = tk.Label(self.__moneyFrame, text= f"Play bet= $0")
        self.__betplayleft.grid(row = 3, column = 0)  
        
        self.__controlFrame = tk.LabelFrame(self.__parent)
        self.__controlFrame.grid(row = 0, column = 2,rowspan =2)
        

        self.__playBut = tk.Button(self.__controlFrame, text = "Play",bg="dodger blue",activebackground="gold2",borderwidth = 5,  command = self.Play)
        self.__playBut.grid(row = 0, column = 0, padx = 5, pady = 5)
      
        
        self.__ExitButton = tk.Button(self.__controlFrame, text = "Exit",bg="dodger blue",activebackground="gold2",borderwidth = 5, command = self.exit)
        self.__ExitButton.grid(row = 1, column = 0, padx = 5, pady = 5)
    
        
        self.__restartButton = tk.Button(self.__controlFrame, text = "New Game",bg="dodger blue",activebackground="gold2",borderwidth = 5, command= self.newGame)
        self.__restartButton.grid(row = 2, column = 0, padx = 5, pady = 5)
      
        self.newGame()
        
        
        
        
        
    def Nothing(self):
        return None 
    
    def exit(self):
        self.__parent.destroy()  
          
    def Play(self):
        self.__collector.getNewValue()
                        
        for _ in range(3):
            C1 = self.__collector.PlayCard()
            C2 = self.__collector.PlayCard()
            self.__player.addCard(C1)
            self.__dealer.addCard(C2)
            
        self.__player.render()
        self.__playBut["text"] = "Bet Play" 
        self.__playBut["command"] = self.BetPlay
        self.__ExitButton["text"] = "Fold"
        self.__ExitButton["command"] = self.Fold
        self.__restartButton["text"] = "-"
        self.__restartButton["command"] = self.Nothing
        
    
    def BetPlay(self):
        
        while self.__player.getMoney() < (self.Antebet*2 + self.Pairbet):
            self.__askmoney = askinteger("Money", "How much money do you want Change?")
            self.__player.addMoney(self.__askmoney)
            
        self.__betplayleft["text"]= f"Pair bet= ${self.Antebet}"
        self.__moneyleft["text"]= f"Balance = ${(self.__player.getMoney()-(2*self.Antebet+self.Pairbet))}"
        
        self.__dealer.render()
        
        Dealer_Status = {} 
        Player_Status = {}        
        for _ in self.__dealer.getCard():
            if self.__dealer.checkHighCard():
                Dealer_Status["HighCard"]= self.__dealer.checkHighCard()
            else: 
                Dealer_Status["HighCard"]= False
                
        for _ in self.__player.getCard():
            if self.__player.checkHighCard():
                Player_Status["HighCard"]= self.__player.checkHighCard()
            else: 
                Player_Status["HighCard"]= False
                
        for _ in self.__player.getCard():   
            if self.__player.checkPair():
                Player_Status["Pair"]= self.__player.checkPair()
            else: 
                Player_Status["Pair"]= False 
                
        for _ in self.__player.getCard():
            if self.__player.checkFlush():
                Player_Status["Flush"]= self.__player.checkFlush()
            else: 
                Player_Status["Flush"]= False
              
        for _ in self.__player.getCard():  
            if self.__player.checkStraight():
                Player_Status["Straight"]= self.__player.checkStraight()
            else: 
                Player_Status["Straight"]= False
        
        for _ in self.__player.getCard():
            if self.__player.checkThreeOfKind():
                Player_Status["Three of a kind"]= self.__player.checkThreeOfKind()
            else: 
                Player_Status["Three of a kind"]= False
                
        for _ in self.__player.getCard():  
            if self.__player.checkStraightFlush():
                Player_Status["Straight Flush"]= self.__player.checkStraightFlush()    
            else: 
                Player_Status["Straight Flush"]= False
                
        if Dealer_Status["HighCard"] == False:
            self.__player.addMoney(self.Antebet)
            if Player_Status["Straight"] == True:
                self.__player.getCanvas().create_text(30, 10, text=f"Bonus!")
                self.__player.addMoney(self.Antebet)
            if Player_Status["Three of a kind"] == True:
                self.__player.getCanvas().create_text(30, 20, text=f"Bonus!")
                self.__player.addMoney(self.Antebet*4)
            if Player_Status["Straight Flush"] == True:
                self.__player.addMoney(self.Antebet*5)
                self.__player.getCanvas().create_text(30, 30, text=f"Bonus!")
                
            if Player_Status["Pair"] == True:
                self.__player.addMoney(self.Pairbet)
            elif Player_Status["Pair"] == False :
                self.__player.giveMoney(self.Pairbet)
                #### Pair Bonus ###
            if Player_Status["Flush"] == True:
                self.__player.addMoney(self.Pairbet*3)
                self.__player.getCanvas().create_text(30, 60, text=f"Bonus!")
            if Player_Status["Straight"] == True:
                self.__player.addMoney(self.Pairbet*6)
                self.__player.getCanvas().create_text(30, 70, text=f"Bonus!")
            if Player_Status["Three of a kind"] == True:
                self.__player.addMoney(self.Pairbet*30)
                self.__player.getCanvas().create_text(30, 80, text=f"Bonus!")
            if Player_Status["Straight Flush"] == True:
                self.__player.addMoney(self.Pairbet*40)
                self.__player.getCanvas().create_text(30, 90, text=f"Bonus!")
            

            self.__player.getCanvas().create_text(150, 10, text=f"You have ${self.__player.getMoney()}.")
            
        
        elif Dealer_Status["HighCard"] == True: 
            if Player_Status["HighCard"] == False:
                self.__player.giveMoney(self.Antebet)
            elif Player_Status["HighCard"] == True:
                num1 = self.__player.HighestValuedCard()
                num2 = self.__dealer.HighestValuedCard()
                if num1 > num2:
                    self.__player.addMoney(self.Antebet*2) 
                elif num1 <= num2: # New Rule
                    self.__player.giveMoney(self.Antebet*2)
                    
            if Player_Status["Pair"] == True:
                self.__player.addMoney(self.Pairbet)
            elif Player_Status["Pair"] == False :
                self.__player.giveMoney(self.Pairbet)
            #### Pair Bonus ###
            if Player_Status["Flush"] == True:
                self.__player.addMoney(self.Pairbet*3)
                self.__player.getCanvas().create_text(30, 10, text=f"Bonus!")
            if Player_Status["Straight"] == True:
                self.__player.addMoney(self.Pairbet*6)
                self.__player.getCanvas().create_text(30, 20, text=f"Bonus!")
            if Player_Status["Three of a kind"] == True:
                self.__player.addMoney(self.Pairbet*30)
                self.__player.getCanvas().create_text(30, 30, text=f"Bonus!")
            if Player_Status["Straight Flush"] == True:
                self.__player.addMoney(self.Pairbet*40)
                self.__player.getCanvas().create_text(30, 40, text=f"Bonus!")
                
            self.__player.getCanvas().create_text(150, 10, text=f"You have ${self.__player.getMoney()}.")
        
        self.__playBut["text"] = "-" 
        self.__playBut["command"] = self.Nothing
        self.__ExitButton["text"] = "Exit"
        self.__ExitButton["command"] = self.exit
        self.__restartButton["text"] = "Restart"
        self.__restartButton["command"] = self.newGame
        
    def Fold(self):
        self.__player.giveMoney(self.Antebet)
        self.__dealer.render()
        
        Dealer_Status = {} 
        Player_Status = {}        
        for _ in self.__dealer.getCard():
            if self.__dealer.checkHighCard():
                Dealer_Status["HighCard"]= self.__dealer.checkHighCard()
            else: 
                Dealer_Status["HighCard"]= False
                
        for _ in self.__player.getCard():
            if self.__player.checkHighCard():
                Player_Status["HighCard"]= self.__player.checkHighCard()
            else: 
                Player_Status["HighCard"]= False
                
        for _ in self.__player.getCard():   
            if self.__player.checkPair():
                Player_Status["Pair"]= self.__player.checkPair()
            else: 
                Player_Status["Pair"]= False 
                
        for _ in self.__player.getCard():
            if self.__player.checkFlush():
                Player_Status["Flush"]= self.__player.checkFlush()
            else: 
                Player_Status["Flush"]= False
              
        for _ in self.__player.getCard():  
            if self.__player.checkStraight():
                Player_Status["Straight"]= self.__player.checkStraight()
            else: 
                Player_Status["Straight"]= False
        
        for _ in self.__player.getCard():
            if self.__player.checkThreeOfKind():
                Player_Status["Three of a kind"]= self.__player.checkThreeOfKind()
            else: 
                Player_Status["Three of a kind"]= False
                
        for _ in self.__player.getCard():  
            if self.__player.checkStraightFlush():
                Player_Status["Straight Flush"]= self.__player.checkStraightFlush()    
            else: 
                Player_Status["Straight Flush"]= False
                
        if Dealer_Status["HighCard"] == False:
            if Player_Status["Pair"] == True:
                self.__player.addMoney(self.Pairbet)
                pass
            elif Player_Status["Pair"] == False :
                self.__player.giveMoney(self.Pairbet)
                pass
                #### Pair Bonus ###
            if Player_Status["Flush"] == True:
                self.__player.addMoney(self.Pairbet*3)
                self.__player.getCanvas().create_text(30, 60, text=f"Bonus!")
            if Player_Status["Straight"] == True:
                self.__player.addMoney(self.Pairbet*6)
                self.__player.getCanvas().create_text(30, 70, text=f"Bonus!")
            if Player_Status["Three of a kind"] == True:
                self.__player.addMoney(self.Pairbet*30)
                self.__player.getCanvas().create_text(30, 80, text=f"Bonus!")
            if Player_Status["Straight Flush"] == True:
                self.__player.addMoney(self.Pairbet*40)
                self.__player.getCanvas().create_text(30, 90, text=f"Bonus!")
            

            self.__player.getCanvas().create_text(150, 10, text=f"You have ${self.__player.getMoney()}.")
        
        elif Dealer_Status["HighCard"] == True: 
            
            if Player_Status["Pair"] == True:
                self.__player.addMoney(self.Pairbet)
            elif Player_Status["Pair"] == False :
                self.__player.giveMoney(self.Pairbet)
            #### Pair Bonus ###
            if Player_Status["Flush"] == True:
                self.__player.addMoney(self.Pairbet*3)
                self.__player.getCanvas().create_text(30, 10, text=f"Bonus!")
            if Player_Status["Straight"] == True:
                self.__player.addMoney(self.Pairbet*6)
                self.__player.getCanvas().create_text(30, 20, text=f"Bonus!")
            if Player_Status["Three of a kind"] == True:
                self.__player.addMoney(self.Pairbet*30)
                self.__player.getCanvas().create_text(30, 30, text=f"Bonus!")
            if Player_Status["Straight Flush"] == True:
                self.__player.addMoney(self.Pairbet*40)
                self.__player.getCanvas().create_text(30, 40, text=f"Bonus!")
            
            self.__player.getCanvas().create_text(150, 10, text=f"You have ${self.__player.getMoney()}.")
        
        self.__playBut["text"] = "-" 
        self.__playBut["command"] = self.Nothing
        self.__ExitButton["text"] = "Exit"
        self.__ExitButton["command"] = self.exit
        self.__restartButton["text"] = "Restart"
        self.__restartButton["command"] = self.newGame
        
    def newGame(self):
        
        if self.__player.getMoney() <= 0:
            self.__askmoney = askinteger("Money", "How much money do you want Change?")
            self.__player.setMoney(self.__askmoney)
        
        self.Antebet = 0
        while self.Antebet <= 0:
            self.Antebet = askinteger("Money", "How much money do you want bet against the dealer?")
            if self.Antebet <= self.__player.getMoney():
                break
        
        if self.__player.getMoney() <= 0:
            self.__askmoney = askinteger("Money", "How much money do you want Change?")
            self.__player.setMoney(self.__askmoney)
        
        self.Pairbet = 0
        while self.Pairbet <= 0:
            self.Pairbet = askinteger("Money", "How much money do you want bet for a Pair?")
            if self.Pairbet <= (self.__player.getMoney()- self.Antebet):
                break
            else:
                self.__askmoney = askinteger("Money", "How much money do you want Change?")
                self.__player.addMoney(self.__askmoney)
                self.Pairbet = 0
              
    
        self.__deck.reset()
        self.__deck.shuffle()
        
        self.__collector.getCard().clear()
        self.__dealer.getCard().clear()
        self.__player.getCard().clear()
        
        
        self.__dealer.render()
        self.__player.render()
        
        
        self.__moneyleft["text"]= f"Balance = ${(self.__player.getMoney()-(self.Antebet+self.Pairbet))}"
        self.__betleft["text"]= f"Ante bet= ${self.Antebet}"
        self.__betpairleft["text"]= f"Pair bet= ${self.Pairbet}"
        self.__betplayleft["text"]= "Pair bet= $0"
        while self.__deck.hasNext():
            self.__collector.addCard(self.__deck.dealCard())
            
        self.__collector.setBack(self.__deck.backOfCard)  
        self.__collector.render()
        
        self.__playBut["text"] = "Play" 
        self.__playBut["command"] = self.Play
        self.__ExitButton["text"] = "Exit"
        self.__ExitButton["command"] = self.exit
        
        
    
        
        
        
        
if __name__ == "__main__":
    win = tk.Tk()
    thePoker = PokerG(parent=win)
    win.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        