import json
import fonctions as f

def info_latest_by_country():
    countries = list()
    countries_info = dict()

    with open('estimates.json') as json_file:
        info_dict = json.load(json_file)
        for info in info_dict:
            countries.append(info[ "Region/Country/Area"])
            
    countries = list(dict.fromkeys(countries))
    for country in range(len(countries)):
            countries_info[countries[country]] = f.get_latest_by_country(countries[country])
    
    return countries_info
