# 55. Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

lineLen = 50										# terminal line interface length
print('\n{0}'.format('=' * lineLen))		# terminal first line interface

anoAt = date.today().year		# ano atual
maior = 0							# pessoas em maioridade

for i in range(1, 8):
	nasc  = int(input('| Em que ano a {0}ª pessoas nasceu? '.format(i)))
	idade = anoAt - nasc
	if idade >= 18:
		maior += 1

print('{0}'.format('-' * lineLen))			# terminal middle line interface

print('| {0} das pessoas são maiores de idade.'.format(maior))

print('{0}\n'.format('=' * lineLen))		# terminal last line interface
