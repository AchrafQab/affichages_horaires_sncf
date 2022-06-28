# Affichage_Horaires
Application web d'affichage dynamique des horaires en gare SNCF et l'aéroport Lorraine.


## Utilisation 

### url services 
L'application est actuellement fonctionnelle sur l'url :
##### https://gaffevlatafdachraf.g-ny.eu/affichages_horaires?train_dep=1&train_arr=1&vol_dep=1&vol_arr=1&train_dep_attente=0000&train_arr_attente=1000&vol_dep_attente=2000&vol_arr_attente=4000&code_gare=NCY

Les paramètres de l'url sont les suivants :
#### Variables d'affichage des tableaux des horaires de trains et avion : 

##### 1ér paramètre : train_dep : 
    - train_dep = 1 ==> affiche le tableau des horaires de trains de départ.
    - train_dep = 0 ==> n'affiche pas le tableau des horaires de trains de départ.
##### 2ème paramètre : train_arr : 
    - train_arr = 1 ==> affiche le tableau des horaires de trains d'arrivée.
    - train_arr = 0 ==> n'affiche pas le tableau des horaires de trains d'arrivée.
##### 3ème paramètre : vol_dep : 
    - vol_dep = 1 ==> affiche le tableau des horaires de départ à l'aéroport Lorraine.
    - vol_dep = 0 ==> n'affiche pas le tableau des horaires de départ à l'aéroport Lorraine.
##### 4ème paramètre : vol_arr : 
    - vol_arr = 1 ==> affiche le tableau des horaires d'arrivée à l'aéroport Lorraine.
    - vol_arr = 0 ==> n'affiche pas le tableau des horaires d'arrivée à l'aéroport Lorraine.
##### 5ème paramètre : code_gare : 
    - code_gare = ncy : ce paramètre permet de choisir le nom de la gare qui ne doit pas dépasser 3 lettres, par exemple : ncy (Nancy) + Jarv (Jarville) + Str (Strasbourg)

#### Varibales de temps d'affichage de chaque tableau des horaires de trains et avion :

##### 5ème paramètre : train_dep_attente : 
    - train_dep_attente = 5000 ==> afficher le tableau des horaires de trains de départ en 5 secondes.
    - train_dep_attente = 0000 ==> desactiver le tableau des horaires de trains de départ.
##### 6ème paramètre : train_arr_attente : 
    - train_arr_attente = 4000 ==> afficher le tableau des horaires de trains d'arrivée en 4 secondes.
    - train_arr_attente = 0000 ==> desactiver le tableau des horaires de trains d'arrivée.
##### 7ème paramètre : vol_dep_attente : 
    - vol_dep_attente   = 5000 ==> afficher le tableau des horaires de départ à l'aéroport Lorraine en 5 secondes.
    - vol_dep_attente   = 0000 ==> desactiver le tableau des horaires de départ à l'aéroport Lorraine.
##### 8ème paramètre : vol_arr_attente : 
    - vol_arr_attente   = 4000 ==> afficher le tableau des horaires d'arrivée à l'aéroport Lorraine en 4 secondes.
    - vol_arr_attente   = 0000 ==> desactiver le tableau des horaires d'arrivée à l'aéroport Lorraine.

On peut donc choisir le tableau et le délais d'affichage depuis les paramètres de l'url.

## Environnement de développement
### Serveur
1/ Installer Putty pour l'utilisation du proxy et la spécification du login.

2/ Procéder les paramétrages suivants :
- Host Name (or IP address) : 152.228.229.45     
- Port : 22
- Saved Sessions / New Folder : g-ny2 - SBG7 - 152.228.229.45

3/ Cliquer sur le bouton Open.

4/ La fenetre de console Putty s'ouvre, puis on saisis les données de connexion suivants : 
- login : achraf
- password : SuperAfficheur

5/ Maintenant, on est connecté au serveur, on lance les commandes suivants pour lancer l'application : 
###### #cd /opt/affichage_horaires 
###### #source venv/bin/activate 
###### #pyhton3 app.py

6/ L'application est lancé sur l'url : 
##### https://gaffevlatafdachraf.g-ny.eu/affichages_horaires?train_dep=1&train_arr=1&vol_dep=1&vol_arr=1&train_dep_attente=6000&train_arr_attente=4000&vol_dep_attente=6000&vol_arr_attente=4000&code_gare=NCY
