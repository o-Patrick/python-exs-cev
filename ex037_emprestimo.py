# 37. Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o empréstimo será negado.

print('\n{0}'.format('-=-' * 30))		# interface

# var
preco = float(input('| Qual o preco da casa? R$'))
sal   = float(input('| Qual é o seu salário? R$'))
anos  = int(input('| Em quantos anos será pago?'))
mens  = preco / (anos * 12)		# mensalidade
prcnt = (mens / sal) * 100			# porcentagem da mensalidade comparada ao salário

print('\n| Mensalidade: R${0:.2f}'.format(mens))
print('\n| A mensalidade é {0:.2f}% do seu salário.'.format(prcnt))

if mens <= (sal * 0.3):
	print('| PARABÉNS: o empréstimo pode ser liberado!')
elif mens > (sal * 0.3):
	print('| NEGADO: a mensalidade ultrapassa o limite de 30% do seu salário em {0:.2f}%!'.format(prcnt-30))

print('{0}\n'.format('-=-' * 30))		# interface
