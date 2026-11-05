"""
THIS FILE CONTAINS GRID-RELATED FUNCTIONS

"""

from functions.miscFunctions import *


gridPositions=[]
width, height = getSize()[0], getSize()[1] 

for i in range(8):
    #width_positions.append((i)*width//8)
    for t in range(8):
        #height_positions.append((t)*height//8)
        gridPositions.append(tuple(((i)*width//8, (t)*height//8)))
    
