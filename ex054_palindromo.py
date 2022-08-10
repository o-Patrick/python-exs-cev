# 54. Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

lineLen = 50										# terminal line interface length
print('\n{0}'.format('=' * lineLen))		# terminal first line interface

frase = str(input('| Digite uma frase: ')).strip().upper().split()
junto = ''.join(frase)
inverso = junto[::-1]

print('{0}'.format('-' * lineLen))			# terminal middle line interface

print('| Inversão: {0}'.format(inverso))

print('{0}'.format('-' * lineLen))			# terminal middle line interface

if junto == inverso:
	print('| A frase é um palíndromo!')
else:
	print('| A frase não é um palíndromo!')

print('{0}\n'.format('=' * lineLen))		# terminal last line interface

''' # usando for
lineLen = 50										# terminal line interface length
print('\n{0}'.format('=' * lineLen))		# terminal first line interface

frase    = input('| Digite uma frase: ').strip().upper().split()
junto    = ''.join(frase)
inverso  = ''

print('{0}'.format('-' * lineLen))			# terminal middle line interface

for letra in range(len(junto) - 1, -1, -1):
	inverso += junto[letra]
print('| Inversão: {0}'.format(inverso))

print('{0}'.format('-' * lineLen))			# terminal middle line interface

if junto == inverso:
	print('| A frase é um palíndromo!')
else:
	print('| A frase não é um palíndromo!')

print('{0}\n'.format('=' * lineLen))		# terminal last line interface
'''
