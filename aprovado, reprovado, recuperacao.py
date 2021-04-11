
print ('Aviso: para o programa funcionar adequadamente, digite sua nota em formatos : 70 , 80, 100 ou 65.67, \n não use : 7.5 , 8.4 , 5 , 6')
n1= float (input ('Digite sua primeira nota. ()'))
n2 = float (input ('Agora digite a sua segunda nota '))

nf = n1 + n2 
nf1 = nf / 2 

if nf1 < 50 :
       print ('R E P R O V A D O')
       print (f'Sua nota aqui : {nf1}')

elif nf1 >= 70 :
    print (' PARABÉNS, VOCÊ FOI  A P R O V A D O')
    print (f'Sua nota aqui : {nf1}')

elif nf1 >= 50.0 and nf1 <= 69.99 :
     print ('ESTÁS DE RECUPERAÇÃO, VÁ ESTUDAR IMEDIATAMENTE.')
     print (f'Sua nota aqui : {nf1}')

else:
     print ('Olá, não conseguimos entender oque você digitou, tente novamente mais tarde.')

