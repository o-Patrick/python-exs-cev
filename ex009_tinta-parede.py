# 9. Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2.

width = float(input('Wall height: '))
height = float(input('Wall width: '))
area = width * height
paint = area/2
print('The amount of paint needed is {0:.2f}l to an area of {1:.2f}m2'.format(paint, area))
