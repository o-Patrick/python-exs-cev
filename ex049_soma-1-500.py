# 49. Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 a 500.

lineLen = 50										# terminal line interface length
print('\n{0}'.format('=' * lineLen))		# terminal first line interface

print('{0:^{1}}'.format('é ÍMPAR? é MÚLTIPLO DE 3?', lineLen))

print('{0}'.format('-' * lineLen))			# terminal middle line interface

soma = 0
for i in range(1, 501, 2):		# como os números são controlados, desta forma a quantidade de iterações é a metade comparando ao for comentado
	if i % 3 == 0:		# todo número ímpar tem resto 0 se dividido por 3
		soma += i
print('{0:^{1}}'.format('então SOMA: {0}!'.format(soma), lineLen))

print('{0}\n'.format('=' * lineLen))		# terminal last line interface
