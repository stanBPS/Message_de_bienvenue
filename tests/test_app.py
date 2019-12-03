from app import *

def test_bonjour_1_prenom():
    assert bonjour_1_prenom("Bob") == "Hello, Bob"
    assert bonjour_1_prenom("bob") == "Hello, Bob"
    assert bonjour_1_prenom("stan") == "Hello, Stan"
    assert bonjour_1_prenom("mike") == "Hello, Mike"

