import pygame
import os
from modules import map
from modules.hero import hero
from modules.enemy import enemy
from modules.settings import screen, finish, heart1, heart2, heart3
pygame.init()
clock = pygame.time.Clock()
start = True
scene = 'Menu'
font = pygame.font.Font(None, 50)
play_button = pygame.Rect(220, 90, 160, 80)
play_text = font.render('Play', True, 'black')
exit_button = pygame.Rect(220, 210, 160, 80)
exit_text = font.render('Exit', True, 'black')
while start:
    clock.tick(60)
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
        # print(pygame.mouse.get_pos())
    if scene == 'Game':
        screen.fill((0, 0, 250))
        for i in map.list_block:
            i.show_sprite()
        if hero.count_hearts > 0:
            if hero.count_hearts == 3:
                heart3.show_sprite()
                heart2.show_sprite()
                heart1.show_sprite()
            elif hero.count_hearts == 2:
                heart3.show_sprite()
                heart2.show_sprite()
            elif hero.count_hearts == 1:
                heart3.show_sprite()
            hero.show_sprite()
            hero.move()
            hero.hero_fell()
            hero.jump()
        enemy.show_sprite()
        finish.show_sprite()
        enemy.move_enemy()
        hero.enemy_colision(enemy)
        if hero.count_hearts == 0:
            scene = 'Menu'
        if hero.finish_colision(finish):
            scene = 'Menu'
    elif scene == 'Menu':
        pygame.draw.rect(screen, (100, 200, 100), play_button)
        screen.blit(play_text, (266, 113))
        if play_button.collidepoint(pygame.mouse.get_pos()):
            scene = 'Game'
            hero.X = 0
            hero.Y = 0
            hero.count_hearts = 3
            enemy.X = 200
            enemy.Y = 0
            enemy.DIRECTION = 'r'
        pygame.draw.rect(screen, (200, 100, 100), exit_button)
        screen.blit(exit_text, (266, 233))
        if exit_button.collidepoint(pygame.mouse.get_pos()):
            start = False
    pygame.display.flip()