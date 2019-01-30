class Word:

    def __init__(self, word='', hint=''):
        self._word = word
        self._hint = hint
        self._askword = []
        self._dict = {}

        self._genDict()
        self._genAskWord()

    def _genDict(self):
        for i in range(self._word.__len__()):
            index = int(i)
            key = self._word[i]
            if key in self._dict:
                self._dict[key].append(index)
            else:
                self._dict[key] = [index]

    def _genAskWord(self):
        self._askword = list('_'*self._word.__len__())

    def checkAskWord(self, char):
        if char in self._dict:
            self._removeDict(char)
            return True
        else:
            return False

    def _addAskWord(self, index, char):
        self._askword[index] = char

    def _removeDict(self, char):
        index = self._dict[char].pop(0)
        self._addAskWord(index, char)

        if not self._dict[char]:
            self._dict.pop(char)

    def getAskWord(self):
        return ' '.join(self._askword)

    def getWord(self):
        return self._word

    def getHint(self):
        return self._hint

    def isPass(self):
        return not self._dict
