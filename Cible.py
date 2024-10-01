class Cible:
    """
    Classe qui représente les informations sur une forme cible (mot ou suite de mots) et ses probabilités de traduction
    """

    def __init__(self, forme):
        """
        Constructeur :
        - Mémorise la forme sous forme d'attribut
        - Initialise les 3 probabilités de traduction (prob_cs_anymalign,
        prob_cs_giza et prob_cs_phrasetable) à 0

        :param forme: forme cible sous forme de chaîne de caractères
        :param proba_cs_anymalign: probabilité de traduction de la forme cible avec Anymalign
        :param proba_cs_giza: probabilité de traduction de la forme cible avec Giza++
        :param proba_cs_phrasetable: probabilité de traduction de la forme cible avec Phrasetable
        """
        self.forme = forme
        self.prob_cs_anymalign = 0
        self.prob_cs_giza = 0
        self.prob_cs_phrasetable = 0

    def calcule_somme(self):
        """
        Fonction qui calcule la somme des trois probabilités de traduction (prob_cs_anymalign, prob_cs_giza et prob_cs_phrasetable)

        :return: la somme des trois probabilités
        """
        return self.prob_cs_anymalign + self.prob_cs_giza + self.prob_cs_phrasetable

    def _get_forme(self):
        """
        Accesseur

        :return: la forme sous chaîne de caractères
        """
        return self.forme

    forme = property(fget=_get_forme)

    def _set_forme(self, val):
        """
        Mutateur

        :param val: la nouvelle valeur de l'attribut forme
        """
        self._forme = val

    forme = property(fget=_get_forme, fset=_set_forme)

    def _get_proba_cs_anymalign(self):
        """
        Accesseur

        :return: probabilité de cible sachant source dans le fichier généré par Anymalign
        """
        return self.prob_cs_anymalign

    def _set_proba_cs_anymalign(self, val):
        """
        Mutateur

        :param val: la valeur de la probabilité de cible sachant source dans le fichier généré par Anymalign
        """

        self.prob_cs_anymalign = val

    prob_cs_anymalign = property(_get_proba_cs_anymalign, _set_proba_cs_anymalign)

    def _get_proba_cs_giza(self):
        """
        Accesseur

        :return: probabilité de cible sachant source dans le fichier dictionary généré par GIZA++
        """
        return self.prob_cs_giza

    def _set_proba_cs_giza(self, val):
        """
        Mutateur

        :param val: la valeur de la probabilité de cible sachant source dans le fichier dictionary généré par GIZA++
        """

        self.prob_cs_giza = val

    prob_cs_giza = property(_get_proba_cs_giza, _set_proba_cs_giza)

    def _get_proba_cs_phrasetable(self):
        """
        Accesseur

        :return: probabilité de cible sachant source dans le fichier phrase-table généré par GIZA++
        """
        return self.prob_cs_phrasetable

    def _set_proba_cs_phrasetable(self, val):
        """
        Mutateur

        :param val: la valeur de la probabilité de cible sachant source dans le fichier phrase-table généré par GIZA++
        """
        self.prob_cs_phrasetable = val

    prob_cs_phrasetable = property(_get_proba_cs_phrasetable, _set_proba_cs_phrasetable)

    def __repr__(self):
        """
        :return: chaîne de caractères représentant l'objet
        """
        print(f"Cible(forme={self.forme}, prob_cs_anymalign={self.prob_cs_anymalign}, "
              f"prob_cs_giza={self.prob_cs_giza}, prob_cs_phrasetable={self.prob_cs_phrasetable})")
