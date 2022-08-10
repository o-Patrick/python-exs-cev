# 48. Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

lineLen = 147										# terminal line interface length
print('\n{0}'.format('=' * lineLen))		# terminal first line interface

print('{0:^{1}}'.format('Olá , bela dama... Aceitas estes pares?', lineLen))

print('{0}'.format('-' * lineLen))			# terminal middle line interface

print(' ', end='')		# espaço no início da contagem

for i in range(2, 51, 2):		# como os números são controlados, desta forma a quantidade de iterações é a metade comparando ao for comentado
	if i % 2 == 0:
		print(i, end='... ')

# OU for i in range(1, 51):
# 	if i % 2 == 0:
# 		print(i, end='... ')

print('\n{0}\n'.format('=' * lineLen))		# terminal last line interface
