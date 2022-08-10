# 18. Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot
catOp = float(input('\nQual o comprimento do cateto oposto? '))
catAd = float(input('Qual o comprimento do cateto adjacente? '))
hipot = hypot(catOp, catAd)
# hipot = (catOp ** 2 + catAd ** 2) ** (1/2)
# hipot = sqrt(catOp ** 2 + catAd ** 2)

print('{0}^2 {1}^2 = {2:.2f}\n'.format(catOp, catAd, hipot))
