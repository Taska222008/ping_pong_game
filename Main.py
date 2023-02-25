from pygame import *

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height))
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

window = display.set_mode((700, 500))
window.fill(37, 55, 0)

clock = time.Clock()
running = True
 
while running:
    for e in event.get():
       if e.type == QUIT:
           running = False

    display.update()
    clock.tick(60)