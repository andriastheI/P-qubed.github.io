'''
Created on Feb 9, 2024, during class

This file contains the WarPlayer (WP) class.
We will use this class as part of our War card game.

@author: twendt
'''

import tkinter as tk

class WP(object):
    '''
    classdocs
    '''

    def __init__(self, name = "Jackie Chan", parent = None, back = None):
        '''
        Constructor
        '''
        self.__name = name
        self.__cards = []
        self.__parent = parent
        self.__frame = None
        self.__canvas = None
        self.__back_of_card = back
    def emptyCard(self):
        self.__cards = []
        
    def getCanvas(self):
        return self.__canvas
    
    def numberCard(self):
        return len(self.__cards)
    def getFrame(self):
        '''
        Description: Return a tkinter Frame object that a GUI can use
        '''
        if self.__frame == None:
            # No frame yet.  Let's make one.
            self.__frame = tk.LabelFrame(self.__parent, text = self.getName())
            self.__canvas = tk.Canvas(self.__frame, width = 200, height = 200)
            self.__canvas.grid(row = 0, column = 0, padx = 5, pady = 5)
        
        return self.__frame
            
    
    def render(self):
        '''
        Draw the player's current hand to the canvas. 
        '''
        # Render every 5th card in the hand face down
        for i in range(0, len(self.__cards), 5):
            # self.__cards[i].draw(self.__canvas, 20 + 2*i, 20)
            if self.__back_of_card is not None:
                self.__back_of_card.draw(self.__canvas, 20 + 2*i, 20)
        
    def addCard(self, card):
        '''
        Description: add the card f to the player's personal list
        Arguments: card: a single Card object
        Return: None
        '''
        self.__cards.append(card)
            
    def playCard(self):
        '''
        Description: Remove the first card in the list and return it.
                     If there are no cards, raise an exception
        Arguments:  None
        Return:     A card from the players hand.
        '''
        if self.hasCard():
            myCard = self.__cards.pop(0)
            return myCard
        else:
            raise Exception("I don't have any cards, dummy.")
    
    def hasCard(self):
        '''
        Description: Returns True if the player has cards;
                     Returns False if the player has no cards.
        Arguments:  None
        Return:     boolean
        '''        
        if len(self.__cards) > 0:
            return True
        else:
            return False
        
    def cardsRemaining(self):
        '''
        Description: Returns the number of cards remaining in the player's hand
        Arguments:  None
        Return:     int - the number of cards in the player's hand
        '''          
        return len(self.__cards)
    
    def prepareWar(self):
        '''
        Description: Returns up to 3 cards in preparation for a war
        Arguments:  None
        Return:     list<Card> - a list containing up to 3 cards
        '''              
        temp = []
        if len(self.__cards) > 3:
            for _ in range(3):
                temp.append(self.playCard())
        else:
            while self.hasCard():
                temp.append(self.playCard())
        return temp
    
    def getName(self):
        return self.__name
    
    def setName(self, newName):
        if newName == "Ted Chan":
            print("Stop it.")
        else:
            self.__name = newName
        
if __name__ == "__main__":
    # Test our code to make sure it works.
    from Project_1.Resource.DeckOfCards import DeckOfCards as DC
    from Project_1.Resource.Card import Card
    
    status = "PASSED"
    K = 60
    
    print("Testing functionality of the War Player class.")
############################
# Test default constructor #
############################
    message = "   Testing default constructor:"
    try:
        defaultWP = WP()
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
        standardWP = WP('Napoleon Guzelocak')
        if standardWP.getName() == 'Napoleon Guzelocak':
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
        standardWP.setName('Chris Tucker')
        if standardWP.getName() == 'Chris Tucker':
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but failed to set name.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED':>40s}")
        print(f"      Exception during setName method.")
        status = "FAILED"

####################################
# Test hasCard method (empty hand) #
####################################
    message = "   Testing 'hasCard' method with empty hand:"
    try:
        if not standardWP.hasCard():
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but return incorrect.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during hasCard method.")
        status = "FAILED"    

###########################################
# Test cardsRemaining method (empty hand) #
###########################################
    message = "   Testing 'cardsRemaining' method with empty hand:"
    try:
        if standardWP.cardsRemaining() == 0:
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but return incorrect.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during cardsRemaining method.")
        status = "FAILED"

#####################################
# Test playCard method (empty hand) #
#####################################
    message = "   Testing 'playCard' method with empty hand:"
    try:
        standardWP.playCard()
        print(f"{message:<{K}} {'FAILED'}")
        status = "FAILED"   
    except:
        print(f"{message:<{K}} {'PASSED'}")

#######################################
# Test prepareWar method (empty hand) #
#######################################
    message = "   Testing 'prepareWar' method with empty hand:"
    try:
        c = standardWP.prepareWar()
        if len(c) == 0:
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but return incorrect.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during prepareWar method.")
        status = "FAILED"        

#######################
# Test addCard method #
#######################       
    message = "   Testing 'addCard' method with a single card:"
    myDeck = DC()
    try:
        standardWP.addCard(myDeck.dealCard())
        print(f"{message:<{K}} {'PASSED'}")
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during addCard method.")
        status = "FAILED"

########################################
# Test hasCard method (non-empty hand) #
########################################
    message = "   Testing 'hasCard' method with non-empty hand:"
    try:
        if standardWP.hasCard():
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but return incorrect.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during hasCard method.")
        status = "FAILED"    

###############################################
# Test cardsRemaining method (non-empty hand) #
###############################################
    message = "   Testing 'cardsRemaining' method with non-empty hand:"
    try:
        if standardWP.cardsRemaining() == 1:
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but return incorrect.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during cardsRemaining method.")
        status = "FAILED"


#########################################
# Test playCard method (non-empty hand) #
#########################################
    message = "   Testing 'playCard' method with non-empty hand:"
    try:
        c = standardWP.playCard()
        if c.getFace() == "A" and c.getSuit() == "Clubs":
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but returned wrong card")
            status = "FAILED"  
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during cardsRemaining method.")
        status = "FAILED"

###############################################
# Test prepareWar method (fewer than 3 cards) #
###############################################
    message = "   Testing 'prepareWar' method with fewer than 3 cards:"
    standardWP.addCard(myDeck.dealCard())
    try:
        c = standardWP.prepareWar()
        if len(c) == 1:
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but return incorrect.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during prepareWar method.")
        status = "FAILED"   

#############################################
# Test prepareWar method (at least 3 cards) #
#############################################    
    message = "   Testing 'prepareWar' method with at least 3 cards:"
    standardWP.addCard(myDeck.dealCard())
    standardWP.addCard(myDeck.dealCard())
    standardWP.addCard(myDeck.dealCard())
    try:
        c = standardWP.prepareWar()
        if len(c) == 3:
            print(f"{message:<{K}} {'PASSED'}")
        else:
            print(f"{message:<{K}} {'FAILED'}")
            print(f"      Method executed, but return incorrect.")
            status = "FAILED"
    except:
        print(f"{message:<{K}} {'FAILED'}")
        print(f"      Exception during prepareWar method.")
        status = "FAILED"           
        
    if status == "PASSED":
        print("ALL TESTS PASSED!")
    else:
        print("At least one test failed.  Debug and try again")