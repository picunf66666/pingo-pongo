from pygame import *


font.init()
font1 = font.SysFont('Arial', 40)
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
    def update1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < (win_height - 70):
            self.rect.y += self.speed
    def update2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < (win_height - 70):
            self.rect.y += self.speed


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Pingo Pongo')
background = transform.scale(image.load('chto-takoe-nebo-1024x576.jpg'), (win_width, win_height)) 

player1 = Player('Без названия.jpg', 50, 250, 6) 
player2 = Player('Без названия.jpg', 600, 250, 6)  
ball = GameSprite('m1000x1000.jpg', 350, 250, 5)

clock = time.Clock()
FPS = 60
game = True
finish = False
speed_x = 1
speed_y = 1

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        ball.rect.x +- speed_x
        ball.rect.y +- speed_y
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.blit(background, (0, 0))
        player1.update1()
        player1.reset()
        player2.update2()
        player2.reset()
        ball.update()
        ball.reset()
    if  sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose_message, (200, 200))
    if ball.rect.x > 700:
        finish = True
        window.blit(win_message, (200, 200))
    if ball.rect.y > win_height-50 or ball.rect.y < 0:
        speed_y *= -1
    
    display.update()
    clock.tick(FPS)
