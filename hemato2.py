from functions import *
import hemato

def regleBis1(demande):
    hemato.valeur = demande._valeur
    hemato.repasser = demande._repasser_tests
    hemato.declencher_tests = demande._declencher_tests
    hemato.valider_resultat = demande._valider_resultat
    hemato.regle1(demande)

if __name__ == "__main__":
    D = demande()
    regleBis1(D)
