class Score:

    def __init__(self, k=15, wrong_guess=10):
        self._score = 0
        self._k = k
        self._wrong_guess = wrong_guess

    def addScore(self):
        self._score = self._score + self._k

    def delScore(self):
        self._wrong_guess = self._wrong_guess -1
        self.delWrongGuess()

    def delWrongGuess(self):
        self._score = self._score - self._k

    def __if__(self):
        return self._wrong_guess == 0

    def getScore(self):
        return self._score

    def getWrongGuess(self):
        return self._wrong_guess
