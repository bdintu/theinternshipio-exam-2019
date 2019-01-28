import sys
import json


class Data:

    def __init__(self, data_path=""):
        self._filename = data_path
        self._data = None

        self.loads()

    def loads(self):
        try:
            with open(self._filename) as fp:
                self._data = json.loads(fp.read())
        except FileNotFoundError:
            print('FileNotFoundError')
            sys.exit(1)
        except json.decoder.JSONDecodeError:
            print('JSONDecodeError')
            sys.exit(1)

    def getHeadCategorys(self):
        return list(self._data.keys())

    def getCategory(self, category):
        return self._data[category]

    def __str__(self):
        return str(self._data)
