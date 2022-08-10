# 52. Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética). No final, mostre os 10 primeiros termos dessa progressão.

lineLen = 50										# terminal line interface length
print('\n{0}'.format('=' * lineLen))		# terminal first line interface

pri = int(input('| Primeiro termo: '))
raz = int(input('| Razão: '))
dec = pri + (10 - 1) * raz						# décimo termo

print('{0}'.format('-' * lineLen))			# terminal middle line interface

print('| ', end='')								# pipe de interface no início da PA
for c in range(pri, dec, raz):
	print('{0}'.format(c), end='-> ')		# mostra a pa
print('Acabou!')									# marca o fim

print('{0}\n'.format('=' * lineLen))		# terminal last line interface

''' # só funciona com PA crescente
lineLen = 50										# terminal line interface length
print('\n{0}'.format('=' * lineLen))		# terminal first line interface

ini = int(input('| Insira o primeiro termo da PA: '))
raz = int(input('| Insira a razão da PA: '))
pa = ini + raz		# termo mais recente da PA

print('{0}'.format('-' * lineLen))			# terminal middle line interface

print('| ', end='')								# pipe de interface no início da PA
for c in range(0, 8):
	print('{0} ->'.format(pa), end=' ')		# mostra até o penúltimo termo
	pa += raz										# soma o último termo com a razão
print('{0}'.format(pa), end=' ')				# último termo sem a seta depois

print('\n{0}\n'.format('=' * lineLen))		# terminal last line interface
'''
