import pygame
from .settings import Person
from .map import game_matrix

class Hero(Person):
    def __init__(self, width, height, x, y, image_name, speed, gravity, jump_height, count_heart):
        super().__init__(width, height, x, y, image_name, speed, gravity)
        self.JUMP_COUNT = 0 
        self.JUMP_HEIGHT = jump_height 
        self.count_hearts = count_heart
        self.count_animation = 3
        self.direction = 'r'
    def move(self):
        keys = pygame.key.get_pressed()
        self.check_move_right() 
        self.check_move_left() 
        if keys[pygame.K_LEFT] and self.CAN_MOVE_L:
            self.X -= self.SPEED
            self.count_animation += 1
            self.direction = 'l'
            self.animation()
            self.load_image(True)
            if self.X < 0:
                self.X = 0
        elif keys[pygame.K_RIGHT] and self.CAN_MOVE_R:
            self.X += self.SPEED
            self.count_animation += 1
            self.direction = 'r'
            self.animation()
            self.load_image()
            if self.X + self.WIDTH > 600:
                self.X = 600 - self.WIDTH  
        else:
            self.count_animation = 3
            self.animation()
            if self.direction == 'l':
                self.load_image(True)
            else:
                self.load_image()
    def jump(self):
        keys = pygame.key.get_pressed() 
        self.check_jump() 
        if keys[pygame.K_SPACE]:
            if self.FALL == False: 
                self.JUMP_COUNT = 20
        if self.JUMP_COUNT > 0: 
            self.Y -= self.JUMP_HEIGHT
            self.JUMP_COUNT -= 1 
    def enemy_colision(self, enemy):
        rect_hero = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
        rect_enemy = pygame.Rect(enemy.X, enemy.Y, enemy.WIDTH, enemy.HEIGHT)
        if rect_hero.colliderect(rect_enemy):
            self.count_hearts -= 1
            self.X = 0
            self.Y = 0
    def finish_colision(self, finish):
        rect_hero = pygame.Rect(self.X, self.Y, self.WIDTH, self.HEIGHT)
        rect_finish = pygame.Rect(finish.X, finish.Y, finish.WIDTH, finish.HEIGHT)
        if rect_hero.colliderect(rect_finish):
            return True
        return False
    def animation(self):
        name_file = self.count_animation // 3
        if name_file == 8:
            name_file = 1
            self.count_animation = 3
        folder_name = self.IMAGE_NAME.split('/')[0]
        self.IMAGE_NAME = f'{folder_name}/{name_file}.png'

