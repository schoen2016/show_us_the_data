import json
from os.path import isfile

class Data:
    def __init__(path=''):
        self.path = path
        self.path_type = pathType(path)
        self.dtype = 'dict'
        self.data = []
    
    def __readOptions(self, options):
        self.dtype = option['dtype'] if option['dtype'] else self.dtype

    def __readJSON(self):
        f = open(path)
        self.data = json.load(f)

    def __target(self, path):
        return 'file' if isfile(path) else 'directory'
        
    def readJson(self, options):
        self.__readOptions(options)

        if self.dtype == 'dict':
            if self.path_type == 'file':
                return __readJSON()