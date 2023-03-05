from pygame import *

#background
win_width=700
win_length=500
window = display.set_mode((win_width,win_length))
display.set_caption("Ping Pong Game")



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

p1 = Player1("ufo.png", 100, 65, 5)
p2 = Player2("ufo.png", 300, 65, 5)





clock=time.Clock()
FPS=60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.fill((0,0,0))
    p1.reset()
    p1.update()
    p2.reset()
    p2.update()
    display.update()
    clock.tick(FPS)