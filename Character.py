import pygame
from pygame.constants import K_UP, K_DOWN, K_LEFT, K_RIGHT
"""
Create a class Character with attribute a position: x_position for index of line
and y_position for index of column
"""



class Character:
    def __init__(self, character, x_position, y_position):
        self.character = character
        self.x_position = x_position
        self.y_position = y_position


"""
Create class McGyver that are a children-class Character with special
character m
"""


class McGyver(Character):
    def __init__(self, x_position, y_position):
        Character.__init__(self, "m", x_position, y_position)
        self.inventory = []
        # A list to stock the object
        # (item) that Mc Gyver take

    """
    Method move to move m like My Gyver with keyboard z to up, s:  down, 
    q : left and  d : right
    """
    def move(self):
        keyboard = input("Tell me how you want  move Mc Gyver; "
                         "the key z to up, s:  down, q : left "
                         "and  d : right ")
        if keyboard == 'z':  # if key 'z' is pressed
            self.x_position -= 1
            return self.x_position, self.y_position
        elif keyboard == 's':
            self.x_position += 1
            return self.x_position, self.y_position
        if keyboard == 'q':
            self.y_position -= 1
            return self.x_position, self.y_position
        elif keyboard == 'd':
            self.y_position += 1
            return self.x_position, self.y_position
        else:  # if an other key : make nothing and  write a message
            print("!!!!!!!This key of keyboard is forbiden-!!!!!!!!!!!!!")
            return self.x_position, self.y_position

    def move_gui(self,event):
        if event.key == K_UP:  # to go up
            self.x_position -= 1
        if event.key == K_DOWN:  # Sto go down
            self.x_position += 1
        if event.key == K_LEFT:  # to go leftt
            self.y_position -= 1
        if event.key == K_RIGHT:  # to go right
            self.y_position += 1

    """
    Methode to know the position
    """
    def position(self):
        return self.x_position, self.y_position
    """
    Method to set position
    """
    def set_position(self, x, y):
        self.x_position = x
        self.y_position = y

    """
    Method to inventory the item that Mc Gyver take on the map
    """

    def add_item(self, item_name):
        self.inventory.append(item_name)

"""
Create class Guard those are a children-class Character with special character g
"""


class Guard(Character):
    def __init__(self, x_position, y_position,):
        Character.__init__(self, "g", x_position, y_position)
