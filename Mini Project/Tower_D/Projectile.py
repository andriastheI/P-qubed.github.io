from Tickable import Tickable
from BG_Tile import *

class Projectile(Tickable):
    '''
    classdocs
    
    This class provides the basic framework for projectiles
    '''       
    def __init__(self, left = 0, top = 0, dmg = 2):
        super().__init__(left, top)
        self._damage = dmg
        self._target = None  # The enemy that this projectile is targeting        
        
    def render(self, cvs):
        self.unrender(cvs)
        
        # Compute the scale of this projectile relative to the width of a background tile
        scale = BG_Tile._base_size / 6
        if self._target is not None:
            target_left, target_top = self._target.getCoords()
            # Compute the direction to the target.
            # Use that to determine the slope of the line between this projectile and the target
            # Draw the projectile accordingly
            dx = (target_left - self._left)
            dy = (target_top - self._top)
            dr = (dx**2 + dy**2)**(1/2)
            w = dx/dr * scale
            h = dy/dr * scale
            self._drawings.append(cvs.create_line(self._left, self._top, self._left + w, self._top + h, fill = 'black'))
    
    def tic(self, step = 1):
        scale = step * BG_Tile._base_size / 6
        if self._target is not None:
            target_left, target_top = self._target.getCoords()
            # Compute the direction to the target.
            # Use that to determine the slope of the line between this projectile and the target
            # Set the left and top coordinates accordingly
            dx = (target_left - self._left)
            dy = (target_top - self._top)
            dr = (dx**2 + dy**2)**(1/2)
            w = dx/dr * scale
            h = dy/dr * scale
            self._left += w
            self._top += h
    
    def has_target(self):
        return self._target is not None
    
    def get_target(self):
        return self._target
    
    def set_target(self, target):
        self._target = target
    
    def hit_target(self):
        self._target.take_damage(self._damage)
    
    def dist_to_target(self):
        # Compute the distance to the target.
        if self.has_target():
            target_left, target_top = self._target.getCoords()
            dx = (target_left - self._left)
            dy = (target_top - self._top)
            dr = (dx**2 + dy**2)**(1/2)
            return dr
        else:
            return 0