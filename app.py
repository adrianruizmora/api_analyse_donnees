import json
import logging
import fonctions as f
from flask import Flask, abort
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

"""
Récupérer les infos du fichier :
https://data.un.org/_Docs/SYB/CSV/SYB63_310_202009_Carbon%20Dioxide%20Emission%20Estimates.csv
"""


@app.route('/')
def hello_world():
    'utilisé pour tester si app fonctionne bien'
    return 'Hello, World!'


@app.route('/latest_by_country/<country>')
def by_country(country):
    """Moyenne des emissions totales mondiale sur une année
   Parameters
   -------------
    Country : 'string'
    Entrez le nom du pays pour lequel on souheterait
    voir les résultats.
    Returns
   -------------
   Moyenne Annuelle par an : ' string'
    Emmissions Totales niveau mondial sur une année
    voir example ci dessous
    http://127.0.0.1:5000/latest_by_country/Albania
    '{"country": "albania", "year": "2017", "emissions": "4342.011"}',
    """
    '''on veut la valeur la plus récente des emissions totales
     pour le pays demandé'''
    logging.debug(f"Pays demandé : {country}")
    result = f.get_latest_by_country(country)
    if result != None:
        return result
    else:
        'erreur 404 if country is unkwown'
        abort(404)


@app.route('/average_by_year/<year>')
def average_for_year(year):
    """ Moyenne des emissions totales mondialles sur une année
   Parameters
   -------------
    year : 'string contenant une valeur numérique'
        Entrez l'année pour laquelle on souheterait
        voir les résultats.
    Returns
   -------------
   Moyenne Annuelle par an : ' string'
            Emmissions Totales niveau mondial sur une année
            voir example ci dessous
    http://127.0.0.1:5000/average_by_year/2017
    {"year": "2017", "total": 219666.44571830987}
    """
    '''on cherche la moyenne des émissions totales au niveau mondial
     pour une année demandée'''
    logging.debug(f"Année demandée : {year}")
    resultat = f.average_for_year(year)

    if resultat != 1:
        return json.loads(json.dumps({"year": year, "total": resultat}))
    else:
        abort(404)


@app.route('/per_capita/<country>')
def per_capita(country):
    """ L'emmission de CO2 par habitant d'un pays sur toutes les années disponibles
    Parameters
   -------------
    country : 'string contenant le nom d'un pays'
            Saisir le nom d'un pays
    Returns
   -------------
    CO2 emmissions each year by habitant for a country : ' string'
    Voir Example ci-dessous
     http://127.0.0.1:5000/per_capita/Albania
     {"1975": 1.804, "1985": 2.337, "1995": 0.58, "2005": 1.27,
        "2010": 1.349, "2015": 1.328, "2016": 1.278, "2017":1.511},
    """
    """ Function that allows to return Co2 
    emission per person of one over all years """
    result = f.get_per_capita(country)
    if isinstance(result, dict):
        return result
    else:
        return abort(404)


if __name__ == "__main__":

    f.create_json()
    app.run(debug=True)