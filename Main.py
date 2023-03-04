from pygame import *

background = transform.scale(image.load("download.jpeg"), (700, 500))
class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, width, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (width, height))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y

   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))

class Paddle_1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        
        if (keys[K_w]) and self.rect.y > 5:
            self.rect.y -= self.speed
        if (keys[K_s]) and self.rect.y < 420:
            self.rect.y += self.speed

class Paddle_2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        
        if (keys[K_o]) and self.rect.y > 5:
            self.rect.y -= self.speed
        if (keys[K_l]) and self.rect.y < 420:
            self.rect.y += self.speed

player_1 = Paddle_1("racket.png", 10, 175, 10, 50, 150)
player_2 = Paddle_2("racket.png", 630, 175, 10, 50, 150)  
    
window = display.set_mode((700, 500))
window.fill((37, 55, 00))

clock = time.Clock()
running = True
finish = False

while running:
    for e in event.get():
       if e.type == QUIT:
           running = False
    window.blit(background, (0, 0))

    if finish == False:

        player_1.update()
        player_2.update()

        player_1.reset()
        player_2.reset()

        
        display.update()
        
        clock.tick(60)