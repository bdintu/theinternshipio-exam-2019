class View:

    def displayCategory(category):
        print('Select Category:')
        cat = ''.join(['\t' + str(i) + ': ' + category[i] + '\n' for i in range(category.__len__())])
        print(cat)
        print('-'*20)

    def displayHint(hint):
        print()
        print('Hint:', '"'+hint+'"')

    def displayAskWord(askword, score, wrong_guess, char, wrong):
        print(askword, end='')
        if wrong:
            print(' score {0}, remaining wrong guess {1}'.format(score, wrong_guess))
        else:
            print(' score {0}, remaining wrong guess {1}, wrong guessed: {2}'.format(score, wrong_guess, char))
