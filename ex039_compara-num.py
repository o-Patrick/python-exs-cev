# 39. Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: o primeiro valor é maior, o segundo valor é maior ou ambos são iguais.

print('\n{0}'.format('=' * 40))		# interface início
n1 = int(input('| Insira o 1º número inteiro: '))
n2 = int(input('| Insira o 2º número inteiro: '))

if n1 > n2:
	print('\n| O número {0} é maior que {1}.'.format(n1, n2))
elif n2 > n1:
	print('\n| O número {0} é maior que {1}.'.format(n2, n1))
else:
	print('\n| Os números {0} e {1} são iguais.'.format(n1, n2))
print('{0}\n'.format('=' * 40))		# interface fim
