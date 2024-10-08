from pygame import *
back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)
game = True

        
class GameSprite(sprite.Sprite):
  # class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # We call the class constructor (Sprite):
        sprite.Sprite.__init__(self)
 
        # each sprite must store an image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
        # each sprite must store the rect property it is inscribed in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # method that draws the character in the window
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
# main player class
class Player(GameSprite):
    # method for controlling the sprite with keyboard arrows
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
racket1 = Player('racket.png', 30 ,200, 50, 150, 4)
racket2 = Player('racket.png',520 ,200, 50, 150, 4)
ball = GameSprite('tenis_ball.png', 200, 200, 50, 50, 4)
  # the "fire" method (use the player's place to create a bullet there)
clock = time.Clock()
FPS = 60
while game:
    pass
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    
    window.fill(back)
    racket1.update_l()
    racket2.update_r()
#    ball.updat()    
    racket1.reset()
    racket2.reset()
    ball.reset()


    display.update()
    clock.tick(FPS)

