

a. en terme de théorie des graphes, il s'agit ici d'une modélisation de relations (G, V) ou l'ensemble des collaborateurs en communs de deux acteurs signifie qu'il existe un acteur/noeud dont le degré est de 1 pour les 2 acteurs passé en argument, autrement dit il s'agit d'un noeud relié par des arêtes à la fois au noeud de l'acteur 1 et au noeud de l'acteur 2.

b. Analyse du temps d'execution de la fonction colab_en_commun



2.
```python
def colab_en_commun(dico, acteur1, acteur2): 
  """
  Initialisation des variables, temps linéaire
  """
    res = set() 
    dico_verif_ancien_result = dict()
    """ 
    deux boucles imbriquées la première parcourant les films (clés) de taille N et la seconde parcourant pour chaque film le cast (valeur parcourue) de taille M
    cette partie du code est un algo quadratique dont la borne inférieur est équivalent à Ω(N*M).
    """
    for valeurs in dico.values():
        for cast_actor in valeurs["cast"]:
            if cast_actor != acteur1 and cast_actor != acteur2 not in dico_verif_ancien_result:
                dico_verif_ancien_result[cast_actor] = []
            if acteur1 in valeurs["cast"] and cast_actor != acteur1 and cast_actor != acteur2:
                dico_verif_ancien_result[cast_actor].append(acteur1) 
            if acteur2 in valeurs["cast"] and cast_actor != acteur2 and cast_actor != acteur1:
                dico_verif_ancien_result[cast_actor].append(acteur2)
    """ 
    cout dérisoire O(N) // suite à faire
    """   
    for actor_sus in dico_verif_ancien_result:
         if len(dico_verif_ancien_result[actor_sus]) == 2:
            res.add(actor_sus)
    print(res)
    return res
```
2. Pour déterminer si un acteur u se trouve à distance k d'un autre acteur, le parcours donnée par la fonction collaborateurs s'avère judicieux, en effet on va parcourir de collaborateur en collaborateur (distance i+1 de u jusqu'à i+1 = k le degré). La fonction sera appelée successivement avec un degré de recherche k+1 si le noeud v (acteur cherché) n'est pas présent à un degré k.

Pour analyser la complexité d'un tel algorithme. Analyso les performance de collaborateur proches.

```python
def collaborateurs_proches(G,u,k): # parcours en largeur
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    """
    if u not in G.nodes: # cout linéaire O(1) pour la vérification de l'existance d'un noeud dans un graphe et création des variables
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    print(collaborateurs)
    for i in range(k): # on explore les sucesseurs des successeurs et ainsi de suite à un degrès k maximum du noeud u 
        collaborateurs_directs = set() # cout quadratique, proportionelle au  produit du degré moyen des acteurs à la celui de la distance k soit  O(D*K) pour les 2 boucles
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs) # le cout de l'union est au plus proportionelle à la taille des ensemble unis qui est le cout des acteurs ajoutées une fois. 0(D*K)
    return collaborateurs
```
# on a donc O(D*K)+O(D*K) = 2(O(D*K)) (reste à démontrer si l'on à un nombre moyen de degré pour un noeud sinon résultat volatile)


## problème rencontrees
- gérer les irrégularités dans le fichier de données brut ( 2 crochets parfois 1 etc)
- problème encodage utf 8