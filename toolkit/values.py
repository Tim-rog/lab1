dictionary = {'k':1000, 'm':1/1000, 'c':1/100, '':1}
dict_temp = {'k':lambda x: x-273.15, 'f': lambda x: (x-32)*5/9, '': lambda x: x, 'c':lambda x: x,
             '1/k':lambda x: x+273.15, '1/f': lambda x: x*9/5+32, '1/': lambda x: x, '1/c':lambda x: x}


def translate(f:str, code='st')->str:
        '''
        перевод в станлурнтную, либо заданную сичтему счислений, если на вход поданно просто число, возвращает просто число
        :param f: строка с числом
        :param code: куда переводить
        :return: переведённое число
        '''
        f = f.lower().replace(' ', '')
        code = code.lower().replace(' ', '')
        num = ''
        val = ''
        for x in f:
                nums = True
                if x in '+-0123456789.':
                        if not nums:
                                return 'Неправильнный ввод переводимого'
                        num += x
                else:
                        nums = False
                        val += x

        if val == '':
                return num
        if code == 'st':
                code=val[-1]
        if val == code:
                return num

        cd = ''
        cd_val = ''
        for x in code:
                if cd+x not in dictionary:
                        break
                cd+=x
        for x in val:
                if cd_val+x not in dictionary:
                        break
                cd_val+=x
        cd = cd.replace(code,'')
        cd_val = cd_val.replace(val, '')
        print(cd, code, cd_val, val)
        if val.replace(cd_val, '', 1) != code.replace(cd, '', 1) and not (code[-1] in dict_temp and val[-1] in dict_temp):
                return 'Нельза переводить разные физические велечины'

        if code in dict_temp and val in dict_temp:
                if dict_temp['1/k'](dict_temp[cd_val](float(num))) == 0:
                        return 'Температура ниже абсолютного нуля'
                return str(dict_temp[f'1/{code}'](dict_temp[val](float(num))))
        else:
                return str(dictionary[cd_val]*float(num)/dictionary[cd])