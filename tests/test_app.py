from app import *


def test_bonjour_1_prenom():
    assert bonjour_1_prenom("Bob") == "Hello, Bob"
    assert bonjour_1_prenom("bob") == "Hello, Bob"
    assert bonjour_1_prenom("stan") == "Hello, Stan"
    assert bonjour_1_prenom("mike") == "Hello, Mike"


def test_gestion_chaine_de_caractere_null():
    assert gestion_chaine_de_caractere_null(" ") == "Hello, my friend"
    assert gestion_chaine_de_caractere_null("Bob") == "Hello, Bob"
    assert gestion_chaine_de_caractere_null("    ") == "Hello, my friend"


def test_gestion_des_cris():
    assert gestion_des_cris("JERRY") == "HELLO, JERRY"
    assert gestion_des_cris("jerry") == "Hello, Jerry"
    assert gestion_des_cris(" ") == "Hello, my friend"


def test_gestion_plusieurs_noms():
    assert gestion_plusieurs_noms("Amy,Bob") == "Hello, Amy, Bob"
    assert gestion_plusieurs_noms("Amy,Bob,Mike") == "Hello, Amy, Bob, Mike"


def test_gestion_des_cris_plusieurs_noms():
    assert gestion_des_cris_plusieurs_noms("Amy, BOB, Mike") == "Hello, Amy, Mike. AND HELLO, BOB !"
    assert gestion_des_cris_plusieurs_noms("Amy,BOB,Mike") == "Hello, Amy, Mike. AND HELLO, BOB !"


def test_gestion_liste_avec_et():
    assert gestion_liste_avec_et("Bob, Amy, Jerry") == "Hello, Bob, Amy and Jerry"
    assert gestion_liste_avec_et("Bob,Amy,Jerry") == "Hello, Bob, Amy and Jerry"
    assert gestion_liste_avec_et("Bob, Amy") == "Hello, Bob and Amy"



def test_gestion_virgules_dans_noms():
    assert gestion_virgules_dans_noms("Bob, \"Amy, Jerry\"") ==  "Hello, Bob and Amy, Jerry"
    assert gestion_virgules_dans_noms("\"Amy, Jerry\"") == "Hello, Amy, Jerry"
    assert gestion_virgules_dans_noms("Bob, \"Amy, Jerry\", Mike, \"Stan, Pierre\"") == "Hello, Bob, Amy, Jerry, Mike, and Stan, Pierre"
