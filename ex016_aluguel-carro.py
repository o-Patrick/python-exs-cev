# 16. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos km o cliente percorreu com o carro? '))
dias = int(input('Por quantos dias o cliente permaneceu com o carro? '))
print('Preço final: {0}'.format((km*0.15) + (dias*60)))
