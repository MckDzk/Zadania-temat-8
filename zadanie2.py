import copy

# 2.Funkcję która może przyjąć nieskończenie wiele argumentów a następnie zwraca średnią arytmetyczną.

lista = []
lista2 = copy.copy(lista)

def xxx():
	while True:
		l = float(input())
		if l == 0:
			break
		lista2.append(l)
		
	





xxx()

sr = sum(lista2)/len(lista2)

print(sr)