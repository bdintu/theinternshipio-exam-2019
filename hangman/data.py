import os
import sys
import json


class Data:

    def __init__(self, data_path='data/'):
        self._data_path = data_path
        self._data = {}

        self._loadPath()

    def _loadPath(self):
        listdir = os.listdir(self._data_path)
        
        if listdir.__len__() <2:
            print('dataset < 2 file')
            sys.exit(1)

        for filename in listdir:
            path = os.path.join(self._data_path, filename)
            self._loadFile(path)

    def _loadFile(self, path):
        try:
            with open(path) as fp:
                self._data.update(json.loads(fp.read()))
        except json.decoder.JSONDecodeError:
            print('JSONDecodeError')
            sys.exit(1)

    def getHeadCategorys(self):
        return list(self._data.keys())

    def getCategory(self, category):
        return self._data[category]

    def __str__(self):
        return str(self._data)
