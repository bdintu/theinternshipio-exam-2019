import random

from word import Word


class Category:

    def __init__(self, category=None, N=5):
        self._category = category
        self._N = N
        self._i = 0
        self._nums_shuffle = []

        self._initialCategoty()
        self._cutNWord()

    def _initialCategoty(self):
        self._random()

    def _random(self):
        end = self._category.__len__()
        self._nums_shuffle = [i for i in range(end)]
        random.shuffle(self._nums_shuffle)

    def _cutNWord(self):
        self._nums_shuffle = self._nums_shuffle[:self._N]
        self._N = self._nums_shuffle.__len__()

    def __iter__(self):
        for i in self._nums_shuffle:
            category = self._category[i]
            yield Word(category['word'], category['hint'])
            
            self._i = self._i + 1

    def isStop(self):
        return self._i == self._N

    def getCurIndex(self):
        return (self._i, self._N)
