# 1.Upewnij się czy dobrze rozumiesz jak działa kopiowanie obiektów.. np lst. Jeśli masz wątpliwości wróć tam i siedź tam aż załapiesz co tam się dzieje!!!
import copy
lista = [1, 3]

lista2 = lista

print(lista2)
print(lista)

lista.append(2)
print(lista2)
print(lista)

print("###################")

lista3 = [1 , 3]
lista4 = copy.copy(lista3)

print(lista3)
print(lista4)

lista3.append(2)
print(lista3)
print(lista4)

print("###################")

lista3 = [1 , 3]
lista4 = copy.deepcopy(lista3)

print(lista3)
print(lista4)

lista3.append(2)
print(lista3)
print(lista4)