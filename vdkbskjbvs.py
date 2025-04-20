from pygame import *


font.init()
font1 = font.SysFont('Arial', 80)
win_message = font1.render('PLAYER 1 WINS!', True, (255, 255, 255))
lose_message = font1.render('PLAYER 2 WINS!', True, (180, 0, 0))


score1 = 0
score2 = 0

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.x < (win_width - 70):
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < (win_height - 70):
            self.rect.y += self.speed


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Pingo Pongo')
background = transform.scale(image.load('lanta-klong-nin.jpg'), (win_width, win_height)) 

player1 = Player('Без названия.jpg', 50, 250, 5) 
player2 = Player('Без названия.jpg', 650, 250, 5)  
ball = GameSprite('m1000x1000.jpg', 350, 250, 5)

clock = time.Clock()
FPS = 60
game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.blit(background, (0, 0))
        player1.update()
        player1.reset()
        player2.update()
        player2.reset()
    
    display.update()
    clock.tick(FPS)
