'''
Created on Feb 13, 2024

@author: andri
'''

from DeckOfCards import DeckOfCards
from War_Player import WP

class WarGame():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__deck = DeckOfCards()
        self.__player1 = WP("Spider-Man")
        self.__player2 = WP("The Weeknd")
        self.__spoils = WP("Spoils")
        self.__turns = 0
        
    def playGame(self):
        self.__deck.shuffle()
        
        #distribute the 52 cards to the players
        while self.__deck.hasNext():
            c1 = self.__deck.dealCard()
            c2 = self.__deck.dealCard()
            self.__player1.addCard(c1)
            self.__player2.addCard(c2)
            
        while self.__player1.hasCard() and self.__player2.hasCard() and self.__turns < 1000:
            self.__turns +=1
            card1 = self.__player1.playCard()
            card2 = self.__player2.playCard()
            
            
            self.__spoils.addCard(card1)
            self.__spoils.addCard(card2)
            
            print(f"{card1} vs {card2}", end = " ")
            
            winner = None 
            
            
            if card1 > card2:
                winner = self.__player1
                print(f"{self.__player1.getName()} wins this round", end= "")
            elif card2 > card1:
                winner = self.__player2
                print(f"{self.__player2.getName()} wins this round", end= "")
            else:
                print("!!!!!!!!!This means WAR!!!!!!!!!")
                
                temp = self.__player1.prepareWar()+ self.__player2.prepareWar()
                while temp != []:
                    self.__spoils.addCard(temp.pop(0))
                    
            if winner != None:
                while self.__spoils.hasCard():
                    winner.addCard(self.__spoils.playCard())
                print(f"({self.__player1.cardsRemaining()}, {self.__player2.cardsRemaining()})")
                
            
            
if __name__ == "__main__":
    theWar = WarGame()
    theWar.playGame()
            
            
            
            
            
            
            
            
        