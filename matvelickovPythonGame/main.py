# On importe pygame
import pygame

# On importe le Game depuis le game.py
from game import Game

pygame.init()



# Configuration du titre et de la taille de la fenêtre de jeu
pygame.display.set_caption("MVKC | Mon premier jeu")
screen = pygame.display.set_mode((1080,720))

# Importation de l'arrière plan
background = pygame.image.load('assets/bg.jpg')

# Chargement du jeu
game = Game()

running = True

# Boucle while qui s'exécute tant que la condition est vraie
while running:

    # Appliquer l'arrière plan du jeu
    screen.blit(background, (0,-200))

    # Appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # Récuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # Appliquer l'ensemble des images du groupe de projectiles
    game.player.all_projectiles.draw(screen)

    # Vérifier si le joueur souhaite aller à droite ou à gauche
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # Mise à jour de l'écran
    pygame.display.flip()

    # Si le joueur ferme la fenêtre
    for event in pygame.event.get():

        # Si l'evenement = fermeture de fenêtre alors on ferme
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Détecter si un joueur appuie une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # Détecter si la touche ESPACE est pressée
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False