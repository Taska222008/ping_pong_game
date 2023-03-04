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

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed + 5
        self.rect.y += self.speed
        if self.rect.y > 450 or self.rect.y < 50:
            self.speed = self.speed* -1
    def collide(self, paddle):
        if sprite.collide_rect(paddle, self):
            self.speed = self.speed* -1
    

ball = Ball("tenis_ball.png", 700/2, 500/2, 13, 50, 50)
player_1 = Paddle_1("racket.png", 10, 175, 10, 50, 150)
player_2 = Paddle_2("racket.png", 630, 175, 10, 50, 150)  
    
window = display.set_mode((700, 500))
window.fill((37, 55, 00))

font.init()
font_1 = font.SysFont("Arial", 27) 
font_2 = font.SysFont("Arial", 100) 
font_3 = font.SysFont("Arial", 50)

green = (144, 198, 0)

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

        ball.reset()
        ball.update()
        
        ball.collide(player_1)
        ball.collide(player_2)
        
        if ball.rect.x > 700:
            lose = font_2.render("Player 1 Win", 1, green)
            
            window.blit(lose, (100, 50))
            finish == True
        if ball.rect.x < 0:
            win = font_2.render("Player 2 Win", 1, green)
            
            window.blit(win, (100, 50))
            finish == True
            
        display.update()
        
        clock.tick(60)