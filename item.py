"""
Create a class Item to def the object (item)
"""
class Item:
    def __init__(self, character, name, x, y):
        self.character =  character
        self.name = name
        self.x = x
        self.y = y

    def set_position(self, x, y): #attribut de position
        self.x = x
        self.y = y
