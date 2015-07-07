import pygame, sys, time
from pygame.locals import *

pygame.init()

FPS = 60 #frames per second setting
fpsClock = pygame.time.Clock()

#Setting up window
DISPLAYSURF = pygame.display.set_mode((600,300)) 
pygame.display.set_caption('Tuan yeu Thuy Anh')

WHITE = (255,255,255)
GREEN = (0,255,0)
BLUE = (0,0,128)

fontObj = pygame.font.Font('freesansbold.ttf',32)
textSurfaceObj = fontObj.render('Tuan yeu Thuy Anh nhieu lam',True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (300,150)
textSurfaceX = 10
textSurfaceY = 10
direction = 'right'




while True: #main game loop
    DISPLAYSURF.fill(WHITE)
    pygame.mixer.music.load('mop.mp3') #sound obj
    pygame.mixer.music.play(-1, 0.0)
    
    if direction == 'right':
        textSurfaceX += 5
        if textSurfaceX == 110:
            direction = 'down'
    elif direction == 'down':
        textSurfaceY += 5
        if textSurfaceY == 220:
            direction = 'left'
    elif direction == 'left':
        textSurfaceX -=5
        if textSurfaceX == 10:
            direction = 'up'
    elif direction == 'up':
        textSurfaceY -= 5
        if textSurfaceY == 10:
            direction = 'right'
            
    DISPLAYSURF.blit(textSurfaceObj, (textSurfaceX,textSurfaceY))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            pygame.mixer.music.stop()
    pygame.display.update()
    fpsClock.tick(FPS)
