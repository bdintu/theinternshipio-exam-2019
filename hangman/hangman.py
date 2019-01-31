from data import Data
from game import Game


class Hangman:

    def __init__(self, data_path):
        data = Data(data_path)
        self._game = Game(data)

        self._char = ''
        self._wrong = True

    def getch(self):
        self._char = ''

        while not self._char:
            try:
                self._char = input('>> ')[0]
            except IndexError:
                continue

    def run(self):
        self._game.displayCategory()        
        category_id = self._game.inputCategory()
        self._game.selectCategory(category_id)

        while not self._game.isEndGame():
            if self._game.isWordPass():
                self._game.genWord()
                self._game.displayHint()

            self._game.displayAskWord(self._char, self._wrong)
            self.getch()
            
            wrong = self._game.checkAskWord(self._char)

        self._game.displayBye()


if __name__ == '__main__':

    data_path = 'data.json'
    hangman = Hangman(data_path)
    hangman.run()
