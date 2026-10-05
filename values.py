columns = ['length', 'weight', 'tempeture']

dictionary = {'k':1000, 'm':1/1000, 's':1}


def translate(f, code='st'):
        if len(code) < 2:
                code = 'st'
        if f[-1] != code[-1] and code != 'st':
                return 'Mistake, wrong operands'

        num = ''
        for i in f:
                if i not in '0123456789':
                        if i in dictionary.keys():
                                return float(num)*dictionary[i]/dictionary[code[0]]
                else:
                        num += i

        return num
print(translate('1024420'))