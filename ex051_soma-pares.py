# 51. Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

lineLen = 50										# terminal line interface length
print('\n{0}'.format('=' * lineLen))		# terminal first line interface

soma = 0
for i in range(0,6):
	num = int(input('{0:^{1}}'.format('| Insira um número inteiro: ', lineLen-3)))
	if num % 2 == 0:
		soma += num

print('{0}'.format('-' * lineLen))			# terminal middle line interface

print('{0:^{1}}'.format('Soma dos pares: {0}', lineLen).format(soma))

print('{0}\n'.format('=' * lineLen))		# terminal last line interface

''' # tentativa com arrays e randint
from random import randint

lineLen = 50										# terminal line interface length
print('\n{0}'.format('=' * lineLen))		# terminal first line interface

nums = []
soma = 0
for i in range(0,5):		# povoa o vetor e realiza a soma
	nums[i] = randint(0,9)
	soma += nums[i]

print('{0}'.format(nums[0]), end='')		# exibe o 1º valor do vetor

for i in range(1, 4):
	print(' + {0} + '.format(nums[i]), end='')		# exibe até o penúltimo valor do vetor

print('{0} = {1}'.format(nums[len(nums)], soma))		# exibe o ultimo valor do vetor e a soma

print('{0}\n'.format('=' * lineLen))		# terminal last line interface
'''
