# 13. Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt

num = int(input('Number: '))
print('{0} times two is {1}'.format(num, num*2))
print('{0} times three is {1}'.format(num, num*3))
print('{0} square root is {1:.2f}'.format(num, sqrt(num)))

# OU import math
#	  math.sqrt(num)
# OU num ** (1/2)
# OU pow(num, (1/2))
