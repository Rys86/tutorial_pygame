import pygame, sys

pygame.init()
res = (1280,720)
screen =  pygame.display.set_mode(res)
box = pygame.Rect(10,10,50,50)
x = 10

while True:
    # Handle Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
            # box.x += 100


    # Checking Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        box.x += 1
    if keys[pygame.K_a]:
        box.x -= 1
    if keys[pygame.K_w]:
        box.y -= 1
    if keys[pygame.K_s]:
        box.y += 1

    # Drawing
    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0,150,255), box )
    pygame.display.flip()