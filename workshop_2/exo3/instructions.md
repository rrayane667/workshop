    Les modules python ne sont ni plus ni moins que des fichiers python réutilisables qui contiennent des objects comme des fonctions, des variables ou des classes. Chaque module contient des outils pour faire des tâches spécifiques. Par exemple pour les calculs mathématiques, on utilisera le module math présent par défaut. Il existe néanmoins des modules externes téléchargeables qui permettent d'ajouter des capacités étendues à un programme Python (fenêtres graphiques, développement web, ...)

# Utilisation de modules:
Le but de cet exercice est de créer soit même des modules à utiliser pour calculer le volume d'une sphère, pour cela trois fichiers seront nécessaires, une fichier `func.py` qui va contenir la fonction __calcul_volume_sphère__, un fichier `monte_carlo` qui va être copié du workshop précedent pour la valeur de pi, et un fichier main.py pour l'execution du programme.

# Instructions:

- Copier le fichier `monte_carlo.py` dans le répertoire `exo3`, ce fichier nous donnera la valeur de pi nécessaire pour notre calcul, 
- Créer la fonction `__calcul_volume_sphère(pi, rayon) -> volume__` qui calcul le volume d'une sphère
- Complèter le fichier `main.py` qui permet d'importer les deux modules (fichiers) et affiche le volume d'une sphère de rayon 2.2m
- Modifier le fichier `monte_carlo.py` pour que la dernière ligne de l'affichage ne s'execute que si le fichier est executé de lui-même et n'est pas importé par un autre fichier 