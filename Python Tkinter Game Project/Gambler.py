'''
Created on Feb 20, 2024

@author: andri
'''
import tkinter as tk

class GB(object):
    '''
    classdocs
    '''


    def __init__(self,name = None, parent = None, back=None, status = False, money = None):
        '''
        Constructor
        '''
        self.__name = name
        self.__cards = []
        self.__parent = parent
        self.__frame = None
        self.__canvas = None
        self.__back_of_card = back
        self.__dealer = status 
        self.__money = money

        
    def setBack(self, back):
        '''
        Description: Assigns the self.__back to Back(to draw the back of the cards)
        Arguments:  back(boolean value)
        Return:     None
        '''
        self.__back_of_card =  back
        
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
        
    def setName(self,new_name):
        '''
        Description: Used to assign a new name
        Arguments:  new_name
        Return:     None
        '''
        self.__name = new_name
        
    def getName(self):
        '''
        Description: Used to access the name of the class
        Arguments:  None
        Return:     self.__name(assigned name of the class)
        '''
        return self.__name
    def getCard(self):
        '''
        Description: Used to access the cards of the class
        Arguments:  None
        Return:     self.__cards(assigned cards of the class)
        '''
        return self.__cards
    
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

    def render(self):
        '''
        Description: Used to draw from the classes hand to the canvas
        Arguments:  None
        Return:     None
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
        Arguments:  None
        Return:     a Frame
        '''
        if self.__frame == None:
            # No frame yet.  Let's make one.
            self.__frame = tk.LabelFrame(self.__parent, text = self.getName())
            self.__canvas = tk.Canvas(self.__frame, width = 300, height = 200)
            self.__canvas.grid(row = 0, column = 0, padx = 5, pady = 5)
        
        return self.__frame
    
    def get_newValue(self,card):
        '''
        Description: Used to assigned new value to cards in the game
        Arguments:  card(the cards)
        Return:     returns their new assigned value
        '''
        val = {"A":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
        for key,value in val.items():
            if card.getFace() == key:
                Value = value
        return Value
    
    def getCanvas(self):
        '''
        Description: used to access the classes canvas
        Arguments:  None
        Return:     self.__canvas
        '''
        return self.__canvas
    
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
    
    def __str__(self):
        return f"{self.__name}'s cards:\n" + '\n'.join(str(card) for card in self.__cards)   

if __name__ == "__main__":
    
    status = "PASSED"
    K = 60

    print("Testing functionality of Gambler class.")
############################
# Test default constructor #
############################
    message = "   Testing default constructor:"
    try:
        defaultSwimTime = GB()
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
        standard = GB(name = "The-Flash")
        if standard.getName() == "The-Flash":
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
# Test setFrame method #
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
    
    
    
    
    
    
        