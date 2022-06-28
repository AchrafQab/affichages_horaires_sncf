#! python3
# coding: utf8

from os import makedirs, path
import logzero

# import des infos sensibles
from secret import login, password, http_proxy, https_proxy

app_path = path.dirname(path.abspath(__file__))

# Création d'un logger
loglevel = logzero.INFO
logpath = path.join(app_path, 'logs')
if not path.exists(logpath): makedirs(logpath)
logfile = path.join(logpath, "app.log")
logzero.setup_default_logger(logfile=logfile, maxBytes=1000000, backupCount=10, level=loglevel)

# Proxy
if len(http_proxy) > 0:
    proxy = { 
        "http"  : http_proxy, 
        "https" : https_proxy
    }
ssl_verify = False

url_sncf_arrivee = "https://api-test.g-ny.org/sncf/arrivee"
url_sncf_depart = "https://api-test.g-ny.org/sncf/depart"

url_airport_depart= "https://api-test.g-ny.org/airport/depart"
url_airport_arrivee= "https://api-test.g-ny.org/airport/arrivee"