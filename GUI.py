from random import randint, choice
from Map import Map
from Character import McGyver, Guard
from item import Item
import pygame
from pygame.locals import *


class Gui:
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
        self.affichage()

        # Variable qui continue la boucle si = 1, stoppe si = 0
        continuer = 1
        # Boucle infinie
        while continuer:
            for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
                if event.type == QUIT:  # Si un de ces événements est de type QUIT
                   continuer = 0  # On arrête la boucle


    def load_image (self,file_image):
        self.file_image= file_image
        image_charge = pygame.image.load(file_image).convert()
        return image_charge

    def affichage(self):
        # list image
        list_image = ["venv/Images/Background.png", "venv/Images/Wall.png", "venv/Images/MacGyver.png",
                      "venv/Images/Gardien.png", "venv/Images/potion.png", "venv/Images/baton.png",
                      "venv/Images/pipe.png", "venv/Images/youwin.png", "venv/Images/youdied.png"]
        # Création de la fenêtre
        self.fenetre = pygame.display.set_mode((600, 600))

        # dispo image dans fenetre
        self.fond = self.load_image(list_image[0])
        self.fenetre.blit(self.fond, (0, 0))
        for x, line in enumerate(self.map.map_structure):
            for y, c in enumerate(line):
                if c == "x":
                    self.fenetre.blit(self.load_image(list_image[1]), (y*40, x*40))
                if c == "m":
                    self.mc_image= self.load_image(list_image[2])
                    self.fenetre.blit(self.mc_image, (self.mcgyver.y_position*40,self.mcgyver.x_position*40))
                if c == "g":
                    self.fenetre.blit(self.load_image(list_image[3]), (y*40, x*40))
                if c == "e":
                    self.fenetre.blit(self.load_image(list_image[4]), (y*40, x*40))
                if c == "n":
                    self.fenetre.blit(self.load_image(list_image[5]), (y * 40, x * 40))
                if c == "p":
                    self.fenetre.blit(self.load_image(list_image[6]), (y*40, x*40))
        # Rafraîchissement de l'écran
        pygame.display.flip()

    def start(self):

        # Rafraîchissement de l'écran
        pygame.display.flip()

        while (self.mcgyver.x_position, self.mcgyver.y_position) != (self.guard.x_position, self.guard.y_position):
            # Rafraîchissement de l'écran
            pygame.display.flip()
            continuer = 0
            continuer = 1
            self.map.write_character(" ", self.mcgyver.x_position, self.mcgyver.y_position)
            #x_position, y_position = self.mcgyver.x_position, self.mcgyver.y_position
            x_position, y_position = self.mcgyver.position()
            #x_position_moving, y_position_moving = self.mcgyver.move()
            while continuer:
                for event in pygame.event.get():  # Attente des événements
                    if event.type == QUIT:
                        continuer = 0
                    if event.type == KEYDOWN:
                        if event.key == K_UP:  # Si fleche vers le haut
                            self.mcgyver.x_position -= 1
                    if event.type == KEYDOWN:
                        if event.key == K_DOWN:  # Si fleche vers le haut
                            self.mcgyver.x_position += 1
                    if event.type == KEYDOWN:
                        if event.key == K_LEFT:  # Si fleche vers le haut
                            self.mcgyver.y_position -= 1
                    if event.type == KEYDOWN:
                        if event.key == K_RIGHT:  # Si fleche vers le haut
                            self.mcgyver.y_position += 1
                    x_position_moving, y_position_moving = self.mcgyver.position()
                    # Test to know, is it a good move?
                    if self.map.retrieve_character(x_position_moving, y_position_moving) != "x":
                        for item in self.items:
                            if self.map.retrieve_character(x_position_moving, y_position_moving) == item.character:
                                self.mcgyver.inventury.append(item.name)
                                #tester quel caractere pour l'effacer
                        self.mcgyver.set_position(x_position_moving, y_position_moving)
                        self.map.write_character("m", self.mcgyver.x_position, self.mcgyver.y_position)
                        # Re-collage
                        #self.fenetre.blit(self.fond, (0, 0))
                        self.affichage()
                        self.fenetre.blit(self.mc_image, (y_position_moving*40, (x_position_moving *40)))

                        # Rafraichissement
                        pygame.display.flip()


                    else:
                        print(" No, You can't go here")
                        self.mcgyver.set_position( x_position, y_position)
                        self.map.write_character("m", self.mcgyver.x_position, self.mcgyver.y_position)
                        self.affichage()

        # Condition to WIN or LOSE
        if len(self.mcgyver.inventury) == 3 :
            self.map.write_character("m", self.mcgyver.x_position, self.mcgyver.y_position)
            win = self.load_image("venv/Images/youwin.png").convert()
            self.fenetre.blit(win, (260, 260))
            pygame.display.flip()
            #print("YOU ARE A WINNER---YOU ARE A WINNER---YOU ARE A WINNER---YOU ARE A WINNER---YOU ARE A WINNER---")
        else:
            print("Sorry but you haven't the three object: YOU LOSE---YOU LOSE---YOU LOSE---YOU LOSE---YOU LOSE---")
            print("It fail ", int(3 -len(self.mcgyver.inventury)), " objet(s)")











