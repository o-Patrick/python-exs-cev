# 32. Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

km = float(input('\n| Insert the distance in Km/h: '))
if km <= 200:
	price = km * 0.5
else:
	price = km * 0.45
print('| The final price is R${0:.2f}\n'.format(price))
