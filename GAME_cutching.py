from pygame import *
from random import randint
font.init()
font = font.SysFont('Courier New', 100)
win = font.render('YOU WIN!',True, (255,255,255))
lose = font.render('YOU LOSE!',True, (255,255,255))
w = 700
h = 500

window = display.set_mode((w,h))
mixer.init()

display.set_caption('CUG')
background = transform.scale(image.load("background.jpg"), (w,h))
player_image = "spr1.1.png"
sprite2 = transform.scale(image.load("monster2.png"), (80,80))
game = True
finish = False
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (90,90))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        speed = 7
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y>5:
            self.rect.y -= speed
        if keys[K_s] and self.rect.y<430:
            self.rect.y += speed
        if keys[K_a] and self.rect.x>5:
            self.rect.x -= speed
        if keys[K_d] and self.rect.x<630:
            self.rect.x += speed

class Enemy(GameSprite):
    def update(self):
        mon = randint(1,4)
        if mon == 1 and self.rect.x<=400:
            self.rect.x += self.speed
        if mon == 2 and self.rect.x>=5:
            self.rect.x -= self.speed
        if mon == 3 and self.rect.y>=5:
            self.rect.y -= self.speed
        if mon == 4 and self.rect.y<=300:
            self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self,color1,color2,color3):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_ball(self):
        window.blit(ball,(self.rect.x, self.rect.y))

balls = list()
balls.append(Ball('ball 2',randint(0,700),randint(0,500),0,255,255,255)) 
balls.append(Ball('ball 2',randint(0,700),randint(0,500),0,255,255,255))
balls.append(Ball('ball 2',randint(0,700),randint(0,500),0,255,255,255))
balls.append(Ball('ball 2',randint(0,700),randint(0,500),0,255,255,255))
balls.append(Ball('ball 2',randint(0,700),randint(0,500),0,255,255,255))
balls.append(Ball('ball 2',randint(0,700),randint(0,500),0,255,255,255))

player_image = Player('spr1.1.png',20,230,7)
monster = Enemy('monster.png', 400,200,40)

while game:
    if finish != True:
        for e in event.get():
            if e.type == QUIT:
                game = False
        window.blit(background,(0,0))
        keys_pressed = key.get_pressed()
        player_image.update()
        player_image.reset()
        upd = randint(1,3)
        if upd == 1:
            monster.update()
        monster.reset()
        if sprite.collide_rect(player_image,monster):
            window.blit(win,(150,200))
            finish = True
        for wall in walls:
                wall.draw_wall()
        if sprite.collide_rect(player_image,ball):
            window.blit(lose,(150,200))
            finish = True

        display.update()
        clock.tick(FPS)
