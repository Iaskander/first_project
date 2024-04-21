#Создай собственный Шутер!
from pygame import *
from random import randint
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("PON")
background = transform.scale(image.load("fon.png"), (win_width, win_height))


lost = 0

font.init()
font2 = font.Font(None,36)
font3 = font.Font(None,70)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
     def update(self):
         keys = key.get_pressed()
         if keys[K_LEFT] and self.rect.x > 5:
             self.rect.x -= self.speed
         if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed



     def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)


lost = 0 #пропущено кораблей
score = 0
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 440:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            
            lost = lost + 1

class Bullet(GameSprite):
     def update(self):
         self.rect.y += self.speed
         if self.rect.y < 0:
            self.kill()


player = Player('yolter.png', 325, 425, 80, 80, 5)
monster1 = Enemy('ufo.png',randint(80, 620),0, 80, 60, randint(1,5))
monster2 = Enemy('ufo.png',randint(80, 620),0, 80, 60, randint(1,5))
monster3 = Enemy('ufo.png',randint(80, 620),0, 80, 60, randint(1,5))
monster4 = Enemy('ufo.png',randint(80, 620),0, 80, 60, randint(1,5))
monster5 = Enemy('ufo.png',randint(80, 620),0, 80, 60, randint(1,5))

monsters = sprite.Group()
monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)
monsters.add(monster5)

bullets = sprite.Group()


clock = time.Clock()
FPS = 60
run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                player.fire()
        

    if finish != True:  
        text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 222, 255))
        text_score = font2.render("Счет: " + str(score), 1, (255, 255, 255))
        window.blit(background, (0, 0))
        window.blit(text_score,(20,20))
        window.blit(text_lose,(20,50))
        player.update() 
        player.reset()

        bullets.update()
        bullets.draw(window)

        monsters.draw(window)
        monsters.update()

    sprite_list = sprite.groupcollide(monsters, bullets, True, True)
    for el in sprite_list:
        score += 1
        monster1 = Enemy('ufo.png',randint(80, 620),0, 80, 60, randint(1,3))
        monsters.add(monster1)   
    if score > 10:
        text_win = font3.render("YRA", 1, (255, 222, 255))
        window.blit(text_win, (250, 200))
        finish = True
    if lost > 3:
        end = font3.render('LUSER', 1, (255, 222, 255))
        window.blit(end, (250, 200))
        finish = True






    display.update()
    clock.tick(FPS)
    
 
 
