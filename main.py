'''Main module of the game
Instantiating the game Engine and running it.
'''

from engine import Engine

game = Engine()

if __name__ == '__main__':
    game.choose_level()
    game.initialize()
    game.run()
