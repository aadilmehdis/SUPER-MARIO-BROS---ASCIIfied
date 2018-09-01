'''Implementation of game objects and obstacles'''
from colorama import Fore


class Item:
    '''General item class to define various
    obstacles and objects
    '''

    def __init__(self, x, y, height, width, board):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.matrix = []

    def get_matrix(self):
        '''Function to return the matrix
        '''
        return self.matrix

    def check_overlap(self, item):
        '''Function to check overlap with another item
        or person
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
        else:
            return False


class Coin(Item):
    '''Class for Coin item
    '''

    def __init__(self, x, y, height, width, board):
        super().__init__(x, y, height, width, board)
        self.height = 3
        self.width = 5
        self.matrix = [
            [' ', '*', '*', '*', ' '],
            ['*', '$', '$', '$', '*'],
            [' ', '*', '*', '*', ' '],
        ]
        for i in range(self.height):
            for j in range(self.width):
                self.matrix[i][j] = Fore.YELLOW + \
                    self.matrix[i][j] + Fore.RESET

    def check_collected(self, player):
        '''Function to check if the coin is
        collected by the player
        '''
        if self.check_overlap(player):
            return True
        return False


class Castle(Item):
    '''Class for Castle item
    '''

    def __init__(self, x, y, height, width, board):
        super().__init__(x, y, height, width, board)
        self.height = 14
        self.width = 28
        self.matrix = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', ':', '\\', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '.', '\\', ' ', ' ', ' ', '\\', ':', '/', ' ', ' ', ' ', '/', '.', '\\', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ')', '.', '(', ' ', ' ', ' ', '|', ':', '|', ' ', ' ', ' ', ')', '.', '(', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', '/', '.', '.', '.', '\\', ' ', '/', ':', ':', ':', '\\', ' ', '/', '.', '.', '.', '\\', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ')', '.', '.', '.', '(', ' ', ')', ':', '?', ':', '(', ' ', ')', '.', '.', '.', '(', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ')', '.', '?', '.', '(', ' ', ')', ':', ':', ':', '(', ' ', ')', '.', '?', '.', '(', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ')', '.', '.', '.', '(', '_', '_', '_', '_', '_', '_', '_', ')', '.', '.', '.', '(', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', '|', '.', '.', '.', '.', '.', '.', '_', '_', '_', '_', '_', '.', '.', '.', '.', '.', '.', '|', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', '|', '.', '.', '.', '.', '.', '/', '<', '<', '<', '<', '<', '\\', '.', '.', '.', '.', '.', '|', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', '|', '.', '.', '.', '.', '.', '|', '>', '>', '>', '>', '>', '|', '.', '.', '.', '.', '.', '|', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', '|', '.', '.', '.', '.', '.', '|', '<', '<', '<', '<', '<', '|', '.', '.', '.', '.', '.', '|', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', '/', '@', '@', '@', '@', '@', '@', '@', ':', ':', ':', ':', ':', '@', '@', '@', '@', '@', '@', '@', '\\', ' ', ' '],
            [' ', ' ', ' ', '_', '/', '@', '@', '@', '@', '@', '@', '@', ':', ':', ':', ':', ':', '@', '@', '@', '@', '@', '@', '@', '@', '@', '\\', ' '],
            [' ', ' ', '/', '@', '@', '@', '@', '@', '@', '@', '@', ':', ':', ':', ':', ':', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '@', '\\'],
        ]
        for i in range(self.height):
            for j in range(self.width):
                if self.matrix[i][j] is '|' or self.matrix[i][
                        j] is '_' or self.matrix[i][j] is ')' or self.matrix[i][j] is '(':
                    self.matrix[i][j] = Fore.YELLOW + \
                        self.matrix[i][j] + Fore.RESET
                elif self.matrix[i][j] is '.':
                    self.matrix[i][j] = Fore.MAGENTA + \
                        self.matrix[i][j] + Fore.RESET
                elif self.matrix[i][j] is '@':
                    self.matrix[i][j] = Fore.GREEN + \
                        self.matrix[i][j] + Fore.RESET
                elif self.matrix[i][j] is '>' or self.matrix[i][j] is '<':
                    self.matrix[i][j] = Fore.RED + \
                        self.matrix[i][j] + Fore.RESET
                else:
                    self.matrix[i][j] = Fore.CYAN + \
                        self.matrix[i][j] + Fore.RESET

    def check_won(self, player):
        '''Function to check
        if the player won the game
        '''
        if self.check_overlap(player):
            player.win = True


class Flagpole(Item):
    '''Class to define the Flagpole
    '''

    def __init__(self, x, y, height, width, board):
        super().__init__(x, y, height, width, board)
        self.height = 24
        self.width = 3
        self.matrix = [
            ['I', 'M', 'I'], ['I', 'M', 'I'], ['I', 'M', 'I'],
            ['I', 'M', 'I'], ['I', 'M', 'I'], ['I', 'M', 'I'],
            ['I', 'M', 'I'], ['I', 'M', 'I'], ['I', 'M', 'I'],
            ['I', 'M', 'I'], ['I', 'M', 'I'], ['I', 'M', 'I'],
            ['I', 'M', 'I'], ['I', 'M', 'I'], ['I', 'M', 'I'],
            ['I', 'M', 'I'], ['I', 'M', 'I'], ['I', 'M', 'I'],
            ['I', 'M', 'I'], ['I', 'M', 'I'], ['I', 'M', 'I'],
            ['I', 'M', 'I'], ['I', 'M', 'I'], ['I', 'M', 'I'],
        ]


class Cloud1(Item):
    '''Class to define the Cloud
    '''

    def __init__(self, x, y, height, width, board):
        super().__init__(x, y, height, width, board)
        self.height = 4
        self.width = 16
        self.matrix = [
            [' ', ' ', ' ', ' ', '_', ' ', ' ', '_', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
            [' ', ' ', ' ', '(', ' ', '`', ' ', ' ', ' ', ')', '_', ' ', ' ', ' ', ' ', ' ', ],
            [' ', ' ', '(', ' ', ' ', ' ', ' ', ')', ' ', ' ', ' ', ' ', '`', ')', ' ', ' ', ],
            ['(', '_', ' ', ' ', ' ', '(', '_', ' ', '.', ' ', ' ', '_', ')', ' ', '_', ')', ]
        ]
        for i in range(self.height):
            for j in range(self.width):
                self.matrix[i][j] = Fore.BLUE + self.matrix[i][j] + Fore.RESET
