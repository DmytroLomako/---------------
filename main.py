import pygame
import json
from modules import map
from modules.hero import Hero
from modules.enemy import Enemy
from modules.settings import screen, finish, heart1, heart2, heart3
from modules.load_save import load
pygame.init()

with open('data.json', 'r') as file:
    data = json.load(file)
print(data)
hero = Hero(25, 50, data['hero_x'], data['hero_y'], 'Animation/1.png', 3, 4, 5, data['count_heart'])
enemy_list = []
for object in data['enemies']:
    enemy = Enemy(20, 40, object['enemy_x'], object['enemy_y'], 'enemy.png', 2, 4, 180, 350, object['direction'])
    enemy_list.append(enemy)

clock = pygame.time.Clock()
start = True
scene = 'Menu'
font = pygame.font.Font(None, 50)
font1 = pygame.font.Font(None, 25)
play_button = pygame.Rect(200, 40, 200, 80)
play_text = font.render('PLAY', True, 'black')
exit_button = pygame.Rect(200, 280, 200, 80)
exit_text = font.render('EXIT', True, 'black')
play_again_button = pygame.Rect(190, 140, 220, 100)
play_again_text = font.render('PLAY AGAIN', True, 'black')
exit_again_button = pygame.Rect(0, 0, 50, 50)
exit1_text = font1.render('EXIT', True, 'black')
continue_button = pygame.Rect(200, 160, 200, 80)
continue_text = font.render('CONTINUE', True, 'black')
while start:
    clock.tick(60)
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            new_data = {
                "count_heart" : hero.count_hearts,
                "hero_x" : hero.X,
                "hero_y" : hero.Y,
                "level" : 1,
                'enemies' : []
            }
            for enemy in enemy_list:
                enemy_dict = {
                    'enemy_x' : enemy.X,
                    'enemy_y' : enemy.Y,
                    'direction' : enemy.DIRECTION
                }
                new_data['enemies'].append(enemy_dict)
                with open('data.json', 'w') as file:
                    json.dump(new_data, file, indent=4)
            start = False
        # print(pygame.mouse.get_pos())
    if scene == 'Game':
        screen.fill((0, 0, 250))
        for i in map.list_block:
            i.show_sprite()
        if hero.count_hearts > 0:
            if hero.count_hearts >= 3:
                heart1.show_sprite()
            if hero.count_hearts >= 2:
                heart2.show_sprite()
            if hero.count_hearts >= 1:
                heart3.show_sprite()
            hero.show_sprite()
            hero.move()
            hero.hero_fell()
            hero.jump()
        finish.show_sprite()
        for enemy in enemy_list:
            enemy.show_sprite()
            enemy.move_enemy()
            hero.enemy_colision(enemy)
        if hero.count_hearts == 0:
            scene = 'Game over'

        if hero.finish_colision(finish):
            scene = 'Menu'
    elif scene == 'Menu':
        pygame.draw.rect(screen, (100, 200, 100), play_button)
        screen.blit(play_text, (256, 63))
        if play_button.collidepoint(pygame.mouse.get_pos()):
            scene = 'Game'
            hero.X = 0
            hero.Y = 0
            hero.count_hearts = 3
            enemy.X = 200
            enemy.Y = 0
            enemy.DIRECTION = 'r'
        pygame.draw.rect(screen, (200, 100, 100), exit_button)
        screen.blit(exit_text, (256, 303))
        if exit_button.collidepoint(pygame.mouse.get_pos()):
            start = False
        pygame.draw.rect(screen, (100, 200, 100), continue_button)
        screen.blit(continue_text, (205, 183))
        if continue_button.collidepoint(pygame.mouse.get_pos()):
            scene = 'Game'
    elif scene == 'Game over':
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (137, 0, 0), play_again_button)
        screen.blit(play_again_text, (196, 175))
        pygame.draw.rect(screen, (210, 0, 0), exit_again_button)
        screen.blit(exit1_text, (4, 17))
        if exit_again_button.collidepoint(pygame.mouse.get_pos()):
            start = False
        elif play_again_button.collidepoint(pygame.mouse.get_pos()):
            hero.count_hearts = 3
            scene = 'Game'
    pygame.display.flip()