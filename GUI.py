from random import randint, choice
from Map import Map
from Character import McGyver, Guard
from item import Item
import pygame
from pygame.locals import *


class Gui
    def __init__(self):
        self.map = Map("maps.txt")
        # We looking for the position of Mc Gyver with is charater special "m"
        (x_pos_bigining, y_pos_bigining) = self.map.find_one_character("m")
        #  Test:
        print("la position de Mc Gyver est", x_pos_bigining, y_pos_bigining)
        # We looking for the position of Guard with is charater special "g"
        (x_pos_end, y_pos_end) = self.map.find_one_character("g")
        #  Test:
        print("la position du guard est ligne  ", x_pos_end, ", et colonne  ", y_pos_end)
        #  Create object mcgyver in his position
        self.mcgyver = McGyver(x_pos_bigining, y_pos_bigining)
        #  Create object guard in his position
        self.guard = Guard(x_pos_end, y_pos_end)
        # Create three objects
        self.items = [Item("e", "Ether", -1, -1), Item("n", "Needle", -1, -1), Item("p", "Pipe", -1, -1)]
        #  We looking for the frees positions (Character = " "), we write the positions in a  empty_space list
        empty_spaces = self.map.find_all_characters(" ")

        #  We add in the map the 3 random objects
        for item in self.items:
            position = choice(empty_spaces)  # random position in the list empty_space
            item.set_position(position[0], position[1])  # We place object on the map
            self.map.write_character(item.character, item.x, item.y)  # We put three objects in a  map

        #Initialisation de la bibliothèque Pygame
        pygame.init()

        #Création de la fenêtre
        fenetre = pygame.display.set_mode((600, 600))
        fond = pygame.image.load("venv/Images/Background.png").convert()
        fenetre.blit(fond, (0,0))
        # Chargement et collage du personnage
        perso = pygame.image.load("venv/Images/MacGyver.png").convert()
        fenetre.blit(perso, (0, 560))
        pygame.display.flip()

#Variable qui continue la boucle si = 1, stoppe si = 0
continuer = 1

#Rafraîchissement de l'écran
pygame.display.flip()



#Boucle infinie
while continuer:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			continuer = 0      #On arrête la boucle
