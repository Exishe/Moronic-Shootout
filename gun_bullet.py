import pygame

class Gun_Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, player, gunImage):
        '''инициализация пушки'''
        pygame.sprite.Sprite.__init__(self)

        '''из объекта player берем переменную facing '''
        self.facing = player.facing

        self.screen = screen
        self.image = pygame.image.load(gunImage).convert_alpha()
        self.rect = self.image.get_rect()  # берем координ. png пушки

        self.speed = 20

        '''ставим пулю в нужное место с игроком исходя из facing-a'''
        if self.facing == 'right':
            self.rect.left = player.rect.centerx + 15
        elif self.facing == 'left':
            self.rect.right = player.rect.centerx - 15

        self.rect.centery = player.rect.centery  # чтобы пушка двигалась вместе с персонажем
        self.x = float(self.rect.x)  # плавное движение


    def update(self):
        '''перемещение пули направо'''
        if self.facing  == 'right':
            self.x += self.speed
            self.rect.x = self.x
        elif self.facing  == 'left':
            self.x -= self.speed
            self.rect.x = self.x

    def draw_gun_bullet(self):
        """рисование пули пушки"""
        self.screen.blit(self.image, self.rect)