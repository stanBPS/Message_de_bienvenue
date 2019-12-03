
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