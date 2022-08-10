# 23. Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiúsculas, o nome com todas minúsculas, quantas letras ao todo (sem considerar espaços) e quantas letras tem o primeiro nome.

lineLen = 50	 # separator lines length

print('{0}{1}'.format('\n', '=' * lineLen))
name = (input('| Full name: '))	 # name input
name = name.strip()	 # corrects empty space on string's start and end
lett = name.replace('', ' ').split()	 # total of letters in name into list
nameSplit = name.split()	 # name separated by words into list
lettFN = nameSplit[0].replace('', ' ').split()	 # total of letter in first name into list

print('-' * lineLen)
print('| Full upper case: {0}'.format(name.upper()))
print('| Full lower case: {0}'.format(name.lower()))
print('| Quantity of letters: {0}'.format(len(lett)))		# without spaces
	# OR (in this case, eliminate <name = name.strip()>)
	# print('| Quantity of letters: {0}'.format(len(name) - name.count(' ')))		# without spaces;
print('| Quantity of letters on the first name: {0}'.format(len(lettFN)))
	# OR (in this case, eliminate <lettFN = nameSplit[0].replace('', ' ').split()>)
	# print('| Quantity of letters on the first name: {0}'.format(name.find(' ')))		# not having strip() may cause issues
print('=' * lineLen, '\n')
