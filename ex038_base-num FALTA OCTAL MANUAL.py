# 38. Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

# lineLen = 80		# terminal interface lines length
# print('\n{}'.format('=' * lineLen))

# num = int(input('| Insert an integer to convert: '))
# radix = int(input('| Convert to:\n| [1] Binary\n| [2] Hexadecimal\n| [3] Octal\n| Type the number: '))

# if radix == 1 or radix == 2 or radix == 3:
# 	if radix == 1 or radix == 2:
# 		# Converts to binary. Both binary and hexadecimal use this value
# 		bin = ''

# 		if num >= 128:
# 			num -= 128
# 			bin = '1'
# 		else:
# 			bin = '0'

# 		if num >= 64:
# 			num -= 64
# 			bin += '1'
# 		else:
# 			bin += '0'

# 		if num >= 32:
# 			num -= 32
# 			bin += '1'
# 		else:
# 			bin += '0'

# 		if num >= 16:
# 			num -= 16
# 			bin += '1'
# 		else:
# 			bin += '0'

# 		if num >= 8:
# 			num -= 8
# 			bin += '1'
# 		else:
# 			bin += '0'

# 		if num >= 4:
# 			num -= 4
# 			bin += '1'
# 		else:
# 			bin += '0'

# 		if num >= 2:
# 			num -= 2
# 			bin += '1'
# 		else:
# 			bin += '0'

# 		if num >= 1:
# 			num -= 1
# 			bin += '1'
# 		else:
# 			bin += '0'

# 	if radix == 1:		# shows binary
# 		prod = bin

# 	elif radix == 2:		# to hex
# 		hex0 = 0		# first half
# 		hex1 = 0		# second half
# 		if bin[0] == '1':
# 			hex0 = 8
# 		if bin[1] == '1':
# 			hex0 += 4
# 		if bin[2] == '1':
# 			hex0 += 2
# 		if bin[3] == '1':
# 			hex0 += 1
# 		if bin[4] == '1':
# 			hex1 = 8
# 		if bin[5] == '1':
# 			hex1 += 4
# 		if bin[6] == '1':
# 			hex1 += 2
# 		if bin[7] == '1':
# 			hex1 += 1
# 		if hex0 > 9 or hex1 > 9:
# 			# first half
# 			if hex0 == 10:
# 				hex0 = 'A'
# 			elif hex0 == 11:
# 				hex0 = 'B'
# 			elif hex0 == 12:
# 				hex0 = 'C'
# 			elif hex0 == 13:
# 				hex0 = 'D'
# 			elif hex0 == 14:
# 				hex0 = 'E'
# 			elif hex0 == 15:
# 				hex0 = 'F'

# 			# second half
# 			if hex1 == 10:
# 				hex1 = 'A'
# 			elif hex1 == 11:
# 				hex1 = 'B'
# 			elif hex1 == 12:
# 				hex1 = 'C'
# 			elif hex1 == 13:
# 				hex1 = 'D'
# 			elif hex1 == 14:
# 				hex1 = 'E'
# 			elif hex1 == 15:
# 				hex1 = 'F'
# 		prod = str(hex0) + str(hex1)

# # elif radix == 3:		# to octal
# # 	#

# else:		# error
# 	prod = '[E R R O R] Please restart and insert 1, 2 or 3 . . .'

# print('{0}'.format('-' * lineLen))
# print('| Product: {}'.format(prod))
# print('{0}\n'.format('=' * lineLen))

# guanabara
num = int(input('\nDigite um número inteiro: '))
print("""Escolha uma das bases para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal""")
opcao = int(input('Sua opção: '))
if opcao == 1:
	print('{} convertido para  BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
	print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
	print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
	print('Opção inválida, tente novamente.')
# nos resultados, sem [2:] nos formats: 0b == binário; 0o == octal; 0x == hexadecimal;

print('\n')