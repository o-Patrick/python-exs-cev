# *** 47. Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 a 0, com uma pausa de 1 segundo entre eles.

from time import sleep

lineLen = 61										# terminal line interface length
print('\n{0}'.format('=' * lineLen))		# terminal first line interface

print('  * * *  R E V É I L L O N   M A C H I N E   3 0 0 0  * * *')

print('{0}'.format('-' * lineLen))			# terminal middle line interface

print('   ', end='')								# espaço no início da contagem
for i in range(10, -1, -1):
	print('{0}'.format(i), end='... ')
	sleep(.5)

print('\n{0}'.format('-' * lineLen))		# terminal middle line interface

print('{0:^{1}}'.format('! ! !  F E L I Z  N O V O  ! ! !', lineLen))

print('{0}\n'.format('=' * lineLen))		# terminal last line interface
