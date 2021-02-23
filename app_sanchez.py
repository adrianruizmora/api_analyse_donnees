import csv
import json


def create_json(filename_path_csv='estimates.csv', filename_path_json='estimates.json'):
    output = list()

    with open(filename_path_csv, 'r') as f:
        next(f, None)
        reader = csv.DictReader(f)
        for records in reader:
            records["id"] = records.pop("Region/Country/Area")
            records["Region/Country/Area"] = records.pop("")
            output.append(records)

    with open(filename_path_json, 'w') as outfile:
        json.dump(output, outfile,sort_keys=True, indent=4, ensure_ascii=False)
    
def get_latest_by_country(countryName, jsonFile='estimates.json'):
    years, emissions = list(), str()

    with open(jsonFile, 'r') as f:
        info_dict = json.load(f)
        for info in info_dict:
            if info["Region/Country/Area"].lower() == countryName.lower() and 'thousand' in info['Series']:
                years.append(info['Year'])
                emissions = info['Value']
    try:
        return json.dumps({"country": countryName, "year": max(years), "emissions": emissions})
    except:
        return None

# @app.route('/per_capita/<country>')
def per_capita(jsonFile, country):
# Fonction qui permet de renvoyé l'émission par habitant d'un pays sur plusieurs années
    dic = {}
    years = []
    emissions = list()
    # on créé une liste dict pour les émissions, et une liste pour les années
    with open(jsonFile, 'r') as f:
        # on lit le fichier json
        info_dict = json.load(f)
        # on le charge 
        for info in info_dict:
            if info["Region/Country/Area"].lower() == country.lower() and 'per capita' in info['Series']:
                # si il trouve le pays et que per capita se trouve dans la colonne series
                years.append(info["Year"])
                # on ajoute l'année à la liste years
                emissions.append(float(info["Value"]))
                # on ajoute l'émission à la liste emissions



    for cpt, i in enumerate(years):
        dic[i] = emissions[cpt]
        # permet de renvoyer la valeur de l'année et l'émission pour chaque années, dans le dic

        
    return dic

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