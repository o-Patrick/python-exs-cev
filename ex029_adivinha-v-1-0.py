# 29. Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
# OU from random import randrange
from time import sleep

print('\n| I will guess an integer between 0 and 5 . . .')
num = randint(0, 6)		# random number generator

guess = int(input('\n| Guess which number computer has chosen: '))

print('\n| P r o c e s s i n g . . .')
sleep(3)
print('| Computer choice: {0}'.format(num))
print('| Congratulations, you win!\n') if guess == num else print('| Oh no! Try again!\n')
