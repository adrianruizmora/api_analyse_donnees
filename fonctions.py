import csv
import json
import os

def create_json(filename_path_csv='estimates.csv', filename_path_json='estimates.json'):
    output = list()
         
    if not isinstance(filename_path_csv, str) or os.path.isdir(filename_path_csv):
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
            records["Region/Country/Area"] = records.pop("")
            output.append(records)

    with open(filename_path_json, 'w') as outfile:
        json.dump(output, outfile,sort_keys=True, indent=4, ensure_ascii=False)
    
    return 0

    
def get_latest_by_country(country_name, filename_path_json='estimates.json'):
    years, emissions = list(), str()
    
    if not filename_path_json.endswith('json'):
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
