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
f.create_json()
@app.route('/')
def hello_world():
    #utilisé pour tester si l'app fonctionne bien
    return 'Hello, World!'

@app.route('/latest_by_country/<country>')
def by_country(country):
    #on veut la valeur la plus récente des emissions totales pour le pays demandé
    logging.debug(f"Pays demandé : {country}")
    result = f.get_latest_by_country(country)
    if  result != None:
        return result
    else:
        #erreur 404 si on demande un pays qui n'est pas connu
        abort(404)

@app.route('/average_by_year/<year>')
def average_for_year(year):
    #on cherche la moyenne des émissions totales au niveau mondial pour une année demandée
    logging.debug(f"Année demandée : {year}")
    resultat = f.average_for_year(year)

    if resultat != 1:
        return json.dumps({"year": year, "total":resultat})
    else:
        abort(404)

@app.route('/per_capita/<country>')
def per_capita(country):
    logging.debug(f"Pays demandé : {country}")
    result = f.get_per_capita("estimates.json",country)
    if result != 1:
        return json.dumps(result)
    else:
        abort(404)

if __name__=="__main__":
    app.run(debug=True)
    
