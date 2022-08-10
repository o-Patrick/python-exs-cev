# 30. Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

km = float(input('\n| Car velocity in Km/h: '))

if km > 80:
	print('\n| Limit exceeded! Your traffic ticket will cost R${0:.2f}'.format((km - 80) * 7))

print('| Safe travels!')
