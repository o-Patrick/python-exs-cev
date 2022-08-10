# 36. Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

lineLen = 40		# interface lenght

print('\n{0:=^{1}}'.format('Triangle', lineLen))		# interface

len1 = float(input('| Insert the 1º lenght: '))
len2 = float(input('| Insert the 2º lenght: '))
len3 = float(input('| Insert the 3º lenght: '))

print('-' * lineLen)		# interface

if (len1 + len2) >= len3 and (len1 + len3) >= len2 and (len2 + len3) >= len1:
	print('| The triangle EXISTS.')
else:
	print('| The triangle DOES NOT exist.')

print('{0}\n'.format('=' * lineLen))		# interface