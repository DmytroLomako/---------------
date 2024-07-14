import pygame
import os
from modules import map
from modules.hero import hero
from modules.enemy import enemy
from modules.settings import screen, finish
pygame.init()
clock = pygame.time.Clock()
start = True
scene = 'Menu'
font = pygame.font.Font(None, 35)
play_button = pygame.Rect(220, 100, 160, 50)
play_text = font.render('Play', True, 'black')
exit_button = pygame.Rect(220, 170, 160, 50)
exit_text = font.render('Exit', True, 'black')
while start:
    clock.tick(60)
    screen.fill((0, 0, 250))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
        # print(pygame.mouse.get_pos())
    if scene == 'Game':
        for i in map.list_block:
            i.show_sprite()
        if hero.count_hearts > 0:
            hero.show_sprite()
            hero.move()
            hero.hero_fell()
            hero.jump()
        enemy.show_sprite()
        finish.show_sprite()
        enemy.move_enemy()
        hero.enemy_colision(enemy)
        if hero.finish_colision(finish):
            scene = 'Menu'
    elif scene == 'Menu':
        pygame.draw.rect(screen, (100, 200, 100), play_button)
        screen.blit(play_text, (275, 110))
        if play_button.collidepoint(pygame.mouse.get_pos()):
            scene = 'Game'
            hero.X = 0
            hero.Y = 0
            hero.count_hearts = 1
            enemy.X = 200
            enemy.Y = 0
            enemy.DIRECTION = 'r'
        pygame.draw.rect(screen, (200, 100, 100), exit_button)
        screen.blit(exit_text, (275, 180))
        if exit_button.collidepoint(pygame.mouse.get_pos()):
            start = False
    pygame.display.flip()