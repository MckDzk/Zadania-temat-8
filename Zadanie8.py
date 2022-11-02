# 8.Funkcja która skopiuje i zwrócił listę w której występuje największy element.
import copy

def xxx():
	lista1 = [1, 3, 4, 5, 2, 60]
	lista2 = [3, 4, 8, 3, 10, 1]
 
	print(lista1)
	print(lista2)
	


	if max(lista1) > max(lista2):
		print(copy.copy(lista1))

	if max(lista2) > max(lista1):
		print(copy.copy(lista2))

xxx()