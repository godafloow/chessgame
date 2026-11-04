#We define a general class that has a coordinates and a onBoard property
class chessman:
    def __init__(self,coordinates: tuple, onBoard: bool):
        self.coordinates = coordinates
        self.onBoard = onBoard

#Class Definition For The King Piece
class king(chessman):
    
    icon = """chessgame\\icons\\intro_ball.gif"""
    
    def __init__(self,coordinates, onBoard):
        super().__init__(coordinates, onBoard)
            
    
    
#Class Definition For The Queen Piece
class queen(chessman):
    def __init__(self, coordinates, onBoard):
        super().__init__(coordinates, onBoard)
    


#Class Definition For The Rook Piece
class rook(chessman):
    def __init__(self, coordinates, onBoard):
        super().__init__(coordinates, onBoard)
    

#Class Definition For The Bishop Piece
class bishop(chessman):
    def __init__(self, coordinates, onBoard):
        super().__init__(coordinates, onBoard)
    

#Class Definition For The Knight Piece
class knight(chessman):
    def __init__(self, coordinates, onBoard):
        super().__init__(coordinates, onBoard)
    
#Class Definition For The Pawn Piece
class pawn(chessman):
    def __init__(self, coordinates, onBoard):
        super().__init__(coordinates, onBoard)
        
