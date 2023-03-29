# On importe pygame
import pygame

# Classe qui va gérer le projectile du joueur
class Projectile(pygame.sprite.Sprite):

    # Définir le constructeur de la classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80

    def move(self):
        self.rect.x += self.velocity

        # Condition si le projectile n'est plus présent sur l'écran
        if self.rect.x > 1080:
            # Supprimer le projectile (en dehors de l'écran)
            self.player.all_projectiles.remove(self)


