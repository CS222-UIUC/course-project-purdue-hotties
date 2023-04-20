#! /usr/bin/python3
from lib.game import Game

if __name__ == "__main__":
    options = {"portal" : True, "block" : False}
    game = Game(options)
    game.game_start()
