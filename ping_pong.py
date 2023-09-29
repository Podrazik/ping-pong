from pygame import *

window_size = [700, 500]
window = display.set_mode(window_size)
display.set_caption('Пинг-понг')
window.fill([240, 250, 235])

game = True
FPS = 60
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False




    display.update()
    clock.tick(FPS)
