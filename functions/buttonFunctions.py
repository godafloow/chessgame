from pygame import Rect
from pygame.mouse import get_pos, get_pressed

def clickButton(rect: Rect):
    """
    You give throw Rect argument and it tells you if the mouse has been clicked in that area
    """
 
    if (rect[0] < get_pos()[0] < rect[0] + rect[2]) and (rect[1] < get_pos()[1] < rect[1] + rect[3]) and (get_pressed()[0] == True):
        return True
    else:
        return False
    