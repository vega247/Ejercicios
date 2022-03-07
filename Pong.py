import pygame
from pygame.locals import *
import pygwidgets
import sys

BLACK = (0,0,0)
WHITE = (200,200,200)
GRAY = (100,100,100)
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 60


class Player():
    def __init__(self,x,y,speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.movement = 0 
        self.width = 20
        self.height = 120

    def ScreenLimits(self):
        if self.y < 0:
            self.y = 0
        elif (self.y + self.height) >  WINDOW_HEIGHT:
            self.y = WINDOW_HEIGHT - self.height

    def draw(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(window, WHITE, rect)

#TODO Oponente
        

#TODO Ball

class Ball():
    #Iniciar en el centro, colisiones
    def __init__(self):
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.speed = 7
        self.radius = 10

    def move(self):
        self.x = self.x + self.speed

    def draw(self):
        pygame.draw.circle(window, WHITE, (self.x,self.y), self.radius)
#TODO marcadores 


if __name__ == "__main__":
    pygame.init()
    font = pygame.font.SysFont("Arial", 25)
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    oRightPalete = Player(WINDOW_WIDTH - 20, (WINDOW_HEIGHT - 120)//2,5)
    oLeftPalete = Player(0,(WINDOW_HEIGHT - 120)//2,5)
    oBall = Ball()
    while True:
        window.fill(BLACK)
        oRightPalete.draw()
        oLeftPalete.draw()
        oBall.draw()
        pygame.draw.rect(window, WHITE, pygame.Rect((WINDOW_WIDTH // 2) - 1, 0, 1, WINDOW_HEIGHT))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_UP:
                    oRightPalete.movement -= oRightPalete.speed
                if event.key == K_DOWN:
                    oRightPalete.movement += oRightPalete.speed
            if event.type == pygame.KEYUP:
                if event.key == K_UP:
                    oRightPalete.movement += oRightPalete.speed
                if event.key == K_DOWN:
                    oRightPalete.movement -= oRightPalete.speed
                
        oRightPalete.y += oRightPalete.movement
        oRightPalete.ScreenLimits()
        oBall.move()
        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)