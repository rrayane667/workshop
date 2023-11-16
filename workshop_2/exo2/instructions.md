
    Écrire le code dans le fichier main.p

# Devine le nombre :

le but de cet exercice est de deviner un nombre déterminé aléatoirement par le programme au début de l'execution. l'utilisateur peut à chaque étape rentrer un nombre, et le programme lui donne des indices (plus grand ou plus petit) jusqu'à ce que l'utilisateur devine correctement le nombre, à la fin le programme renvoie le nombre de tentatives utilisées.

# Étapes :

- Génerer un nombre aléatoire à l'aide de la méthode 'randome.randint'.
- Créer une boucle dans laquelle l'utilisateur donne une valeur, le programme teste si elle est supérieur, inférieur ou égale, et le programme affiche un message correspondant.
- au cas où l'utilisateur à deviné juste, le programme le félicite et lui donne le nombre de tentatives utilisées

# Module à utiliser :
random : module qui met à disposition des méthodes liées à l'aléatoire, comment la génération de nombres aléatoires

- **random.randint(a, b)** : génére un nombre aléatoire entre a et b inclus, ex : random.randint(2, 23).
