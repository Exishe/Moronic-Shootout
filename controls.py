import pygame
import sys
from gun_bullet import Gun_Bullet


width = 600

def events(screen, player1, player2, gunfile1, gunfile2, bullets1, bullets2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # KEYDOWN
        elif event.type == pygame.KEYDOWN:
            '''player1'''
            if event.key == pygame.K_s:  # Down
                player1.mDOWN = True
            elif event.key == pygame.K_w:  # Up
                player1.mUP = True
            # banana: здесь пользуемся классом пушки
            elif event.key == pygame.K_SPACE:
                new_bullet1 = Gun_Bullet(screen, player1, gunfile1)
                bullets1.add(new_bullet1)

            '''player2'''
            if event.key == pygame.K_DOWN:
                player2.mDOWN = True
            elif event.key == pygame.K_UP:
                player2.mUP = True
            #arbuz десь пользуемся классом пушки
            if event.key == pygame.K_RETURN:
                new_bullet2 = Gun_Bullet(screen, player2, gunfile2)
                bullets2.add(new_bullet2)

        elif event.type == pygame.KEYUP:
            '''player1'''
            if event.key == pygame.K_s:
                player1.mDOWN = False
            elif event.key == pygame.K_w:
                player1.mUP = False
            '''player2'''
            if event.key == pygame.K_DOWN:
                player2.mDOWN = False
            elif event.key == pygame.K_UP:
                player2.mUP = False

def update(bullets):
    for bullet in bullets.sprites():
        bullet.draw_gun_bullet()

def update_bullets(player1, player2, bullets1, bullets2):
    '''обновляем позиции пуль'''
    bullets1.update()
    bullets2.update()
    for bullet in bullets1.copy():
        if bullet.rect.left >= width:
            bullets1.remove(bullet)
    for bullet in bullets2.copy():
        if bullet.rect.right <= 0:
            bullets2.remove(bullet)







