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

def drawLineFractal(window, a, b, n, angle=90):
    
    if n == 0:
        pygame.draw.line(window, colour, a, b)
    else:
        center = ((a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0)
        c = rotate(a, center, angle)
        drawLineFractal(window, c, b, n - 1, angle)
        drawLineFractal(window, a, c, n - 1, angle)
        
def drawPeeFagOrTree(window, a, b, n, angle, length):     
    if n == 0:
        pygame.draw.line(window, colour, a, b)
    else:
        r = ((b[0] - a[0]) * length + (a[0] + b[0]) / 2.0, (b[1] - a[1]) * length + (a[1] + b[1]) / 2.0)
        c1 = rotate(r, b, angle)
        c2 = rotate(r, b, -angle)
        pygame.draw.line(window, colour, a, b)
        drawPeeFagOrTree(window, b, c1, n - 1, angle, length)
        drawPeeFagOrTree(window, b, c2, n - 1, angle, length)
    
        
    
if __name__ == '__main__':
    pygame.init()
    #create the screen
    window = pygame.display.set_mode((800, 800)) 
    colour = (255, 255, 255)
    #drawSerpinskiCarpet(window, (400, 400), 800, 5)
    #draw it to the screen
    
    #input handling (somewhat boilerplate code):
    #drawMandelbrot(window, 0.6 + 0.6j, 100)
    pygame.display.flip()
    while True:
        window.fill((0, 0, 0)) 
        drawPeeFagOrTree(window, (400, 750), (400, 600),12,
                         pygame.mouse.get_pos()[1] / 50.0,
                         0.7+pygame.mouse.get_pos()[0] / 400.0)
        pygame.display.flip()
        
        for event in pygame.event.get(): 
            if event == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                sys.exit(0)

