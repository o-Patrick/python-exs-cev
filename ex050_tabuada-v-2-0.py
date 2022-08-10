# 50. Refaça o exercício 7, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

lineLen = 50										# terminal line interface length
print('\n{0}'.format('=' * lineLen))		# terminal first line interface

num = int(input('| Escolha uma tabuada: '))

print('{0}'.format('-' * lineLen))			# terminal middle line interface

for i in range(0, 11):
	print('| {0} * {1} = {2}'.format(num, i, num*i))

print('{0}\n'.format('=' * lineLen))		# terminal last line interface
