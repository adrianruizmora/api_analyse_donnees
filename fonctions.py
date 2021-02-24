import csv
import json
import os

""" function that allows to create the json file from the csv. Correction of the tables: 
replacement of the column (RegionCountryArea) by (id), and of the column "(empty)" by (RegionCountryArea) 
arranging of the tables so that they are ordered, and able to handle the accents."""

def create_json(filename_path_csv='estimates.csv', filename_path_json='estimates.json'):

    output = list()
    logging.info("lancement de la fonction create_json")     
    if not isinstance(filename_path_csv, str) or os.path.isdir(filename_path_csv):
        logging.debug("test du type des paramètre de la fonction ")
        return 1
    if not filename_path_csv.endswith('.csv') or not filename_path_json.endswith('json'):
        logging.debug("Test du format des parametres")
        return 1
    try:
        f = open(filename_path_csv)
        logging.debug("Test de l'existance du fichier csv..")
    except FileNotFoundError:
        return 1
   
    with f:

        next(f, None)
        logging.debug("Ouverture du fichier csv, on saute la premiere ligne")
        reader = csv.DictReader(f)
        for records in reader:
            records["id"] = records.pop("Region/Country/Area")            
            records["Region/Country/Area"] = records.pop("")            
            output.append(records) 

        logging.debug("remplacement de la colonne Region/Country/Area par id")
        logging.debug("remplacement de la colonne vide par Region/Country/Area")

    with open(filename_path_json, 'w') as outfile:
        json.dump(output, outfile,sort_keys=True, indent=4, ensure_ascii=False)

        logging.debug("ouverture et écriture du fichier json")
        logging.debug("ordonnement de la table, prise en compte des caractères spéciaux")
        logging.debug("telechargement et modification du fichier json réussi")

    return 0
    
""" Function that allows to send back the Co2 emission of a country
    in the last year and to send in output """
    
def get_latest_by_country(country_name, filename_path_json='estimates.json'):

    years, emissions = list(), str()
    logging.debug("Appel de la fonction lastest_country")
    if not filename_path_json.endswith('.json'):
        logging.debug("Test de format du fichier json")
        return None
    try:
        country_name.lower()
    except:
        return None

    with open(filename_path_json, 'r') as f:

        info_dict = json.load(f)
        logging.debug("Ouverture et lecture du fichier json")
        for info in info_dict:
            if info["Region/Country/Area"].lower() == country_name.lower() and 'thousand' in info['Series']:                
                years.append(info['Year'])
                emissions = round(float(info['Value']),3)                
                emissions = str(emissions)

            logging.debug("ajout de l'année et de l'émission total dans la liste")
            logging.debug("Recherche de l'entrée dans la colonne country et son émission total")
    try:
        logging.debug("tentative d'affichage de la liste dic contenant le resultat de la fonction")
        return json.dumps({"country": country_name.lower(), "year": max(years), "emissions": emissions})
    
    except:
        logging.debug("Opération réussi")
        return None

    
def get_latest_by_country(country_name, filename_path_json='estimates.json'):
    years, emissions = list(), str()
    
    if not filename_path_json.endswith('.json'):
        return None
    try:
        country_name.lower()
    except:
        return None

    with open(filename_path_json, 'r') as f:
        info_dict = json.load(f)
        for info in info_dict:
            if info["Region/Country/Area"].lower() == country_name.lower() and 'thousand' in info['Series']:
                years.append(info['Year'])
                emissions = round(float(info['Value']),3)
                emissions = str(emissions)
    try:
        return json.dumps({"country": country_name.lower(), "year": max(years), "emissions": emissions})
    except:
        return None


def average_for_year(year):
    emissions = []
    with open("estimates.json", 'r') as f:
        info_dict = json.load(f)
        for info in info_dict:
            if info["Year"].lower() == year.lower() and 'thousand' in info['Series']:  
                emissions.append(float(info['Value']))
    
    return sum(emissions)/len(emissions)
