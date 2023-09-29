from pygame import *

window_size = [700, 500]
window = display.set_mode(window_size)
display.set_caption('Пинг-понг')
window.fill([240, 250, 235])

class GameSprite(sprite.Sprite): 
    def __init__(self, player_image ,x_size , y_size, x_cor, y_cor, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(x_size, y_size))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x_cor
        self.rect.y = y_cor

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()   
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed 
        if keys_pressed[K_s] and self.rect.y <= 440:
            self.rect.y += self.speed 
    def update_r(self):
        keys_pressed = key.get_pressed()   
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed 
        if keys_pressed[K_DOWN] and self.rect.y <= 440:
            self.rect.y += self.speed

rocket_l = Player('rocket.png', 30, 90, 5, 30, 5)  
rocket_r = Player('rocket.png', 30, 90, 665, 30, 5)
game = True
FPS = 60
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    rocket_l.update_l()
    rocket_r.update_r()

    window.fill([240, 250, 235])

    rocket_l.reset()
    rocket_r.reset()


    display.update()
    clock.tick(FPS)
