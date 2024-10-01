from Cible import Cible


class Source:
    """
    Classe qui représente les informations sur une forme source
    - forme (chaîne de caractères)
    - dictionnaire contenant ses traductions (clé = forme cible, valeur = objet de type Cible)
    """

    def __init__(self, forme):
        """
        Constructeur :
        forme: de chaîne de caractères
        dictionnaire: contiendra les traductions (clé = forme cible, valeur = objet de type Cible)
        """
        self.forme = forme
        self.traductions = {}

    def ajoute_cible(self, cible, proba, attribut):
        """
        Ajoute une probabilité de traduction à une forme cible.
        La méthode vérifie d'abord si la forme cible se trouve dans le
        dictionnaire traductions. Si non, un nouvel objet de type Cible est
        créé. La probabilité de traduction passée en argument est ajoutée à
        l'objet Cible.

        :param cible: la forme cible sous forme de chaîne de caractères
        :param proba: probabilité de traduction
        :param attribut: probabilité à ajouter (sous forme de chaîne de caractères : prob_cs_anymalign, prob_cs_giza ou prob_cs_phrasetable
        """

        if cible not in self.traductions:
            self.traductions[cible] = Cible(cible)
        if attribut == 'prob_cs_anymalign':
            self.traductions[cible].prob_cs_anymalign += proba
        elif attribut == 'prob_cs_giza':
            self.traductions[cible].prob_cs_giza += proba
        elif attribut == 'prob_cs_phrasetable':
            self.traductions[cible].prob_cs_phrasetable += proba

    def meilleures_traductions(self, num=10):
        """
        Retourne les meilleures traductions de la source, triées en fonction
        de la somme des probabilités

        :param num: nombre de traductions à retourner
        :return: Liste de tuples (forme cible, somme des probabilités) triée par ordre de somme de probabilités décroissante
        """
        sorted_traductions = sorted(self.traductions.items(), key=lambda x: x[1].calcule_somme(), reverse=True)
        return [(cible, trad.calcule_somme()) for cible, trad in sorted_traductions][:num]
