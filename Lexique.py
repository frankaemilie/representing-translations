from Source import Source


class Lexique:
    """
    Classe qui représente l'ensemble des informations issues des fichiers.
    """

    def __init__(self):
        """
        Constructeur
        Crée un dictionnaire vide appelé entrees
        """
        self.entrees = {}

    def __len__(self):
        """
        Retourne le nombre d'entrées du lexique

        :return: nombre d'entrées
        """
        return len(self.entrees)

    def meilleures_traductions(self, w, num=10):
        """
        Retourne les meilleures traductions pour une source passée en argument

        :param w: la forme source sous forme de chaîne de caractères
        :param num: nombre de traductions à retourner
        :return: Liste de tuples (forme cible, somme des probabilités) triée
         par ordre de somme de probabilités décroissante
        """

        if w in self.entrees:
            return sorted(self.entrees[w].items(), key=lambda x: x[1], reverse=True)[:num]
        else:
            return []

    def lire_anymalign(self, fichier):
        """
        Lit le fichier généré par Anymalign et remplit le dictionnaire entrees

        :param fichier: chemin vers le fichier
        """

        with open(fichier, 'r', encoding='utf8') as f:
            for line in f:
                line = line.strip().split('\t')
                source = line[0].strip()
                cible = line[1].strip()
                prob_without_split = line[3]
                prob = float(prob_without_split.split(' ')[0])
                if source not in self.entrees:
                    self.entrees[source] = {}
                self.entrees[source][cible] = self.entrees[source].get(cible, 0) + prob

    def lire_giza_simple(self, fichier):
        """
        Lit le fichier dictionary généré par GIZA++ et remplit le dictionnaire entrees

        :param fichier: chemin vers le fichier
        """

        with open(fichier, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip().split(' ')
                source = line[0].strip()
                cible = line[1].strip()
                prob = float(line[2])
                if source not in self.entrees:
                    self.entrees[source] = {}
                self.entrees[source][cible] = self.entrees[source].get(cible, 0) + prob

    def lire_giza_expressions(self, fichier):
        """
        Lit le fichier phrase-table généré par GIZA++ et remplit le dictionnaire entrees

        :param fichier: chemin vers le fichier
        """

        with open(fichier, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip().split('\t')
                source = line[0].strip()
                cible = line[1].strip()
                prob = float(line[2])
                if source not in self.entrees:
                    self.entrees[source] = {}
                self.entrees[source][cible] = self.entrees[source].get(cible, 0) + prob
