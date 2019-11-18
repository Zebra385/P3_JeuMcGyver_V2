from random import randint, choice
from Map import Map
from Character import McGyver, Guard
from item import Item
import pygame
from pygame.locals import *
"""
Class Gui to transform a file text in a labyrinthe: We can go in a empty espace and the wall is the character"x"
We use Pygame to open a window and load the differents pictures
"""

class Gui:
    def __init__(self):
        self.map = Map("maps.txt") #  to read the file text
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
        self.affichage() # Attribut to open the window Pygame whose create the labyrinth, yhe picture of Mc Gyver,
                         # the picture of guard and the pictures of three objects

        # Variable that  continue the condition "while" if is value is egal 1 and stop is his value is 0
        self.continuer = 1


    """ 
    To load a file picture with Pygame
    """

    def load_image (self,file_image):
        self.file_image= file_image
        image_charge = pygame.image.load(file_image).convert_alpha()
        return image_charge
    """
    To open a window Pygame whose create the labyrinth
    """
    def affichage(self):
        # Initialisation Pygame
        pygame.init()
        # list of differents pictures
        list_image = ["venv/Images/Background.png", "venv/Images/Wall.png", "venv/Images/MacGyver.png",
                      "venv/Images/Gardien.png", "venv/Images/potion.png", "venv/Images/baton.png",
                      "venv/Images/pipe.png", "venv/Images/youwin.png", "venv/Images/youdied.png"]
        # Open a window height and width egal 600 pixels
        self.fenetre = pygame.display.set_mode((600, 600))

        # load picture and put them in the window Pygame
        self.fond = self.load_image(list_image[0])
        self.fenetre.blit(self.fond, (0, 0))
        """
        We transform file text to a window Pygame : "x" = the wall , "m"= Mc Gyver,"g"= Guard, "e", "n" and "p" the three objects: potion, baton and pipe
        """
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
        # clear the window
        pygame.display.flip()
    """
    Attribut to star the game, we continue to play while the position of Mc Gyver is different to the position of guard 
    and the variable self.continue different to 0. In fact this variable wait that the player put on a  key of keyboard
    we use keyboard arrow key: K_UP to go up, K_DOWN to go down, K_LEFT to go left and K_RIGHT to go right
    """
    def start(self):


        while (self.mcgyver.x_position, self.mcgyver.y_position) != (self.guard.x_position, self.guard.y_position) and self.continuer :
           # We bigining to replace Mc Gyver position with " " instead of "m"
            self.map.write_character(" ", self.mcgyver.x_position, self.mcgyver.y_position)

            x_position, y_position = self.mcgyver.position()
            # TEST
            # print("la position de Mc Gyver est", x_position, y_position)
            #x_position_moving, y_position_moving = self.mcgyver.move()

            for event in pygame.event.get():  # Wait a key evenement
                if event.type == QUIT:  #  If we put in the cross in th heigt and right of the xwindow Pygame we can
                                        #  stop the play to close the window
                    self.continuer = 0
                if event.type == KEYDOWN:
                    if event.key == K_UP:  # to go up
                        self.mcgyver.x_position -= 1
                if event.type == KEYDOWN:
                    if event.key == K_DOWN:  # Sto go down
                        self.mcgyver.x_position += 1
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:  # to go leftt
                        self.mcgyver.y_position -= 1
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:  # to go right
                        self.mcgyver.y_position += 1
                x_position_moving, y_position_moving = self.mcgyver.position()  # New position of Mc Gyver after put on a
                                                                                # keyboard arrow key
                # Test to know, is it a good move?
                if self.map.retrieve_character(x_position_moving, y_position_moving) != "x":
                    # Test to know if Mc Gyver have take an object
                    for item in self.items:
                        if self.map.retrieve_character(x_position_moving, y_position_moving) == item.character:
                            self.mcgyver.inventury.append(item.name)# we add a object to Mc Gyver
                    #We change the position of Mc Gyver in the file text and we replace " " in "m"
                    self.mcgyver.set_position(x_position_moving, y_position_moving)
                    self.map.write_character("m", self.mcgyver.x_position, self.mcgyver.y_position)
                    # TEST print("la position de Mc Gyver a bougé en ", x_position_moving, y_position_moving)
                    # We move Mc Gyver ton the window Pygame
                    self.fenetre.blit(self.mc_image, (y_position_moving*40, (x_position_moving *40)))
                    # We display corectly Mc Gyver in this new position in the labyrinth
                    self.affichage()
                    pygame.display.flip()

                #  Test is not a good move
                else:
                    #  Test
                    print(" No, You can't go here")
                    self.mcgyver.set_position( x_position, y_position)
                    self.map.write_character("m", self.mcgyver.x_position, self.mcgyver.y_position)
                    self.affichage()


    # Conditions to WIN or LOSE
    def stop(self):

        pygame.display.flip()
        while self.continuer:
            if len(self.mcgyver.inventury) == 3 :
                print("YOU ARE A WINNER---YOU ARE A WINNER---YOU ARE A WINNER---YOU ARE A WINNER---YOU ARE A WINNER---")

                win = self.load_image("venv/Images/youwin.png").convert() # load picture when we win
                self.affichage()
                self.fenetre.blit(win, (0, 0))
                pygame.display.flip()

                for event in pygame.event.get():  #  If we put in the cross in th heigt and right of the xwindow Pygame we can
                                                 #  stop the play to close the window
                    if event.type == QUIT:
                        self.continuer = 0
                pygame.display.flip()


            else:
                print("Sorry but you haven't the three object: YOU LOSE---YOU LOSE---YOU LOSE---YOU LOSE---YOU LOSE---")
                print("It fail ", int(3 - len(self.mcgyver.inventury)), " objet(s)")
                dead = self.load_image("venv/Images/youdied.png").convert()# load picture when we died
                self.affichage()
                self.fenetre.blit(dead, (0, 0))
                pygame.display.flip()


                # Boucle infinie

                for event in pygame.event.get():  #  If we put in the cross in th heigt and right of the xwindow Pygame we can
                                                  #  stop the play to close the window
                    if event.type == QUIT:
                        self.continuer = 0
                pygame.display.flip()









