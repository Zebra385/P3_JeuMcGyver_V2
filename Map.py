# coding: utf-8  # encodage in French

"""
Create a class Map to play , the map is a file text that transform in a
array[line, column], name map_structure
"""


class Map:
    def __init__(self, file):
        self.file = file
        self.map_structure = []  # My array to map
        # Method open can read the text in the file
        with open(self.file) as f:
            lines = f.readlines()
            # Method readlines to seperate ligne of the text
            for line in lines:
                line = line.strip()
                self.map_structure.append(list(line))
                #  Add list line in list  map_structure

    # We change the "print", to can write the map like a array
    def __str__(self):
        map_str = ""  # def the array that we wanr to write
        for line in self.map_structure:
            map_str += "".join(line)  # We add a new line to the array
            map_str += "\n"  # return at the line
        return map_str

    # Def find_one_character to determinate the position of a character
    def find_one_character(self, character):
        x_character = int()
        y_character = int()
        for x, line in enumerate(self.map_structure):
            for y, c in enumerate(line):
                if character == c:
                    x_character = int(x)
                    y_character = int(y)
        return (x_character, y_character)
        # return the position of this character

    """
    Definition a method those find the position     to the same character and
    whose add in the list position
    """
    def find_all_characters(self, character):
        positions = []
        # enumerate return 2 variables the first "x"
        # is the index  and the second "line" is the value
        for x, line in enumerate(self.map_structure):
            for y, c in enumerate(line):
                if character == c:
                    positions.append((x, y))
        return positions

    """
    We def a attribut to write a character to the position line x and column y.
    """
    def write_character(self, character, x, y):
        self.map_structure[x][y] = character

    """
    We def an attribut whose return the
    character in  position line x and column y.
    """
    def retrieve_character(self, x, y):
        character = self.map_structure[x][y]
        return character
