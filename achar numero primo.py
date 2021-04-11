primo = int (input('Digite um numero inteiro aí '))

r = primo % 2 

if primo > 2 and r >0:
    print('É NUMERO PRIMO.')
elif r==0 :
    print('NAO É NUMERO PRIMO.')
else: print('ERROR')



print('-' * 30 )
print('Fim do programa.')
print('-' * 30 )