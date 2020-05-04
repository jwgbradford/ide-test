import pygame, sys, math, random
from pygame.locals import *

class Bat:
    def __init__(self):
        self.x=screen.get_width()/2
        self.y=screen.get_height()-20

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT] and self.x > 40:
            self.x -= 5
        if pressed_keys[K_RIGHT] and self.x < 360:
            self.x += 5

    def draw(self):
        pygame.draw.line(screen,(0,0,0),(self.x-30,self.y),(self.x+30,self.y),6)

class Ball:
    def __init__(self):
        self.setup()

    def setup(self):
        self.direction = math.pi + math.pi /3 * random.random()
        self.speed = 5
        self.dx=math.sin(self.direction)*self.speed
        self.dy=math.cos(self.direction)*self.speed
        self.x=screen.get_width()/2
        self.y=screen.get_height()-60
        self.r = 10
        self.colour = (0,0,0)

    def move(self):
        self.x +=self.dx
        self.y +=self.dy
    def bounce(self, blocks, score):
        #bounce off the sides
        if (self.x<=20 and self.dx < 0) or (self.x>=screen.get_width()-20 and self.dx > 0):
            self.dx *= -1

        #bounce off the top
        if self.y < 10:
            self.dy *= -1
            
        #bounce off the bat
        if pygame.Rect(bat.x-30,bat.y,60,10).colliderect(self.x-10,self.y-10,20,20):
            self.dy *= -1
            print(self.dx)
            #reverse direction if near the edge of the bat
            if self.x - bat.x < -20 or self.x - bat.x > 20:
                self.dx *= -1
                self.dx +=0.5

        #bounce off the blocks
        for block in blocks:
            if pygame.Rect(block.x,block.y,50,20).colliderect(self.x-10,self.y-10,20,20):
                self.dy *= -1
                blocks.remove(block)
                score += 10
                if score % 50 == 0:
                    self.dy *= 1.25
                    self.dx *= 1.25
        return blocks, score
            
    def draw(self):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.r, 0)

class Block:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour

    def draw(self):
        pygame.draw.rect(screen, self.colour, Rect(self.x, self.y, 50, 20), 0)

def spaceToContinue(blocks):
    txt = font.render("Press Space to Play",True,(0, 0, 0))
    screen.blit(txt,(screen.get_width()*0.25,screen.get_height()*0.2))
    pygame.display.update()
    wait = True

    while wait:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    wait = False
            if event.type == QUIT:
                pygame.quit()
                raise SystemExit
    blocks = []
    i = 0
    for y in range(50, 350, 50):
        for x in range(25, 360, 60):
            blocks.append(Block(x, y, colours[i]))
        i += 1
    ball.setup()
    return blocks
        
def gameOver(blocks):
    pygame.draw.rect(screen, (255,255,255), Rect(10,10, screen.get_width()-20, screen.get_height()-20), 0)

    txt = font.render("Score",True,(0,0,0))
    screen.blit(txt,(screen.get_width() / 2 - txt.get_width() / 2,50))
    txt = font.render(str(score),True,(0,0,0))
    screen.blit(txt,(screen.get_width() / 2 - txt.get_width() / 2,70))
    blocks = spaceToContinue(blocks)
    return blocks

pygame.init()

pygame.display.set_caption("Breakout")
screen = pygame.display.set_mode((400,600))
clock = pygame.time.Clock()

score = 0

font = pygame.font.Font(None,30)

ball = Ball()
bat = Bat()

blocks = []

#block colours
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
TEAL = (0, 255, 255)
colours = [RED, BLUE, GREEN, PURPLE, YELLOW, TEAL]

screen.fill((0,0,0))
pygame.draw.rect(screen, (255,255,255), Rect(10,10, screen.get_width()-20, screen.get_height()-20), 0)

blocks = spaceToContinue(blocks)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            blocks = spaceToContinue(blocks)
            
    pygame.draw.rect(screen, (255,255,255), Rect(10,10, screen.get_width()-20, screen.get_height()-20), 0)

    for block in blocks:
        block.draw()
        
    bat.move()
    ball.move()

    bat.draw()
    ball.draw()

    blocks, score = ball.bounce(blocks, score)

    if len(blocks) == 0 or ball.y > screen.get_height()-10:
        blocks = gameOver(blocks)
        score = 0

    txt = font.render("Score",True,(0,0,0))
    screen.blit(txt,(screen.get_width() / 2 - txt.get_width() / 2,15))
    txt = font.render(str(score),True,(0,0,0))
    screen.blit(txt,(screen.get_width() / 2 - txt.get_width() / 2,30))

    pygame.display.update()
    
    clock.tick(60)
