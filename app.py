from fileinput import filename
from urllib import response
from flask import Flask, redirect, render_template, jsonify, request, url_for
# import pandas as pd
import json
import os
import config
import horaires
from logzero import logger

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False

# 
@app.route('/')
def index():
    return' Paramètre à url'

#  Afficher la page des horaires de trains et vol en appelant notre template "horaires.html"
@app.route('/affichages_horaires', methods=['GET','POST'])
def affichage_horaires():
    # output= request.args.get('output', 'html')

    code_gare = request.args.get('code_gare', '').upper()
    aff_train_dep = request.args.get('train_dep', '0')
    aff_train_arr = request.args.get('train_arr', '0')
    aff_vol_dep = request.args.get('vol_dep', '0')
    aff_vol_arr = request.args.get('vol_arr', '0')
    train_dep_delai = request.args.get('train_dep_attente', 5000)
    train_arr_delai = request.args.get('train_arr_attente',5000)
    vol_dep_delai = request.args.get('vol_dep_attente',5000)
    vol_arr_delai = request.args.get('vol_arr_attente',5000)
    # Création des URL qui seront utilisées par le code JS pour le rechargement des données
    domain = 'https://{0}/'.format(request.host)
    url_train_depart = url_train_arrivee = url_vol_depart = url_vol_arrivee = ""
    # train_dep_delai = train_arr_delai = vol_dep_delai = vol_arr_delai = "00000"
    if aff_train_dep=='1':
        url_train_depart = url_for('get_horaire', sens='depart', code_gare=code_gare, mode='train')
        logger.info(url_train_depart)
    if aff_train_arr=='1' :
        url_train_arrivee = url_for('get_horaire', sens='arrivee', code_gare=code_gare, mode='train')
        logger.info(url_train_arrivee)
    if aff_vol_dep == '1':
        url_vol_depart = url_for('get_horaire', sens='depart', mode='vol')
        logger.info(url_vol_depart)
    if aff_vol_arr == '1' :
        url_vol_arrivee = url_for('get_horaire', sens='arrivee', mode='vol')
        logger.info(url_vol_arrivee)

    # On lance le template avec des horaires de train au départ
    # C'est pas grave si les infos sont vides parce que c'est le JS qui devra charger les données juste après le chargement de la page
    rep = horaires.horaires(code_gare=code_gare, aff_train_dep='1', aff_train_arr='1', aff_vol_dep='1', aff_vol_arr='1', 
                            train_dep_delai=5000, train_arr_delai = 5000, vol_dep_delai = 5000, vol_arr_delai =5000)
    tableau_train = rep['data_train_dep'], rep['data_train_arr'], rep['data_vol_dep'], rep['data_vol_arr']

    # On lance le render_template avec les deux templates : horaires.html avec le widget forcast7 ou horaires_meteo.html avec le widget meteo-france en cas de panne 
    # return render_template("horaires_meteo.html",
    #     tableau_train = tableau_train,
    #     url_train_depart=url_train_depart,
    #     url_train_arrivee=url_train_arrivee,
    #     url_vol_depart=url_vol_depart,
    #     url_vol_arrivee=url_vol_arrivee, 
    #     train_dep_delai = train_dep_delai, 
    #     train_arr_delai = train_arr_delai, 
    #     vol_dep_delai = vol_dep_delai,
    #     vol_arr_delai = vol_arr_delai)
    return render_template("horaires.html",
        tableau_train = tableau_train,
        url_train_depart=url_train_depart,
        url_train_arrivee=url_train_arrivee,
        url_vol_depart=url_vol_depart,
        url_vol_arrivee=url_vol_arrivee, 
        train_dep_delai = train_dep_delai, 
        train_arr_delai = train_arr_delai, 
        vol_dep_delai = vol_dep_delai,
        vol_arr_delai = vol_arr_delai)
    # return render_template('404.html', errmessage="Sorry, site not found :-/"), 404
    

@app.route('/horaires', methods=['GET','POST'])
def get_horaire():
    """get_horaires
    Retournes de horaires de train ou d'avion.
    Paramètres :
    mode : "train" ou "vol"
    sens : "depart" ou "arrivee"
    code_gare : code de la gare (pour les trains)
    Returns:
        tableau des horaires en JSON (différents si on a des trains ou des avions)
    """
    mode = request.args.get('mode', '')
    sens = request.args.get('sens', '')
    code_gare = request.args.get('code_gare', '')
    
    data = "{}"
    if mode=='train' and len(code_gare)==3:
        if sens == 'depart':
            rep = horaires.horaires(code_gare=code_gare, aff_train_dep='1')
            data = json.dumps(rep['data_train_dep'])
        elif sens == "arrivee":
            rep = horaires.horaires(code_gare=code_gare, aff_train_arr='1')
            data = json.dumps(rep['data_train_arr'])
    elif mode == 'vol':
        if sens == 'depart':
            rep = horaires.horaires(aff_vol_dep='1')
            data = json.dumps(rep['data_vol_dep'])
        elif sens == 'arrivee':
            rep = horaires.horaires(aff_vol_arr='1')
            data = json.dumps(rep['data_vol_arr'])

    
    return data, 200, {'Content-Type': 'application/json; charset=utf-8'}


#  Test de méthodes 
if __name__ == '__main__':

    app.run(debug=True)
