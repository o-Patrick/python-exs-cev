# 40. Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade: se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou o tempo de alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoNasc  = int(input('\n| Qual é o ano do seu nascimento? '))
anoAtual = date.today().year
idade    = anoAtual - anoNasc

if anoNasc > anoAtual:
	print('\n|| [ERRO] Ano de nascimento inválido!')
else:
	if idade < 18:
		print('|| Você ainda não atingiu a idade mínima de 18 anos para o alistamento obrigatório.')
		if idade > 16:
			print('|| Porém a partir de 16 anos, voce já pode se alistar!')
	elif idade == 18:
		print('|| Você está na idade para o alistamento obrigatório!')
	else:
		print('|| Você já passou da idade do alistamento obrigatório!')
		print('|| Verifique no site oficial ou na junta militar mais próxima de sua casa, se possui alguma pendência com o alistamento. A idade limite para se regularizar é 45 anos.')
		if idade <= 21:
			print('|| A idade limite para entrar no exército é 21! Caso ainda queira se juntar à nós, basta realizar a devida prova. Mais informações no site oficial.')

print('')
