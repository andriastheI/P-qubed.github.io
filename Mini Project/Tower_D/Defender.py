from Tickable import Tickable
from Projectile import Projectile
from BG_Tile import BG_Tile

from PIL import Image, ImageTk

class Defender(Tickable):
    '''
    classdocs
    
    This class provides the basic framework for defender towers
    '''
    enemy_image = None
    @classmethod
    def _load_image(cls, filename):
        try:
            temp = Image.open(f"../img/{filename}.png")
            Defender.enemy_image = temp
        except FileNotFoundError:
            print(f"File '{filename}.png' is not found in the directory 'img'")
        except:
            print("Error occurred loading the image")
        return None

    def __init__(self, dmg = 1, ran = 160, refire = 25, proj_speed = 5):
        super().__init__()
        self._damage = dmg
        self._range = ran
        self._refire = refire
        self._projectile_speed = proj_speed
        self._ready_to_fire = True

        if Defender.enemy_image == None:
            Defender._load_image("Tower")

        temp = Defender.enemy_image
        resized_image = temp.resize((60, 60))
        self._image = ImageTk.PhotoImage(resized_image)
    
    def can_fire(self):
        return self._ready_to_fire
    
    def fire(self, target):
        # Generate a new projectile aimed at the targer.
        # Return the projectile so that it can be managed by the game controller.
        self._ready_to_fire = False
        p = Projectile(left = self._left + BG_Tile._base_size / 2, top = self._top + BG_Tile._base_size / 2)
        p.set_target(target)
        self.reset_count()
        return p
    
    def get_range(self):
        return self._range
      
    def render(self, cvs):
        self.unrender(cvs)
        t = self._top
        L = self._left
        s = BG_Tile._base_size - 2
        if self._image is not None:
            super().render(cvs)
        else:
            self._drawings.append(cvs.create_image(self._bound["left"]+L , self._bound["top"]+t, image = self._image, anchor = "nw"))
    
    def tic(self, step = 1):
        super().tic(step)
        
        # Determine whether the tower is ready to fire again.
        if self.get_count() > self._refire:
            self.reset_count()
            self._ready_to_fire = True
            
    def dist_to_target(self, target):
        # Compute the distance to the given target (using the standard distance formula)
        target_left, target_top = target.getCoords()
        dx = (target_left - self._left)
        dy = (target_top - self._top)
        dr = (dx**2 + dy**2)**(1/2)
        return dr    