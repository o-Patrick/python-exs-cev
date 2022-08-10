'''57. Desenvolva um programa que leia nome, idade e sexo de quatro pessoas. No final do programa, mostre:
		- A média de idade do grupo;
		- Qual é o nome do homem mais velho;
		- Quantas mulheres têm menos de 20 anos.
'''

# cabeçalho
lineLen = 110															# terminal line interface length
print('\n{0}'.format('=' * lineLen))							# terminal first line interface
print('{0:^{1}}'.format('R E G I S T R O', lineLen))		# título
print('{0}'.format('=' * lineLen))								# terminal first line interface

# var
somaIdades   = 0		# total de idades para a média
mMaiorIdade = 0		# masculino maior idade
mMaisVelho  = ''		# masculino mais velho
fQtdMenos20 = 0		# feminino < 20 anos

for i in range(1, 5):
	print('{0:-^{1}}'.format('{0}ª pessoa', lineLen+2).format(i))
	# inputs
	nome  = input('| Nome: '.format(i)).strip()
	idade = int(input('| Idade: '))
	sexo  = input('| Sexo [I/F/M]: ').strip()

	somaIdades += idade

	if i == 1 and sexo in 'Mm':		# trata o primeiro masculino como mais velho
		mMaiorIdade = idade
		mMaisVelho  = nome
	if sexo in 'Mm' and idade > mMaiorIdade:		# altera o masculino mais velho
		mMaiorIdade = idade
		mMaisVelho  = nome
	if sexo in 'Ff' and idade < 20:		# feminino < 20
		fQtdMenos20 += 1

media = somaIdades / 4		# média das idades

print('{0}'.format('-' * lineLen))			# terminal middle line interface
# outputs
print('| Média das idades                            : {0:.1f} anos'.format(media))
print('| Homem mais velho                            : {0} com {1}'.format(mMaisVelho, mMaiorIdade))
print('| Total de pessoas do sexo feminino < 20 anos : {0}'.format(fQtdMenos20))
print('{0}\n'.format('=' * lineLen))		# terminal last line interface
