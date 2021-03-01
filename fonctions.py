import csv
import json
import os
import logging


logging.basicConfig(level=logging.DEBUG)


def create_json(filename_path_csv='estimates.csv',
                filename_path_json='estimates.json'):
    """
    This functions creates an organized json file from a csv file
    """

    output = list()
    logging.info("lancement de la fonction create_json")
    if (not isinstance(filename_path_csv, str) or
            os.path.isdir(filename_path_csv)):
        logging.debug("test du type des paramètre de la fonction ")
        return 1
    if (not filename_path_csv.endswith('.csv') or
            not filename_path_json.endswith('.json')):
        logging.debug("Test du format des parametres")
        return 1
    try:
        f = open(filename_path_csv)
        logging.debug("recherche du fichier csv..")

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
        logging.debug("replacing empty column by Region/Country/Area")


    with open(filename_path_json, 'w') as outfile:
        logging.debug("ouverture et écriture du fichier json")
        json.dump(output, outfile, sort_keys=True, indent=4,
                  ensure_ascii=False)

        logging.debug("""ordonne la table, prise en compte de caractères
        spéciaux""")
        logging.debug("telechargement et modification du fichier json réussi")

    return 0


def get_latest_by_country(country_name, filename_path_json='estimates.json'):

    """ Function that allows to send back the Co2 emission of a country
    in the last year and to send in output """

    logging.debug("Appel de la fonction lastest_country")

    years, emissions = list(), str()
    if not filename_path_json.endswith('.json'):
        logging.debug("Test de format du fichier json")
        return None
    try:
        country_name.lower()
    except AttributeError:
        return None

    with open(filename_path_json, 'r') as f:

        info_dict = json.load(f)
        logging.debug("Ouverture et lecture du fichier json")
        for info in info_dict:
            if (info["Region/Country/Area"].lower() == country_name.lower() and
                    'thousand' in info['Series']):
                years.append(info['Year'])
                logging.debug("ajout de l'année et de l'émission total")
                emissions = round(float(info['Value']), 3)
                emissions = str(emissions)

    logging.debug("Searching country and total emissions")

    try:
        logging.debug("Displays the list that contains fucntion result")
        return json.loads(json.dumps({"country": country_name.lower(),
                          "year": max(years), "emissions": emissions}))
        logging.debug("Opération réussi")
    except Exception:
        return None


def average_for_year(year):
    """ The function calculates the sum of the CO2 consumption of all countries
    and divides it by the number of countries to obtain a world average"""
    emissions = []
    logging.debug("Appel de la fonction average_for_year")
    with open("estimates.json", 'r') as f:

        info_dict = json.load(f)
        logging.debug("Ouverture et lecture du fichier json")
        logging.debug("Searching in year column and the total emissions")
        for info in info_dict:
            if (info["Year"] == year and
                    'thousand' in info['Series']):
                logging.debug("ajout de la valeur de l'émission à la liste")
                emissions.append(float(info['Value']))

    logging.debug("Calcul de la moyenne des émissions mondiale de Co2")
    try:
        return sum(emissions)/len(emissions)
    except ZeroDivisionError:
        return 1


def get_per_capita(country, jsonFile="estimates.json"):

    """ Function that allows to return Co2 emission per person of
    one over all years"""

    dic = {}
    years = []
    emissions = list()
    logging.debug("Appel de la fonction per_capita")

    if isinstance(jsonFile, str):
        if not jsonFile.endswith('.json'):
            logging.debug("Test de format du fichier json")
            return False
    try:
        f = open(jsonFile, "r")
    except Exception:
        return False
    with f:
        info_dict = json.load(f)
        logging.debug("Ouverture et lecture du fichier json")
        logging.debug("Searching for emisions by habitant ")
        for info in info_dict:
            if (info["Region/Country/Area"].lower() == country.lower() and
                    'per capita' in info['Series']):
                logging.debug("Adding year and emissions by habitants")
                years.append(info["Year"])
                emissions.append(float(info["Value"]))

    logging.debug("Emissions of all years by habitants")

    for cpt, i in enumerate(years):
        dic[i] = emissions[cpt]
    if len(dic) == 0:
        return None
    else:
        return dic
