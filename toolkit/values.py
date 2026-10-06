dictionary = {'k':1000, 'm':1/1000, 'c':1/100, 's':1}
dict_temp = {'K':lambda x: x-273.15, 'F': lambda x: (x-32)*5/9, 'st': lambda x: x, 'C':lambda x: x,
             '1/K':lambda x: x+273.15, '1/F': lambda x: x*9/5-32, '1/st': lambda x: x}



def translate(f:str, code='st')->float:
        '''
        перевод в станлурнтную, либо заданную сичтему счислений, если на вход поданно просто число, возвращает просто число
        :param f: строка с числом
        :param code: куда переводить
        :return: переведённое число
        '''
        if all([(x in '+-0123456789') for x in f]):
                return float(f)
        elif code[-1] != f[-1]:
                return 'Нельза переводить разные физические велечины'
        if (len(code) < 2 and code.upper() != code) or code=='C':
                code = 'st'
        if f[-2] in '+-0123456789' and f[-1] not in '+-0123456789' and f[-1].upper()!=f[-1]:
                f = f[:-1]+f's{f[-1]}'
        num = ''
        for i in f:
                if i not in '+-0123456789':
                        if i in dictionary.keys():
                                return float(num)*dictionary[i]/dictionary[code[0]]
                        elif i in dict_temp.keys():
                                return dict_temp[f'1/{code}'](dict_temp[i](float(num)))
                else:
                        num += i