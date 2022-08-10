# 45. Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#		- À vista dinheiro/cheque: 10% de desconto;
#		- À vista no cartão: 5% de desconto;
#		- Em até 2x no cartão: preço normal;
#		- 3x ou menos no cartão: 20% de juros.

lineLen = 50		# terminal line interface length
print('\n{0}'.format('=' * lineLen))		# terminal first line interface

preco = float(input('| Qual é o preço do produto? '))

print('{0}'.format('-' * lineLen))		# terminal middle line interface

formaPag = int(input('''| Qual a forma de pagamento?
| [1] À vista dinheiro/cheque (10% de desconto)
| [2] À vista no cartão (5% de desconto)
| [3] Em até 2x no cartão (preço normal)
| [4] 3x ou menos no cartão (20% de juros)
| Digite o número: '''))

# cálculo
if formaPag == 1:			# À vista dinheiro/cheque (10% de desconto)
	precoFinal = preco - (preco * 0.1)
elif formaPag == 2:		# À vista no cartão (5% de desconto)
	precoFinal = preco - (preco * 0.05)
elif formaPag == 3:		# Em até 2x no cartão (preço normal)
	precoFinal = preco
elif formaPag == 4:		# 3x ou menos no cartão (20% de juros)
	precoFinal = preco + (preco * 0.2)

print('{0}'.format('-' * lineLen))		# terminal middle line interface

print('| Total: {0}'.format(precoFinal))

if formaPag == 3:
	print('| Em 2x parcelas de {0}'.format(precoFinal / 2))
elif formaPag == 4:
	print('| Em 3x parcelas de {0}'.format(precoFinal / 3))

print('{0}\n'.format('=' * lineLen))		# terminal last line interface