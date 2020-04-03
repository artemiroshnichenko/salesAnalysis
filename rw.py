import pandas as pd 
import json
import csv

def r_json(FILE_LOCATION):
    with open(FILE_LOCATION) as json_file:
        data = json.load(json_file)
    return data

def w_json(data, filename): 
    with open(filename,'w') as f: 
        json.dump(data, f, indent=4)
        
def r_csv(FILE_LOCATION,separate,head): 
    return pd.read_csv(FILE_LOCATION, header=head, sep=separate)

def w_csv(FILE_LOCATION,df):
    df.to_csv (FILE_LOCATION, index = None, header=True)
