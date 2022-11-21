###IMPORTATION DES LIBRAIRIES, ET DE CERTAINES DE LEURS FONCTIONS NON INTEGREES (FONT)###

import pygame 
import os
pygame.font.init()
pygame.init()

###DEFINITION DE LA FENETRE DE JEU, DE SES DIMENSIONS ET DE SON ECRITAU
LONGUEUR = 600
LONGUEUR2 = LONGUEUR // 3 + 9
LONGUEUR3 = 2 * LONGUEUR // 3 + 13
LONGUEUR4 = LONGUEUR // 3 + 14
WINDOW = pygame.display.set_mode((LONGUEUR, LONGUEUR))
pygame.display.set_caption("Jeu de morpion")

###DEFINITION DES FPS ET DU SYSTEME DE TOUR###

FPS = 30
TOUR = [0]

###DEFINITION DE LA VARIABLE DE COULEUR
PURPLE = (128, 0, 128)

###DEFINITION DE L'APPARENCE DE LA POLICE D'ECRITURE DU GAGNANT ET DE LA TAILLE DE POLICE
WINNER_FONT = pygame.font.SysFont('comicsansms', 45)

###IMPORTATION DES IMAGES DE LA GRILLE ET DE L ECRAN DE FIN###

END_SCREEN = pygame.image.load(
    os.path.join('end_screen.png')
)
###IMPORATION DE LA GRILLE + REDIMENSSION DE CELLE-CI AUX DIMENSIONS DE LA FENETRE
GRID = pygame.transform.scale(
    pygame.image.load(
        os.path.join('grid.png')), (LONGUEUR, LONGUEUR))

###DEFINITION DE LA CLASSE POUR LES CERCLES ET LES CROIX

class Xo():
    ###ME PERMET DE REDIMENSIONNER LES IMAGES DES CERCLES ET CROIX POUR QU'ELLES RENTRENT DANS LES CASES
    def __init__(self, file, width, height):
        self.image = pygame.transform.scale(pygame.image.load(file), (width, height))
    ###PERMET D'AFFICHER LES CELRCLES ET CROIX EN COORDONNEES x, y
    def draw(self, x, y):
        WINDOW.blit(self.image, (x, y))

###IMPORTATION DES IMAGES DES CERCLES ET CROIX + DECLARATION DE LEUR APPARTENANCE A LA CLASSE Xo + REDIMENSSION DE CHACUN AUX DIMENSIONS DES CASES
CIRCLE1 = Xo('circle.png', 189, 189)
CIRCLE2 = Xo('circle.png', 181, 189)
CIRCLE3 = Xo('circle.png', 189, 175)
CIRCLE4 = Xo('circle.png', 175, 175)

CROSS1 = Xo('cross.png', 189, 189)
CROSS2 = Xo('cross.png', 181, 189)
CROSS3 = Xo('cross.png', 189, 175)
CROSS4 = Xo('cross.png', 175, 175)

###IMPORTATION DES 9 CARRES POUR LA GRILLE + CONVERSION DES IMAGES POUR QUE LEUR AFFICHAGE SOIT PLUS OPTIMISE###
UP_LEFT = pygame.image.load('pixil-frame-1.png').convert_alpha()
UP_MIDDLE = pygame.image.load('pixil-frame-2.png').convert_alpha()
UP_RIGHT = pygame.image.load('pixil-frame-3.png').convert_alpha()
MIDDLE_LEFT = pygame.image.load('pixil-frame-4.png').convert_alpha()
MIDDLE_MIDDLE = pygame.image.load('pixil-frame-5.png').convert_alpha()
MIDDLE_RIGHT = pygame.image.load('pixil-frame-6.png').convert_alpha()
DOWN_LEFT = pygame.image.load('pixil-frame-7.png').convert_alpha()
DOWN_MIDDLE = pygame.image.load('pixil-frame-8.png').convert_alpha()
DOWN_RIGHT = pygame.image.load('pixil-frame-9.png').convert_alpha()

###DEFINITION DE LA CLASSE POUR LES HITBOXS DES CASES DE LA GRILLE
class Hitbox():
    
    def __init__(self, x, y, image):
        ###FAIT EN SORTE QUE CHAQUE HITBOX CORRESPONDE A SON IMAGE RESPECTIVE  
        self.image = image
        ###OBTIENT LE RECTANGLE CORRESPONDANT A L'IMAGE
        self.rect = self.image.get_rect()
        ### ASSOCIE LES COORDONEES 0, 0 DU RECTANGLE AUX COORDONEES VOULUES 
        self.rect.topleft = (x, y)
        ### DEFINIT SI LE BOUTON EST CLIQUE
        self.clicked = False
    ###FONCTION QUI PERMET DE DESSINER LES CARRES SUR LA GRILLE + VERIFIE S'ILS SONT CLIQUES
    def draw(self):
        ###DECLARATION DES VARIABLES POUR DIRE SI UNE ACTION EST NECESSAIRE + POUR OBTENIR LA POSITION DE LA SOURIS
        action = False
        pos = pygame.mouse.get_pos()
        ###SI LE CARRE ET LA SOURIS SONT EN COLLISIION ET QUE LA SOURIS ET CLIQUEE, LA FONCTION DEVIENT TRUE
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        
        
        
        WINDOW.blit(self.image, (self.rect.x, self.rect.y))
        return action

###DECLARATION DE L'APPARTENANCE DES HITBOX A LA CLASSE Hitbox
UL_hitbox = Hitbox(0, 0, UP_LEFT)
UM_hitbox = Hitbox(LONGUEUR2, 0, UP_MIDDLE)
UR_hitbox = Hitbox(LONGUEUR3, 0, UP_RIGHT)
ML_hitbox = Hitbox(0, LONGUEUR4, MIDDLE_LEFT)
MM_hitbox = Hitbox(LONGUEUR4, LONGUEUR4, MIDDLE_MIDDLE)
MR_hitbox = Hitbox(LONGUEUR3, LONGUEUR4, MIDDLE_RIGHT)
DL_hitbox = Hitbox(0, LONGUEUR3, DOWN_LEFT) 
DM_hitbox = Hitbox(LONGUEUR2, LONGUEUR3, DOWN_MIDDLE)
DR_hitbox = Hitbox(LONGUEUR3, LONGUEUR3, DOWN_RIGHT)

###DECLARATION DE LA FONCTION QUI AFFICHE LE TEXTE EN CAS DE VICTOIRE###
def draw_winner(text):
    ###DETERMINE CE QUE LE PROGRAMME DOIT AFFICHER, DANS QUELLE POLICE ET COULEUR IL DOIT L'AFFICHER
    winner_text = WINNER_FONT.render(text, 1, PURPLE)
    ###ECRAN BLANC POUR QUE LE TEXTE SOIT PLUS FACILE A LIRE
    WINDOW.blit(END_SCREEN, (0, 0))
    ###AFFICHAGE DU TEXTE A L'ECRAN
    WINDOW.blit(winner_text, (LONGUEUR // 2 - winner_text.get_width() // 2, LONGUEUR // 2 - winner_text.get_height() // 2))
    pygame.display.update()
    ###LAISSE UN DELAI POUR QU'ON AI LE TEMPS DE LIRE CE QUI EST AFFICHE
    pygame.time.delay(5000)
    

###FONCTION PRINCIPALE
def main():
    ###DEFINITION DE CE QUI PERMET DE SAVOIR SI LE PROGRAMME DOIT TOURNER ET A QUELLE FRAMERATE IL DOIT LE FAIRE
    run = True
    clock = pygame.time.Clock()
    
    ###VARIABLES QUI ME PERMETTENT DE SAVOIR SI LES QUELQUE CHOSE SE TROUVE SUR LES CASE DE LA GRILLE
    UL = 0
    UM = 0
    UR = 0
    ML = 0
    MM = 0
    MR = 0
    DL = 0
    DM = 0
    DR = 0
    
    ###BOUCLE PRINCIPALE
    while run:
        ###FRAMERATE
        clock.tick(FPS)
        ###CE QUI EST AFFICHE A L'ECRAN (FOND BLANC + GRILLE)
        WINDOW.fill((255, 255, 255))
        WINDOW.blit(GRID, (0, 0))
        ###VARIALE QUI PERMET DE DETERMINER LE TOUR
        tour = len(TOUR)
        ###CONDITIONS DE VICTOIRE
        winner_text = ""
        if UL + UM + UR == 30 or ML + MM + MR == 30 or DL + DM + DR == 30 or UL + ML + DL == 30 or UM + MM + DM == 30 or UR + MR + DR == 30 or UL + MM + DR == 30 or UR + MM + DL == 30:
            winner_text = "LES CROIX ONT GAGNÉ"
        
        if UL + UM + UR == 3 or ML + MM + MR == 3 or DL + DM + DR == 3 or UL + ML + DL == 3 or UM + MM + DM == 3 or UR + MR + DR == 3 or UL + MM + DR == 3 or UR + MM + DL == 3:
            winner_text = "LES CERCLES ONT GAGNÉ"
        
        if tour == 10:
            winner_text = "EGALITE"
        
        ###APPELLE LA FONCTION QUI AFFICHE LE TEXTE EN CAS DE VICTOIRE
        if winner_text != "":
            draw_winner(winner_text)
            break
        ###VERIFICATION DE SI LES CASES SONT CLIQUEES A L'AIDE DE LA METHODE PRESENTE DANS LA CLASSE HITBOX; VARIABLE DIFFERENTE EN FONCTION DU TOUR + AUGMENTATION DE LA VALEUR DE TOUR
        ###HAUT GAUCHE
        if UL_hitbox.draw():
            if tour % 2 == 0:
                UL += 10    
            else:
                UL += 1
            TOUR.append(0)
        ###HAUT MILIEU
        if UM_hitbox.draw():
            if tour % 2 == 0:
                UM += 10
            else:
                UM += 1
            TOUR.append(0)
        ###HAUT DROITE
        if UR_hitbox.draw():
            if tour % 2 == 0:
                UR += 10
            else:
                UR += 1
            TOUR.append(0)
        ###MILIEU GAUCHE
        if ML_hitbox.draw():
            if tour % 2 == 0:
                ML += 10
            else:
                ML += 1
            TOUR.append(0)
        ###MILIEU MILIEU
        if MM_hitbox.draw():
            if tour % 2 == 0:
                MM += 10
            else:
                MM += 1
            TOUR.append(0)
        ###MILIEU DROITE
        if MR_hitbox.draw():
            if tour % 2 == 0:
                MR += 10
            else:
                MR += 1
            TOUR.append(0)
        ###BAS GAUCHE
        if DL_hitbox.draw():
            if tour % 2 == 0:
                DL += 10
            else:
                DL += 1
            TOUR.append(0)
        ###BAS MILIEU
        if DM_hitbox.draw():
            if tour % 2 == 0:
                DM += 10
            else:
                DM += 1
            TOUR.append(0)
        ###BAS DROITE
        if DR_hitbox.draw():
            if tour % 2 == 0:
                DR += 10
            else:
                DR += 1
            TOUR.append(0)
        
        ###PERMET DE SAVOIR SI LES VALEURS ASSOCIEES AU HITBOX SONT DIFFERENTES DE 0, AFFICHE UNE CROIX OU UN CERCLE EN FONCTION DU TOUR
        ###HAUT GAUCHE
        if UL == 10:
            CROSS1.draw(0, 0)
        if UL == 1:
            CIRCLE1.draw(0, 0)
        #HAUT MILIEU
        if UM == 10:
            CROSS2.draw(LONGUEUR2, 0)
        if UM == 1:
            CIRCLE2.draw(LONGUEUR2, 0)        
        #HAUT DROITE
        if UR == 10:
            CROSS1.draw(LONGUEUR3, 0)
        if UR == 1:
            CIRCLE1.draw(LONGUEUR3, 0)
        #MILIEU GAUCHE
        if ML == 10:
            CROSS3.draw(0, LONGUEUR4)
        if ML == 1:
            CIRCLE3.draw(0, LONGUEUR4)
        #MILIEU MILIEU
        if MM == 10:
            CROSS4.draw(LONGUEUR4, LONGUEUR4)
        if MM == 1:
            CIRCLE4.draw(LONGUEUR4, LONGUEUR4) 
        #MILIEU DROITE
        if MR == 10:
            CROSS3.draw(LONGUEUR3, LONGUEUR4)
        if MR == 1:
            CIRCLE3.draw(LONGUEUR3, LONGUEUR4)
        #BAS GAUCHE
        if DL == 10:
            CROSS1.draw(0, LONGUEUR3)
        if DL == 1:
            CIRCLE1.draw(0, LONGUEUR3)
        #BAS MILIEU
        if DM == 10:
            CROSS2.draw(LONGUEUR2, LONGUEUR3)
        if DM == 1:
            CIRCLE2.draw(LONGUEUR2, LONGUEUR3)
        #BAS DROITE
        if DR == 10:
            CROSS1.draw(LONGUEUR3, LONGUEUR3)
        if DR == 1:
            CIRCLE1.draw(LONGUEUR3, LONGUEUR3)
        ###SI LA CROIX EST CLIQUEE, LE PROGRAMME SE FERME
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        pygame.display.update()



#FAIT EN SORTE QUE LA FONCTION MAIN TOURNE BIEN SI IMPORTE DANS UN AUTRE PROGRAMME
if __name__ == "__main__":
    main()