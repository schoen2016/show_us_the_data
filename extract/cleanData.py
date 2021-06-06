'''
    Filename: cleanData.py
    Author: Alexander Schoen
    Date: 5/30/2021
    Description: 
    Reads a ref CSV file containing filenames and patterns (clean_label).

    Reads JSON files in 'source' directory specified by the ref CSV.  JSON files are expected to contain a list of objects with 'section_title' and 'title' keys-values.  

    Config JSON:
        reference: path to reference CSV (train.csv)
        padding: number of words to extract around pattern (clean_label)
        source: path to raw data (train/)
        dest: path to save cleaned JSON files.
'''
version = 'v2.0.0'

import json
import pandas as pd
from sys import argv
from os.path import exists
from os.path import split
from os import mkdir
from extractPattern import extract
from pprint import pprint

# read json files
def readJSON(filename):
    fopen = open(filename)
    return json.load(fopen) 

# user input
config_path = argv[1]
step=int(argv[2])
iteration=int(argv[3])

# batch processing winodow
start = (iteration-1) * step
end = start + step

# read config
config = readJSON(config_path)
source = config['source']
padding = config['padding']

# read reference csv
ref = pd.read_csv(config['reference'])
end = end if end < len(ref) else len(ref)
ref = ref[start:end]

for index,row in ref.iterrows():
    
    pattern = row['cleaned_label']
    file_id = row['Id']
    filename = file_id + '.json'
    destPath = config['dest'] + version + '/'
    dest = destPath + filename
    src_path = source + filename

    # read destination file if it exits
    dest_data = readJSON(dest) if exists(dest) else list()

    # extract data
    options = {
        'tag':file_id, 
        'padding':padding,
        'remove_stopwords':True,
        'version':version
    }
    data = readJSON(src_path)
    x = extract(data, pattern, options)

    # append previously extracted data
    dest_data.extend(x)
    jsonData = json.dumps(dest_data)

    # save data
    if (not exists(destPath)): mkdir(destPath, mode=0o777)
    f = open(dest, 'w')
    f.write(jsonData)
    f.close()
