import pygame
import os
from .map import list_block, game_matrix, list_hearts, list_empty_hearts

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Game')
class Image:
    def __init__(self, width, height, x, y, image_name):
        self.WIDTH = width
        self.HEIGHT = height
        self.X = x
        self.Y = y
        self.IMAGE_NAME = image_name
        self.IMAGE = None
        self.load_image()
    def load_image(self, flip_x = False):
        path_folder = os.path.abspath(__file__ + '/../../image')
        path_image = os.path.join(path_folder, self.IMAGE_NAME)
        self.IMAGE = pygame.image.load(path_image)
        self.IMAGE = pygame.transform.scale(self.IMAGE, (self.WIDTH, self.HEIGHT))
        self.IMAGE = pygame.transform.flip(self.IMAGE, flip_x, False)
    def show_sprite(self):
        screen.blit(self.IMAGE, (self.X, self.Y))
class Person(Image):
    def __init__(self, width, height, x, y, image_name, speed, gravity):
        super().__init__(width, height, x, y, image_name)
        self.SPEED = speed
        self.FALL = True
        self.GRAVITY = gravity
        self.CAN_MOVE_R = True 
        self.CAN_MOVE_L = True 
    def hero_fell(self):
        self.check_fall()
        if self.JUMP_COUNT == 0:
            if self.FALL:
                self.Y += self.GRAVITY
    def check_fall(self):
        for block in list_block:
            if self.Y + self.HEIGHT > block.Y - 4 and self.X < block.X + block.WIDTH and self.X + self.WIDTH > block.X and self.Y < block.Y + block.HEIGHT: #
                self.FALL = False
                self.Y = block.Y - self.HEIGHT
                break
            else:
                self.FALL = True
    def check_move_right(self): 
        for block in list_block: 
            
            if self.X + self.WIDTH > block.X - 3 and self.X < block.X + block.WIDTH and self.Y + self.HEIGHT > block.Y and self.Y < block.Y + block.HEIGHT: 
                self.CAN_MOVE_R = False 
                
                break 
            else:
                self.CAN_MOVE_R = True 
    def check_move_left(self):
        for block in list_block:
            if self.Y + self.HEIGHT > block.Y and self.Y < block.Y + block.HEIGHT and self.X < block.X + block.WIDTH + 3 and self.X + self.WIDTH > block.X:
                self.CAN_MOVE_L = False
                break
            else:
                self.CAN_MOVE_L = True
    def check_jump(self):
        for block in list_block:
            if self.X < block.X + block.WIDTH and self.X + self.WIDTH > block.X and self.Y < block.Y + block.HEIGHT + 3 and self.Y > block.Y:
                self.JUMP_COUNT = 0
                self.FALL = True
                break
x = 0
y = 0
finish = None
for i in game_matrix:
    for j in i:
        
        if j == 1:
            block = Image(25, 25, x, y, 'block.png')
            list_block.append(block)
        elif j == 'f':
            finish = Image(50, 50, x, y, 'finish.png')
        elif j == 'h1':
            heart1 = Image(50, 50, x, y, 'heart.png')
        elif j == 'h2':
            heart2 = Image(50, 50, x, y, 'heart.png')
        elif j == 'h3':
            heart3 = Image(50, 50, x, y, 'heart.png')
        x += 25


    y += 25
    x = 0