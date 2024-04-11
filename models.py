from random import *

class Joueur:
    nom = ' '
    manche_gagnee = ' '
    argent = 1220
    pokemons = ' '


    def __init__(self, nom, manche_gagnee, argent, pokemons):
        self.nom = nom
        self.manche_gagnee = manche_gagnee
        self.argent = argent
        self.pokemons = pokemons

    def choisir_pokemon(self):
        
        pokemons = []
        print(pokemons)
    
    def ajouter_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def choisir_attaque(self, pokemon_adverse):
        ##attaque_pokemon_engagé = 
        i = int(input("Quelle attaque voulez-vous utiliser ?"))
        return self.pokemons[1].Pokemon.attaques[i]
        
    def recuperer_pokemon(self, pokemon):
        return self.ajouter_pokemon()

    def afficher_pokemon(self):
        print(f"Nom: {self.pokemons.nom}, Prix: {self.pokemons.prix}, type: {self.pokemons.type}, PV: {self.pokemons.point_de_vie}, Niveau: {self.pokemons.niveau}, Attaque: {self.pokemons.attaque}, Attaque spéciale: {self.pokemons.Pokemon.attaque_speciale}, Défense: {self.pokemons.defense}, Défense spéciale: {self.pokemons.defense_speciale}, Vitesse: {self.pokemons.vitesse}")

    def afficher(self):
        print(f"Nom: {self.nom}, Manche gagnée: {self.manche_gagnee}, Argent: {self.argent}")


class Pokemon:
    nom = ' '
    prix = ' '
    type = ' '
    point_de_vie = 5000
    niveau = ' '
    attaque = ' '
    attaque_speciale = ' '
    defense = ' '
    defense_speciale = ' '
    vitesse = ' '
    attaques = []
    pokemon_combat = ' '

    def __init__(self, nom, prix, type, point_de_vie, niveau, attaque, attaque_speciale, defense, defense_speciale, vitesse, attaques):
        self.nom = nom
        self.prix = prix
        self.type = type
        self.point_de_vie = point_de_vie
        self.niveau = niveau
        self.attaque = attaque
        self.attaque_speciale = attaque_speciale
        self.defense = defense
        self.defense_speciale = defense_speciale
        self.vitesse = vitesse
        self.attaques = attaques

    def ajouter_attaque(self, Attaque):
        self.attaques.append(Attaque)

    def attaquer(self, pokemon_adverse, attaque_utilisee):
        return pokemon_adverse, attaque_utilisee

    def est_ko(self):
        if self.pokemons[1] < 0:
            return True
        else:
            return False
        
    def afficher_attaques(self):
        print(f"Nom: {self.pokemons[1].Attaque.nom}, type: {self.pokemons[1].Attaque.type},  Catégorie: {self.pokemons[1].Attaque.categorie_attaque}, Précision: {self.pokemons[1].Attaque.precision}, Puissance: {self.pokemons[1].Attaque.puissance}, PP: {self.pokemons[1].Attaque.pp}")

    def afficher(self):
         print(f"Nom: {self.nom}, Prix: {self.prix}, type: {self.type}, PV: {self.point_de_vie}, Niveau: {self.niveau}, Attaque: {self.attaque}, Attaque spéciale: {self.attaque_speciale}, Défense: {self.defense}, Défense spéciale: {self.defense_speciale}, Vitesse: {self.vitesse}")


class Attaque:
    nom = ' '
    type = ' '
    categorie_attaque = ' '
    precision = ' '
    puissance = ' '
    pp = ' '

    def __init__(self, nom, type, categorie_attaque, precision, puissance, pp):
        self.nom = "Draco-queue"
        self.type = "dragon"
        self.categorie_attaque = "physique"
        self.precision = 90
        self.puissance = 60
        self.pp = 10

    def calculer_degats(self, pokemon_attaquant, pokemon_attaquer):
        if type.attaque == pokemon_attaquant.type:
            stab = 1.5
        else:
            stab = 1
        pv_perdus = (((Pokemon.niveau*0.4 + 2)*Pokemon.attaque*self.puissance)/(Pokemon.defense*50)+2)*stab*(self.precision / 100)
        resultat = Pokemon.point_de_vie - pv_perdus
        print(resultat)


class Jeu:
    def __init__(self):
        self.joueurs = []

    def jouer(self):
        for i in range(2):
            nom = input(f"Nom du joueur {i+1}: ")
            argent = 1220 
            joueur = Joueur(nom, argent)
            joueur.choisir_pokemon(pokemons_disponibles)
            self.joueurs.append(joueur)

            #Boucke des manches
            for i in range(3):
                for joueur in self.joueurs:
                adversaire = self.joueurs[1] if joueur == self.joueurs[0] else self.joueurs[0]
                pokemon_joueur = joueur.recuperer_pokemon(1) # Pour simplifier, on prend toujours le premier pokemon
                pokemon_adversaire = adversaire.recuperer_pokemon(1)

                attaque_joueur = joueur.choisir_attaque(pokemon_joueur)
                attaque_adversaire = adversaire.choisir_attaque(pokemon_adversaire)

                if pokemon_joueur.vitesse > pokemon_adversaire.vitesse:
                    degats = attaque_joueur.calculer_degats(pokemon_joueur, pokemon_adversaire)
                    pokemon_adversaire.pv -= degats
                    print(f"{pokemon_joueur.nom} attaque avec {attaque_joueur.nom} et inflige {degats} dégâts à {pokemon_adversaire.nom}")

                    if pokemon_adversaire.est_ko():
                        print(f"{pokemon_adversaire.nom} est K.O.")
                        joueur.manche_gagnee += 1
                        break

                    degats = attaque_adversaire.calculer_degats(pokemon_adversaire, pokemon_joueur)
                    pokemon_joueur.pv -= degats
                    print(f"{pokemon_adversaire.nom} attaque avec {attaque_adversaire.nom} et inflige {degats} dégâts à {pokemon_joueur.nom}")

                    if pokemon_joueur.est_ko():
                        print(f"{pokemon_joueur.nom} est K.O.")
                        adversaire.manche_gagnee += 1
                        break

                else:
                    degats = attaque_adversaire.calculer_degats(pokemon_adversaire, pokemon_joueur)
                    pokemon_joueur.pv -= degats
                    print(f"{pokemon_adversaire.nom} attaque avec {attaque_adversaire.nom} et inflige {degats} dégâts à {pokemon_joueur.nom}")

                    if pokemon_joueur.est_ko():
                        print(f"{pokemon_joueur.nom} est K.O.")
                        adversaire.manche_gagnee += 1
                        break

                    degats = attaque_joueur.calculer_degats(pokemon_joueur, pokemon_adversaire)
                    pokemon_adversaire.pv -= degats
                    print(f"{pokemon_joueur.nom} attaque avec {attaque_joueur.nom} et inflige {degats} dégâts à {pokemon_adversaire.nom}")

                    if pokemon_adversaire.est_ko():
                        print(f"{pokemon_adversaire.nom} est K.O.")
                        joueur.manche_gagnee += 1
                        break

        # Détermination du vainqueur
        vainqueur = None
        for joueur in self.joueurs:
            if joueur.manche_gagnee >= 2:
                vainqueur = joueur
                break

        if vainqueur:
            print(f"{vainqueur.nom} a gagné la partie!")
        else:
            print("Match nul.")


#Tout les Pokemeon
type_feu = type("feu")
type_eau = type("Eau")
type_fée = type("Fée")
type_ténèbres = type("ténèbres")
type_Dragon = type("dragon")
type_Psy = type("Psy")
type_inconnu = type("Inconnu")

Attaque_feu = Attaque("Nitrocharge", type_feu, "Physique", 50, 100, 20)
Attaque_eau =Attaque("Sheauriken", type_eau, "Physique", 100, 15, 20)
Attaque_fée = Attaque("Eclair magique", type_fée, "Spécial", 80, 100, 10)
Attaque_Ténèbres = Attaque("Bombe puante", type_ténèbres, "Spécial", 100, 70, 8)
Attaque_Dragon = Attaque("Dragon céleste", type_Dragon, "Spécial", 100, 228422, 22842 )
Attaque_Psy = Attaque("Boutefeu", type_fée, "Spécial", 100, 120, 15)
Attaque_Inconnu = Attaque("Enfantin", type_inconnu, "Physique", 50, 6000, 2)

Pokemon_Goupelin = Pokemon("Goupelin", 75, [type_feu], 354, 46, 69, 72, 74, 100 , 104)
Pokemon_Amphinobi = Pokemon("Amphinobi", 80, [type_eau], 348, 50, 95, 67, 103, 71, 122)
Pokemon_Xernéas = Pokemon("Xernéas", 100, [type_fée], 456, 20, 131, 95, 131, 98, 99)
Pokemon_Tokodombi = Pokemon("Toko dombi", 10, [type_ténèbres], 1492, 105, 60, 60, 70, 95)
Pokemon_neduj = Pokemon("neduj", 1000, [type_Dragon], 374, 1, 73, 70, 73, 115 , 67)
Pokemon_Solgaléo = Pokemon("Solgaléo", 120, [type_Psy], 478, 15, 137, 107, 113, 89, 97)
Pokemon_Norman = Pokemon("Norman", 16, {type_inconnu}, 470, 36, 73, 115, 100, 144, 20)

Pokemon_Goupelin.ajouter_attaque(Attaque_feu)
Pokemon_Amphinobi.ajouter_attaque(Attaque_eau)
Pokemon_Xernéas.ajouter_attaque(Attaque_fée)
Pokemon_Tokodombi.ajouter_attaque(Attaque_Ténèbres)
Pokemon_neduj.ajouter_attaque(Attaque_Dragon)
Pokemon_Solgaléo.ajouter_attaque(Attaque_Psy)
Pokemon_Norman.ajouter_attaque(Attaque_Inconnu)

Pokemon_disponible = [Pokemon_Goupelin, Pokemon_Amphinobi, Pokemon_Xernéas, Pokemon_Tokodombi, Pokemon_neduj, Pokemon_Solgaléo, Pokemon_Norman]
