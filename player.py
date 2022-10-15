import pygame

class Player(pygame.sprite.Sprite):
    # width height y jnjel enq
    def __init__(self, screen, playerImage, facing):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load(playerImage).convert_alpha()
        self.rect = self.image.get_rect()
        '''facing'''
        self.facing = facing
        if self.facing == 'right':
            self.rect.topleft = self.screen_rect.topleft  # topleft угол персонажа ставим в topleft угол экрана
        elif self.facing == 'left':
            self.rect.topright = self.screen_rect.topright  # topright угол персонажа ставим в topright угол экрана
        self.mUP = False
        self.mDOWN = False

    def draw_player(self):
        self.screen.blit(self.image, self.rect)

    def update_player(self, speed):
        '''обновление персонажа
        случаи когда клавиша зажата
        '''
        '''переменные mUP mDOWB = True, False находятся в  controls.py
        '''
        if self.mUP and self.rect.top > self.screen_rect.top:
            self.rect.centery -= speed  # bardzracnuma verev slacik kerpov
        elif self.mDOWN and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += speed  # ijacnuma nerqev slacik kerpov



