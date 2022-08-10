# 20. Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import choice

n1 = input('\nInsira o 1º nome: ')
n2 = input('Insira o 2º nome: ')
n3 = input('Insira o 3º nome: ')
n4 = input('Insira o 4º nome: ')
lista = [n1, n2, n3, n4]

print('\nO nome escolhido foi: {0}\n'.format(choice(lista)))
