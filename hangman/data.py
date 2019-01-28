import json

class Data:

    def __init__(self, filename=""):
        self._filename = filename
        self._data = None

    def loads(self):
        with open(self._filename) as fp:
            self._data = json.loads(fp.read())

    def getCategory(self, category):
        return self._data[category]

    def getSizeCategory(self, category):
        return self.getCategory(category).__len__()

    def getSizeCategorys(self):
        return self._data.__len__()

    def __str__(self):
        return str(self._data)
