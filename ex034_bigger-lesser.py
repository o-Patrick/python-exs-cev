# 34. Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('\n| Insert the 1º number: '))
n2 = float(input('| Insert the 2º number: '))
n3 = float(input('| Insert the 3º number: '))

les = n1
if n2 < n1 and n3 < n3:
	les = n2
if n3 < n1 and n3 < n2:
	les = n3

big = n1
if n2 > n1 and n2 > n3:
	big = n2
if n3 > n1 and n3 > n2:
	big = n3

print("""\n| The bigger number is {0:.1f}
| The lesser number is {1:.1f}\n""".format(big, les))

# if n1 > n2 and n1 > n3:
# 	big = n1
# else:
# 	if n2 > n1 and n2 > n3:
# 		big = n2
# 	else:
# 		big = n3

# if n1 < n2 and n1 < n3:
# 	les = n1
# else:
# 	if n2 < n1 and n2 < n3:
# 		les = n2
# 	else:
# 		les = n3
