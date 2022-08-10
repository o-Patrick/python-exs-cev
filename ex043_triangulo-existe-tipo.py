# 43. Refaça o exercício 36 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# 		- Equilátero: todos os lados iguais;
# 		- Isósceles: dois lados iguais;
# 		- Escaleno: todos os lados diferentes.

lineLen = 50		# terminal line interface length
print('\n{0}'.format('=' * lineLen))		# terminal first line interface

comp1 = float(input('| Insira o comprimento do 1º lado: '))
comp2 = float(input('| Insira o comprimento do 2º lado: '))
comp3 = float(input('| Insira o comprimento do 3º lado: '))

print('{0}'.format('-' * lineLen))		# terminal middle line interface

if (comp1 + comp2) < comp3 or (comp2 + comp3) < comp1 or (comp3 + comp1) < comp2:
	print('|| Este triângulo não existe!')
else:
	if comp1 == comp2 and comp1 == comp3:
		tipo = 'equilátero'
	elif comp1 == comp2 or comp1 == comp3 or comp2 == comp3:
		tipo = 'isósceles'
	else:
		tipo = 'escaleno'
	print('|| Este triângulo {0} existe!'.format(tipo))

print('{0}\n'.format('=' * lineLen))		# terminal last line interface