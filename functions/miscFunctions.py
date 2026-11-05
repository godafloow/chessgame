from random import randint
import screeninfo as sc

def colorChooser():
    random_number = randint(0,1)
    if random_number == 1:
        return True
    else:
        return False
    
    
def getSize():
    for m in sc.get_monitors():
        if m.is_primary == True:
            if m.height < m.width:
                height = m.height//1.5
                width = m.height//1.5
            else:
                height = m.width//1.5
                width = m.width//1.5
    return (width, height)
                        