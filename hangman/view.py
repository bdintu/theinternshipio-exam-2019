class View:

    def displayCategory(category):
        print('Select Category:')
        cat = ''.join(['\t' + str(i) + ': ' + category[i] + '\n' for i in range(category.__len__())])
        print(cat)
        print('-'*20)
