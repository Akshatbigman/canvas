import pygame
from pygame.locals import QUIT

pygame.init()
window = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Paint')

#colours
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
red = (255, 0, 0)
grey = (128, 128, 128)
blue = (0, 0, 255)

#window dimension
window_height = 300
window_width = 400
toolbar_height = 50

#bg
canvas = pygame.Surface((400,300))
canvas.fill(white)

#variables
brush_colour = black
brush_size=2
min_brush_size = 1 
max_brush_size = 10 
drawing = False
eraser_mode = False
last_position = None

#surface for toolbar
toolbar = pygame.Surface((window_width, toolbar_height))
toolbar.fill(grey)




running = True
while running:
    #draw toolbar
    toolbar.fill(grey)
    #Pen
    fontP = pygame.font.Font(None, 24)
    pentext = fontP.render('P', True, white)

    #Eraser
    fontE = pygame.font.Font(None, 50)
    penEraser = fontE.render('E', True, white)

    toolbar.blit(pentext, (40, 20))
    toolbar.blit(penEraser, (80, 20))

    #decrease, increase
    fontD = pygame.font.Font(None, 36)
    decreaseText = fontD.render('-', True, white)

    fontI = pygame.font.Font(None, 36)
    increaseText = fontI.render('+', True, white)

    toolbar.blit(decreaseText, (120, 20))
    toolbar.blit(increaseText, (160, 20))

    #clear
    fontC = pygame.font.Font(None, 36)
    clearText = fontC.render('C', True, white)

    toolbar.blit(clearText, (200, 20))
        
    #color
    colour_width, colour_height = 20,20
    blue_buttn = pygame.draw.circle(toolbar,blue, (285,25), colour_width//2 , colour_height//2)

    red_buttn = pygame.draw.circle(toolbar,red, (305,25), colour_width//2, colour_height//2)

    green_buttn = pygame.draw.circle(toolbar,green, (325,25), colour_width//2, colour_height//2)

    yellow_buttn = pygame.draw.circle(toolbar,yellow, (345,25), colour_width//2, colour_height//2)

    window.fill(white)

    #drawing canvas and toolbar on window
    window.blit(toolbar, (0,0))
    window.blit(canvas, (0,toolbar_height))

    #events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        #mouse events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[1] <= toolbar_height:
                pen = pentext.get_rect(topleft=(40,20))
                
                eraser = penEraser.get_rect(topleft=(80,20))
                
                increase = increaseText.get_rect(topleft=(160,20))
                
                decrease = decreaseText.get_rect(topleft=(120,20))
                
                clear = clearText.get_rect(topleft=(200,20))
                                
                if pen.collidepoint(event.pos):
                    eraser_mode = False
                elif eraser.collidepoint(event.pos):
                    eraser_mode = True
                elif increase.collidepoint(event.pos):
                    brush_size = brush_size + 5
                elif decrease.collidepoint(event.pos):
                    brush_size = brush_size - 5
                elif clear.collidepoint(event.pos):
                    canvas.fill(white)
                elif blue_buttn.collidepoint(event.pos):
                    brush_colour = blue
                elif red_buttn.collidepoint(event.pos):
                    brush_colour = red
                elif green_buttn.collidepoint(event.pos):
                    brush_colour = green
                elif yellow_buttn.collidepoint(event.pos):
                    brush_colour = yellow
                
                
            else:
                drawing = True
                last_position = (event.pos[0], event.pos[1]-toolbar_height)
                
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_position = None
        
        elif event.type == pygame.MOUSEMOTION and drawing:
            color = brush_colour if not eraser_mode else white
            last_position = (event.pos[0], event.pos[1]-toolbar_height)
            
            pygame.draw.line(canvas, color, last_position, event.pos, brush_size)
            last_position = (event.pos[0], event.pos[1]-toolbar_height)
            
    pygame.display.flip()
pygame.quit()

