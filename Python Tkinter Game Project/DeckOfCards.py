'''
Created on Feb 8, 2022

@author: twendt
'''

from PIL import Image, ImageTk
from Card import Card
import random

class DeckOfCards(object):
    '''
    classdocs
    '''
    size = 52
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cardImages = None
    width = 0
    height = 0
    @classmethod # changes the class method self to cls
    def loadCardImages(cls, filename):
        try:
            DeckOfCards.cardImages = Image.open(f"../img/{filename}")
            DeckOfCards.width, DeckOfCards.height = DeckOfCards.cardImages.size
            DeckOfCards.width //= 13
            DeckOfCards.height //= 5
            
        except FileNotFoundError:
            print(f"File '{filename}' cannot be found in the directory '../img'.")
        except:
            print("An error occurred loading your image")
            
    @classmethod
    def __loadImage(self, row, col):
        '''
        preconditions: 
          * The class 'cardImages' file has been opened.
          * The image for the deck has the cards arranged in 13 rows and 4 columns.
          * The columns are ordered A-2-3-4-...-J-Q-K
          * The rows are ordered Clubs-Diamonds-Hearts-Spades
          * The 'back' image for the cards is in the fifth row in the third column (i.e row = 4, col = 2)
        postconditions:
          * The 'cropped' image for this card is returned.
        '''
        assert DeckOfCards.cardImages is not None
        assert DeckOfCards.width > 0
        assert DeckOfCards.height > 0

        img = DeckOfCards.cardImages.crop((col*DeckOfCards.width, 
                                           row*DeckOfCards.height,
                                           (col + 1)*DeckOfCards.width,
                                            (row + 1)*DeckOfCards.height))
        t = ImageTk.PhotoImage(img)
        return t    
            
    def __init__(self, deckImages = None):
        '''
        Constructor
        '''
        if deckImages is not None:
            DeckOfCards.loadCardImages(deckImages)
            self.backOfCard = Card(None, None, 0, DeckOfCards.__loadImage(4, 2))
        else:
            self.backOfCard = None
            
        # Create a deck
        self.__cards = []
        self.currentCard = 0
        for i in range(len(DeckOfCards.faces)):
            for j in range(len(DeckOfCards.suits)):
                face = DeckOfCards.faces[i]
                suit = DeckOfCards.suits[j]
                value = i
                if deckImages is not None:
                    img = DeckOfCards.__loadImage(j, i)
                else:
                    img = None
                
                card = Card(face, suit, value, img)
                
                 
                self.__cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.__cards)

    def dealCard(self):
        if not self.isEmpty():
            c = self.__cards[self.currentCard]
            self.currentCard += 1
        else:
            c = None
        return c
        
    def cardsRemaining(self):
        return len(self.__cards) - self.currentCard
    
    def isEmpty(self):
        return self.cardsRemaining() == 0
    
    def hasNext(self):
        return not self.isEmpty()
    
    def reset(self):
        self.currentCard = 0