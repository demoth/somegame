'''
Required code cleanup and decent variable naming
Author: Sorseg, Demoth
'''
import pygame
import sys
import math

def rotate(vector, center, angle):
    '''todo rotation around center'''
    r = (vector[0] - center[0], vector[1] - center[1])
    x = r[0] * math.cos(angle) - r[1] * math.sin(angle)
    y = r[0] * math.sin(angle) + r[1] * math.cos(angle)
    r = (x + center[0], y + center[1])
    return r

def drawSerpinskiCarpet(window, pos, size, n):
    ''' Recursive algorythm, parameters are pretty self explanatory '''
    if n > 0:
        size /= 3
        rect = pygame.Rect(pos[0] - size / 2, pos[1] - size / 2, size, size)
        coolColour = (pos[0] * size % 255, pos[1] * size % 255, pos[1] * pos[0] % 255)
        pygame.draw.rect(window, coolColour, rect)
        drawSerpinskiCarpet(window, (pos[0] + size, pos[1] + size), size, n - 1)
        drawSerpinskiCarpet(window, (pos[0] + size, pos[1] - size), size, n - 1)
        drawSerpinskiCarpet(window, (pos[0] + size, pos[1]), size, n - 1)
        drawSerpinskiCarpet(window, (pos[0] - size, pos[1] + size), size, n - 1)
        drawSerpinskiCarpet(window, (pos[0] - size, pos[1] - size), size, n - 1)
        drawSerpinskiCarpet(window, (pos[0] - size, pos[1]), size, n - 1)
        drawSerpinskiCarpet(window, (pos[0] , pos[1] + size), size, n - 1)
        drawSerpinskiCarpet(window, (pos[0] , pos[1] - size), size, n - 1)

def drawLevyFractal(window, a, b, n, angle=90):
    
    if n == 0:
        pygame.draw.line(window, foreground, a, b)
    else:
        center = ((a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0)
        c = rotate(a, center, angle)
        drawLevyFractal(window, c, b, n - 1, angle)
        drawLevyFractal(window, a, c, n - 1, angle)
        
def drawPythagorasTree(window, a, b, n, angle):     
    if n == 0:
        pygame.draw.line(window, foreground, a, b)
    else:
        r = ((b[0] - a[0])  + (a[0] + b[0]) / 2.0, (b[1] - a[1])  + (a[1] + b[1]) / 2.0)
        c1 = rotate(r, b, angle)
        c2 = rotate(r, b, -angle)
        pygame.draw.line(window, foreground, a, b)
        drawPythagorasTree(window, b, c1, n - 1, angle)
        drawPythagorasTree(window, b, c2, n - 1, angle)

def drawWindedPythagorasTree(window, a, b, n, angle):
    ''' TODO WINDED PYTHAGORAS TREEE '''     
    if n == 0:
        pygame.draw.line(window, foreground, a, b)
    else:
        r = ((b[0] - a[0])  + (a[0] + b[0]) / 2.0, (b[1] - a[1])  + (a[1] + b[1]) / 2.0)
        c1 = rotate(r, b, angle)
        c2 = rotate(r, b, -angle)
        pygame.draw.line(window, foreground, a, b)
        drawPythagorasTree(window, b, c1, n - 1, angle)
        drawPythagorasTree(window, b, c2, n - 1, angle)    

def update(coord,center,vel,k):
    '''
    Hooke's Law
    '''
    vel += -k*(coord - center)
    vel /= 1.01
    coord += vel
    return coord,vel        
    
if __name__ == '__main__':
    pygame.init()
    # create the screen
    width = 800
    height = 800
    centerX = width / 2
    centerY = height / 2
    window = pygame.display.set_mode((width, height))
    # some colours  
    foreground = (255, 255, 255)
    background = (0,0,0)
    # mouse capture
    mousePos = (0,0)
    # FUCK! cannot find proper name for this
    savedX = 0
    # we want this to happen once
    needToSetMouse = False
    # mathematical part
    # size
    size = 100 
    # balance point
    x0 = math.pi/2.0
    # velocity
    v = 0;
    # the coordinate (angle)
    x = 1.0
    # some sort of frequency
    k = 0.001
    while True:
        window.fill(background)
        # recalculate
        # if mouse is not pressed - simply recalculate
        # else - use mouse position to set new coordinate value 
        if not pygame.mouse.get_pressed()[0]:
            x,v = update(x,x0,v,k)
            needToSetMouse = True
        else:
            if needToSetMouse:
                mousePos = pygame.mouse.get_pos()
                savedX = x
                needToSetMouse = False
            else:
                x = ((pygame.mouse.get_pos()[0] - mousePos[0]))/100.0 + savedX             
            v = 0.0
            
        #redraw
        #drawLevyFractal(window, (centerX - size, centerY), (centerX + size, centerY), 6, x)
        #drawPythagorasTree(window, (centerX, centerY + size), (centerX, centerY - size), 6, x)
        drawWindedPythagorasTree(window, (centerX, centerY + size), (centerX, centerY - size), 6, x)
        pygame.display.flip()
        
        for event in pygame.event.get(): 
            if event == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                sys.exit(0)

