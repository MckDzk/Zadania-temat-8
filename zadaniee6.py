from random import randint

def zadanie6():
    lista = []
    while len(lista) != 10:
        inp = randint(1,10)
        if inp % 2 != 0 and inp % 3 != 0 and inp % 4 != 0 and inp % 5 != 0 and inp % 6 != 0 and inp % 7 != 0 and inp % 8 != 0 and inp % 9 != 0 and inp % 10  != 0 and inp % 11 != 0 and inp % 22 != 0 and inp % 33 != 0 and inp % 44 != 0 and inp % 55 != 0 and inp % 66 != 0 and inp % 77 != 0 and inp % 88 != 0:
            lista.append(inp)
    print(lista)

zadanie6()