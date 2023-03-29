# On importe pygame
import pygame

# On importe le Player depuis player.py
from player import Player



# Classe qui représente le jeu
class Game:

    def __init__(self):
        self.player = Player()
        self.pressed = {
        }