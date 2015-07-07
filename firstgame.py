import pygame,sys
from pygame.locals import*

pygame.init()

#set up the window
DISPLAYSURF = pygame.display.set_mode((800, 600),0,32)
pygame.display.set_caption("Tuan yeu Thuy Anh nhieu lam")

#set up the color
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

#draw on the surface object
DISPLAYSURF.fill(WHITE)
#pygame.draw.polygon(DISPLAYSURF, GREEN, ((100,10), (160,10), (130,10), (130,40)))
#pygame.draw.polygon(DISPLAYSURF, GREEN, ((210,10),(220,10),(220,30),(240,30),(240,10),(250,10),(250,60),(240,60),(240,40),(220,40),(220,60),(210,60)))
#pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)

#pygame.draw.line(DISPLAYSURF, BLUE, (90, 60), (90, 100), 4)

#pygame.draw.line(DISPLAYSURF, BLUE, (130, 60), (130, 100), 4)

#pygame.draw.line(DISPLAYSURF, BLUE, (130, 80), (150, 80), 4)

#pygame.draw.line(DISPLAYSURF, BLUE, (150, 60), (150, 100), 4)

#pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
#pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)

#pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)
#pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)
#pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))


pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj

while True: #main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()
