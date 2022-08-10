# 53. Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

lineLen = 70										# terminal line interface length
print('\n{0}'.format('=' * lineLen))		# terminal first line interface

num = int(input('| Insira um número inteiro: '))
div = 0		# quantidade de número pelos quais num é divisível

print('{0}'.format('-' * lineLen))			# terminal middle line interface

for i in range(1, num+1):
	if num % i == 0:								# é divisor
		print('\033[32m| {0}\033[m'.format(i), end=' ')
		div += 1
	else:												# não é divisor
		print('\033[31m| {0}\033[m'.format(i), end=' ')
print()												# quebra a linha para a condicional abaixo

if div > 2:
	print('| {0} NÃO é primo'.format(num))
else:
	print('| {0} É PRIMO'.format(num))

print('{0}\n'.format('=' * lineLen))		# terminal last line interface
