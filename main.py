import pygame
import random

# Initialisation de Pygame
pygame.init()

# Constantes
LARGEUR = 800
HAUTEUR = 600
TAILLE_CASE = 20
VITESSE = 10

# Couleurs
NOIR = (0, 0, 0)
VERT = (0, 255, 0)
ROUGE = (255, 0, 0)
ORANGE = (255, 165, 0)
BLANC = (255, 255, 255)

# Création de la fenêtre
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Snake")

# Polices
police_score = pygame.font.SysFont(None, 35)
police_message = pygame.font.SysFont(None, 50)

# Fonction pour dessiner le serpent
def dessiner_serpent(serpent):
    for segment in serpent:
        pygame.draw.rect(ecran, VERT, [segment[0], segment[1], TAILLE_CASE, TAILLE_CASE])

# Fonction pour dessiner le fruit
def dessiner_fruit(fruit):
    pygame.draw.rect(ecran, fruit[2], [fruit[0], fruit[1], TAILLE_CASE, TAILLE_CASE])

# Fonction pour afficher le score
def afficher_score(score):
    texte_score = police_score.render(f"Score: {score}", True, BLANC)
    ecran.blit(texte_score, [LARGEUR - 150, 10])

# Fonction pour afficher un message
def afficher_message(msg, couleur):
    texte_message = police_message.render(msg, True, couleur)
    texte_rect = texte_message.get_rect(center=(LARGEUR // 2, HAUTEUR // 2))
    ecran.blit(texte_message, texte_rect)

# Fonction pour l'écran de démarrage
def ecran_demarrage():
    ecran.fill(NOIR)
    afficher_message("Appuyez sur ESPACE pour commencer", BLANC)
    pygame.display.update()
    
    attente = True
    while attente:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                attente = False
    return True

# Fonction pour l'écran de fin
def ecran_fin(score):
    ecran.fill(NOIR)
    
    # Affichage du score
    texte_score = police_message.render(f"Game Over! Score final: {score}", True, BLANC)
    texte_score_rect = texte_score.get_rect(center=(LARGEUR // 2, HAUTEUR // 2 - 50))
    ecran.blit(texte_score, texte_score_rect)
    
    # Affichage du message pour rejouer
    texte_rejouer = police_message.render("Appuyez sur ESPACE pour rejouer", True, ORANGE)
    texte_rejouer_rect = texte_rejouer.get_rect(center=(LARGEUR // 2, HAUTEUR // 2 + 50))
    ecran.blit(texte_rejouer, texte_rejouer_rect)
    
    pygame.display.update()
    
    attente = True
    while attente:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                attente = False
    return True

# Fonction principale du jeu
def jeu_snake():
    # Position initiale du serpent
    x = LARGEUR // 2
    y = HAUTEUR // 2

    # Mouvement initial
    dx = TAILLE_CASE
    dy = 0

    # Liste pour stocker les segments du serpent
    serpent = [[x, y]]
    longueur_serpent = 1

    # Position initiale du fruit
    fruit = generer_fruit(serpent)

    clock = pygame.time.Clock()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -TAILLE_CASE
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = TAILLE_CASE
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -TAILLE_CASE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = TAILLE_CASE

        # Mise à jour de la position du serpent
        x += dx
        y += dy

        # Vérification des collisions avec les bords
        if x >= LARGEUR or x < 0 or y >= HAUTEUR or y < 0:
            return longueur_serpent

        ecran.fill(NOIR)

        # Ajout du nouveau segment à la tête du serpent
        tete_serpent = [x, y]
        serpent.append(tete_serpent)

        # Suppression des segments en trop
        if len(serpent) > longueur_serpent:
            del serpent[0]

        # Vérification des collisions avec le corps du serpent
        for segment in serpent[:-1]:
            if segment == tete_serpent:
                return longueur_serpent

        dessiner_serpent(serpent)
        dessiner_fruit(fruit)
        afficher_score(longueur_serpent)

        pygame.display.update()

        # Vérification de la collision avec le fruit
        if x == fruit[0] and y == fruit[1]:
            fruit = generer_fruit(serpent)
            if fruit[2] == ROUGE:
                longueur_serpent += 2
            else:
                longueur_serpent += 1

        clock.tick(VITESSE)

    return longueur_serpent

# Fonction pour générer un nouveau fruit
def generer_fruit(serpent):
    while True:
        fruit_x = round(random.randrange(0, LARGEUR - TAILLE_CASE) / TAILLE_CASE) * TAILLE_CASE
        fruit_y = round(random.randrange(0, HAUTEUR - TAILLE_CASE) / TAILLE_CASE) * TAILLE_CASE
        
        # Vérifier si le fruit n'est pas sur le corps du serpent
        if [fruit_x, fruit_y] not in serpent:
            fruit_color = ROUGE if random.random() < 0.1 else ORANGE  # 10% de chance d'être rouge
            return [fruit_x, fruit_y, fruit_color]

# Boucle principale du programme
def main():
    while True:
        if not ecran_demarrage():
            break
        score = jeu_snake()
        if not ecran_fin(score):
            break
    
    pygame.quit()

# Lancement du jeu
if __name__ == "__main__":
    main()
