import pygame
import math
import numpy as np
from pygame import mixer

win = pygame.display.set_mode((600,600),)

#プレイキャラ
class Player:
    def __init__(self,win):
        self.x = 300
        self.y = 550
        self.width = 20
        self.height = 40
        self.vel = 1
        self.win = win

    def draw(self):
        pygame.draw.rect(self.win,(0, 206, 209),(self.x,self.y,self.width,self.height),0)

    def move(self,keys):
        if keys[pygame.K_RIGHT] and self.x < 600 - self.width - self.vel:
            self.x += self.vel
        elif keys[pygame.K_LEFT] and self.x > self.vel:
            self.x -= self.vel

#敵キャラ
class Enemy:
    def __init__(self,win,x):
        self.x = x
        self.y = 100
        self.radius = 30
        self.win = win
        self.hitcircle = (self.x,self.y)
        self.xdir = 0.1  
        self.ydir = 0
        self.edge = False
        self.moveloop = 0

    def draw(self):
        pygame.draw.circle(self.win,(255,255,255), (self.x,self.y), self.radius)
        self.hitcircle = (self.x,self.y)



    def move(self):
        self.x += self.xdir

    def shiftDown(self):
        self.xdir *= -1
        self.y += self.radius
        self.edge = False

#打ち出す弾
class Shot:
    def __init__(self,win,x):
        self.win = win
        self.y =  350
        self.vel = 10
        self.x = x
        self.r = 8

    def draw(self):
        pygame.draw.rect(self.win,(0,255,255),(self.x,self.y,self.r*2,self.r*2),0)

    def collide(self,drop,flower):
        dist = math.sqrt(np.abs(flower.hitcircle[0]-drop.x)**2+np.abs(flower.hitcircle[1]-drop.y)**2)
        if dist < 38:
            return True
        return False 

def drawWindow(ship,players):
    ship.draw()

    for i in players:
        i.draw()

    for b in enemyes:
        b.draw()
        b.move()  
    pygame.display.update()

#敵の生成
players = []
enemyes = []
shootloop = 0
for i in range(20):
    x = i*60 + 80
    enemyes.append(Enemy(win,x))
ship = Player(win)
run = True

while run:            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False   

    keys = pygame.key.get_pressed()

    if shootloop > 0:
        shootloop += 1
    if shootloop > 20:
        shootloop = 0
    
    #弾の打ち出し＆音
    if keys[pygame.K_SPACE] and shootloop == 0:
        #if len(drops) <= 5:
        players.append(Shot(win,ship.x))
        pygame.display.update()
        mixer.init()
        mixer.music.load("fig/手裏剣を投げる.mp3")
        mixer.music.play(1)
        shootloop = 1

    for drop in players:
        if drop.y > 0:
            drop.y -= 1
        else:
            players.pop(players.index(drop))    

        for flower in players:
            if drop.collide(drop,flower):
                players.pop(players.index(drop))

    for flower in enemyes:
        if flower.x > 600 or flower.x < 0:
            flower.edge = True

        if flower.edge:
            flower.shiftDown()

    ship.move(keys)
    win.fill((0, 0, 0))
    drawWindow(ship,players)



if __name__ == "__main__":
    pygame.quit()
