from random import randint

def zadanie7():
    lista = []
    while len(lista) != 10:
        inp = randint(1,10)
        if inp % 2 != 0 and inp % 3 != 0 and inp % 5 != 0 and inp % 7 != 0 and inp % 11 != 0 and inp % 13 != 0 and inp % 17 != 0 and inp % 19 != 0 and inp % 23  != 0 and inp % 29 != 0 and inp % 31 != 0 and inp % 37 != 0 and inp % 41 != 0:
            lista.append(inp)
    print(lista)
