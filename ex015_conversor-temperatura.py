# 15. Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

cel = float(input('Insira a temperatura em ºC: '))
kel = cel + 273.15
fah = ((9 / 5) * cel) + 32 # OU ((9 * cel) / 5) + 32
print('{0:.2f} ºC = {1:.2f} K'.format(cel, kel))
print('{0:.2f} ºC = {1:.2f} ºF'.format(cel, fah))
# print('{} ºC'.format(cel))