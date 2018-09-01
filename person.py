'''Person Class Definition'''
from colorama import Fore
from config import MAP_COMPONENTS as mp


class Person:
    '''A class to define general characteristic of the players and enemies in the game'''

    def __init__(self, x, y, height, width, dx, dy, gravity, board):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.dx = dx
        self.dy = dy
        self.init_gravity = gravity
        self.gravity = 0
        self.matrix = []

    def get_matrix(self):
        '''Function to return the matrix
        representation of the person
        '''
        return self.matrix

    def check_right_collision_with_map(self, board):
        '''Function to check if the person has
        collided with a map element from the right
        '''
        for i in range(self.y, self.y + self.height):
            if board.matrix[i][self.x + self.width + 1] in mp:
                return True

    def check_left_collision_with_map(self, board):
        '''Function to check if the person has
        collided with a map element from the left
        '''
        for i in range(self.y, self.y + self.height):
            if board.matrix[i][self.x - 1] in mp:
                return True

    def check_bottom_collision_with_map(self, board):
        '''Function to check if the person has
        collided with a map element from the bottom
        '''
        for i in range(self.x, self.x + self.width):
            if board.matrix[self.y + self.height][i] in mp:
                return True
        return False

    def check_top_collision_with_map(self, board):
        '''Function to check if the person has
        collided with a map element from the top
        '''
        for i in range(self.x, self.x + self.width):
            if board.matrix[self.y - 1][i] in mp:
                return True
        return False

    def check_side_collision_with_map(self, board):
        '''Function to check if the person has
        collided with a map element in the horizontal directions
        '''
        if self.check_left_collision_with_map(
                board) or self.check_right_collision_with_map(board):
            return True
        return False

    def check_up_collision_with_map(self, board):
        '''Function to check if the person has
        collided with a map element in the vertical directions
        '''
        if self.check_top_collision_with_map(
                board) or self.check_bottom_collision_with_map(board):
            return True
        return False

    def check_left_collision_with_item(self, item):
        '''Function to check if the person has
        collided with an item from the left
        '''
        if self.x in range(item.x, item.x + item.width):
            return True
        return False

    def check_right_collision_with_item(self, item):
        '''Function to check if the person has
        collided with an item from the right
        '''
        if self.x + self.width in range(item.x, item.x + item.width):
            return True
        return False

    def check_top_collision_with_item(self, item):
        '''Function to check if the person has
        collided with an item from the top
        '''
        if self.y in range(item.y, item.y + item.height):
            return True
        return False

    def check_bottom_collision_with_item(self, item):
        '''Function to check if the person has
        collided with an item from the bottom
        '''
        if self.y + self.height in range(item.y, item.y + item.height):
            return True
        return False

    def check_up_collision_with_item(self, item):
        '''Function to check if the person has
        collided with an item in the vertical directions
        '''
        if self.check_top_collision_with_item(
                item) and self.check_bottom_collision_with_item(item):
            return True
        return False

    def check_side_collision_with_item(self, item):
        '''Function to check if the person has
        collided with an item in the horizontal directions
        '''
        if self.check_left_collision_with_item(
                item) and self.check_right_collision_with_item(item):
            return True
        return False

    def check_complete_collision_with_item(self, item):
        '''Function to check if the person has
        collided with an item.
        '''
        if self.check_side_collision_with_item(
                item) and self.check_up_collision_with_item(item):
            return True
        return False

    def check_overlap_with_item(self, item):
        '''Function to check if the person has
        overlapped with an item.
        '''
        if self.x < (
                item.x +
                item.width) and (
                self.x +
                self.width) > item.x and self.y < (
                item.y +
                item.height) and (
                    self.y +
                self.height) > item.y:
            return True
        return False


class Mario(Person):
    '''Class to define the main player of the game.
    Initilized Mario with its size, matrix and velocities.
    '''

    def __init__(self, x, y, height, width, dx, dy, gravity, board):
        super().__init__(x, y, height, width, dx, dy, gravity, board)
        self.height = 3
        self.lives = 3
        self.width = 6
        self.dx = 3
        self.dy = -1
        self.jump = 8
        self.height_at_jump = 0
        self.score = 0
        self.killed = 0
        self.gravity = 1
        self.coins = 0
        self.win = False
        self.matrix = [
            ['[', '[', 'm', 'm', ']', ']'],
            [' ', '-', '|', '|', '-', ' '],
            [' ', '/', '/', '\\', '\\', ' '],
        ]
        for i in range(self.height):
            for j in range(self.width):
                if self.matrix[i][j] is 'm':
                    self.matrix[i][j] = Fore.CYAN + \
                        self.matrix[i][j] + Fore.RESET
                elif self.matrix[i][j] is ']' or self.matrix[i][j] is '[':
                    self.matrix[i][j] = Fore.YELLOW + \
                        self.matrix[i][j] + Fore.RESET
                elif self.matrix[i][j] is '-' or self.matrix[i][j] is '/' or self.matrix[i][j] is '\\':
                    self.matrix[i][j] = Fore.MAGENTA + \
                        self.matrix[i][j] + Fore.RESET
                else:
                    self.matrix[i][j] = Fore.RED + \
                        self.matrix[i][j] + Fore.RESET

    def mario_jump(self):
        '''Function to initialize the players jump
        '''
        self.height_at_jump = 0

    def mario_update_y(self, board):
        '''Function to update the player's y co-ordinates and
        instill the effect of gravity
        '''
        if self.height_at_jump <= self.jump:
            self.dy = -1
            self.height_at_jump += 1
            if self.check_top_collision_with_map(board):
                self.height_at_jump += 9
                self.dy = 1
        else:
            self.dy = 1

        if not self.check_bottom_collision_with_map(board):
            self.y += self.dy

    def enemy_kill(self, item):
        '''Function to check if the player jumps and
        kills the enemy
        '''
        if self.x < (
                item.x +
                item.width) and (
                self.x +
                self.width) > item.x and self.y < (
                item.y +
                item.height) and (
                    self.y +
                self.height) > item.y:
            if self.y < item.y:
                return True
        return False

    def check_hit_flagpole(self, item):
        '''Function to check if the player has captured the flagpole
        '''
        if self.check_overlap_with_item(item):
            return True
        return False


class Enemy(Person):
    '''Class to define the normal enemy
    '''

    def __init__(self, x, y, height, width, dx, dy, gravity, board):
        super().__init__(x, y, height, width, dx, dy, gravity, board)
        self.kill = False
        self.height = 3
        self.width = 6
        self.dy = 0
        self.matrix = [
            [' ', ' ', ' ', ' ', ' ', ' '],
            ['{', '(', 'O', 'O', ')', '}'],
            [' ', '~', '}', '{', '~', ' '],
        ]
        for i in range(self.height):
            for j in range(self.width):
                if self.matrix[i][j] is 'O':
                    self.matrix[i][j] = Fore.BLUE + \
                        self.matrix[i][j] + Fore.RESET
                elif self.matrix[i][j] is '~':
                    self.matrix[i][j] = Fore.RED + \
                        self.matrix[i][j] + Fore.RESET
                else:
                    self.matrix[i][j] = Fore.GREEN + \
                        self.matrix[i][j] + Fore.RESET

    def move(self, board):
        '''Function to move the enemy laterally around in
        the game
        '''
        if self.check_side_collision_with_map(board):
            self.dx = -1 * self.dx
        self.x += self.dx

    def enemy_update_y(self, board):
        '''Function to instill the effect of gravity
        on the enemy
        '''
        if not self.check_up_collision_with_map(board):
            self.dy = 1
            self.y += self.dy

    def kill_player(self, item):
        '''Function to check if the enemy killed
        the player
        '''
        if self.x < (
                item.x +
                item.width) and (
                self.x +
                self.width) > item.x and self.y < (
                item.y +
                item.height) and (
                    self.y +
                self.height) > item.y:
            if item.y + item.height > self.y:
                return True
        return False


class SmartEnemy(Person):
    '''Class to define a smart enemy that follows the player
    around, avoiding obstacles.
    '''

    def __init__(self, x, y, height, width, dx, dy, gravity, board):
        super().__init__(x, y, height, width, dx, dy, gravity, board)
        self.height = 3
        self.width = 6
        self.kill = False
        self.dy = -1
        self.dx = 1
        self.jump = 6
        self.height_at_jump = 0
        self.matrix = [
            [' ', ' ', 'M', 'M', ' ', ' '],
            ['<', '[', 'W', 'W', ']', '>'],
            [' ', '~', '}', '{', '~', ' '],
        ]
        for i in range(self.height):
            for j in range(self.width):
                if self.matrix[i][j] is 'M' or self.matrix[i][j] is '>' or self.matrix[i][j] is '<':
                    self.matrix[i][j] = Fore.RED + \
                        self.matrix[i][j] + Fore.RESET
                elif self.matrix[i][j] is 'W':
                    self.matrix[i][j] = Fore.MAGENTA + \
                        self.matrix[i][j] + Fore.RESET

    def smart_enemy_jump(self):
        '''Function for the smart enemy to jump
        '''
        self.height_at_jump = self.y
        self.y -= self.jump

    def smart_enemy_update_y(self, board):
        '''Function to update the ordinate of the
        smart enemy
        '''
        if not self.check_up_collision_with_map(board):
            self.dy = 1
            self.y += self.dy

    def move(self, mario, board):
        '''Function for the enemy to move and
        follow the player
        '''
        if self.check_side_collision_with_map(board):
            self.smart_enemy_jump()
        if mario.x < self.x:
            if self.dx > 0:
                self.dx = self.dx * -1
        if mario.x > self.x:
            if self.dx < 0:
                self.dx = self.dx * -1
        self.x += self.dx

    def kill_player(self, item):
        '''Function to check if the smart enemy has
        killed the player
        '''
        if self.x < (
                item.x +
                item.width) and (
                self.x +
                self.width) > item.x and self.y < (
                item.y +
                item.height) and (
                    self.y +
                self.height) > item.y:
            return True
        return False
