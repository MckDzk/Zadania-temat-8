# 3.Funkcja co prosi o podanie od użytkownika n, min, max i generuje listę/tablice o wielkości n, o losowych wartościach max i min. 



from random import randint


def genrand(n, min, max):
	lst = [None] * n
	i = 0
	while i != n:
		lst[i] = randint(min,max)
		print(lst[i])
		i = i + 1
	


genrand(5,2,7)



