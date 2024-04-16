from Drawable import Drawable
from PIL import Image, ImageTk
import random
class BG_Tile(Drawable):
    '''
    classdocs
    This class defines background tiles for the game.
    These tiles could contain one of six different road types, or they could be 'empty'.
    
    This class also provides the parameter "_base_size", which is used to scale other objects for the screen.
    '''
    Background_image = None
    @classmethod
    def _load_image(cls,filename):
        try:
            temp = Image.open(f"../img/{filename}.png")
            BG_Tile.Background_image = temp
        except FileNotFoundError:
            print(f"File '{filename}.png' is not found in the directory 'img'")
        except:
            print("Error occurred loading the image")
        return None

    _base_size = 60
    _types = {"Road-H":0, "Road-V":1, "Road-L1":2, "Road-L2":3,"Road-L3":4,"Road-L4":5,"Empty":6,"Building":7}
    
    def __init__(self, left = 0, top = 0, tile_type = None):
        super().__init__()
        self._type = tile_type
        self._width = BG_Tile._base_size
        self._height = BG_Tile._base_size
        self._top = top
        self._left = left
        self._image = []
        if BG_Tile.Background_image == None:
            BG_Tile._load_image("Casttle")
        temp = BG_Tile.Background_image
        resized_img = temp.resize((80,80))
        self._image.append(ImageTk.PhotoImage(resized_img))

    def removebuilding(self):
        loc = random.choice(self._castle)
        self._castle.remove(loc)

    def render(self, cvs):
        # Remove all previously drawn components of this object
        self.unrender(cvs)
        t = self._top
        L = self._left
        w = self._width
        h = self._height





        cvs.create_rectangle( L, t, L + w, t + h, fill = 'green', outline = "")
        
        if self._type == 0:
            # Horizontal road segment
            cvs.create_rectangle( L, t + h/3, L + w, t + 2*h/3, fill = 'khaki1', outline = "")
        elif self._type == 1:
            # Vertical road segment
            cvs.create_rectangle( L + w/3, t, L + 2*w/3, t + h, fill = 'khaki1', outline = "")
        elif self._type == 2:
            # Road segment connecting left side and top side
            cvs.create_polygon( L, t + h/3, 
                                L, t + 2*h/3, 
                                L + 2*w/3, t + 2*h/3, 
                                L + 2*w/3, t,
                                L + w/3, t,
                                L + w/3, t + h/3, fill = 'khaki1', outline = "" )
        elif self._type == 3:
            # Road segment connecting top side to right side
            cvs.create_polygon( L + w/3, t, 
                                L + 2*w/3, t, 
                                L + 2*w/3, t + h/3, 
                                L + w, t + h/3,
                                L + w, t + 2*h/3,
                                L + w/3, t + 2*h/3, fill = 'khaki1', outline = "" )
        elif self._type == 4:
            # Road segment connecting right side to bottom side.
            cvs.create_polygon( L + w/3, t + h, 
                                L + w/3, t + h/3, 
                                L + w, t + h/3, 
                                L + w, t + 2*h/3,
                                L + 2*w/3, t + 2*h/3,
                                L + 2*w/3, t + h, fill = 'khaki1', outline = "" )
        elif self._type == 5:
            # Road segment connecting bottom side to left side.
            cvs.create_polygon( L, t + h/3,
                                L, t + 2*h/3,
                                L + w/3, t + 2*h/3,
                                L + w/3, t + h,
                                L + 2*w/3, t + h,
                                L + 2*w/3, t + h/3, fill = 'khaki1', outline = "" )
        elif self._type == 7:
            loca = [(160, 110), (280, 230), (280, 350), (400, 470), (40, 290), (40, 400), (280, 50), (400, 50),
                    (460, 170)]
            # Fill this object's rectangle solid green.
            self._castle = []
            self._castle.extend(loca)
            for location in self._castle:
                building = cvs.create_image(location, image=self._image, anchor="nw")
        else:
            # Ordinary background tile with no road.
            cvs.create_rectangle( L+1, t+1, L + w-1, t + h-1, fill = '', outline = "black")