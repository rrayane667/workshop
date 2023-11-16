# Ces exercices traitent des chaînes de caractères, écrire les réponses dans :

## Exercice 1.1 : Extraction d'informations d'une chaîne
Écrivez une fonction qui prend une chaîne de caractères contenant des informations sur une personne sous la forme "Nom Prénom Age" et extrait chaque élément séparément.

Exemple d'entrée : "Dupont Jean 35"
Sortie attendue : ("Dupont", "Jean", "35")

## Exercice 1.2 : Validation de mot de passe
Écrivez une fonction qui vérifie si un mot de passe respecte certaines règles :

Doit avoir au moins 8 caractères.
Doit contenir au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial parmi !@#$%^&*.
Exemple d'entrée : "MotDePasse1!"
Sortie attendue : True

## Exercice 1.3 : Remplacement de mots
Écrivez une fonction qui prend une chaîne de caractères et remplace chaque occurrence d'un mot spécifique par un autre mot.

Exemple d'entrée : "Le chat est sur le toit." (Remplacer "chat" par "chien")
Sortie attendue : "Le chien est sur le toit."

## Exercice 1.4 : Comptage de fréquence de lettres
Écrivez une fonction qui compte la fréquence d'apparition de chaque lettre dans une chaîne de caractères (en ignorant la casse et en ne tenant compte que des lettres).

Exemple d'entrée : "Bonjour, comment ça va ?"
Sortie attendue : {'b': 1, 'o': 5, 'n': 2, 'j': 1, 'u': 1, 'r': 1, 'c': 2, 'm': 2, 'e': 2, 't': 2, 'ç': 1, 'v': 1, 'a': 1}

## Exercice 1.5 : Conversion de texte en acronyme
Écrivez une fonction qui prend une phrase et retourne l'acronyme de cette phrase (les initiales de chaque mot en majuscules).

Exemple d'entrée : "Bonjour tout le monde"
Sortie attendue : "BTLM"

# Exercice 1.6 : classification de sentiments
Écrivez une fonction classificateur_sentiments qui prend en entrée une liste de phrases et attribue un sentiment (positif, négatif ou neutre) à chaque phrase en se basant sur des mots-clés spécifiques.
Utilisez une approche simple basée sur des mots-clés pour attribuer les sentiments :

-Si la phrase contient des mots-clés tels que "heureux", "merveilleux", "super", "adoré", attribuez le sentiment "Positif".
-Si la phrase contient des mots-clés tels que "nul", "déteste", "mauvais", "horrible", attribuez le sentiment "Négatif".
-Sinon, attribuez le sentiment "Neutre".

mots_cles_positifs = ["heureux", "merveilleux", "super", "adoré"]
mots_cles_negatifs = ["nul", "déteste", "mauvais", "horrible"]

commentaires = [
    "J'ai adoré ce film !",
    "C'était vraiment nul...",
    "Super expérience utilisateur",
    "Je déteste cette chanson",
    "J'aime bien ce produit"
]

---
---
---

# Ces exercices traitent les dictionnaires: 

## Exercice 2.1 : Analyse des occurrences de mots
Écrivez une fonction qui prend une chaîne de caractères en entrée et renvoie un dictionnaire où les clés sont les mots uniques présents dans la chaîne et les valeurs sont le nombre d'occurrences de chaque mot.
 Exemple : 
chaine = "Le chat est sur le toit, le chien est dans la cour."
Sortie attendue : {'Le': 1, 'chat': 1, 'est': 2, 'sur': 1, 'le': 2, 'toit,': 1, 'chien': 1, 'dans': 1, 'la': 1, 'cour.': 1}



## Exercice 2.2 : Fusion de dictionnaires
Écrivez une fonction qui fusionne deux dictionnaires en prenant en compte les valeurs des clés communes. Si une clé existe dans les deux dictionnaires, ajoutez les valeurs correspondantes; sinon, conservez la valeur existante.

Exemple:
dictionnaire1 = {'a': 10, 'b': 20, 'c': 30}
dictionnaire2 = {'b': 5, 'c': 15, 'd': 25}
Sortie attendue : {'a': 10, 'b': 25, 'c': 45, 'd': 25}



## Exercice 2.3 : Conversion de dictionnaire imbriqué en liste de tuples
Écrivez une fonction qui prend un dictionnaire imbriqué en entrée et le convertit en une liste de tuples contenant des paires clé-valeur, en incluant les clés de niveau supérieur pour les dictionnaires imbriqués.

Exemple:
dictionnaire_imbrique = {'a': 1, 'b': {'c': 2, 'd': {'e': 3, 'f': 4}}}
Sortie attendue : [('a', 1), ('b', [('c', 2), ('d', [('e', 3), ('f', 4)])])]



## Exercice 2.4 : Fusion de dictionnaires imbriqués
Écrivez une fonction qui fusionne deux dictionnaires imbriqués (dictionnaires ayant des dictionnaires comme valeurs) en un seul dictionnaire, en combinant les valeurs des clés communes.
Exemple:

dict1 = {'a': 1, 'b': {'c': 2, 'd': 3}}
dict2 = {'b': {'e': 4, 'f': {'g': 5, 'h': 6}}, 'i': 7}
Sortie attendue : {'a': 1, 'b': {'c': 2, 'd': 3, 'e': 4, 'f': {'g': 5, 'h': 6}}, 'i': 7}


## Exercice 2.5 : Triez un dictionnaire en fonction de ses valeurs
Écrivez une fonction qui prend un dictionnaire en entrée et renvoie un nouveau dictionnaire trié en fonction de ses valeurs, du plus petit au plus grand.

Exemple d'utilisation :
dico = {'a': 5, 'b': 2, 'c': 8, 'd': 1}
Sortie attendue : {'d': 1, 'b': 2, 'a': 5, 'c': 8}
