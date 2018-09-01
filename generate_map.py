'''Generate and Display the Game's Map'''
from colorama import Fore


def superimpose(x, y, height, width, board_matrix, item_matrix):
    '''Function to place objects
    onto the map of the board
    '''
    ii = 0
    for i in range(y, y + height):
        jj = 0
        for j in range(x, x + width):
            board_matrix[i][j] = item_matrix[ii][jj]
            jj += 1
        ii += 1


class Map:
    '''Class to define, set and initialize the map
    of the game.
    '''

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.x_cross = 0
        self.matrix = [[' ' for x in range(width)] for y in range(height)]

        # 1*9
        self.plane = [
            ['_', '_', '_', '_', '_', '_', '_', '_', '_'],
        ]

        for i in range(1):
            for j in range(9):
                self.plane[i][j] = Fore.YELLOW + self.plane[i][j] + Fore.RESET

        # 3*9
        self.block = [
            ['_', '_', '|', '_', '_', '|', '_', '_', '|'],
            ['_', '|', '_', '_', '|', '_', '_', '|', '_'],
            ['_', '_', '|', '_', '_', '|', '_', '_', '|'],
        ]

        for i in range(3):
            for j in range(9):
                self.block[i][j] = Fore.RED + self.block[i][j] + Fore.RESET

        # 3*6
        self.brick = [
            ['_', '_', '_', '_', '_', '_'],
            ['|', '_', '_', '|', '_', '|'],
            ['|', '_', '|', '_', '_', '|'],
        ]

        for i in range(3):
            for j in range(6):
                self.brick[i][j] = Fore.RED + self.brick[i][j] + Fore.RESET

        # 21*10
        self.tunnel1 = [
            ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
            ['|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|'],
            [' ', ' ', ' ', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', '|', ' ', ' ', ' ', ' '],
        ]

        for i in range(10):
            for j in range(21):
                self.tunnel1[i][j] = Fore.GREEN + \
                    self.tunnel1[i][j] + Fore.RESET

        # 7*15
        self.ditch = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ],
        ]

        self.reset_matrix()

    def get_matrix(self):
        '''Function to return the matrix form of the
        map
        '''
        return self.matrix

    def update_matrix(self, new_matrix):
        '''Function to update the matrix with a new matrix
        '''
        self.matrix = new_matrix

    def reset_matrix(self):
        '''Function to reset and update the matrix
        based on character, enemy and object movment
        '''
        self.matrix = [[' ' for x in range(self.width)]
                       for y in range(self.height)]
        superimpose(70, 25, 3, 6, self.matrix, self.brick)
        superimpose(80, 18, 3, 6, self.matrix, self.brick)
        superimpose(80, 25, 3, 6, self.matrix, self.brick)
        superimpose(50, 25, 3, 6, self.matrix, self.brick)
        superimpose(90, 25, 3, 6, self.matrix, self.brick)
        superimpose(270, 25, 3, 6, self.matrix, self.brick)
        superimpose(276, 25, 3, 6, self.matrix, self.brick)
        superimpose(282, 25, 3, 6, self.matrix, self.brick)
        superimpose(294, 20, 3, 6, self.matrix, self.brick)
        superimpose(300, 20, 3, 6, self.matrix, self.brick)
        superimpose(312, 25, 3, 6, self.matrix, self.brick)
        superimpose(336, 25, 3, 6, self.matrix, self.brick)
        superimpose(348, 25, 3, 6, self.matrix, self.brick)

        for i in range(371, 419, 6):
            superimpose(i, 18, 3, 6, self.matrix, self.brick)

        superimpose(120, self.height - 13, 10, 21, self.matrix, self.tunnel1)
        superimpose(180, self.height - 17, 10, 21, self.matrix, self.tunnel1)
        superimpose(230, self.height - 12, 10, 21, self.matrix, self.tunnel1)

        k = 0
        for i in range(self.height - 9, self.height - 24, -3):
            l = 0
            for j in range(492, 522, 6):
                if l > k:
                    superimpose(j, i, 3, 6, self.matrix, self.brick)
                l += 1
            k += 1

        k = 0
        for i in range(self.height - 21, self.height - 6, 3):
            l = 0
            for j in range(532, 604, 6):
                if l < k:
                    superimpose(j, i, 3, 6, self.matrix, self.brick)
                l += 1
            k += 1

        k = 0
        for i in range(self.height - 9, self.height - 21, -3):
            l = 0
            for j in range(600, 636, 6):
                if l > k:
                    superimpose(j, i, 3, 6, self.matrix, self.brick)
                l += 1
            k += 1

        superimpose(636, self.height - 7, 7, 15, self.matrix, self.ditch)

        k = 0
        for i in range(self.height - 21, self.height - 6, 3):
            l = 0
            for j in range(651, 681, 6):
                if l < k:
                    superimpose(j, i, 3, 6, self.matrix, self.brick)
                l += 1
            k += 1

        k = 0
        for i in range(self.height - 21, self.height - 6, 3):
            l = 0
            for j in range(651, 681, 6):
                if l < k:
                    superimpose(j, i, 3, 6, self.matrix, self.brick)
                l += 1
            k += 1

        superimpose(711, self.height - 17, 10, 21, self.matrix, self.tunnel1)
        superimpose(781, self.height - 15, 10, 21, self.matrix, self.tunnel1)

        k = 0
        for i in range(self.height - 9, self.height - 27, -3):
            l = 0
            for j in range(802, 862, 6):
                if l > k:
                    superimpose(j, i, 3, 6, self.matrix, self.brick)
                l += 1
            k += 1

        for i in range(0, self.width, 9):
            superimpose(i, self.height - 7, 1, 9, self.matrix, self.plane)
            superimpose(i, self.height - 3, 3, 9, self.matrix, self.block)
            superimpose(i, self.height - 6, 3, 9, self.matrix, self.block)

        superimpose(636, self.height - 7, 7, 15, self.matrix, self.ditch)
        superimpose(300, self.height - 7, 7, 15, self.matrix, self.ditch)
        superimpose(314, self.height - 7, 7, 15, self.matrix, self.ditch)
        superimpose(400, self.height - 7, 7, 15, self.matrix, self.ditch)

    def printmatrix(self, x):
        '''Function to print the matrix
        on the terminal as per the player
        movement.
        '''
        string_matrix = ""
        for i in range(self.height):
            for j in range(x, 108 + x):
                string_matrix += self.matrix[i][j]
            string_matrix += '\n'
        return string_matrix

    def __str__(self):
        '''Function to print the matrix
        on the terminal
        '''
        string_matrix = ""

        for i in range(self.height):
            for j in range(self.width):
                string_matrix += self.matrix[i][j]
            string_matrix += '\n'
        return string_matrix


if __name__ == '__main__':
    a = Map(40, 972)
    print(a)
