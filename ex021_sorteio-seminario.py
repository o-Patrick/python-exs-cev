# 21. O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

n1 = input('\nInsira o 1º nome: ')
n2 = input('Insira o 2º nome: ')
n3 = input('Insira o 3º nome: ')
n4 = input('Insira o 4º nome: ')

lista = [n1, n2, n3, n4]
shuffle(lista)

print('\nOrdem de apresentação:\n{0}\n'.format(lista))
