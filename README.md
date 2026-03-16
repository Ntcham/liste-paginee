# liste-paginee
Implémentation d'une liste paginée en Python - INF21307

## Auteurs
Akoua Marie-Reine N'TCHAM
Alpha Oumar DIALLO

## Langage et environnement
- Langage : Python 3
- Système : Windows
- Environnement : exécution via terminal

## Description
Ce programme implémente une structure de données appelée du nom de: liste paginée.  
Une liste paginée est composée de pages reliées entre elles. Chaque page contient
un nombre fixe de cases permettant de stocker des éléments.

La structure permet d’effectuer plusieurs opérations sur les éléments.

## Fonctionnalités
- **add(valeur)** : ajoute un élément dans la première case libre disponible.
- **search(valeur)** : recherche un élément dans la liste et retourne sa position.
- **remove(numero_page, position)** : supprime un élément à la position demandée.
- **compact()** : réorganise les éléments afin de supprimer les cases vides.
- **elements()** : retourne le nombre d’éléments présents dans la liste.
- **pages()** : retourne le nombre de pages utilisées.

## Sources 
- Notes de cours du cours INF21307
- Documentation officielle Python
- Concepts généraux sur les structures de données (listes chaînées)

## Exécution
Pour exécuter le programme :

```bash
python liste_paginee.py