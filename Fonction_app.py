import csv
import json
import os

logging.basicConfig(level=logging.DEBUG)

""" function that allows to create the json file from the csv. Correction of the tables: 
replacement of the column (RegionCountryArea) by (id), and of the column "(empty)" by (RegionCountryArea) 
arranging of the tables so that they are ordered, and able to handle the accents."""

def create_json(filename_path_csv='estimates.csv', filename_path_json='estimates.json'):
    output = list()
    logging.info("lancement de la fonction creat_json")     
    if not isinstance(filename_path_csv, str) or os.path.isdir(filename_path_csv):
        logger.debug("Tentative de téléchargement du fichier csv")
        return 1
    if not filename_path_csv.endswith('.csv') or not filename_path_json.endswith('json'):
        return 1
    try:
        f = open(filename_path_csv)
    except FileNotFoundError:
        return 1
   
    with f:
        next(f, None)
        reader = csv.DictReader(f)
        for records in reader:
            records["id"] = records.pop("Region/Country/Area")
            logger.debug("remplacement de la colonne Region/Country/Area par id")
            records["Region/Country/Area"] = records.pop("")
            logger.debug("remplacement de la colonne vide par Region/Country/Area")
            output.append(records)

    with open(filename_path_json, 'w') as outfile:
        logger.debug("ouverture et écriture du fichier json")
        json.dump(output, outfile,sort_keys=True, indent=4, ensure_ascii=False)
        logger.debug("ordonnement de la table, prise en compte des caractères spéciaux")
    
    return 0
    logger.debug("telechargement et ordonnement du fichier json réussi")

""" Function that allows to send back the Co2 emission of a country
    in the last year and to send in output """
    
def get_latest_by_country(country_name, filename_path_json='estimates.json'):
    years, emissions = list(), str()
    logger.debug("Appel de la fonction lastest_country")
    if not filename_path_json.endswith('json'):
        return None
    try:
        country_name.lower()
    except:
        return None

    with open(filename_path_json, 'r') as f:
        logger.debug("Ouverture et lecture du fichier json")
        info_dict = json.load(f)
        for info in info_dict:
            if info["Region/Country/Area"].lower() == country_name.lower() and 'thousand' in info['Series']:
                logger.debug("Recherche de l'entrée dans la colonne country et son émission total")
                years.append(info['Year'])
                emissions = round(float(info['Value']),3)
                logger.debug("ajout de l'année et de l'émission total dans la liste")
                emissions = str(emissions)
    try:
        return json.dumps({"country": country_name.lower(), "year": max(years), "emissions": emissions})
        logger.debug("tentative d'affichage de la liste dic contenant le resultat de la fonction")
    except:
        return None
    logger.debug("Opération réussi")

""" The function calculates the sum of the CO2 consumption of all countries 
and divides it by the number of countries to obtain a world average. """ 

def average_for_year(year):
    emissions = []
    logger.debug("Appel de la fonction average_for_year")
    with open("estimates.json", 'r') as f:
        info_dict = json.load(f)
        logger.debug("Ouverture et lecture du fichier json")
        for info in info_dict:
            if info["Year"].lower() == year.lower() and 'thousand' in info['Series']: 
                logger.debug("Recherche de l'entrée dans la colonne year et son émission total")
                emissions.append(float(info['Value']))
                logger.debug("ajout de la valeur de l'émission à la liste")
    logger.debug("Calcule de la moyenne desémissions mondiale de Co2")
    return sum(emissions)/len(emissions)
    logger.debug("Opération réussi")

# @app.route('/per_capita/<country>')

""" Function that allows to return the Co2 
emission per person of one over all years"""

def per_capita(jsonFile, country):

    dic = {}
    years = []
    emissions = list()
    logger.debug("Appel de la fonction per_capita")
    with open(jsonFile, 'r') as f:
        info_dict = json.load(f)    
        logger.debug("Ouverture et lecture du fichier json")    
        for info in info_dict:
            if info["Region/Country/Area"].lower() == country.lower() and 'per capita' in info['Series']:
                logger.debug("Recherche de l'entrée dans la colonne Region/Country/Area et son émission par habitant")
                years.append(info["Year"])
                emissions.append(float(info["Value"]))
                logger.debug("Ajout de l'année et de l'émission par habitant à la liste")
                
    for cpt, i in enumerate(years):
        dic[i] = emissions[cpt]
        logger.debug("Recherche de toutes les années d'émission par habitant du pays")
       

        
    return dic
    logger.debug("opération réussi")

    # try:
    #     return json.dumps({})
    # except:
    #     return None

# def return_string(this_is_a_string):
#     return this_is_a_string

# def return_is_string(this_is_a_string):
#     return isinstance(this_is_a_string, str)

create_json()
x = per_capita("estimates.json", "Albania")

print(x)