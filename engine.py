'''The game's Engine'''
import os
import sys
import subprocess
import time
import config
from input import Get, input_to
from person import Mario, Enemy, SmartEnemy
from colorama import Fore, Style
from items import Coin, Flagpole, Castle, Cloud1
from generate_map import Map
from utilities import superimpose, clear_sprite, playsound, stop_all_sound


class Engine:
    '''Class to define the Engine of the game.
    '''

    def __init__(self):
        self.FRAMES = 0
        self.screen = Map(40, 972)
        self.flagpole = Flagpole(904, 10, 24, 3, self.screen)
        self.castle = Castle(924, self.screen.height - 21, 14, 28, self.screen)
        self.mario = Mario(0, self.screen.height - 10,
                           1, 1, 1, 1, 1, self.screen)
        self.MOVE_BG = False
        self.Level = 0
        self.starting_fly_pos = []
        self.clouds = []
        self.coins = []
        self.enemies = []
        self.smart_enemies = []
        self.starting_enemy_pos = config.starting_enemy_pos[:]
        self.starting_smart_enem = config.starting_smart_enem[:]

    def deploy_smart_enemies(self):
        '''Function to check the current frame postion
        and deploy smart enemies.
        '''
        for i in self.starting_smart_enem:
            if i[0] in range(self.screen.x_cross, self.screen.x_cross + 108):
                if i[0] % 2 is 0:
                    self.smart_enemies.append(SmartEnemy(
                        i[0], i[1], 1, 1, 2, 1, 1, self.screen))
                else:
                    self.smart_enemies.append(SmartEnemy(
                        i[0], i[1], 1, 1, -2, 1, 1, self.screen))
                self.starting_smart_enem.remove(i)

    def deploy_normal_enemies(self):
        '''Function to check the current frame postion
        and deploy normal enemies.
        '''
        for i in self.starting_enemy_pos:
            if i[0] in range(self.screen.x_cross, self.screen.x_cross + 108):
                if i[0] % 2 is 0:
                    self.enemies.append(
                        Enemy(
                            i[0],
                            i[1],
                            1,
                            1,
                            1,
                            1,
                            1,
                            self.screen))
                else:
                    self.enemies.append(
                        Enemy(i[0], i[1], 1, 1, -1, 1, 1, self.screen))
                self.starting_enemy_pos.remove(i)

    def initialize_items(self):
        '''Function to initialize various objects on the
        game's map.
        '''
        coins_pos = config.coins_pos
        for coin in coins_pos:
            self.coins.append(Coin(coin[0], coin[1], None, None, self.screen))

        cloud_pos = config.cloud1_pos
        for cloud in cloud_pos:
            self.clouds.append(Cloud1(cloud[0], cloud[1], 4, 16, self.screen))

    def restart(self):
        '''Function to reset the player's and enemies positions
        if the player loses a life.
        '''
        self.render(self.MOVE_BG)
        time.sleep(3)
        os.system("clear")
        playsound('resources/main_theme.wav')
        del self.enemies[:]
        del self.smart_enemies[:]
        self.starting_enemy_pos = config.starting_enemy_pos[:]
        self.starting_smart_enem = config.starting_smart_enem[:]
        self.mario.x = 0
        self.mario.y = self.screen.height - 10
        self.screen.x_cross = 0

    def cue_end_animation(self):
        '''Function to display the flag capture animation when the
        player wins.
        '''
        stop_all_sound()
        del self.enemies[:]
        del self.smart_enemies[:]
        time.sleep(1)
        self.mario.score += (self.screen.height - self.mario.y) * 50
        playsound('resources/flagdown.wav')
        while not self.mario.check_bottom_collision_with_map(self.screen):
            self.mario.y += 1
            os.system('clear')
            self.update()
            self.render(self.MOVE_BG)
            time.sleep(0.1)
        playsound('resources/captureflag.wav')
        while not self.mario.x > self.castle.x + (self.castle.width / 2):
            self.mario.x += 1
            os.system('clear')
            self.update()
            self.render(self.MOVE_BG)
            time.sleep(0.1)
        time.sleep(1)
        os.system('clear')
        print('You Won !!!')
        print('Score :', self.mario.score)
        sys.exit()

    def cue_lost_card(self):
        '''Function to check the current frame postion
        and deploy normal enemies.
        '''
        stop_all_sound()
        playsound('resources/gameover.wav')
        os.system('clear')
        print('You Lost !!!')
        print('Score :', self.mario.score)
        time.sleep(2)
        sys.exit()

    def render(self, move_bg):
        '''Function to draw all the objects,
        players and enemies onto the screen'''
        life_string = ""
        for i in range(self.mario.lives):
            life_string += "❤️  "

        print(
            "💵 :",
            self.mario.coins,
            "\t\t\t\t\t\t\t\t\t\t\t\t   ",
            life_string)
        print("Score :", self.mario.score)
        self.screen.reset_matrix()
        for coin in self.coins:
            superimpose(coin, self.screen)
        for cloud in self.clouds:
            superimpose(cloud, self.screen)
        for enemy in self.enemies:
            superimpose(enemy, self.screen)
        for enemy in self.smart_enemies:
            superimpose(enemy, self.screen)
        superimpose(self.flagpole, self.screen)
        superimpose(self.castle, self.screen)
        superimpose(self.mario, self.screen)

        print(self.screen.printmatrix(self.screen.x_cross))
        print("🤖 :", self.mario.killed)

    def update(self):
        '''Function to update the status and the position
        of the objects, enemies and player
        '''
        if self.mario.x < self.screen.x_cross:
            self.mario.x = self.screen.x_cross

        if (self.mario.y + self.mario.height) > (self.screen.height - 2):
            stop_all_sound()
            playsound('resources/mariodie.wav')
            self.mario.lives -= 1
            self.restart()

        if self.mario.lives <= 0:
            self.cue_lost_card()

        if self.Level is 1:
            self.deploy_normal_enemies()
        elif self.Level is 2:
            self.deploy_smart_enemies()
        elif self.Level is 3:
            self.deploy_normal_enemies()
            self.deploy_smart_enemies()

        for coin in self.coins:
            if coin.check_collected(self.mario):
                playsound('resources/coin.wav')
                self.mario.coins += 1
                self.mario.score += 150
                self.coins.remove(coin)

        for enemy in self.enemies:
            if self.mario.enemy_kill(enemy) or (
                    enemy.y +
                    enemy.height) > (
                    self.screen.height -
                    4):
                if self.mario.enemy_kill(enemy):
                    self.mario.killed += 1
                    self.mario.score += 100
                    playsound('resources/stompenemy.wav')
                self.enemies.remove(enemy)
            enemy.move(self.screen)
            enemy.enemy_update_y(self.screen)

        for enemy in self.smart_enemies:
            if self.mario.enemy_kill(enemy) or (
                    enemy.y +
                    enemy.height) > (
                    self.screen.height -
                    4):
                if self.mario.enemy_kill(enemy):
                    self.mario.killed += 1
                    self.mario.score += 100
                    playsound('resources/stompenemy.wav')
                self.smart_enemies.remove(enemy)
            enemy.smart_enemy_update_y(self.screen)
            enemy.move(self.mario, self.screen)

        for enemy in self.enemies:
            if enemy.kill_player(self.mario):
                stop_all_sound()
                playsound('resources/mariodie.wav')
                self.mario.lives -= 1
                self.restart()

        for enemy in self.smart_enemies:
            if enemy.kill_player(self.mario):
                stop_all_sound()
                playsound('resources/mariodie.wav')
                self.mario.lives -= 1
                self.restart()

        self.mario.mario_update_y(self.screen)

    def quit(self):
        '''Function to quit the game
        '''
        stop_all_sound()
        os.system('clear')
        sys.exit()

    def choose_level(self):
        '''Function to select a level
        '''
        os.system('clear')
        playsound('resources/itsame.wav')
        print(Style.BRIGHT + Fore.BLUE + 'WELCOME TO MARIO' + Style.RESET_ALL)
        time.sleep(1.5)
        os.system('clear')
        print(Style.BRIGHT + Fore.MAGENTA + 'CHOOSE A LEVEL' + Style.RESET_ALL)
        print(
            'Level 0 : Conventional Mario with ' +
            Style.BRIGHT +
            Fore.CYAN +
            'No' +
            Style.RESET_ALL +
            ' Enemies')
        print(
            'Level 1 : Conventional Mario with ' +
            Style.BRIGHT +
            Fore.GREEN +
            'Easy' +
            Style.RESET_ALL +
            ' Enemies')
        print(
            'Level 2 : Conventional Mario with ' +
            Style.BRIGHT +
            Fore.YELLOW +
            'Difficult' +
            Style.RESET_ALL +
            ' Enemies')
        print('Level 3 : Conventional Mario with ' + Style.BRIGHT +
              Fore.RED + 'Impossible' + Style.RESET_ALL + ' Enemies')
        print('\nPress q to Quit\n')
        choice = input('OPTION : ')
        if choice is 'q':
            self.quit()
        try:
            choice = int(choice)
        except ValueError:
            os.system('clear')
            print(Style.BRIGHT + Fore.RED + 'INVALID OPTION' + Style.RESET_ALL)
            print('Terminating Game ...')
            time.sleep(1.5)
            self.quit()
        if choice not in range(4):
            os.system('clear')
            print(Style.BRIGHT + Fore.RED + 'INVALID OPTION' + Style.RESET_ALL)
            print('Terminating Game ...')
            time.sleep(1.5)
            self.quit()
        self.Level = choice

    def initialize(self):
        '''Function to initilize the objects
        and enemies onto the game screen based
        on the difficulty level
        '''
        os.system('clear')
        print(
            Style.BRIGHT +
            Fore.YELLOW +
            'Setting up the MAP ...' +
            Style.RESET_ALL)
        self.initialize_items()
        time.sleep(0.5)
        print(
            Style.BRIGHT +
            Fore.YELLOW +
            'Deploying Enemeies ... ' +
            Style.RESET_ALL)
        time.sleep(0.5)
        if self.Level is 1:
            self.deploy_normal_enemies()
        if self.Level is 2:
            self.deploy_smart_enemies()
        if self.Level is 3:
            self.deploy_normal_enemies()
            self.deploy_smart_enemies()
        playsound("resources/herewego.wav")

    def run(self):
        '''Function to run the main game loop
        '''
        playsound('resources/main_theme.wav')
        getch = Get()
        while True:
            self.FRAMES += 1
            input = input_to(getch)

            if input is not None:
                if input is 'd':

                    if self.mario.x + self.mario.width < self.screen.x_cross + 108 / 2:
                        clear_sprite(self.mario, self.screen)
                        if not self.mario.check_right_collision_with_map(
                                self.screen):
                            self.mario.x += self.mario.dx
                    elif self.screen.x_cross >= 864:
                        clear_sprite(self.mario, self.screen)
                        if not self.mario.check_right_collision_with_map(
                                self.screen):
                            self.mario.x += self.mario.dx
                    else:
                        if not self.mario.check_right_collision_with_map(
                                self.screen):
                            self.screen.x_cross += self.mario.dx
                            clear_sprite(self.mario, self.screen)
                            self.mario.x += self.mario.dx
                elif input is 'a':
                    clear_sprite(self.mario, self.screen)
                    if not self.mario.check_left_collision_with_map(
                            self.screen):
                        self.mario.x -= self.mario.dx
                elif input is 'w':
                    playsound('resources/jump.wav')
                    if self.mario.check_bottom_collision_with_map(self.screen):
                        clear_sprite(self.mario, self.screen)
                        self.mario.y -= 3
                        self.mario.mario_jump()

                elif input is 'q':
                    self.quit()

            if self.mario.check_hit_flagpole(self.flagpole):
                self.cue_end_animation()

            if self.mario.lives <= 0:
                self.cue_lost_card()

            os.system('clear')
            self.update()
            self.render(self.MOVE_BG)
            time.sleep(0.02)
