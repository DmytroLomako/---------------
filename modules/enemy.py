from .settings import Person

class Enemy(Person):
    def __init__(self, width, height, x, y, image_name, speed, gravity, pos1, pos2, direction):
        super().__init__(width, height, x, y, image_name, speed, gravity)
        self.POS1 = pos1
        self.POS2 = pos2
        self.DIRECTION = direction
        self.JUMP_COUNT = 0
    def move_enemy(self):
        self.hero_fell()
        self.check_move_right()
        self.check_move_left()
        if self.DIRECTION == 'r':
            self.X += self.SPEED
            self.load_image(True)
            if self.CAN_MOVE_R == False:
                self.DIRECTION = 'l'
            elif self.X > self.POS2:
                self.DIRECTION = 'l'
        elif self.DIRECTION == 'l':
            self.X -= self.SPEED
            self.load_image()
            if self.CAN_MOVE_L == False:
                self.DIRECTION = 'r'
            elif self.X < self.POS1:
                self.DIRECTION = 'r'
