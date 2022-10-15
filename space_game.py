import pygame
import player
import controls
from pygame.sprite import Group

score1 = score2 = 0


'''Цветы'''
WHITE = (255, 255, 255)
L_BLUE = (0, 204, 255)


'''экран'''
w = 600
'''ВНИМАНИЕ!!!!!
weight есть еще в модуле controls
'''
h = 400
resolution = (w, h)

def run():
    pygame.init()

    '''настройки экрана'''
    pygame.display.set_caption('Moronic Shootout')
    bg = pygame.image.load("images/jungle2.png")
    screen = pygame.display.set_mode(resolution)



    '''Врема, FPS'''
    FPS = 30
    clock = pygame.time.Clock()

    '''Позиции, скорость'''
    speed = 15

    '''ИГРОК'''
    playerImage1 = 'images/person1.png'
    playerImage2 = 'images/person2.png'
    player1 = player.Player(screen, playerImage1, 'right')
    player2 = player.Player(screen, playerImage2, 'left')

    '''Пули sprites'''
    bullets1 = Group()
    bullets2 = Group()

    '''Фрукты'''
    bananaImage = 'images/banana.png'
    arbuzImage = 'images/watermelon.png'



    while True:
        controls.events(screen, player1, player2, bananaImage, arbuzImage, bullets1, bullets2)
        screen.blit(bg, (0, 0))
        player1.update_player(speed)  # mUP mDOWN
        player2.update_player(speed)  # mUP mDOWN
        controls.update(bullets1)
        controls.update(bullets2)

        player1.draw_player()  # self.screen.blit() function
        player2.draw_player()  # self.screen.blit() function
        # bullets.update()  # переместил в controls.uptade(bullets)
        controls.update_bullets(player1, player2, bullets1, bullets2)

        #collide = pygame.Rect.coll

        pygame.display.update()
        clock.tick(FPS)


run()
