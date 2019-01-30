import random

from word import Word


class Category:

    def __init__(self, category=None):
        self._category = category
        self._nums_shuffle = []

        self._initialCategoty()

    def _initialCategoty(self):
        self._random()

    def _random(self):
        end = self._category.__len__()
        self._nums_shuffle = [i for i in range(end)]
        random.shuffle(self._nums_shuffle)

    def __iter__(self):
        for i in self._nums_shuffle:
            category = self._category[i]
            yield Word(category['word'], category['hint'])
