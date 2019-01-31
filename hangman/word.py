import random


class Word:

    def __init__(self, word='', hint=''):
        self._word = word
        self._hint = hint
        self._askword = []
        self._dict = {}

        self._genDict()
        self._genAskWord()

#        if self._word:
#            self._cut1Word()

    def _genDict(self):
        for i in range(self._word.__len__()):
            index = int(i)
            key = self._word[i]
            if key.isalpha():
                if key in self._dict:
                    self._dict[key].append(index)
                else:
                    self._dict[key] = [index]

    def _genAskWord(self):
        self._askword = [i if not i.isalpha() else '_' for i in self._word]

    def _cut1Word(self):
        if self._sumAlpha() <2:
            return

        while True:
            rand_index = random.randint(0, self._word.__len__()) -1
            char = self._word[rand_index]

            if char.isalpha():
                self._removeDict(char)
                break

    def _sumAlpha(self):
        return sum(i.isalpha() for i in self._word)

    def _cut1Word(self):
        rand_index = random.randint(0, self._word.__len__()) -1
        self._removeDict(self._word[rand_index])

    def checkAskWord(self, char):
        if char in self._dict:
            self._removeDict(char)
            return True
        else:
            return False

    def _addAskWord(self, index, char):
        self._askword[index] = char

    def _removeDict(self, char):
        if not char:
            char = self._word[index]
        
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
