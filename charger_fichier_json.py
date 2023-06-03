#%%
import time
import json
import matplotlib.pyplot as plt


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
                    if ("|" in personne):
                        liste_noms_avec_paran = personne.split("|")
                        liste_noms_sans_paran = liste_noms_avec_paran[0].split("(")
                        personne = liste_noms_sans_paran[0]
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

# print(convert_txt_to_dict("./little_data.txt"))
# convert_txt_to_dict("./data.txt")

print(convert_txt_to_dict("./error.txt"))

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


<<<<<<< charger_fichier_json.py
# dico_little_data = convert_txt_to_dict("./little_data.txt")
dico_medium_data = convert_txt_to_dict("./medium_data.txt")
# dico_medium_plus_data = convert_txt_to_dict("./medium_plus_data.txt")
=======
# dico_little_data = convert_txt_to_dict("./little_data.txt")
dico_medium_data = convert_txt_to_dict("./medium_data.txt")
dico_medium_plus_data = convert_txt_to_dict("./medium_plus_data.txt")
>>>>>>> charger_fichier_json.py

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
<<<<<<< charger_fichier_json.py
    pos = nx.spring_layout(g, k=0.3)
    nx.draw(g, with_labels=True, font_size=2, pos=pos)
    plt.savefig("graph.svg", format="svg")
=======
    #nx.draw(g, with_labels=True)
>>>>>>> charger_fichier_json.py
    return g


#temps d'exec
debut = time.time()  # tps debut
<<<<<<< charger_fichier_json.py
graphe = creation_graphe(dico_medium_data)
fin = time.time()  # tps fin
# debut exec
print(fin - debut)



def collaborateurs_proches(G,u,k): # parcours en largeur
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    """
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    for i in range(k): # on explore les sucesseurs des successeurs et ainsi de suite à un degrès k maximum du noeud u 
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return collaborateurs


def distance_acteurs(G, u, v, k):
    collaborateurs = collaborateurs_proches(G, u, k)
    if u in G.nodes:
        if v in collaborateurs:
            return k
        else:
            k += 1
            for collaborateur in collaborateurs:
                collaborateurs = distance_acteurs(G, collaborateur, v, k)
            return k
    return k
























































































def eloignement_max(G):
    max = 0
    val = None
    for acteur1 in G.nodes:
        for acteur2 in G.nodes:
            if acteur1!= acteur2:
                distance = distance_acteurs(G, acteur1, acteur2,0)
                if val is None or distance > val:
                    max = distance
    return max
print(eloignement_max(graphe))

print(collaborateurs_proches(graphe, "Herbert Grönemeyer",1))
        
# print(len(collaborateurs_proches(graphe, "Burt Ward", 1)))
# print(len(collaborateurs_proches(graphe, "Burt Ward", 5)))


print(distance_acteurs(graphe,"Herbert Grönemeyer","Uwe Ochsenknecht", 0))
# noeud_proximite = nx.closeness_centrality(graphe)
# noeud_central = max(noeud_proximite, key=noeud_proximite.get) 
=======
#graphe = creation_graphe(dico_medium_data)
fin = time.time()  # tps fin
# debut exec
#print(fin - debut)


def calculer_centralite_acteur(Gc, acteur):
    centralite = nx.closeness_centrality(Gc, u=acteur)
    return centralite

# print(calculer_centralite_acteur(graphe,"Tommy Lee Jones" ))

def trouver_acteur_plus_central(G):
    noeud_proximite = nx.closeness_centrality(G)
    noeud_central = max(noeud_proximite, key=noeud_proximite.get)
    return noeud_central
# print(trouver_acteur_plus_central(graphe))

def distance_maximale_entre_acteurs(Gc):
    distances = []
    for acteur1 in Gc.nodes():
        for acteur2 in Gc.nodes():
            if acteur1 != acteur2:
                try:
                    distance = nx.shortest_path_length(Gc, acteur1, acteur2)
                    distances.append(distance)
                except nx.NetworkXNoPath:
                    # Si aucun chemin n'existe entre les acteurs, la distance est infinie
                    distances.append(0)  # Distance 0 pour représenter une distance infinie
    distance_max = max(distances)
    return distance_max
#print(distance_maximale_entre_acteurs(graphe))
>>>>>>> charger_fichier_json.py

# %%
