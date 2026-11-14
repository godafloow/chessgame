"""
THIS FILE CONTAINS GRID-RELATED FUNCTIONS

"""

from functions.miscFunctions import *
from pygame import *
from config import *

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
        gridPositions.append(tuple((i+1, t+1)))
    
def detRectCliked():
    """
    Detects What Grid Is Clicked with simplified format (integers ranging from 1 to 8)
    
    """
    
    if mouse.get_pressed()[0] != True:
        return None
    
    posMouse = mouse.get_pos()
    x=0
    y=0
    
    for i in widthPositions:
        if i >= posMouse[0]:
            break
        else:
            x = i 
            
    for i in heightPositions:
            if i >= posMouse[1]:
                break
            else:
                y = i
    
    return (x/(width//8)+1, y/(width//8)+1)


def getSurRect(rect):
    """
    This function returns a list of the surrounding Rects of another Rect (Seperated into X and Y axis) 
    in simplified format (integer numbers ranging from 1 to 8)
    
    """

    xAxis = []
    yAxis = []
    

    for i in range(3):
        if (rect[0]+(i) >= 0) and (rect[0]+(i) < 9): xAxis.append(rect[0]+(i-1))
        if (rect[1]+(i) >= 0) and (rect[1]+(i) < 9): yAxis.append(rect[1]+(i-1))  
    

    return [xAxis, yAxis]


currentColor = [100,100,100]
firstGo = False

def colorGradient():

    """
    This functions is reponsible for the change of color between two colors
    
    """

    global currentColor
    global firstGo

    

    if not firstGo:
        for i in range(3): 
            currentColor[i] += gradientSpeed[i]
    else:
        for i in range(3): 
            currentColor[i] -= gradientSpeed[i]

    if currentColor == secondColorGradient or currentColor == firstColorGradient:
            firstGo = not firstGo


    return currentColor[0], currentColor[1], currentColor[2] 

def clickFeedback(screen: Surface, rect: Rect):
    global width

    rectPositions=[]

    for i in range(8):
        rectPositions.append(((i*(width//8), rect[1]),(rect[2], rect[3])))
        rectPositions.append(((rect[0], (height//8)*i),(rect[2], rect[3])))

    for t in rectPositions:
        draw.rect(screen, colorGradient(), t)

    