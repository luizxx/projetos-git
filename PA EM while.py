pa = int (input('Digite a primeira PA ' ))
razao = int (input('Digite a razão ' ))
paf = int(input('Digite o final da sua pa. ' ))


res = 'z'
while res != '1' or res != '2' or res != 'l':
   if pa >0 or razao >0 :
        for c in range(pa,paf +1,razao):
           print(f'{c}',end=' = ')

   print('ACABOUU!')
   res = input('Voce quer continuar ? \n [1]-SIM \n [2]-NÃO ' )
   if res == '1' :
       pa1 = int (input('Digite a primeira 1 PA ' ))
       razao = int (input('Digite a razão ' ))
       paf = int(input('Digite o final da sua pa. ' ))
   elif res == '2' :
       print('Programa encerrado.')
       break

   

      