
def bonjour_1_prenom(nom):
    return("Hello, "+nom.capitalize())

def gestion_chaine_de_caractere_null(nom):
    if len(nom.strip()) == 0:
        return "Hello, my friend"
    else:
        return bonjour_1_prenom(nom)

def gestion_des_cris(nom):
    if len(nom.strip()) == 0:
        return gestion_chaine_de_caractere_null(nom)
    elif nom.isupper():
        return ("HELLO, "+nom)
    else:
        return bonjour_1_prenom(nom)

def gestion_plusieurs_noms(chaineNom):
    nomTab = chaineNom.split(',')
    chaine = "Hello"
    separator = ", "
    for nom in nomTab:
        chaine = chaine+separator+nom
    return chaine

def gestion_des_cris_plusieurs_noms(chaineNom):
    nomTab = chaineNom.split(',')
    separator = ", "
    chaine_maj=""
    chaine_minus=""
    for nom in nomTab:
        if nom.isupper():
            chaine_maj=chaine_maj+separator+nom.strip()
        else:
            chaine_minus=chaine_minus+separator+nom.strip()
    chaine= "Hello"+chaine_minus +". AND HELLO" +chaine_maj+" !"
    return (chaine)


def gestion_liste_avec_et(chaineNom):
    nomTab = chaineNom.split(',')
    chaine="Hello"
    separator1 = ", "
    separator2 = " and "
    for nom in nomTab:
        if nomTab.index(nom) == len(nomTab)-1:
            chaine = chaine+separator2+nom.strip()
        else:
            chaine = chaine+separator1+nom.strip()
    return chaine

