""" 
Module contenant une fonction qui teste si le nombre passé en paramètre est premier.
"""

from math import sqrt

#### Fonction secondaire

def isprime(p):
    """
    Retourne la vérité de la proposition : "p est premier".

    Args:
        p: le nombre à tester pour savoir s'il est premier.
    
    Returns:
        True: si p est premier.
        False: si p n'est pas premier.
    """
    premier = True
    if p in (0,1):
        premier = False
        return premier
    racine = int(sqrt(p))
    for d in range(2,racine + 1):
        if p % d == 0:
            premier = False
    return premier

#### Fonction principale

def main():
    """ appel de la fonction isprime(p) sur l'intervalle [0,99] """
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
