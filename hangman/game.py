import random

from data import Data
from view import View


class Game:

    def __init__(self, data):
        self._data = data

        self.category = None
        self.seed = 4848
        self.nums_shuffle = []

    def displayCategory(self):
        cat = self._data.getHeadCategorys()
        View.displayCategory(cat)

    def selectCategory(self):
        cat_id = input("select: ")
        try:
            cat_id = int(cat_id)
        except ValueError:
            print('press key integer')
            self.selectCategory()

        head = self._data.getHeadCategorys()
        if cat_id in range(head.__len__()):
            self.category = self._data.getCategory(head[cat_id])
        else:
            print('press key in range')
            self.selectCategory()


    def _random(self):
        self._nums_shuffle = [i for i in range()]
        random.shuffle(self._nums_shuffle)


