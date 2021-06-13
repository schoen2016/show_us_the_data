import pandas as pd
from utils.read import readJSON


config = readJSON('config.json')
path_source = config['extract_source']
path_dest = config['extract_dest']
file_ref = config['reference']
path_stopwords = config['stopwords']
padding = config['padding']
bool_rws = config['remove_stopwords']
list_stopwords = config['stopwords_plus']


ref = pd.read_csv(file_ref)

cleaned_label = ref['cleaned_label'].unique()

for l in cleaned_label:
    print(l)

