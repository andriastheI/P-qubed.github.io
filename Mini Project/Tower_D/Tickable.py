from Drawable import Drawable

class Tickable(Drawable):
    '''
    classdocs
    
    This class provides the basic framework for all objects that have their own timer.
    That includes enemies that move at a given rate, defense structures that fire projectiles, etc.
    '''
    def __init__(self, left = 0, top = 0):
        super().__init__(left, top)
        self._counter = 0

    def tic(self, step = 1):
        self._counter += step
        
    def get_count(self):
        return self._counter
    
    def reset_count(self):
        self._counter = 0