# -*- coding: utf-8 -*-

import sys
from functions import demande

if __name__ == "__main__":
    to_check = sys.argv[1]
    if not to_check:
        print "Usage: python check.py FILEXPORTEDFROMDRAKON"
        sys.exit(1)
    print "Trying to import", to_check
    the_module = __import__(to_check)
    functions_to_check = []
    for fname in dir(the_module):
        f = getattr(the_module, fname)
        if callable(f) and f.__module__ == the_module.__name__:
            functions_to_check.append(f)

    for f in functions_to_check:
        if hasattr(the_module, 'SCENARIOS'):
            for i, scenario in enumerate(the_module.SCENARIOS):
                print "##################"
                print "Scenario", i
                D = demande()
                D.loadScenario(scenario)
                print D.resultats
                print D.prescription
                the_module.valeur = D._valeur
                the_module.repasser = D._repasser_tests
                the_module.declencher_tests = D._declencher_tests
                the_module.valider_resultat = D._valider_resultat
                print "------------------"
                f(D)
                print "------------------"
                print D.resultats
                print D.prescription
                print "##################"
        else:
            D = demande()
            the_module.valeur = D._valeur
            the_module.repasser = D._repasser_tests
            the_module.declencher_tests = D._declencher_tests
            the_module.valider_resultat = D._valider_resultat
            f(D)
            print D.resultats
            print D.prescription

