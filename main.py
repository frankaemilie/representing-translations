from Lexique import Lexique
from Source import Source
from Cible import Cible

# Pour des raisons de lisibilité, j'ai choisi de mettre chaque partie du code (= chaque classe)
# dans un fichier différent. La liaison entre les fichiers se fait via des imports.
# Chaque programme est nommé par la classe qu'il contient (ex: Lexique.py contient la classe Lexique)

if __name__ == '__main__':
    tl = Lexique()
    print("Lecture du fichier Anymalign")
    tl.lire_anymalign('input/resultat_tatoeba_en.txt')
    print("Lecture du fichier Giza")
    tl.lire_giza_simple('input/dictionary-fr-en')
    print("Lecture du fichier PhraseTable")
    tl.lire_giza_expressions('input/phrase-table-fr-en')
    print(f'Il y a {len(tl)} entrées dans le lexique')
    #on teste avec des mots qui ont des traductions et d'autres qui n'en ont pas (comme blablablalade)
    mots = ["travail", "erreur", "problème", "examen", "blablablalade"]
    for m in mots:
        source = tl.meilleures_traductions(m)
        if source == []:  # pas de traduction trouvée
            print(f"Aucune traduction trouvée pour '{m}'")
        else:
            print(f"Meilleures traductions pour '{m}' :")
            print(source)
    # La boucle a été changé afin de prendre en compte les mots qui n'ont pas de traduction
