# 17. Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc

num = float(input('\nInsert the number: '))
print('{0} as an integer is {1}\n'.format(num, trunc(num)))

''' OU
num = float(input('\nInsert the number: '))
print('{0} as an integer is {1}\n'.format(num, int(num)))
'''
