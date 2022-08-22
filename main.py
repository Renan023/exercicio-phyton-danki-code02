from datetime import date

at = date.today().year
n = str(input('Nome '))
nasc = int(input('Seu ano de nascimento '))
id = at - nasc
print('Sua idade {} anos em {}'.format(id, at))
print('='*20)
if id < 16:
    print('{} é de menor'.format(n))
elif id <18:
    print('{} é emancipado'.format(n))
else:
    print('{} é de maior'.format(n))
print('='*20)