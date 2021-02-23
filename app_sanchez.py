import csv
import json

""" function that allows to create the json file from the csv. Correction of the tables: 
replacement of the column (RegionCountryArea) by (id), and of the column "(empty)" by (RegionCountryArea) 
arranging of the tables so that they are ordered, and able to handle the accents."""

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

""" Function that allows to send back the Co2 emission of a country
    in the last year and to send in output """

def get_latest_by_country(countryName, jsonFile='estimates.json'):
    years, emissions = list(), str()

    try:
        countryName.lower()
    except:
        return None

    with open(jsonFile, 'r') as f:
        info_dict = json.load(f)
        for info in info_dict:
            if info["Region/Country/Area"].lower() == countryName.lower() and 'thousand' in info['Series']:
                
                years.append(info['Year'])
                emissions = round(float(info['Value']),3)
                emissions = str(emissions)
    try:
        return json.dumps({"country": countryName.lower(), "year": max(years), "emissions": emissions})
    except:
        return None
    
with open(filename_path_json, 'w') as outfile:
        json.dump(output, outfile,sort_keys=True, indent=4, ensure_ascii=False)

""" The function calculates the sum of the CO2 consumption of all countries 
and divides it by the number of countries to obtain a world average. """ 

def average_for_year(year):
    emissions = []
    with open("estimates.json", 'r') as f:
        info_dict = json.load(f)
        for info in info_dict:
            if info["Year"].lower() == year.lower() and 'thousand' in info['Series']: 
                emissions.append(float(info['Value']))
    
    return sum(emissions)/len(emissions)
  

# @app.route('/per_capita/<country>')

""" Function that allows to return the Co2 
emission per person of one over all years"""

def per_capita(jsonFile, country):

    dic = {}
    years = []
    emissions = list()

    with open(jsonFile, 'r') as f:
        info_dict = json.load(f)        
        for info in info_dict:
            if info["Region/Country/Area"].lower() == country.lower() and 'per capita' in info['Series']:
                years.append(info["Year"])
                emissions.append(float(info["Value"]))
                
    for cpt, i in enumerate(years):
        dic[i] = emissions[cpt]
       

        
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