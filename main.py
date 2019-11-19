# coding: utf-8 # For French language
from GUI import Gui
from GameManager import GameManager
import argparse



"""" 
    This program is to star The Game Mac Gyver
"""
#create a class parse to choice between two option to play the Game,
#With GameManager or with GUI
def parse_arguments():
    parser= argparse.ArgumentParser()
    parser.add_argument("-d", "--datafile", help=""" Type of file: GameManager.py to game in console or GUI.py to game 
                        with window Pygame""")
    return  parser.parse_args()
"""
We can choice how to play with main 
"""
def main():
    args = parse_arguments()
    datafile = args.datafile

    if args.datafile == "GameManager.py":
        game = GameManager()
        game.start()
    elif args.datafile == "GUI.py":
        game = Gui()
        game.start()
        game.stop()


if __name__ == "__main__":  # Main is to star the play like a programm
    main()
