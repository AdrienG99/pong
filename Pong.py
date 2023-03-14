#By Adrien Grant Jr (A00425511)

import pygame, random
pygame.init()

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

#Variables
y = 180
bx = 310
by = 230
speed = [random.choice([-5,5]),random.choice([-5,5])]
cS = 0
pS = 0
introcol = WHITE
endcol = BLACK

#Screen
size = (640,480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong! By Adrien Grant (A00425511)")


#Main program
running = True
started = False
clock = pygame.time.Clock()

while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
            pygame.quit()
    screen.fill(BLACK)

    #text
    font = pygame.font.SysFont("Calibri", 36)
    font1 = pygame.font.SysFont("Ravie", 72)
    font2 = pygame.font.SysFont("Ravie", 24)
    compScore = font.render(str(cS), True, WHITE)
    screen.blit(compScore,(50,50))
    plrScore = font.render(str(pS), True, WHITE)
    screen.blit(plrScore,(590,50))
    intro = font1.render("PONG!",True, introcol)
    screen.blit(intro,(200,50))
    start = font2.render("Press Enter to Start...", True, introcol)
    screen.blit(start,(150,240))
    loss = font1.render("You Lost!", True, endcol)
    win = font1.render("You Won!", True, endcol)
    retry = font2.render("Press N to replay...", True, endcol)
    end = font2.render("Press X to close game...", True, endcol)
    screen.blit(retry,(150,200))
    screen.blit(end,(150,280))
   
    pressed = pygame.key.get_pressed()
   
    if pressed[pygame.K_RETURN]:
        started = True
        introcol = BLACK

    if started:
        #user movement
        if pressed[pygame.K_UP]: y -= 5
        if pressed[pygame.K_DOWN]:y += 5
        if y > 360: y = 360
        if y < 0: y = 0

    #ball movement
        bx += speed[0]
        by += speed[1]
       
    if by < 10 or by > 470: speed[1] = -speed[1]
    if bx < 10:
         bx = 310
         by = 230
         speed[0] = -speed[0]
         pS += 1

    if bx > 630:
         bx = 310
         by = 230
         speed[0] = -speed[0]
         cS += 1

    if cS == 15:
        started = False
        endcol = WHITE
        screen.blit(loss,(100,50))

    if pS == 15:
        started = False
        endcol = WHITE
        screen.blit(win,(100,50))

    if not started:
        if pressed[pygame.K_n]:
            endcol = BLACK
            introcol = WHITE
            cS = 0
            pS = 0
        elif pressed[pygame.K_x]:
            pygame.quit()
       
   
   
   
    comp = pygame.draw.rect(screen, BLUE, (10, by-60, 15, 120))
    user = pygame.draw.rect(screen, RED, (615,y,15,120))
    ball = pygame.draw.rect(screen, GREEN, (bx,by,10,10))

    #collision
    if ball.colliderect(comp):
        speed[0] = -speed[0]

    if ball.colliderect(user):
        speed[0] = -speed[0]

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)


pygame.quit()
