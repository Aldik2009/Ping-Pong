from pygame import *

class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        #Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
 
 
        #каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
 
        #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_l = key.get_pressed()
        if keys_l[K_w]:
            self.rect.y -= 5
        if keys_l[K_s]:
            self.rect.y += 5

    def update_r(self):
        keys_r = key.get_pressed()
        if keys_r[K_UP]:
            self.rect.y -= 5
        if keys_r[K_DOWN]:
            self.rect.y += 5

img_back = 'green_back.jpg'
img_player = 'black_stick.png'
img_ball = 'ball_for_game.png'
win_width = 700
win_height = 500
display.set_caption('Пинг-Понг')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

Player_l = Player(img_player, 50, 200, 8, 110, 5)
Player_r = Player(img_player, 650, 300, 8, 110, 5)
ball = GameSprite(img_ball, 400, 300, 80, 80, 5)

speedx = 3
speedy = 5
run = True
finish = False
FPS = 60
clock = time.Clock()
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.blit(background, (0, 0))

        Player_l.update_l()
        Player_l.reset()

        Player_r.update_r()
        Player_r.reset()

        ball.update()
        ball.reset()

        ball.rect.x += speedx
        ball.rect.y += speedy

        if ball.rect.y >= 455:
            speedy *= -1
        if ball.rect.y <= 0:
            speedy *= -1
        collide_l = sprite.collide_rect(Player_l, ball)
        if collide_l:
            speedx *= -1
        collide_r = sprite.collide_rect(Player_r, ball)
        if collide_r:
            speedx *= -1

        if ball.rect.x > win_width:
            finish = True
        if ball.rect.x < 0:
            finish = True

        display.update()

    clock.tick(FPS)