'''Utility Functions'''
import os

def playsound(path):
    '''Function to play sounds
    (Works only on Linux based OS)
    '''
    try:
        os.system('aplay -q '+ path +' 2> /dev/null &')
        os.system('afplay  '+ path +' 2> /dev/null &')
    except:
        pass

def stop_all_sound():
    '''Function to stop all sounds
    (Works only on Linux based OS)
    '''
    try:
        os.system("ps ax | grep aplay | grep -v grep | awk \'{print \"kill -9 \" $1}\' | sh 2> /dev/null")
        os.system("ps ax | grep afplay | grep -v grep | awk \'{print \"kill -9 \" $1}\' | sh 2> /dev/null")
    except:
        pass
        
def superimpose(item, board):
    '''Function to place objects
    onto the map of the board
    '''
    board_matrix = board.get_matrix()
    item_matrix = item.get_matrix()
    ii = 0
    for i in range(item.y, item.y + item.height):
        jj = 0
        for j in range(item.x, item.x + item.width):
            board_matrix[i][j] = item_matrix[ii][jj]
            jj += 1
        ii += 1
    board.update_matrix(board_matrix)


def clear_sprite(item, board):
    '''Function to clear the object off the
    console screen
    '''
    board_matrix = board.get_matrix()

    for i in range(item.y, item.y + item.height):
        for j in range(item.x, item.x + item.width):
            board_matrix[i][j] = ' '
    board.update_matrix(board_matrix)
