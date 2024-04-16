
import tkinter

class Drawable(object):
    '''
    classdocs
    '''
    def __init__(self, left = 0, top = 0):
        '''
        Constructor
        '''
        self._image = None      # A tkinter image 
        self._left = left       # The left-most coordinate of this object
        self._top = top         # The top-most coordinate of this object
        self._drawings = []     # A collection of all of the parts of this object that
                                # have been drawn to the canvas.  
    
    def getCoords(self):
        return (self._left, self._top)
    
    def moveTo(self, newLeft, newTop):
        self._left = newLeft
        self._top = newTop
    
    def setImage(self, img):
        self._image = img
    
    def render(self, cvs):
        # First, remove all of the previous drawings of this object from the canvas
        for d in self._drawings:
            cvs.delete(d)
        
        # Render this object's image if there is one.
        if self._image is not None:
            self._drawings.append(cvs.create_image(self._left, self._top, image = self._image, anchor = "nw"))
            
    def unrender(self, cvs):
        for d in self._drawings:
            cvs.delete(d) 