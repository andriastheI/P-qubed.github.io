'''
Created on Feb 22, 2024

@author: andri
'''
import tkinter as tk

class HL(object):
    '''
    classdocs
    '''


    def __init__(self, name = None, parent = None, back=None, status = False, money = None):
        '''
        Constructor
        '''
        self.__name = name
        self.__cards = []
        self.__money = money 
        self.__parent = parent
        self.__frame = None
        self.__canvas = None
        self.__back_of_card = back
        self.__dealer = status 
    
    def getCanvas(self):
        '''
        Description: used to access the classes canvas
        Arguments:  None
        Return:     self.__canvas
        '''
        return self.__canvas
    
    def setStatus(self, status):
        ''''
        Description: Assigns the self.__dealer to Status(to draw the back of the cards)
        Arguments:  status(boolean value)
        Return:     None
        '''
        self.__dealer =  status
        
    def setframe(self, frame):
        '''
        Description: Used to set a frame
        Arguments:  Frame
        Return:     None
        '''
        self.__frame= frame  
          
    def setBack(self, back):
        '''
        Description: Assigns the self.__back to Back(to draw the back of the cards)
        Arguments:  back(boolean value)
        Return:     None
        '''
        self.__back_of_card =  back  
        
    def render(self):
        '''
        Draw the player's current hand to the canvas. 
        '''
        # Render every card in the hand face down
        self.__canvas.delete(tk.ALL)
        for i in range(0, len(self.__cards)):
            if self.__back_of_card is not None and self.__dealer:
                self.__back_of_card.draw(self.__canvas, 20 + 2*i, 20)
            else:
                self.__cards[i].draw(self.__canvas, 20*i+100, 20)
                
    def getFrame(self):
        '''
        Description: Return a tkinter Frame object that a GUI can use
        '''
        if self.__frame == None:
            # No frame yet.  Let's make one.
            self.__frame = tk.LabelFrame(self.__parent, text = self.getName())
            self.__canvas = tk.Canvas(self.__frame, width = 300, height = 200)
            self.__canvas.grid(row = 0, column = 0, padx = 5, pady = 5)
        
        return self.__frame
       
    def getNewValue(self):
        val = {"A":13, "2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":7, "9":8, "10":9, "J":10, "Q":11, "K":12}
        for key,value in val.items():
            for card in self.__cards:
                if card.getFace() == key:
                    card.setValue(value)
    
    def setName(self, name):
        '''
        Description: Used to assign a new name
        Arguments:  name
        Return:     None
        '''
        self.__name = name
        
    def setMoney(self, money):
        '''
        Description: Used to assign self.__money
        Arguments:  money
        Return:     None
        '''
        self.__money = money 
        
    def addMoney(self, mulla):
        '''
        Description: Used to add money to self.__money
        Arguments:  mulla
        Return:     None
        '''
        self.__money += mulla
    def giveMoney(self, mulla):
        '''
        Description: Used to take money from self.__money
        Arguments:  mulla
        Return:     None
        '''
        self.__money -= mulla
    def getMoney(self):
        '''
        Description: Used to access self.__money
        Arguments:  None
        Return:     self.__money
        '''
        return self.__money
    
    def addCard(self, cards):
        '''
        Description: Used to add a card to the self.__cards pile
        Arguments:  cards(new card)
        Return:     None
        '''
        self.__cards.append(cards)
    
    def PlayCard(self):
        '''
        Description: Used to access take one card from the card pile
        Arguments:  None
        Return:     the picked card
        '''
        the_card = self.__cards.pop(0)
        return the_card
    
    def emptyCard(self):
        '''
        Description: Used to set the cards in hand to nothing
        Arguments:  None
        Return:     None
        '''
        self.__cards = []
        
    def getCard(self):
        '''
        Description: Used to access the cards of the class
        Arguments:  None
        Return:     self.__cards(assigned cards of the class)
        '''
        return self.__cards
    
    def getName(self):
        '''
        Description: Used to access the name of the class
        Arguments:  None
        Return:     self.__name(assigned name of the class)
        '''
        return self.__name
    
    def checkHighCard(self):
        '''
        Description: Used to check if the player has a HighCard
        Arguments:  None
        Return:     Boolean value
        '''
        for card in self.__cards:
            if card.getFace() in ["A","Q","K"]:
                return True
        return False
    
    def checkPair(self):
        '''
        Description: Used to check if the player has a Pair
        Arguments:  None
        Return:     Boolean value
        '''
        cards = []
        for card in self.__cards:
            cards.append(card.getFace())
        
        for face in cards:
            if cards.count(face) == 2:
                return True 
        return False 
    
    def checkFlush(self):
        '''
        Description: Used to check if the player has a a Flush
        Arguments:  None
        Return:     Boolean value
        '''
        one_card = self.__cards[0].getSuit()
        for card in self.__cards:
            if one_card != card.getSuit():
                return False 
        return True 
    
    def checkStraight(self):  
        '''
        Description: Used to check if the player has a Straight
        Arguments:  None
        Return:     Boolean value
        ''' 
        cardvalue  = []
        for card in self.__cards:
            cardvalue.append(card.getValue())
            
        sortedCard = sorted(cardvalue)
        
        for i in range(1, len(sortedCard)):
            if sortedCard[i] != sortedCard[i-1] + 1:
                return False 
        return True 
    
    def checkThreeOfKind(self):
        '''
        Description: Used to check if the player has a Three of Kind
        Arguments:  None
        Return:     Boolean value
        '''
        one_card = self.__cards[0].getFace()
        for card in self.__cards:
            if one_card != card.getFace():
                return False 
        return True 
    
    def checkStraightFlush(self):
        '''
        Description: Used to check if the player has a Flush
        Arguments:  None
        Return:     Boolean value
        '''
        if self.checkStraight() == True and self.checkFlush() == True:
            return True
        return False
    
    def HighestValuedCard(self):
        '''
        Description: Used to access the highest valued card
        Arguments:  None
        Return:     the maximum valued card
        '''
        temp = []
        for card in self.__cards:
            temp.append(card.getValue())
        maxnum = max(temp)
        
        return maxnum
        

if __name__ == '__main__':
        
    status = "PASSED"
    K = 60

    print("Testing functionality of Gambler class.")
############################
# Test default constructor #
############################
    message = "   Testing default constructor:"
    try:
        defaultSwimTime = HL()
        print(f"{message:<{K}} {'PASSED'}")

    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during instantiation.")
        status = "FAILED"

#############################
# Test standard constructor #
#############################
    message = "   Testing standard constructor:"
    try:
        standard = HL(name = "Superman")
        if standard.getName() == "Superman":
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Object instantiated, but name is wrong.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during instantiation.")
        print(f"      Exiting test.")
        status = "FAILED"
        exit()

#######################
# Test setName method #
#######################
    message = "   Testing 'setName' method:"
    try:
        standard.setName("DeadPool")
        if standard.getName() == "DeadPool":
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but failed to set name.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED':>40s}")
        print(f"      Exception during setName method.")
        status = "FAILED"

#######################
# Test setMoney method #
#######################
    message = "   Testing 'setMoney' method:"
    try:
        standard.setMoney(2000)
        if standard.getMoney()== 2000:
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but failed to set Money.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED':>40s}")
        print(f"      Exception during setMoney method.")
        status = "FAILED"

#######################
# Test setframe method #
#######################
    message = "   Testing 'setframe' method:"
    try:
        standard.setframe(True)
        if standard.getFrame() == True:
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but failed to set name.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED':>40s}")
        print(f"      Exception during setframe method.")
        status = "FAILED"

#######################
# Test addCard method #
#######################
    message = "   Testing 'addCard' method:"
    try:
        standard.addCard("DeadPool")
        if standard.PlayCard() == "DeadPool":
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but failed to add card.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED':>40s}")
        print(f"      Exception during addCard method.")
        status = "FAILED"

#######################
# Test emptyCard method #
#######################
    message = "   Testing 'emptyCard' method:"
    try:
        standard.emptyCard()
        if standard.getCard() == []:
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but failed to empty Cards.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED':>40s}")
        print(f"      Exception during emptyCard method.")
        status = "FAILED"



























