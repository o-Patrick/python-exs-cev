# 24. Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados (ex: 1922; unidade: 2, dezena: 2, centena: 9, milhar: 1).

lineLen = 40		# lenght os separating lines
print('{0}{1}'.format('\n', '=' * lineLen))

num = int(input('| Insert a number (ex: 1922): '))

# separing the unit, ten, hundred and thousand usaing math
uni = num // 1 % 10
ten = num // 10 % 10
hun = num // 100 % 10
tho = num // 1000 % 10

print("""{0}
| Unit: {1}
| Ten: {2}
| Hundred: {3}
| Thousand: {4}
{5}{6}""".format(('-' * lineLen),
uni,
ten,
hun,
tho, ('=' * lineLen), '\n'))

# OR as a string; in this case num needs to be at least 1000
# print("""{0}
# | Unit: {1}
# | Ten: {2}
# | Hundred: {3}
# | Thousand: {4}
# {5}{6}""".format(('-' * lineLen),
# num[3],
# num[2],
# num[1],
# num[0],('=' * lineLen),'\n'))
