# api_analyse_donnees

Auteurs : Adrian, Djan, Yoan

Technologies : Python, flask, postman, Json

Ce programme permet d'interagir avec les données de l'ONU sur les émissions de Co2 dans le monde, il comprendra quantre script:
1] le fichier "Fonction" qui comprendra quatre fonctions principales :

Le programme sera testé en amont avec Flask et l'API Postman avant d'être déployé en réseau local.

1) Fonction "create_json()", qui permet de créé le fichier json à partir du csv:

Correction des tables:
- Changement manuel du nom du fichier csv 
- remplacement de la colonne " Region/Country/Area " par " id ", et de la colonne "(vide)" par Region/Country/Area 
- rangement des tables pour qu'elles soient ordonnée, et en mesure de traité les accents

2) Fonction "by_country()", qui permet de d'afficher l'émission de Co2 total d'un pays la dernière année:

- L'utilisateur saisie un pays en entré http, le programme recherche dans l'émission de Co2 de ce pays la dernière année
- Il renvoie la valeur dans la sortie

3) Fonction "average_for_year", qui permet de renvoyer la moyenne d'émission de Co2 Mondial par année:

- L'utilisateur saisie une année, le programme calcul la somme des émissions de Co2 mondial et la divise par le nombre
  de pays pour faire une moyenne mondial
- Il renvoie ce résultat dans la sortie 
  
4) Fonction "per_capita", qui permet de renvoyé l'émission de Co2 par personne de toutes les années d'un pays entré en http:

- L'utilisateur saisie un pays en entré http, le programme prend en compte toute les années correspondant au pays 
- Si 'thousand' se trouve dans la colonne Series de ces lignes, on l'ajoute à notre liste 
- Il renvoie les valeurs dans la sortie 

2] Le fichier "app.py" qui comprend toutes les requêtes http, avec l'appel des fonctions depuis le fichier "Fonction.py":










