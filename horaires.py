
import config as cfg
import json
import requests
from logzero import logger


def horaires(code_gare="", aff_train_dep="0",aff_train_arr="0", aff_vol_dep="0", aff_vol_arr="0",
             train_dep_delai ="5000", train_arr_delai = "5000", vol_dep_delai = "5000", vol_arr_delai = "5000"):
    
    ret=dict()
    ret['data_train_dep'] = "{}"
    ret['data_train_arr'] = "{}"
    ret['data_vol_dep'] = "{}"
    ret['data_vol_arr'] = "{}"
    ret['status_train_dep'] = 400
    ret['status_train_arr'] = 400
    ret['status_vol_dep'] = 400
    ret['status_vol_arr'] = 400
    ret['train_nom_gare'] = ""
    
    if len(code_gare) == 3:
        if aff_train_dep == '1' :
            ret['status_train_dep'], ret['data_train_dep'], ret['train_nom_gare'] = get_sncf(sens="depart", code_gare=code_gare)
        if aff_train_arr == '1' and train_arr_delai == '5000':
            ret['status_train_arr'], ret['data_train_arr'], ret['train_nom_gare'] = get_sncf(sens="arrivee", code_gare=code_gare)
    # modification 
    if aff_vol_dep == '1' :
        ret['status_vol_dep'], ret['data_vol_dep'] = get_airport(sens='depart')
    if aff_vol_arr == '1' :
        ret['status_vol_arr'], ret['data_vol_arr'] = get_airport(sens='arrivee')

    return ret

def get_sncf(sens :str, code_gare :str, forceupdate :bool=False):

    ret = None
    params = dict()
    url = ""
    nom_gare = ""
    status=400

    if sens.lower() == "depart":
        url = cfg.url_sncf_depart
    elif sens.lower() == "arrivee":
        url = cfg.url_sncf_arrivee
        
    data = "{}"

    if len(url) > 0 and len(code_gare) == 3:
        params ['code_gare'] = code_gare.upper()
        response = requests.get(url=url, params=params, verify=cfg.ssl_verify)
        status = response.status_code
        if status == 200:
            ret = response.json()
            status = ret['status']
            if status == 200:
                data = ret['train']
                nom_gare = ret['nom_gare']

    return status, data, nom_gare
  
def get_airport(sens :str, forceupdate:bool=False):
    
    if sens.lower() == "depart":
        url = cfg.url_airport_depart
    elif sens.lower() == "arrivee":
        url = cfg.url_airport_arrivee
  
    data = "{}"
    if len(url) > 0:
        
        response = requests.get(url=url, verify=cfg.ssl_verify)
        status = response.status_code
        print(response.status_code)
        if status == 200:
            ret = response.json()
            status = ret['status']
            if status == 200:
                data = ret['vols']
                        
    return status, data    

if not cfg.ssl_verify:
    requests.packages.urllib3.disable_warnings()


if __name__ == "__main__" :

    
    # test mauvais code gare
    status, data, nom_gare =  get_sncf(sens="depart", code_gare="NCY")
    logger.info(nom_gare)
    logger.info(status)
    logger.info(str(len(data)) + ' train(s)')
    logger.info(str(data))
    

    # test arrivee Frouard
    status, data, nom_gare =  get_sncf(sens="arrivee", code_gare="NCY")
    logger.info(nom_gare)
    logger.info(status)
    logger.info(str(len(data)) + ' train(s)')
    logger.info(str(data))
    
    status, data = get_airport(sens='depart')
    logger.info(status)
    logger.info(str(len(data)) + ' vols(s)')
    logger.info(str(data))

    status, data = get_airport(sens='arrivee')
    logger.info(status)
    logger.info(str(len(data)) + ' vols(s)')
    logger.info(str(data))


    data = horaires(code_gare='NCY', aff_train_dep='1',aff_train_arr='1', aff_vol_dep='1', aff_vol_arr='1')
    logger.info(str(data))
    
