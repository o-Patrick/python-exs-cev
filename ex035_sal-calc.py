# 35. Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('\n| Insert the salary: R$'))
if sal >= 1250:
	print('| Calculating 10% raise . . . |')
	sal += sal * 0.1
else:
	print('| Calculating 15% raise . . . |')
	sal += sal * 0.15
print('| The new salary is R${0:.2f}\n'.format(sal))
