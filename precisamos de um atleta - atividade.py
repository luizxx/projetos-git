import datetime
ano = datetime.date.today().year




r = input ('A confederação do brazil precisa de um atleta \n para você se cadastrar primeiro digite seu nome :   ')
r1 = int (input ('Agora digite seu ano de nascimento:   '))
r4 = r.upper()

r2 = ano - r1   # saber a idade do mesmo.


if r2 <= 9 :
    print ('MIRIN')
elif r2 <=14  and r2 > 9 :
    print (f'OLA {r4} VOCÊ TEM {r2} ANOS E ESTA NA CATEGORIA INFANTIL')
elif r2 <= 19 and r2 > 14 :
    print (f'OLÁ {r4} VOCÊ TEM {r2} ANOS E ESTA NA CATEGORIA JUNIOR ')
elif r2 == 20 : 
    print (f'OLÁ {r4} VOCÊ TEM {r2} ANOS E ESTA NA CATEGORIA SÊNIOR')
elif r2 > 20 :
    print (f'OLÁ {r4} VOCÊ TEM {r2} ANOS E ESTA NA CATEGORIA MASTER')
else:
    print ('Desculpe não conseguimos entender oque você digitou.')
