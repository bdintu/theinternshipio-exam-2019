from data import Data
from game import Game


class Hangman:

    def __init__(self, data_path):
        data = Data(data_path)
        self._game = Game(data)

    def run(self):
        self._game.displayCategory()        
        self._game.selectCategory()


if __name__ == '__main__':

    data_path = 'data.json'
    hangman = Hangman(data_path)
    hangman.run()
