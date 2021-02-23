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

def average_for_year(year):
    emissions = []
    with open("estimates.json", 'r') as f:
        info_dict = json.load(f)
        for info in info_dict:
            if info["Year"].lower() == year.lower() and 'thousand' in info['Series']:  
                emissions.append(float(info['Value']))
    
    return sum(emissions)/len(emissions)

create_json()
print(average_for_year('2017'))