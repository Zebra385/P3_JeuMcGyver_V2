from random import randint, choice
from Map import Map
from Character import McGyver, Guard
from item import Item


"""
Create class GameManager to star the game

"""
class GameManager:
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
        self.items = [Item("e", "Ether",-1,-1), Item("n", "Needle",-1,-1) , Item("p", "Pipe",-1,-1)]
        #  We looking for the frees positions (Character = " "), we write the positions in a  empty_space list
        empty_spaces = self.map.find_all_characters(" ")

        #  We add in the map the 3 random objects
        for item in self.items:
            position = choice(empty_spaces)# random position in the list empty_space
            item.set_position(position[0], position[1]) #We place object on the map
            self.map.write_character(item.character, item.x, item.y) # We put three objects in a  map


    def start(self):
        print(self.map)
        # End of game while position of character "m" different position of character "g"
        while (self.mcgyver.x_position, self.mcgyver.y_position) != (self.guard.x_position, self.guard.y_position):
            #  Window map
            print(self.map)
            self.map.write_character(" ", self.mcgyver.x_position, self.mcgyver.y_position)
            #x_position, y_position = self.mcgyver.x_position, self.mcgyver.y_position
            x_position, y_position = self.mcgyver.position()
            x_position_moving, y_position_moving = self.mcgyver.move()
            # Test to know, is it a good move?
            if self.map.retrieve_character(x_position_moving, y_position_moving) != "x":
                for item in self.items:
                    if self.map.retrieve_character(x_position_moving, y_position_moving) == item.character:
                        self.mcgyver.inventury.append(item.name)
                self.mcgyver.set_position(x_position_moving, y_position_moving)
                self.map.write_character("m", self.mcgyver.x_position, self.mcgyver.y_position)


            else:
                print(" No, You can't go here")
                self.mcgyver.set_position( x_position, y_position)
                self.map.write_character("m", self.mcgyver.x_position, self.mcgyver.y_position)

        # Condition to WIN or LOSE
        if len(self.mcgyver.inventury) == 3 :
            self.map.write_character("m", self.mcgyver.x_position, self.mcgyver.y_position)
            print(self.map)
            print("YOU ARE A WINNER---YOU ARE A WINNER---YOU ARE A WINNER---YOU ARE A WINNER---YOU ARE A WINNER---")
        else:
            print("Sorry but you haven't the three object: YOU LOSE---YOU LOSE---YOU LOSE---YOU LOSE---YOU LOSE---")
            print("It fail ", int(3 -len(self.mcgyver.inventury)), " objet(s)")
