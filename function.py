import pygame
from screen import screen
from color import *
from object import sq1, sq2, sq3, sq4, sq5, sq6, sq7, sq8, sq9
from constans import CORDS, HALF_TILE


def show():
    pygame.draw.rect(screen, white, sq1)
    pygame.draw.rect(screen, white, sq2)
    pygame.draw.rect(screen, white, sq3)
    pygame.draw.rect(screen, white, sq4)
    pygame.draw.rect(screen, white, sq5)
    pygame.draw.rect(screen, white, sq6)
    pygame.draw.rect(screen, white, sq7)
    pygame.draw.rect(screen, white, sq8)
    pygame.draw.rect(screen, white, sq9)

def circle(i):
    row, col = i // 3, i % 3
    x = int(CORDS[col] + HALF_TILE)
    y = int(CORDS[row] + HALF_TILE)
    pygame.draw.circle(screen, red, (x, y), HALF_TILE - 10, 7)

def cross(i):
    row, col = i // 3, i % 3
    x = int(CORDS[col] + HALF_TILE)
    y = int(CORDS[row] + HALF_TILE)
    pygame.draw.line(screen, blue, (x - HALF_TILE + 10, y - HALF_TILE + 10), (x + HALF_TILE - 10, y + HALF_TILE - 10), 7)
    pygame.draw.line(screen, blue, (x - HALF_TILE + 10, y + HALF_TILE - 10), (x + HALF_TILE - 10, y - HALF_TILE + 10), 7)