# 26. Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA'.

lineLen = 40		# separating lines length
print('{0}{1}'.format('\n', ('=' * lineLen)))

name = str(input('| Name: ')).strip()

print("""{0}
| Does the name contains "Silva"? {1}.
{2}{3}""".format(('-' * lineLen), 'Silva' in name.title(), ('=' * lineLen), '\n'))
