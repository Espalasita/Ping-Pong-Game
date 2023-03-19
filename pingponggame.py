from pygame import *

#background
win_width=700
win_length=500
window = display.set_mode((win_width,win_length))
display.set_caption("Ping Pong Game")
speed_x = 3
speed_y = 3


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x = 65, size_y = 65):
        super().__init__()
        self.image=transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y < win_length - 80:
            self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y < win_length - 80:
            self.rect.y += self.speed

p1 = Player1("rectangle.png", 0, 100, 5,45,250)
p2 = Player2("rectangle.png", 650, 100, 5, 45, 250)
ball = GameSprite("ball.png", 250,250, 5, 45, 45)




clock=time.Clock()
FPS=60
game = True
finish = False

font.init()
font1 = font.Font(None, 35)
lose1 = font1.render('PLAYER 1 LOSES!', True, (180,0, 0))

font.init()
font2 = font.Font(None, 35)
lose2 = font2.render('PLAYER 2 LOSES!', True, (180,0, 0))


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        

    if finish != True:
        window.fill((255,255,255))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        p1.reset()
        p1.update()
        p2.reset()
        p2.update()
        ball.reset()

    if ball.rect.y > win_length - 50 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(p1,ball) or sprite.collide_rect(p2, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200,200))
    if ball.rect.x > win_width - 50:
        finish = True
        window.blit(lose2, (200,200))


    display.update()
    clock.tick(FPS)