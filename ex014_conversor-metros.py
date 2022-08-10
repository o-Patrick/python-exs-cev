# 14. Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print('\n{:=^50}'.format('Distância'))
m = float(input('| Insira a distância em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('{:=^50}'.format('Conversão'))
print('| {0:.2f} m é igual a:'.format(m))
print('|', ('-' * 20))
print('| {0:.2f} km'.format(km))
print('| {0:.2f} hm'.format(hm))
print('| {0:.2f} dam'.format(dam))
print('| {0:.2f} dm'.format(dm))
print('| {0:.2f} cm'.format(cm))
print('| {0:.2f} mm'.format(mm))
print('{:=^50}\n'.format('Fim'))
