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

    with open(nom_fichier) as fichier_open:
        lignes = fichier_open.readlines()
        dico = dict()
        for json_data in lignes:
            Data =json.loads(json_data)
            titre = Data["title"]
            cast = Data["cast"]
            try :
                directeur = Data["directors"]
            except:
                directeur = list()
            try :
                producteur = Data["producers"]
            except:
                producteur = list()
            try :
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
                    Vdirecteur.append(director.replace("[[", "").replace("]]", ""))
            Vproducteur = list()
            if len(producteur) > 0:
                for prod in producteur:
                    Vproducteur.append(prod.replace("[[", "").replace("]]", ""))

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
            
# convert_txt_to_dict("./little_data.txt")
convert_txt_to_dict("./data.txt")