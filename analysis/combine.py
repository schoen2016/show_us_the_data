from sys import argv
from os.path import exists
from os import mkdir
from os import walk
import pandas as pd
import json

version = 'v1.0.0'

# read config
f = open(argv[1])
config = json.load(f)
f.close()

source_dir = config['source']
dest_dir = config['dest'] + version + "/"
csv_name = dest_dir + version + "-combined-features.csv"

# read filenames
try:
    filenames = list(walk(source_dir))[0][2]
except Exception as e:
    print("Source Directory Read Error: %s" % e)

# concatenate data files
frames = list()
for filename in filenames:
    path = source_dir + filename
    frames.append(pd.read_json(path))

df = pd.concat(frames, ignore_index=True)

# save
try:
    if not exists(dest_dir): mkdir(dest_dir)
    df.to_csv(csv_name)
except Exception as e:
    print("Save Error: %s" % str(e))


