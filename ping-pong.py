from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_w, size_h, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_w, size_h))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

win_width = 600
wind_height = 500
background = (200,255,255)
win = display.set_mode((win_width, wind_height))
win.fill(background)

game = True
finish = False
clock = time.Clock()
FPS = 60
racket1 = Player('left.png', 30, 200, 30, 90, 5)
racket2 = Player('right.png', 540, 200, 30, 90, 5)
ball = GameSprite('ball.png', 200, 200, 40, 40, 4)
speed_x = ball.speed
speed_y = ball.speed

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish is not True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        win.fill(background)
        racket1.update_l()
        racket2.update_r()
        ball.reset()
        racket1.reset()
        racket2.reset()
    display.update()
    clock.tick(FPS)