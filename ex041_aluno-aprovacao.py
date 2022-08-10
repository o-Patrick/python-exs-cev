# 41. Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# 		- Média abaixo de 5: reprovado;
# 		- Média entre 5 e 6.9: recuperação;
# 		- Média 7 ou superior: aprovado.

lineLen = 80		# terminal interface line length
print('\n{0}'.format('=' * lineLen))		# terminal line interface

media = float(input('| Insira a média: '))

print('{0}'.format('-' * lineLen))		# terminal line interface

if media < 0 or media > 10:
	print('|| ERRO! As notas na escola funcionam apenas com numeração entre 0 e 10.')
else:
	if media < 5:
		print('|| Discente REPROVADO!')
	elif 7 > media >= 5:		# outro jeito: media >= 5 and media < 7
		print('|| Discente em RECUPERAÇÃO!')
	else:
		print('|| Discente APROVADO!')

print('{0}\n'.format('=' * lineLen))		# terminal line interface