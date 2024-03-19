'''
Created on Feb 22, 2024

@author: andri
'''
from Project_1.Resource.DeckOfCards import DeckOfCards as DC
from Project_1.Projects.Hustler import HL

class Poker(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.__deck = DC()
        self.__Player = HL("Godzilla", 200)
        self.__dealer = HL("Kong", 1000000)
        self.__collector = HL("Collector")
        
    def PlayGame(self):
        game = True 
        
        while game:
            ask = input("Welcome Player, Do you want to play poker(y/n)? ")
            
            if ask.capitalize() == "Y":
                mulla = True
                Ante = 0
                pair = 0
                while mulla:
                    self.__deck.reset()
                    self.__dealer.getCard().clear()
                    self.__Player.getCard().clear()
                    
                    print(f"You have ${self.__Player.getMoney()} in your hand.")
        
                    print("Where do you want to place the bet on?") 
                    print("1, Against(Ante)")
                    print("2, Pair")
                    mo = input("3, Done ")
                    
                    if mo == "1":
                        num = int(input("Amount(in integer, we don't want your penny!)? $"))
                        Ante += num
                        if Ante > self.__Player.getMoney():                            
                            print("Error, We all know You don't have that much money!!!")
                            Ante = 0
                            mulla = True 
                        elif Ante <= self.__Player.getMoney():
                            mulla = True 
                    elif mo == "2":                        
                        numb = int(input("Amount(in integer, we don't want your penny!)? $"))
                        pair += numb
                        
                        if (pair + Ante) > self.__Player.getMoney():
                            print("Error, We all know You don't have that much money!!!")
                            pair = 0
                            mulla = True 
                        elif (pair + Ante) <= self.__Player.getMoney():
                            mulla = True
                            
                    elif mo == "3":
                        print(f"You have ${Ante}, in the Ante bet.")
                        print(f"You have ${pair}, in the Pair bet.")
                        self.__deck = DC()
                        self.__deck.shuffle()
                        while self.__deck.hasNext():
                            self.__collector.addCard(self.__deck.dealCard())
                            
                        self.__collector.getNewValue()
                        
                        for _ in range(3):
                            C1 = self.__collector.PlayCard()
                            C2 = self.__collector.PlayCard()
                            self.__Player.addCard(C1)
                            self.__dealer.addCard(C2)
                            
                        print(f"{self.__Player.getName()}(aka 'you') have:")
                        for card in self.__Player.getCard():
                            print(card)
                        
                        check = True 
                        while check:
                            sure = input("Do you want to place a bet on Play or Fold(p/f)?")
                            
                            if sure.capitalize() == "P":
                                playB = Ante
                                print(f"You have ${playB}, in the Play bet.")
                                check = False
                            elif sure.capitalize() == "F":
                                Ante = 0
                                print(f"You have ${Ante}, in the Ante bet Because You Fold.")
                                check = False
                            else: 
                                print("Error")
                                check = True
                                
                        dave = True 
                        while dave:   
                            reveal = input("Enter 'r' to reveal the dealer's card and your score. ")
                            
                            if reveal.capitalize() == "R":
                                
                                print(f"{self.__dealer.getName()}(aka 'the dealer') has:")
                                for card in self.__dealer.getCard():
                                    print(card)
                                    
                                '''
                                Check Status
                                '''   
                                Dealer_Status = {} 
                                Player_Status = {}        
                                for card in self.__dealer.getCard():
                                    if self.__dealer.checkHighCard():
                                        Dealer_Status["HighCard"]= self.__dealer.checkHighCard()
                                    else: 
                                        Dealer_Status["HighCard"]= False
                                        
                                for card in self.__Player.getCard():
                                    if self.__Player.checkHighCard():
                                        Player_Status["HighCard"]= self.__Player.checkHighCard()
                                    else: 
                                        Player_Status["HighCard"]= False
                                        
                                for card in self.__Player.getCard():   
                                    if self.__Player.checkPair():
                                        Player_Status["Pair"]= self.__Player.checkPair()
                                    else: 
                                        Player_Status["Pair"]= False 
                                        
                                for card in self.__Player.getCard():
                                    if self.__Player.checkFlush():
                                        Player_Status["Flush"]= self.__Player.checkFlush()
                                    else: 
                                        Player_Status["Flush"]= False
                                      
                                for card in self.__Player.getCard():  
                                    if self.__Player.checkStraight():
                                        Player_Status["Straight"]= self.__Player.checkStraight()
                                    else: 
                                        Player_Status["Straight"]= False
                                
                                for card in self.__Player.getCard():
                                    if self.__Player.checkThreeOfKind():
                                        Player_Status["Three of a kind"]= self.__Player.checkThreeOfKind()
                                    else: 
                                        Player_Status["Three of a kind"]= False
                                        
                                for card in self.__Player.getCard():  
                                    if self.__Player.checkStraightFlush():
                                        Player_Status["Straight Flush"]= self.__Player.checkStraightFlush()    
                                    else: 
                                        Player_Status["Straight Flush"]= False
                                        
                                        
                                        
                                if Dealer_Status["HighCard"] == False:
                                    if sure.capitalize() == "P":
                                        self.__Player.addMoney(Ante)
                                        print(f"the dealer didn't Qualify, you get ${Ante}.")
                                        ### Ante Bonus ### 
                                        if Player_Status["Straight"] == True:
                                            self.__Player.addMoney(Ante)
                                            print(f"Bonus, ${Ante} add!!!")
                                        if Player_Status["Three of a kind"] == True:
                                            self.__Player.addMoney(Ante*4)
                                            print(f"Bonus, ${Ante*4} added!!!")
                                        if Player_Status["Straight Flush"] == True:
                                            self.__Player.addMoney(Ante*5)
                                            print(f"Bonus, ${Ante*5} added!!!")
                                            
                                        if Player_Status["Pair"] == True:
                                            self.__Player.addMoney(pair)
                                            print(f"You have a pair, you get ${pair}.")
                                        elif Player_Status["Pair"] == False :
                                            self.__Player.giveMoney(pair)
                                            print(f"You don't have a pair, you lost ${pair}.")
                                            #### Pair Bonus ###
                                        if Player_Status["Flush"] == True:
                                            self.__Player.addMoney(pair*3)
                                            print(f"Bonus, ${pair*3} added!!!")
                                        if Player_Status["Straight"] == True:
                                            self.__Player.addMoney(pair*6)
                                            print(f"Bonus, ${pair*6} added!!!")  
                                        if Player_Status["Three of a kind"] == True:
                                            self.__Player.addMoney(pair*30)
                                            print(f"Bonus, ${pair*30} added!!!")
                                        if Player_Status["Straight Flush"] == True:
                                            self.__Player.addMoney(pair*40)
                                            print(f"Bonus, ${pair*40} added!!!") 
                                            
                                        print(f"You have ${self.__Player.getMoney()} in your hand.")
                                        again = True 
                                        while again: 
                                            asking = input("Do you want to play more(y/n)?")
                                            if asking.capitalize() == "Y":
                                                mulla = True
                                                dave = False
                                                again = False 
                                 
                                            elif asking.capitalize() == "N":
                                                print("Enjoy your virtual Money!!")
                                                mulla = False 
                                                again = False
                                                dave = False 
                                                check = False 
                                                game = False 
                                            else :
                                                print("Error") 
                                                again = True  
                                        
                                    elif sure.capitalize() == "F":
                                        
                                        if Player_Status["Pair"] == True:
                                            self.__Player.addMoney(pair)
                                            print(f"You have a pair, you get {pair}.")
                                            #### Pair Bonus ###
                                        if Player_Status["Flush"] == True:
                                            self.__Player.addMoney(pair*3)
                                            print(f"Bonus, ${pair*3} added!!!")
                                        if Player_Status["Straight"] == True:
                                            self.__Player.addMoney(pair*6)
                                            print(f"Bonus, ${pair*6} added!!!")  
                                        if Player_Status["Three of a kind"] == True:
                                            self.__Player.addMoney(pair*30)
                                            print(f"Bonus, ${pair*30} added!!!")
                                        if Player_Status["Straight Flush"] == True:
                                            self.__Player.addMoney(pair*40)
                                            print(f"Bonus, ${pair*40} added!!!")
                                            
                                        print(f"You have ${self.__Player.getMoney()} in your hand.")
                                        again = True 
                                        while again: 
                                            asking = input("Do you want to play more(y/n)?")
                                            if asking.capitalize() == "Y":
                                                mulla = True
                                                dave = False
                                                again = False
                                            elif asking.capitalize() == "N":
                                                print("Enjoy your virtual Money!!")
                                                mulla = False 
                                                again = False
                                                dave = False 
                                                check = False 
                                                game = False 
                                            else :
                                                print("Error")
                                                again = True 
                                            
                                        
                                elif Dealer_Status["HighCard"] == True: 
                                    if sure.capitalize() == "P":
                                        if Player_Status["HighCard"] == False:
                                            self.__Player.giveMoney(Ante)
                                        if Player_Status["HighCard"] == True:
                                            num1 = self.__Player.HighestValuedCard()
                                            num2 = self.__dealer.HighestValuedCard()
                                            if num1 > num2:
                                                self.__Player.addMoney(Ante*2) 
                                            elif num1 <= num2: # New Rule
                                                self.__Player.giveMoney(Ante*2)
                                                
                                        if Player_Status["Pair"] == True:
                                            self.__Player.addMoney(pair)
                                            print(f"You have a pair, {pair} add!!!")
                                        elif Player_Status["Pair"] == False :
                                            self.__Player.giveMoney(pair)
                                            print(f"You don't have a pair, you lost ${pair}.") 
                                        #### Pair Bonus ###
                                        if Player_Status["Flush"] == True:
                                            self.__Player.addMoney(pair*3)
                                            print(f"Bonus, ${pair*3} added!!!")
                                        if Player_Status["Straight"] == True:
                                            self.__Player.addMoney(pair*6)
                                            print(f"Bonus, ${pair*6} added!!!")  
                                        if Player_Status["Three of a kind"] == True:
                                            self.__Player.addMoney(pair*30)
                                            print(f"Bonus, ${pair*30} added!!!")
                                        if Player_Status["Straight Flush"] == True:
                                            self.__Player.addMoney(pair*40)
                                            print(f"Bonus, ${pair*40} added!!!")
                                            
                                        print(f"You have ${self.__Player.getMoney()} in your hand.")
                                        again = True 
                                        while again: 
                                            asking = input("Do you want to play more(y/n)?")
                                            if asking.capitalize() == "Y":
                                                mulla = True
                                                dave = False  
                                                again = False
                                            elif asking.capitalize() == "N":
                                                print("Enjoy your virtual Money!!")
                                                mulla = False 
                                                again = False
                                                dave = False 
                                                check = False 
                                                game = False                                           
                                            else :
                                                print("Error")
                                                again = True 
                                           
                                    elif sure.capitalize() == "F":
                                        
                                        if Player_Status["Pair"] == True:
                                            self.__Player.addMoney(pair)
                                            print(f"You have a pair, you get {pair}.")
                                        elif Player_Status["Pair"] == False :
                                            self.__Player.giveMoney(pair)
                                            print(f"You don't have a pair, you lost ${pair}.")
                                            #### Pair Bonus ###
                                        if Player_Status["Flush"] == True:
                                            self.__Player.addMoney(pair*3)
                                            print(f"Bonus, ${pair*3} added!!!")
                                        if Player_Status["Straight"] == True:
                                            self.__Player.addMoney(pair*6)
                                            print(f"Bonus, ${pair*6} added!!!")  
                                        if Player_Status["Three of a kind"] == True:
                                            self.__Player.addMoney(pair*30)
                                            print(f"Bonus, ${pair*30} added!!!")
                                        if Player_Status["Straight Flush"] == True:
                                            self.__Player.addMoney(pair*40)
                                            print(f"Bonus, ${pair*40} added!!!")
                                            
                                        print(f"You have ${self.__Player.getMoney()} in your hand.")
                                        again = True 
                                        while again: 
                                            asking = input("Do you want to play more(y/n)?")
                                            if asking.capitalize() == "Y":
                                                mulla = True
                                                dave = False 
                                                again = False                                       
                                            elif asking.capitalize() == "N":
                                                print("Enjoy your virtual Money!!")
                                                mulla = False 
                                                again = False
                                                dave = False 
                                                check = False 
                                                game = False 
                                            else :
                                                print("Error")
                                                again = True 
                                    
                            else:
                                print("Error")
                                dave = True 
                    else:
                        print("Error")
                        mulla = True   
                    
            elif ask.capitalize() == "N":
                print("Thank you for not Playing!!")
                game = False 
            else:
                print("Error Input")   
                game = True 
            
            
if __name__ == '__main__':
    myPoker  = Poker()
    myPoker.PlayGame()

















        