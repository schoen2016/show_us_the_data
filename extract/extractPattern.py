import json
from os.path import split
from sys import argv
from scan import scan


def extract(data, pattern, options={}):
    '''
        Input: 
            data: object with 'section_title' and 'text' keys
            pattern: the pattern used in scan.scan
            tag: optional parameter added to each returned object
        Output
            section_title: section title from data
            feature: padded string from scan
            pattern: pattern used in scan
            tag: optional tag
        
    '''

    tag = options['tag'] if 'tag' in options.keys() else ''
    padding = options['padding'] if 'padding' in options.keys() else 3
    rsw = options['remove_stopwords'] if 'remove_stopwords' in options.keys() else False
    noise = options['noise'] if 'noise' in options else False
    
    try:
        options['version']
    except:
        print("Error: algorithm version required. options = {version:<str>}")

    return_list = list()
    for section in data:
        
        scan_options = {'padding':padding,'remove_stopwords':rsw}
        features = scan(pattern,  section['text'], scan_options)
        for feature in features:
            return_list.append({
                'section_title': section['section_title'],
                'feature': feature,
                'padding': padding,
                'pattern': pattern,
                'tag': tag,
                'version': options['version'],
                'remove_stopword': rsw,
            })

    return return_list


def readJSON(path, options={}):

    f = open(path)
    data = json.load(f)

    return extract(data, cleaned_label, options)


def main():
    path = argv[1]
    pattern = argv[2]
    padding = int(argv[3])

    f = open(path)
    data = json.load(f)

    options={
        'tag':split(path)[1],
        'padding': padding
    }

    result = extract(data, pattern, options)
    print(json.dumps(result))


if __name__=='__main__':
    main()
    