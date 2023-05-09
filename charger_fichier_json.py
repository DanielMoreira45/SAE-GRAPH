import json


# dico[titre] = cast
# ou 
# {titre: {cast : le cast, directors : le directeur, producers : producteurs, companies : les companies}}


def convert_txt_to_dict(nom_fichier):
    """charge un fichier de résultats au DNB donné au format CSV en une liste de résultats

    Args:
        nom_fichier (str): nom du fichier CSV contenant les résultats au DNB

    Returns:
        list: la liste des résultats contenus dans le fichier
    """
    data = dict()
    try:
        liste_resultat = []
        fic = open(nom_fichier, "r", encoding="utf8")
        titre = ""
        for ligne in fic:
            liste_petit_champs = []
            champs = ligne.split(":")
            for liste in champs:
                petit_champs = liste.split(",")
                print(petit_champs)
                liste_petit_champs.append(petit_champs)
            print(liste_petit_champs)
            #dict[].append((int(champs[0]), champs[1], int(champs[2]), int(champs[3]), int(champs[4])))
        return liste_resultat
    except IOError:
        print("Le nom/chemin du fichier indiqué n'existe pas !")
    pass

convert_txt_to_dict("little_data.txt")