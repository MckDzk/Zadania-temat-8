
# 5.Wygeneruj 3 listy korzystając z nowo poznanej metody. (sam wymyśl parametry).

from random import randint

lista = [randint(0,10)]
lista2 = copy.copy(lista)
lista3 = copy.deepcopy(lista2)

print(lista)
print(lista2)
print(lista3)
