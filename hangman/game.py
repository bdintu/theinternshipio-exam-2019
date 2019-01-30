from data import Data
from category import Category
from word import Word
from score import Score
from view import View


class Game:

    def __init__(self, data):
        self._data = data
        self._score = Score()

        self._category = None
        self._iter_category = None
        self._word = None

    def displayCategory(self):
        cat = self._data.getHeadCategorys()
        View.displayCategory(cat)

    def selectCategory(self, category_id=0):
        head = self._data.getHeadCategorys()
        category = self._data.getCategory(head[category_id])
        self._category = Category(category)
        self._iter_category = iter(self._category)

    def inputCategory(self):
        category_id = input("select: ")
        try:
            category_id = int(category_id)
        except ValueError:
            print('press key integer')
            self.inputCategory()

        head = self._data.getHeadCategorys()
        if not category_id in range(head.__len__()):
            print('press key in range')
            self.inputCategory()

        return category_id

    def genWord(self):
        self._word = next(self._iter_category)

    def displayHint(self):
        View.displayHint(self._word.getHint())
        
    def displayAskWord(self, char='', wrong=False):
        askword = self._word.getAskWord()
        score = self._score.getScore()
        wrong_guess  = self._score.getWrongGuess()
        View.displayAskWord(askword, score, wrong_guess, char, wrong)

    def checkAskWord(self, char=''):
        hint_word = self._word.checkAskWord(char)
        if hint_word:
            self._score.addScore()
            return True
        elif self._score.getScore() == 0:
            self._score.delWrongGuess()
        else:
            self._score.delScore()

        return False

    def isEndGame(self):
        return self._score.getWrongGuess() == 0

    def isWordPass(self):
        return self._word.isPass()
