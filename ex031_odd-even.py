# 31. Crie um programa que mostre na tela se um número inteiro é par ou ímpar.

num = int(input('\n| Insert an integer: '))
if num % 2 != 0:
	print('| The number {0} is ODD.\n'.format(num))
else:
	if num % 2 == 0 and num == 0:
		print('| The number {0} is NULL.\n'.format(num))
	else:
		print('| The number {0} is EVEN.\n'.format(num))
