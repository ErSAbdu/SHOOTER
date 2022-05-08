from pygame import *
'''Необходимые классы'''
#класс родитель для спрайтов
class GameSprite(sprite.Sprite):
    # конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        #каждый спрайт должен хранить свойство image
        self.image = transfrom.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        # каждый спрайт должен хранить свои свойства
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#класс-наследник для спрайта-игрока
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

#класс-наследник для врага
class Enemy(GameSprite):
    side = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.side = 'left'
        if  self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy2(GameSprite): #ходит по вертикали
    direction = 'up'
    def update(self):
        if self.rect.y <= 160:
            self.direction = 'down'
        if self.rect.y >= win_height - 80:
            self.direction = 'up'
        
        if self.directon == 'up':
            self.rect.y -= self.speed
        else:
            self.rect.y +=self.speed

#класс для спрайтов-препятствий


class Wall(sprite,Sprite):
    def __init__(self, red, green, blue, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.red = red
        self.blue = blue
        self.green = green
        self.width = wall_width
        self.heiight = wall_height
        self.image = SurFace((self.width, self.height))
        self.image.fill((red, green, blue))
        self.rect = sefl.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


#Игровая сцена:
win_width = 700
win_height = 500
window = display_set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load('backgroun.jpg'), (win_width, win_height))

#Персонажи игры
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120 , win_height - 80, 0)
enemy2 = Enemy2('cyborg.png', 170, 100, 2)
#стены
w1 = Wall(143, 205, 50 ,100, 20, 450, 10)
w2 = Wall(124, 43, 50, 100, 480, 350, 10)
w3 = Wall(4, 205, 50, 100, 20, 10, 300)


            
game = True
finish = False
clock = time.Clock()
FPS = 60

font.int()
font = font.SysFont('Arial', 70)
win = font.render('YOU WIN', True, (255, 215, 0))
lose = font.render('YOu Lose', True, (180, 0, 0))

#музыка
def new_func():
    mixer.init()

new_func()
mixer.music.load('.ogg')
mixer.music.play()

mony = mixer.Sound('.ogg')
kick = mixer.Sound('.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
 window.blit(background,(0,0))
    player.update()
    monster.update()
    enemy2.update()
    player.reset()