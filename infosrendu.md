
a. en terme de théorie des graphes, il s'agit ici d'une modélisation de relations (G, V) ou l'ensemble des collaborateurs en communs de deux acteurs signifie qu'il existe un acteur/noeud dont le degré est de 1 pour les 2 acteurs passé en argument, autrement dit il s'agit d'un noeud relié par des arêtes à la fois au noeud de l'acteur 1 et au noeud de l'acteur 2.

b. Analyse du temps d'execution de la fonction colab_en_commun

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



## problème rencontrees
- gérer les irrégularités dans le fichier de données brut ( 2 crochets parfois 1 etc)
- problème encodage utf 8