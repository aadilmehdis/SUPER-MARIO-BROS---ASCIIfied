# Python Terminal Mario

## Introduction

This is the terminal version of Mario written in Python. It uses the basic Python libraries and modules.

This game has been tested on **Mac OSX** and **Linux** based Operating Systems.

## Structure and Features

The game application exhibits the OOP concepts of Inheritance, Encapsulation, Polymorphism, Abstraction along with Function Overloading.

The game follows PEP8 style guide for python code.

- The Engine of the game is defined `Engine` class, which contains crucial functions necesssary for the running of the game. The engine of the game is responsible for the various updates and rendering of the objects onto the terminal screen. The main game loop is a function of the `Engine` class.

- Every Player or Enemy is derived from `Person` class.
    - The Base class `Person` has basic functionalities common among all the moving entities in the game.
    - The `Mario` class inherits from the `Person` Base Class and has overloaded the functions of the Base class to respond to the environment and the keypress from the Player.
    - The `Enemy` and `SmartEnemy` class inherits from the class `Person` as well and has the move functions overloaded differently than Mario.
    - All the moving entities (`Mario`, `Enemy`, `SmartEnemy`) have their motion subjected to a gravitational simulation.
    - The `SmartEnemy` can detect `Mario`'s position and follow him around to kill him. The `SmartEnemy` can also jump over obstacles and circumvent its path to reach to `Mario` in order to kill him.
    - The `Enemy` is a normal enemy which can kill `Mario` in the event of Mario running into him or vice-versa. 

- Every Obstacle or Item _( Coins, Flag, Bricks, etc.)_ is derived from the `Item` class.
    - The moving entities in the game are all subjected to a possible with the map objects like bricks, tunnels, flagpoles, coins, etc. and change their course of direction or respond to the event of collision accordingly.

- The Game Screen has its own class which generates the game map and can blit object, players and enemies onto the screen.
    - The game has a pre-generated level map which is rendered during the run time and is updated according to `Mario`'s position in the game.

- The game also has interactive sounds which are played on the occurance of any event and has a colorful interface aswell.

## Running the program

1. Install all the requirements:
	- `pip install -r requirements.txt`
2. Run the program:
    - `python3 main.py`

## Controls

- Press **w** to jump
- Press **a** to move left
- Press **d** to move right
- Press **q** to quit the game

## Project Tree

* ./20171043_Assign1
    * README.md
    * requirements.txt
    * main.py
    * engine.py
    * __init__.py
    * input.py
    * config.py
    * person.py
    * utilities.py
    * items.py
    * generate_map.py
    * resources
        * captureflag.wav	
        * coin.wav	
        * flagdown.wav	
        * gameover.wav	
        * herewego.wav	
        * itsame.wav	
        * jump.wav	
        * main_theme.wav	
        * mariodie.wav	
        * stompenemy.wav	
