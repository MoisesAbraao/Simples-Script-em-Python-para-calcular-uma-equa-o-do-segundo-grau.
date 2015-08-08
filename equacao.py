# -*- coding: utf-8 -*-

from math import sqrt

a = input("Informe o valor de A:")
b = input("Informe o valor de B:")
c = input("Informe o valor de C:")

if a == 0 or b == 0:
	print "Essa não pode ser uma equação do segundo grau!"
else:
	delta = (b * b) - (4 * a * c)
	if delta < 0 or delta == 0:
		print "Delta é negativo, então a equação não tem solução!"
	else:
		root = sqrt(delta)

		x1 = (-b + root)/2*a
		x2 = (-b - root)/2*a

		print delta
		print  x1
		print  x2
