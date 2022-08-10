# 19. Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan

deg = float(input('\nInsert the degree: '))
rad = radians(deg)
print('Considering {0}°:'.format(deg))
print('-' * 25)
print('Sin: {:.2f}°'.format(sin(rad)))
print('Cos: {:.2f}°'.format(cos(rad)))
print('Tan: {:.2f}°\n'.format(tan(rad)))
