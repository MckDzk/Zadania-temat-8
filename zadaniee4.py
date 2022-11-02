# 4.Funkcję która zamieni 2 wartości x i y. Zakładając że  x i y występują poza funkcją (Global).

x = 5
y = x

def zzz():
	global x
	x += 5

zzz()