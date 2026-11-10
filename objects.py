from pygame import *
from functions.miscFunctions import *
from functions.gridFunctions import *

#Gets The Resolution Of The Main Screen
width, height = getSize()[0], getSize()[1]

#We define a general class that has a coordinates and a onBoard property
class Chessman():
    def __init__(self, rect: Rect, onBoard: bool, isRival: bool):        

        #self.rect is in a format such as the two axis are two integers numbers from 1 to 8, and cover all posible combinations (simplified format).
        self.rect = rect
        self.rectConverted = Rect(rect[0]/(width//8)+1, rect[1]/(height//8)+1, rect[2], rect[3]) 
        self.onBoard = onBoard
        self.isRival = isRival
    
    def isCliked(self):
        """
        This functions determines if an object is clicked (True) or not (False)
        
        """
        
        (x, y) = self.rectConverted[0], self.rectConverted[1]
        
        if (x, y) == detRectCliked(): 
            self.clicked = True
            return True
        else: 
            self.clicked = False
            return False

    
    def movement(self):
        if detRectCliked() == None:
            return None
        
        if (detRectCliked()[0] in getSurRect(self.rectConverted)[0]) and (detRectCliked()[1] in getSurRect(self.rectConverted)[1]):
            self.rect = Rect(((detRectCliked()[0]-1)*(width//8), (detRectCliked()[1]-1)*(height//8)), (self.rect[2], self.rect[3]))
            self.rectConverted = Rect((detRectCliked()[0], detRectCliked()[1]), (self.rect[2], self.rect[3]))
        return None


#Class Definition For The King Piece
class King(Chessman):
    def __init__(self, rect=None, onBoard=None, isRival=None):
        super().__init__(rect, onBoard, isRival)
        
        self.icon = image.load("icons\\w_king.png").convert_alpha()
        self.icon = transform.scale(self.icon, (width//8,height//8))
        
    
    
#Class Definition For The Queen Piece
class Queen(Chessman):
    
    icon = "icons\\w_queen.png"
    
    def __init__(self, coordinates, onBoard):
        super().__init__(coordinates, onBoard)
    


#Class Definition For The Rook Piece
class Rook(Chessman):
    def __init__(self, coordinates, onBoard):
        super().__init__(coordinates, onBoard)
    

#Class Definition For The Bishop Piece
class Bishop(Chessman):
    def __init__(self, coordinates, onBoard):
        super().__init__(coordinates, onBoard)
    

#Class Definition For The Knight Piece
class Knight(Chessman):
    def __init__(self, coordinates, onBoard):
        super().__init__(coordinates, onBoard)
    
#Class Definition For The Pawn Piece
class Pawn(Chessman):
    def __init__(self, coordinates, onBoard):
        super().__init__(coordinates, onBoard)
        
