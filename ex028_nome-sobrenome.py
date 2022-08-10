# 28. Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último name separadamente.

lineLen = 40
print('{0}{1}'.format('\n', ('=' * lineLen)))

name = str(input('| Name: ')).title().strip().split()

print("""{0}
| First name: {1}
| Last name: {2}
{3}{4}"""
.format(('-' * lineLen), name[0], name[len(name) - 1], ('=' * lineLen), '\n'))
