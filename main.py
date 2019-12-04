# coding: utf-8 # For French language
from GUI import Gui
from GameManager import GameManager
import argparse


""""
This program is to star The Game Mac Gyver
"""
#  create a class parse to choice between two option to play the Game,
#  No option: we play automatically with GUI (Window Pycharm)
#  With option -t : We use the Terminal


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--Terminal", action="store_true",
                        help=""" Without option, we play with window Pygame,
                        with option "-t", we use Terminal""")
    return parser.parse_args()


"""
We can choice how to play with main
"""


def main():
    args = parse_arguments()
    if args.Terminal:
        game = GameManager()
        game.start()
    else:
        game = Gui()
        game.start()
        game.stop()


if __name__ == "__main__":  # Main is to star the play like a program
    main()
