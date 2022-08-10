# 25. Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com 'SANTO'.

city = str(input('City name: ')).strip()
city = city.upper().split()
print('SANTO' in city[0])
	# OR print(city[:5].upper == 'SANTO')		# in this case, city can't be split