'''
Created on Feb 20, 2024
@author: Andrias
'''

from DeckOfCards import DeckOfCards as DC
from Gambler import GB

'''
Description: 

this is a text(console) based Black jack game. made using a gambler(GB) object
which makes you choose the amount of money you want to have as a chips and bet. 

-it is guarded by many if statements it is hard to brake it easily. 


'''
class BlackJack(object):
    def __init__(self):
        '''
        Constructor
        '''
        self.__deck = DC()
        self.__player = GB("AK47")
        self.__handler = GB("SHOT-GUN")
        self.__pile = GB("Pile")
        
    def PlayGame(self):
        self._money = int(input("How much Chips(money) do you want(Int)? $"))
        game = True 
        while game:
            gaming = input("Are you ready to play Black jack(Y/N)? ")
            if gaming.capitalize() == "Y":
                print(f"You have ${self._money} Chips.")
                self.bet = int(input("Place your bet(We don't want your pennies). $"))
                while self.bet > self._money:
                    self._more = int(input("How much Chips(money) do you want? $"))
                    self._money+=self._more
                    
                self.__player.emptyCard()
                self.__handler.emptyCard()
                self.__pile.emptyCard()
                self.__deck = DC()
                
                self.__deck.shuffle()
                for _ in range(2):
                    c1 = self.__deck.dealCard()
                    c2 = self.__deck.dealCard()
                    self.__player.addCard(c1)
                    self.__handler.addCard(c2)
                while self.__deck.hasNext():
                    self.__pile.addCard(self.__deck.dealCard())
                
                winner = None
                while winner is None:
                    value = 0
                    print(f"{self.__player.getName()}, has:")
                    for cards in self.__player.getCard():
                        print(cards)
                    for cards in self.__player.getCard():
                        temp = self.__player.get_newValue(cards)
                        value += temp                
            
                    for card in self.__player.getCard():
                        if card.getFace() == "A" and value <=11:
                            value +=10
                            
                    if value == 21:
                        winner = self.__player
                        print(f"{self.__player.getName()}, Black Jack!")
                        self._money+=self.bet*1.5
                        print(f"${self._money} Chips left.")
                         
                    elif value > 21:
                        winner = self.__handler
                        print(f"{self.__player.getName()}, Bust! So, {self.__handler.getName()}, Wins!")
                        self._money-=self.bet
                        print(f"${self._money} Chips left.") 
                    elif value < 21:
                        demo = True 
                        while demo:
                            ask = input("Choose 'Hit' for another card or 'Stay' to stay where you are. ")
                            if ask.capitalize() == "Hit":
                                new_card = self.__pile.PlayCard()
                                self.__player.addCard(new_card)
                                demo = False  
                            elif ask.capitalize() == "Stay":
                                print(f"{self.__handler.getName()}, has:")
                                for cards in self.__handler.getCard():
                                    print(cards)
                                check = True            
                                while check:
                                    checker = 0
                                    for cards in self.__handler.getCard():                        
                                        temp = self.__player.get_newValue(cards)
                                        checker += temp 
                                    for card in self.__handler.getCard():
                                        if card.getFace() == "A" and checker <=11:
                                            checker+=10
                                    if checker <= 16:
                                        new_cards = self.__pile.PlayCard()
                                        self.__handler.addCard(new_cards)
                                        temp = self.__player.get_newValue(new_cards)
                                        checker += temp 
                                        print(f"{self.__handler.getName()},added {new_cards}")
                                    elif checker > 21:
                                        winner = self.__player
                                        print(f"{self.__handler.getName()}, Bust!So, {self.__player.getName()}, Wins!")
                                        self._money+=self.bet
                                        print(f"${self._money} Chips left.")
                                        check = False
                                         
                                    elif checker > 16:
                                        if value > checker :
                                            winner = self.__player
                                            print(f"{self.__player.getName()}, Wins!")
                                            self._money+=self.bet
                                            print(f"${self._money} Chips left.")
                         
                                            check = False 
                                        elif value <= checker:
                                            winner = self.__handler
                                            print(f"{self.__handler.getName()}, Wins!")
                                            self._money-=self.bet
                                            print(f"${self._money} Chips left.") 
                                            check = False 
                                    
                                demo = False  
                                
                            else:
                                print("Error input")
                                demo = True
                                    
                                              
                game = True

                
            elif gaming.capitalize() == "N":
                print("Thanks for not playing!")
                game = False
            else:
                print("Error Input")
                game = True
if __name__ == "__main__":
    the_BackJack = BlackJack()
    the_BackJack.PlayGame() 
            
            
            
            
            
            
            
            
            
            
            
            
        