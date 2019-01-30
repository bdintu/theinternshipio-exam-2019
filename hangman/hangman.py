from data import Data
from game import Game


class Hangman:

    def __init__(self, data_path):
        data = Data(data_path)
        self._game = Game(data)

    def run(self):
        self._game.displayCategory()        
        category_id = self._game.inputCategory()
        self._game.selectCategory(category_id)

        self._game.genWord()
        self._game.displayHint()

        while not self._game.isEndGame():
            if self._game.isWordPass():
                self._game.genWord()
                self._game.displayHint()
            self._game.displayAskWord()
            char = input('>')[0]
            self._game.checkAskWord(char)

if __name__ == '__main__':

    data_path = 'data.json'
    hangman = Hangman(data_path)
    hangman.run()
