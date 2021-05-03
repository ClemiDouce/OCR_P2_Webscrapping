# OpenClassRoom - Projet 2 - WebScrapping

Ce projet a pour but de créer un script Python permettant d'aller chercher des infos sur des livres via le site https://books.toscrape.com/index.html .

# Utilisation

## Environnement virtuel

Pour mettre en place l'environnement virtuel nécessaire pour faire fonctionner le script, procéder comme suit :

Dans un terminal ouvert dans le dossier ou vous avez cloné le repository, créez un environnement virtuel a l'aide de venv :

```bash
python3 -m venv [nom environnement]
```

Une fois que l'environnement est créé, activez l'environnement (dans cet exemple, 'env' est le nom de mon environnement) :

Windows

```bash
.\env\Scripts\activate
```

Mac / Linux 

```bash
source env/bin/activate
```

Pour vérifier que l'environnement est bien activé, le nom de l'environnement s'affiche a gauche de l'indicateur de position dans le terminal

Installez tout les packages dans ce nouvel environnement listé dans le fichier 'requirements.txt' :

```bash
pip install -r requirements.txt
```

Vérifier que tout les packages sont bien installé a l'aide de la commande `pip freeze`.

## Args

### Arguments unique obligatoire :

*Ces argument permettent d'activer un mode particulier pour le script. On peut en mettre qu'un a la fois, et si jamais on en met plusieurs, le premier sera celui utilisé par le script.*

-a --all : Lance le script pour qu'il aille chercher tout les livres de toutes les catégories. Le script génèrera un fichier .csv pour chaque catégorie du site

-c --categorie :  Affiche une liste de toutes les catégorie du site, et demande a l'utilisateur quel catégorie il veut. Une fois choisis, un .csv sera créé du nom de la catégorie. 

### Argument Optionnel :

-i --image : Les images de tout les produits parcourus seront téléchargé et zippé dans le dossier image.

-z --zip : Toutes les images et les csv seront compressé dans un dossier .zip

### Exemple d'utilisation

Parcourir toutes les catégories du site en téléchargeant les images :

```bash
python .\main.py -a -i
```

Parcourir une catégorie en particulier en zippant les .csv obtenus :

```bash
python .\main.py -c -z
```

Parcourir une catégorie en particulier en zippant les .csv et images obtenus :

```bas
python .\main.py -c -i -z
```

