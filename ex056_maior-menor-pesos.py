# 56. Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor dos pesos.

lineLen = 50										# terminal line interface length
print('\n{0}'.format('=' * lineLen))		# terminal first line interface

maior = 0
menor = 0
for i in range(1, 6):
	peso  = float(input('| Qual é o {0}ª peso? '.format(i)))
	if i == 1:
		maior = peso
		menor = peso
	else:
		if peso > maior:
			maior = peso
		if peso < menor:
			menor = peso

print('{0}'.format('-' * lineLen))			# terminal middle line interface

print('''O maior peso é: {0:.2f}
O menor peso é: {1:.2f}'''.format(maior, menor))

print('{0}\n'.format('=' * lineLen))		# terminal last line interface
