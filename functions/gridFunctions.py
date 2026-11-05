"""
THIS FILE CONTAINS GRID-RELATED FUNCTIONS

"""

from functions.miscFunctions import *
from pygame import mouse


#Not A Function But I Have My Code Already Adapted To This And Im Lazy
gridPositions=[]
widthPositions=[]
heightPositions=[]

width, height = getSize()[0], getSize()[1] 

for i in range(8):
    widthPositions.append((i)*width//8)
    for t in range(8):
        if len(heightPositions) != 8:
            heightPositions.append((t)*height//8)
        gridPositions.append(tuple(((i)*width//8, (t)*height//8)))
    
def detRectCliked():
    """
    Detects What Grid Is Clicked
    
    """
    
    if mouse.get_pressed()[0] != True:
        return None
    
    posMouse = mouse.get_pos()
    x=0
    y=0
    
    for i in widthPositions:
        if i > posMouse[0]:
            break
        else:
            x = i 
            
    for i in heightPositions:
            if i > posMouse[1]:
                break
            else:
                y = i
    
    return (x, y)