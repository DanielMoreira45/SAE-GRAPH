#%%
import time
import json
#import matplotlib.pyplot as plt


# dico[titre] = cast
# ou
# {titre: {cast : le cast, directors : le directeur, producers : producteurs, companies : les companies}}
import networkx as nx

def convert_txt_to_dict(nom_fichier):
    """charge un fichier de résultats au DNB donné au format CSV en une liste de résultats

    Args:
        nom_fichier (str): nom du fichier CSV contenant les résultats au DNB

    Returns:
        list: la liste des résultats contenus dans le fichier
    """

    with open(nom_fichier, encoding='utf-8') as fichier_open:
        lignes = fichier_open.readlines()
        dico = dict()
        for json_data in lignes:
            Data = json.loads(json_data)
            titre = Data["title"]
            cast = Data["cast"]
            try:
                directeur = Data["directors"]
            except:
                directeur = list()
            try:
                producteur = Data["producers"]
            except:
                producteur = list()
            try:
                companies = Data["companies"]
            except:
                companies = list()
            try:
                annee_sorti = Data["year"]
            except:
                annee_sorti = list()
            Vtitre = titre.replace("[[", "").replace("]]", "")
            Vcast = list()
            if len(cast) > 0:
                for personne in cast:
                    Vcast.append(personne.replace("[[", "").replace("]]", ""))

            Vdirecteur = list()
            if len(directeur) > 0:
                for director in directeur:
                    Vdirecteur.append(director.replace(
                        "[[", "").replace("]]", ""))
            Vproducteur = list()
            if len(producteur) > 0:
                for prod in producteur:
                    Vproducteur.append(prod.replace(
                        "[[", "").replace("]]", ""))

            Vcompanies = list()
            if len(companies) > 0:
                for comp in companies:
                    Vcompanies.append(comp.replace("[[", "").replace("]]", ""))
            dico[Vtitre] = dict()
            dico[Vtitre]["cast"] = Vcast
            dico[Vtitre]["director"] = Vdirecteur
            dico[Vtitre]["producers"] = Vproducteur
            dico[Vtitre]["companies"] = Vcompanies
            dico[Vtitre]["year"] = annee_sorti
    return dico

#print(convert_txt_to_dict("./little_data.txt"))
# convert_txt_to_dict("./data.txt")



# bool acteur 2
# ajout d'un acteur suspect si un bool lui est ajoutée (bool acteur 1 =acteur 1)

# Cette requête consiste à renvoyer, pour deux acteurs/actrices donné.e.s,
# lʼensemble des acteurs/actrices qui ont collaboré avec ces deux personnes.
def colab_en_commun(dico, acteur1, acteur2):
    res = set()
    dico_verif_ancien_result = dict()
    for valeurs in dico.values():
        for cast_actor in valeurs["cast"]:
            if cast_actor != acteur1 and cast_actor != acteur2 not in dico_verif_ancien_result:
                dico_verif_ancien_result[cast_actor] = []
            if acteur1 in valeurs["cast"] and cast_actor != acteur1 and cast_actor != acteur2:
                dico_verif_ancien_result[cast_actor].append(acteur1) 
            if acteur2 in valeurs["cast"] and cast_actor != acteur2 and cast_actor != acteur1:
                dico_verif_ancien_result[cast_actor].append(acteur2)
    for actor_sus in dico_verif_ancien_result:
         if len(dico_verif_ancien_result[actor_sus]) == 2:
            res.add(actor_sus)
    print(res)
    return res


dico_little_data = convert_txt_to_dict("./little_data.txt")
# dico_medium_data = convert_txt_to_dict("./medium_data.txt")
dico_medium_plus_data = convert_txt_to_dict("./medium_plus_data.txt")

def creation_graphe(dico): # complexité quadratique (à améliorer si possible)
    g = nx.DiGraph()
    acteurs_vue = set()
    for film in dico.values():
        for i in range(len(film["cast"])):
            acteur1 = film["cast"][i]
            if acteur1 not in acteurs_vue: 
                g.add_node(acteur1)
                acteurs_vue.add(acteur1)
            for b in range(i+1, len(film["cast"])):
                acteur2 = film["cast"][b]
                if acteur2 not in acteurs_vue:
                    g.add_node(acteur2)
                    acteurs_vue.add(acteur2)
                g.add_edge(acteur1, acteur2, length=10)
    nx.draw(g, with_labels=True)
    return g


#temps d'exec
debut = time.time()  # tps debut
graphe = creation_graphe(dico_little_data)
fin = time.time()  # tps fin
# debut exec
print(fin - debut)




# %%
