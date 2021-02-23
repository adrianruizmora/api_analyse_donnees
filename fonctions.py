import csv
import json


def create_json(filenameCsv):
    filename_path_csv = filenameCsv
    filename_path_json = 'estimates.json'
    output = []

    with open(filename_path_csv, 'r') as f:
        next(f, None)
        reader = csv.DictReader(f)
        for records in reader:
            records["id"] = records.pop("Region/Country/Area")
            records["Region/Country/Area"] = records.pop("")
            output.append(records)

    with open(filename_path_json, 'w') as outfile:
        json.dump(output, outfile,sort_keys=True, indent=4, ensure_ascii=False)
    
def get_latest_by_country(jsonFile, countryName):
    years = []
    emissions = str()
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
        

