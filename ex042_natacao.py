# 42. A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# 		- Até 9 anos: mirim;
# 		- Até 14 anos: infantil;
# 		- Até 19 anos: júnior;
# 		- Até 25 anos: sênior;
# 		- Acima: master.

lineLen = 50		# terminal line interface length
print('\n{0}'.format('=' * lineLen))		# terminal first line interface

from datetime import date
anoAtual = date.today().year
anoNasc  = int(input('| Ano de nascimento: '))
idade    = anoAtual - anoNasc

print('{0}'.format('-' * lineLen))		# terminal middle line interface

print('|| O atleta tem {0} anos.'.format(idade))
if idade <= 9:
	print('|| Classificação: mirim!')
elif idade <= 14:
	print('|| Classificação: infantil!')
elif idade <= 19:
	print('|| Classificação: júnior!')
else:
	print('|| Classificação: sênior!')

print('{0}\n'.format('=' * lineLen))		# terminal last line interface	