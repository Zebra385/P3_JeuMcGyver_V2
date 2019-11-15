from random import randint, choice
from Map import Map
from Character import McGyver, Guard
from item import Item
import pygame
from pygame.locals import *

# Initialisation de la bibliothèque Pygame
pygame.init()
# Création de la fenêtre
fenetre = pygame.display.set_mode((600, 600))
list_image = ["venv/Images/Background.png", "venv/Images/Wall.png", "venv/Images/MacGyver.png",
              "venv/Images/Gardien.png", "venv/Images/potion.png", "venv/Images/baton.png", "venv/Images/pipe.png",
              "venv/Images/youwin.png", "venv/Images/youdied.png"]


def load_image(file_image):
    image_charge = pygame.image.load(file_image).convert()
    return image_charge




#dispo image dans fenetre
fond=load_image(list_image[0]).convert()
fenetre.blit(fond,(0, 0))
(x,y) = (40, 560)
mc_image = load_image(list_image[2]).convert_alpha()
fenetre.blit(mc_image ,(x,y))
pygame.display.flip()
#position_perso = mc_image.get_rect()
#print(position_perso)
#position_perso = position_perso.move(40,40)
#print(position_perso)
continuer = 1
while continuer:
    for event in pygame.event.get():  # Attente des événements
        if event.type == QUIT:
            continuer = 0
        if event.type == KEYDOWN:
            if event.key == K_UP:  # Si touche z
                y= y -40
                # Re-collage
    fenetre.blit(fond, (0, 0))
    fenetre.blit(mc_image, (x, y))
    # Rafraichissement
    pygame.display.flip()






