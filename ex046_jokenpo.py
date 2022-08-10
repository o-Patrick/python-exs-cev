# 46. Crie um programa que faça o computador jogar Jokenpô (pedra, papel e tesoura) com você.

lineLen = 60		# terminal line interface length
print('\n{0}'.format('=' * lineLen))		# terminal first line interface

from random import randint

jokenpo = ['pedra', 'papel', 'tesoura']
pc = randint(0, 2)
user = int(input('''| [1] Pedra
| [2] Papel
| [3] Tesoura
| Escolha o número: '''))

print('{0}'.format('-' * lineLen))		# terminal middle line interface

if user < 1 or user > 3:
	print('|| ERRO! Favor favor inserir o número corretamente!')
else:
	# pc
	if pc == 0:
		pc = 'pedra'
	elif pc == 1:
		pc = 'papel'
	elif pc == 2:
		pc = 'tesoura'

	# user
	if user == 1:
		user = 'pedra'
	elif user == 2:
		user = 'papel'
	elif user == 3:
		user = 'tesoura'

	print('|| Usuário: {0}   VS   Computador: {1}'.format(user, pc))		# jogadas

	if user == pc:
		print('|| Empate!')
	else:
		if user == 'pedra' and pc == 'papel':
			venceu = 'Computador'
		elif user == 'pedra' and pc == 'tesoura':
			venceu = 'Usuário'
		elif user == 'papel' and pc == 'pedra':
			venceu = 'Usuário'
		elif user == 'papel' and pc == 'tesoura':
			venceu = 'Computador'
		elif user == 'tesoura' and pc == 'papel':
			venceu = 'Usuário'
		elif user == 'tesoura' and pc == 'pedra':
			venceu = 'Computador'

		print('|| {0} venceu!'.format(venceu))

print('{0}\n'.format('=' * lineLen))		# terminal last line interface