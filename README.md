# OpenClassRoom - Projet 2 - WebScrapping
Ce projet a pour but de créer un script Python permettant d'aller chercher des infos sur des livres via le site https://books.toscrape.com/index.html .


# Utilisation

## Args

### Arguments unique obligatoire :

*Ces argument permettent d'activer un mode particulier pour le script. On peut en mettre qu'un a la fois, et si jamais on en met plusieurs, le premier sera celui utilisé par le script.*

-a --all : Lance le script pour qu'il aille chercher tout les livres de toutes les catégories. Le script génèrera un fichier .csv pour chaque catégorie du site

-c --categorie :  Affiche une liste de toutes les catégorie du site, et demande a l'utilisateur quel catégorie il veut. Une fois choisis, un .csv sera créé du nom de la catégorie. 

### Argument Optionnel :

-i --image : Les images de tout les produits parcourus seront téléchargé et zippé dans le dossier image. Sinon, rien ne sera téléchargé.

