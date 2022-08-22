from datetime import date
from time import sleep
at = date.today().year
print('='*70)
n = input('Nome ')
nasc = int(input('Nascimento '))
id = at - nasc
print('{} tem {} anos. No ano de {}'.format(n, id, at))
print('Processando')
sleep(1)
print('Cadastro  completo. Na competição de natação de 5 anos até 20 anos ')
print('='*70)
if id>=8 and id<=10 :
    print('Modalidade Infantil A ')
elif id>=11 and id <=14:
    print('Modalidade Infantil B')
elif id>=15 and id<=18:
    print('Modalidade juvenil A')
elif id>=19 and id<=20:
    print('Modalideade juvenil B')
else:
    print('Não é possível participar')