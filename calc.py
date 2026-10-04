import asyncio
from functools import *
from re import *
#калькулятор

dict = [')', '*', '%', '/', '+', '-']
prioret = {'0':['(', ')'], '1':['+', '-'], '2':['*', '/', '%']}


def find(op):
    for i in range(0, 3):
        if op in prioret[f'{i}']:
            return i


def sort_1(c):
    s = c.replace(' ', '')
    res = ['']
    n = ''
    for i in s:
        if i in dict:
            if n=='' and res[-1]!=')':
                n+=i
            else:
                if n!='':
                    res.append(int(n))
                n = ''
                res.append(i)
        elif i in ['(', ')']:
            res.append(i)
        else:
            n+=i
    if n != '':
        res.append(int(n))
    res = ['('] + res + [')']
    res.remove('')
    return res


def box(m):
    in_borders = []
    out = []
    inside=True
    for x in m:
        if x == ')':
            inside=False
            out.append(')')
        elif x == '(':
            out = out + in_borders + ['(']
            in_borders = []
        elif inside:
            in_borders.append(x)
        else:
            out.append(x)
    print('Box:', in_borders, out)
    for i in range(0, len(out)):
        if out[i] == '(' and out[i+1] == ')':
            for x in range(0, 1): out.pop(i)
            out.pop(i)
            break
    print('Box:', in_borders, out)
    return [in_borders, out]


def sort_station(s):
    c = sort_1(s)
    steck = []
    res = []
    for el in c:
        if el == '(':
            steck.append(el)
        elif el == ')':
            for x in reversed(box(steck)[0]):
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
    print(res)
    return res


math = {'*':lambda ex: ex[0]*ex[1], '+':lambda ex: ex[0]+ex[1], '/':lambda ex: ex[0]/ex[1],
        '-': lambda ex: ex[0]-ex[1], '%':lambda ex: ex[0]%ex[1]}


def calc(s_detl):
    s = s_detl
    while len(s)>1:
        for i in range(0, len(s)):
            if s[i] in dict:
                s = s[0:i-2]+[math[s[i]]([s[i-2], s[i-1]])]+s[i+1:len(s)]
                break
    return s[0]

@lru_cache(0)
def sort_station_recursion(exp, start):  # exp это маcсив, ограниченный () с двух сторон
    print(exp, start)
    steck = []
    rs = start
    in_borders, out = box(exp)
    for el in in_borders:
        if el in dict:
            while True:
                if len(steck) == 0 or find(el) > find(steck[-1]):
                    steck.append(el)
                    break
                else:
                    rs.append(steck.pop())
        else:
            rs.append(el)
    steck.reverse()
    rs += steck
    print('Recursion', rs, out)
    if len(out) > 0:
        return sort_station_recursion(out, rs)
    else:
        return rs


async def main():
    ex = input('new calculation:')
    res = sort_station(ex)
    print(calc(res))


while True:
    if __name__ == "__main__":
        asyncio.run(main())