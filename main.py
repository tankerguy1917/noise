import pygame, noise, random
from pygame.locals import *
pygame.init()


WIN = (700, 420)
screen = pygame.display.set_mode(WIN, 0, 32)
clock = pygame.time.Clock()


zoom = 0.01
terrain = True


rect_list = []


def gen_map():
    for x in range(WIN[0]):
        for y in range(WIN[1]):
            temp = []
            n = noise.pnoise2(x * zoom, y * zoom, octaves=15, persistence=0.5)
            temp.append(pygame.Rect(x, y, 1, 1))
            temp.append(n)
            rect_list.append(temp)


gen_map()


while terrain == False:
    screen.fill((0, 0, 0))

    for x in rect_list:
        pygame.draw.rect(screen, (255 * abs(x[1]), 255 * abs(x[1]), 255 * abs(x[1])), x[0])

    pygame.display.update()
    clock.tick(60)


while terrain == True:
    screen.fill((0, 0, 0))

    for x in rect_list:
        if x[1] < 0.01: # WATER
            pygame.draw.rect(screen, (20, 20, 255), x[0])
        elif x[1] > 0.01 and x[1] < 0.04: # SAND
            pygame.draw.rect(screen, (194, 178, 128), x[0])
        elif x[1] > 0.3 and x[1] < 0.35: # MOUNTAIN
            pygame.draw.rect(screen, (100, 100, 100), x[0])
        elif x[1] > 0.35: # SNOW
            pygame.draw.rect(screen, (255, 255, 255), x[0])
        else: # TREE
            pygame.draw.rect(screen, (20, 255, 20), x[0])

    pygame.display.update()
    clock.tick(60)