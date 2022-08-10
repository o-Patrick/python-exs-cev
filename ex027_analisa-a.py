# 27. Faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra 'A', em que posição ela aparece pela primeira vez, em que posição ela aparece pela última vez.

lineLen = 60
print('{0}{1}'.format('\n', ('=' * lineLen)))

phrase = str(input('| Type any phrase: ')).upper().strip()

print("""{0}
| The letter A appears: {1} times,
| It's first appearance is at: {2}º position,
| And it's last appearance is at: {3}º position.
{4}{5}"""
.format(('-' * lineLen),
phrase.count('A'),
phrase.find('A')+1,
phrase.rfind('A'),		# not couting the space here
('=' * lineLen),
'\n'))
