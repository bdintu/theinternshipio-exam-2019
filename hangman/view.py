class View:

    def displayCategory(category):
        print('Select Category:')
        cat = ''.join(['\t' + str(i) + ': ' + category[i] + '\n' for i in range(category.__len__())])
        print(cat)
        print('-'*20)

    def displayHint(hint, cur_index):
        print()
        print('No.{0} of {1}, Hint: {2}'.format(cur_index[0] +1, cur_index[1], hint))
        print()

    def displayAskWord(askword, score, wrong_guess, char, wrong):
        print(askword, end='')
        if wrong:
            print(' score {0}, remaining wrong guess {1}'.format(score, wrong_guess))
        else:
            print(' score {0}, remaining wrong guess {1}, wrong guessed: {2}'.format(score, wrong_guess, char))

    def displayBye(score):
        print()
        print('score {0}.'.format(score))
        print()
        print('bye')
