# -*- coding: utf-8 -*-

class demande(object):

    def __init__(self):
        self.resultats = {
            'NFN': 10,
            }
        self.prescription = ['A','B','C']

    def loadScenario(self, scenario):
        self.resultats = scenario.get('resultats', {})
        self.prescription = scenario.get('prescription', [])

    def _valeur(demande, code_test):
        return demande.resultats.get(code_test, None)

    def _valider_resultat(demande, resultat):
        print "Valider", resultat, demande.resultats.get(resultat)
    _valider_resultat.description = u'Valider le résultat passé en paramètre'

    def _declencher_tests(demande, *liste_tests):
        print u"Déclencher", liste_tests
    _declencher_tests.description = u'Rajoute sur la demande tous les tests passés en paramètres'

    def _repasser_tests(demande, *liste_tests):
        print u"Repasser", liste_tests
    _repasser_tests.description = u'Repasser quoi'

