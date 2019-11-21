from random import randint, choice
from Map import Map
from Character import McGyver, Guard
from item import Item
import pygame
from pygame.locals import *


""" 
Class MySprite of pygame to make our texture
"""
SPRITE_SIZE = 40
class MySprite(pygame.sprite.Sprite):
    """ Class which inherit from pygame Sprite class """
    def __init__(self, image):
        super().__init__()# We herit the  __Sinit__ from class de pygame
        self.image = image
        self.rect = self.image.get_rect() #  Pygame create a new rect with the surface of picture , with the position x, y (0, 0).
    def move_sprite(self, x, y):
        """ It defines image rect x and y position from
        a position y, x """
        self.rect.x = y * SPRITE_SIZE
        self.rect.y = x * SPRITE_SIZE

"""
Class Gui to transform a file text in a labyrinthe: We can go in a empty espace and the wall is the character"x"
We use Pygame to open a window and load the differents pictures
"""



class Gui:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()  # We want change the time betwen two new windows
        self.fenetre = pygame.display.set_mode((600, 600))  # Dim of pygame window
        self.map = Map("maps.txt")  # to read the file text

        self.background_sprite_group = pygame.sprite.Group()
        self.Set_background()
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
        self.characters_sprites_group = pygame.sprite.Group()
        self.Set_character()

        #  Create the wall of labyrinth
        self.walls_sprite_group = pygame.sprite.Group()
        self.Set_wall()

        #  Create the 3 items
        self.items_sprite_group = pygame.sprite.Group()
        self.Set_items()

        # Variable that  continue the condition "while" if is value is egal 1 and stop is his value is 0
        self.continuer = 1


    """ 
    Def a method to load a file picture with Pygame
    """

    def load_image(self, file_image):
        # self.file_image = file_image
        image_charge = pygame.image.load(file_image).convert_alpha()
        return image_charge

    """
    Create method to make in good positions the sprite character in a goup
    """
    def Set_character(self):
        mcgyver = self.map.find_one_character("m")
        image_mcgyver = self.load_image("Images/MacGyver.png")
        self.mcgyver_sprite = MySprite(image_mcgyver)
        self.mcgyver_sprite.move_sprite(mcgyver[0], mcgyver[1])
        guard = self.map.find_one_character("g")
        image_guard = self.load_image("Images/Gardien.png")
        guard_sprite = MySprite(image_guard)
        guard_sprite.move_sprite(guard[0], guard[1])
        self.characters_sprites_group.add(self.mcgyver_sprite, guard_sprite)

    """
        Create method to make in good positions the sprite wall in a goup
    """

    def Set_wall(self):
        walls = self.map.find_all_characters("x")
        image_wall = self.load_image("Images/wall.png")
        for wall in walls:
            sprite = MySprite(image_wall)
            sprite.move_sprite(wall[0], wall[1])
            self.walls_sprite_group.add(sprite)

    """
        Create method to make in good positions the sprite background in a goup
    """

    def Set_background(self):
        image_background = self.load_image("Images/Background.png")
        sprite = MySprite(image_background)
        sprite.move_sprite(0, 0)
        self.background_sprite_group.add(sprite)

    """
        Create method to make in good positions the sprite item in a goup
    """
    def Set_items(self):
        #items= self.map.find_all_characters(self.items_sprites_group)
        empty_spaces = self.map.find_all_characters(" ")
        self.items = [Item("e", "Ether", -1, -1), Item("n", "Needle", -1, -1), Item("p", "Pipe", -1, -1)]
        self.ether_sprite = MySprite(self.load_image("Images/potion.png"))
        self.needle_sprite = MySprite(self.load_image("Images/baton.png"))
        self.pipe_sprite = MySprite(self.load_image("Images/pipe.png"))
        self.items_sprite_group.add(self.ether_sprite, self.needle_sprite, self.pipe_sprite)
        for item in self.items:
            position = choice(empty_spaces)  # random position in the list empty_space
            item.set_position(position[0], position[1])  # We place object on the map
            self.map.write_character(item.character, item.x, item.y)  # We put three objects in a  map

        for idx, sprite in enumerate( self.items_sprite_group):
            item = self.items[idx]
            sprite.move_sprite(item.x, item.y)
            self.items_sprite_group.add(sprite)

    """ Method to delete a item_sprite """

    def kill(self, character):
        if character == "e":
            pygame.sprite.Sprite.kill(self.ether_sprite)
        elif character == "n":
            pygame.sprite.Sprite.kill(self.needle_sprite)
        elif character == "p":
            pygame.sprite.Sprite.kill(self.pipe_sprite)

    """
    Method to star the game, we continue to play while the position of Mc Gyver is different to the position of guard 
    and the variable self.continue different to 0. In fact this variable wait that the player put on a  key of keyboard
    we use keyboard arrow key: K_UP to go up, K_DOWN to go down, K_LEFT to go left and K_RIGHT to go right
    """

    def start(self):
        print("we use keyboard arrow key: K_UP to go up, K_DOWN to go down, K_LEFT to go left and K_RIGHT to go right ")

        while (self.mcgyver.x_position, self.mcgyver.y_position) != (
            self.guard.x_position, self.guard.y_position) and self.continuer:
            # We draw in this order background, wall, items (3) and characters(Mc Gyver and the  Guard)
            self.background_sprite_group.draw(self.fenetre)
            self.walls_sprite_group.draw(self.fenetre)
            self.items_sprite_group.draw(self.fenetre)
            self.characters_sprites_group.draw(self.fenetre)

            # We bigining to replace Mc Gyver position with " " instead of "m"
            self.map.write_character(" ", self.mcgyver.x_position, self.mcgyver.y_position)
            x_position, y_position = self.mcgyver.position()

            for event in pygame.event.get():  # Wait a key evenement
                if event.type == QUIT:  # If we put in the cross in th heigt and right of the xwindow Pygame we can
                    #  stop the play to close the window
                    self.continuer = 0
                if event.type == KEYDOWN:
                    if event.key == K_UP:  # to go up
                        self.mcgyver.x_position -= 1
                
                    if event.key == K_DOWN:  # Sto go down
                        self.mcgyver.x_position += 1
                
                    if event.key == K_LEFT:  # to go leftt
                        self.mcgyver.y_position -= 1
                
                    if event.key == K_RIGHT:  # to go right
                        self.mcgyver.y_position += 1

                x_position_moving, y_position_moving = self.mcgyver.position()  # New position of Mc Gyver after put on a
                # keyboard arrow key
                # Test to know, is it a good move?
                if self.map.retrieve_character(x_position_moving, y_position_moving) != "x":
                    # Test to know if Mc Gyver have take an object
                    for  item in self.items:
                       if self.map.retrieve_character(x_position_moving, y_position_moving) == item.character:
                            self.mcgyver.inventury.append(item.name)  # we add a object to Mc Gyver
                            # we kill item_Sprite
                            self.kill(item.character)
                    # We change the position of Mc Gyver in the file text and we replace " " in "m"
                    self.mcgyver.set_position(x_position_moving, y_position_moving)
                    self.map.write_character("m", self.mcgyver.x_position, self.mcgyver.y_position)
                     #TEST
                    print("la position de Mc Gyver a bougé en ", x_position_moving, y_position_moving)
                    # We move Mc Gyver ton the window Pygame
                    self.mcgyver_sprite.move_sprite(x_position_moving, y_position_moving)


                #  Test is not a good move
                else:
                    #  Test
                   print(" No, You can't go here")
                   self.mcgyver.set_position(x_position, y_position)
                   self.map.write_character("m", self.mcgyver.x_position, self.mcgyver.y_position)

            pygame.display.flip()
            self.clock.tick(60)# 60 pictures per second
    """
      Method to stop the game
      WIN when Mc gyver is in a position of guard whith 3 objects
      LOSE if have not the 3 objects
    """

    def stop(self):


        while self.continuer:
            if len(self.mcgyver.inventury) == 3:
                print("YOU ARE A WINNER---YOU ARE A WINNER---YOU ARE A WINNER---YOU ARE A WINNER---YOU ARE A WINNER---")

                win = self.load_image("Images/youwin.png").convert()  # load picture when we win

                self.fenetre.blit(win, (0, 0))
                pygame.display.flip()

                for event in pygame.event.get():  # If we put in the cross in th heigt and right of the xwindow Pygame we can
                    #  stop the play to close the window
                    if event.type == QUIT:
                        self.continuer = 0



            else:
                print("Sorry but you haven't the three object: YOU LOSE---YOU LOSE---YOU LOSE---YOU LOSE---YOU LOSE---")
                print("It fail ", int(3 - len(self.mcgyver.inventury)), " objet(s)")
                dead = self.load_image("Images/youdied.png").convert()  # load picture when we died
                self.fenetre.blit(dead, (0, 0))
                pygame.display.flip()

                # Boucle infinie

                for event in pygame.event.get():  # If we put in the cross in th heigt and right of the xwindow Pygame we can
                    #  stop the play to close the window
                    if event.type == QUIT:
                        self.continuer = 0

