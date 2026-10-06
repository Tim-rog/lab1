from .values import translate
#калькулятор


dict = ['*', '%', '/', '+', '-']
pref = ['+', '-']
borders = ['(', ')']
prioret = {'0':['(', ')'], '1':['+', '-'], '2':['*', '/', '%']}


#определяет приорететность оператора
def find(op):
    for i in range(0, 3):
        if op in prioret[f'{i}']:
            return i


def sort_1(c):
    '''
    :param c: строка
    :return: массив, содержащий float(операнды) и str(операторы)
    '''
    s = '+'+c.replace(' ', '')
    res = []
    n = ''
    for i in range(1, len(s)):
        if s[i] not in dict+borders or (s[i-1] in dict and s[i] in pref):
            n += s[i]
        else:
            if n!='':
                res.append(float(translate(n)))
            res.append(s[i])
            n=''
    if n!= '':
        res.append(float(translate(n)))
    res = ['('] + res + [')']
    return res


#принимает массив, на выход отдаёт массив, состоящий из содержимого самых внутренних скобок
def box(m):
    res = []
    for x in reversed(m):
        if x != '(':
            res.append(x)
        else:
            break
    return res


def sort_station(s):
    '''
    функция, вдохновлённая сортировочной станцией Дейтла, использует те же принципы
    :param s: массив из операторов и операндов
    :return:  массив в посфтиксном формате
    '''
    c = sort_1(s)
    steck = []
    res = []
    for el in c:
        if el == '(':
            steck.append(el)
        elif el == ')':
            for x in box(steck):
                res.append(x)
                steck.pop()
            steck.pop()
        elif el in dict:
            while True:
                if len(steck) == 0 or find(el) > find(steck[-1]):
                    steck.append(el)
                    break
                else:
                    res.append(steck.pop())
        else:
            res.append(el)
    steck.reverse()
    res += steck
    return res


#словарь с функциеями
math = {'*':lambda ex: ex[0]*ex[1], '+':lambda ex: ex[0]+ex[1], '/':lambda ex: ex[0]/ex[1],
        '-': lambda ex: ex[0]-ex[1], '%':lambda ex: ex[0]%ex[1]}


def calc(s_detl):
    '''вычеслитель
     принимает массив в посфтиксном формате
     возвращает результат float'''
    s = s_detl
    while len(s)>1:
        for i in range(0, len(s)):
            if s[i] in dict:                                              #если встречает оператор
                s = s[0:i-2]+[math[s[i]]([s[i-2], s[i-1]])]+s[i+1:len(s)] #берёт всё содержимое массива до оператора и двух операндов,
                                                                        # складывает с [результатт операции на двух ближайших опернадах] и с оставишмя массиавом
                break
    return s[0]


def calculate(ex: str) -> float:
    '''Удобный запуск'''
    res = sort_station(ex)
    return calc(res)