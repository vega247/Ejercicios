import pygame
from pygame.locals import *
import sys

def drawGrid():
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(window, GRAY, rect, 1)

def drawFilledPoints():
    for element in filledPoints:
        x,y = element
        if y < WINDOW_HEIGHT:
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(window, BLACK, rect)

def button(x,y):
    rect = pygame.Rect(x, y, 120, 40)
    return pygame.draw.rect(window, GRAY, rect)


def liveOrDie():
    count = 0
    for element in filledPoints:
        count = 0
        x,y = element
        elementNeighborhood = [(x,y+blockSize),(x+blockSize,y+blockSize),(x+blockSize,y),(x+blockSize,y-blockSize)
        ,(x,y-blockSize),(x-blockSize,y-blockSize),(x-blockSize,y),(x-blockSize,y+blockSize)]
        for i in range(8):
            if elementNeighborhood[i] in filledPoints:
                count += 1
        if count == 2 or count == 3:
            life.add(element)
        else: 
            die.add(element)

def born():
    count = 0
    for element in neighbors:
        count = 0
        x,y = element
        elementNeighborhood = [(x,y+blockSize),(x+blockSize,y+blockSize),(x+blockSize,y),(x+blockSize,y-blockSize)
        ,(x,y-blockSize),(x-blockSize,y-blockSize),(x-blockSize,y),(x-blockSize,y+blockSize)]
        for i in range(8):
            if elementNeighborhood[i] in filledPoints:
                count += 1
        if count == 3: 
            life.add(element)

def Neighborhood():
    for element in filledPoints:
        x,y = element
        neighbors.add((x,y+blockSize))
        neighbors.add((x+blockSize,y+blockSize))
        neighbors.add((x+blockSize,y))
        neighbors.add((x+blockSize,y-blockSize))
        neighbors.add((x,y-blockSize))
        neighbors.add((x-blockSize,y-blockSize))
        neighbors.add((x-blockSize,y))
        neighbors.add((x-blockSize,y+blockSize))

BLACK = (0,0,0)
WHITE = (200,200,200)
GRAY = (100,100,100)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
blockSize = 10
filledPoints = set()
life = set()
neighbors = set()
die = set()
START = False
RATIO = 0
pygame.init()
font = pygame.font.SysFont("Arial", 25)
window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT+40))
clock = pygame.time.Clock()

while True:
    window.fill(WHITE)
    drawGrid()
    drawFilledPoints()
    startButton = button(0,480)
    window.blit(font.render("Start", True, WHITE),(25,485))
    stopButton = button(260,480)
    window.blit(font.render("Stop", True, WHITE),(285,485))
    resetButton = button(520,480)
    window.blit(font.render("Reset", True, WHITE),(545,485))
    x, y = (0,0)
    RATIO = RATIO + 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()
            if x < WINDOW_WIDTH and y < WINDOW_HEIGHT:
                x = x - x % blockSize
                y = y - y % blockSize
                con = (x,y)
                if con in filledPoints:
                    #erase the element in the filledPoints set
                    rect = pygame.Rect(x, y, blockSize, blockSize)
                    pygame.draw.rect(window, WHITE, rect)
                    filledPoints.remove(con)
                else:
                    filledPoints.add(con)
            elif x > startButton.left and x < startButton.right and y < startButton.bottom and y > startButton.top:
                START = True
            elif x > stopButton.left and x < stopButton.right and y < stopButton.bottom and y > stopButton.top:
                START = False
            elif x > resetButton.left and x < resetButton.right and y < resetButton.bottom and y > resetButton.top:
                START = False
                filledPoints = set()
    if START and RATIO % 10 == 0:
        Neighborhood()
        liveOrDie()
        born()
        filledPoints = filledPoints.union(life)
        filledPoints = filledPoints.difference(die)
        life = set()
        neightbors = set()
        die = set()
        RATIO = 0
    
    
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)

