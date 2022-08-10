# 44. Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# 		- Abaixo de 18.5: abaixo do peso;
# 		- Entre 18.5 e 25: peso ideal;
# 		- 25 até 30: sobrepeso;
# 		- 30 até 40: obesidade;
# 		- Acima de 40: obesidade mórbida.

lineLen = 50		# terminal line interface length
print('\n{0}'.format('=' * lineLen))		# terminal first line interface

peso   = float(input('| Insira o peso: '))
altura = float(input('| Insira a altura: '))

print('{0}'.format('-' * lineLen))		# terminal middle line interface

imc = peso / (altura ** 2)
print('|| IMC: {0:.2f} kg/m2'.format(imc))

print('{0}'.format('-' * lineLen))		# terminal middle line interface

if imc < 18.5:
    imcFaixa = 'abaixo do peso'
elif imc <= 25:
    imcFaixa = 'no peso ideal'
elif imc <= 30:
    imcFaixa = 'com sobrepeso'
elif imc <= 40:
    imcFaixa = 'com obesidade'
else:
    imcFaixa = 'com obesidade mórbida'
print('|| Você está {0}.'.format(imcFaixa))

print('{0}\n'.format('=' * lineLen))		# terminal last line interface