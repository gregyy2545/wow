from pygame import *
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
while game:
    pass
    for e in event.get():
        if e.type == QUIT:
            game = False

        display.update()