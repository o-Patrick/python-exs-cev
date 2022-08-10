# 33. Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

year = int(input('\n| Insert a year (0 for the current year): '))

if year == 0:
	year = date.today().year

if year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
	print('| {0} is a normal year.\n'.format(year))
else:
	print('| {0} is a leap year.\n'.format(year))

# cent = (year // 1 % 10 == 0) and (year // 10 % 10 == 0)		# is a century year
# OR if year % 4 != 0:
# 	print('| {0} is a normal year.\n'.format(year))
# else:
# 	if cent:
# 		if year % 400 == 0:
# 			print('| {0} is a leap year.\n'.format(year))
# 		else:
# 			print('| {0} is a normal year.\n'.format(year))
# 	else:
# 		print('| {0} is a leap year.\n'.format(year))
