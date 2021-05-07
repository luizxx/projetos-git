
valor =  int (input('[VALOR1] Digite um valor: ' ))
valor1 =  int (input('[VALOR2] Digite outro valor ' ))
funcao = 'l'
while funcao != '1' or funcao != '2' or funcao != '3' :
          funcao =  input(' \n [1] SOMAR \n [2] MULTIPLICAR \n [3] MAIOR \n [4] NOVOS NUMEROS \n [5] FATORIAL \n [6] PA DE UM NUMERO \n [7] FECHAR O PROGRAMA \n R:'  )
          if funcao == '1'   :
           somar = float (valor) + float (valor1) 
           print(f'Resposta: \n {valor} + {valor1} =  {somar} ' )
          elif funcao == '2'    :
               multiplicar = float (valor) * float (valor1)
               print(f'Resposta: \n {valor} x {valor1} = {multiplicar} ' )
          elif funcao == '3' :
             if valor > valor1 :
                     print(f'{valor} é o maior numero e {valor1} o menor .')
             elif  valor1 >  valor :
                     print(f'{valor1} é o maior numero e {valor} o menor .')
             else:
                     print(f'Ambos valores são iguais, portanto não há diferença entre {valor1} e {valor}.')
          elif funcao == '4':
                print('Então você quer adicionar novos numeros, né.. ')
                valor =  int (input('Digite um valor: ' ))
                valor1 =  int (input('Digite outro valor ' ))
          elif funcao == '5': 
              resul = 1
              resul1 = 1
              va = 2
              
              for c in range (1,valor+1,1):
                   resul = resul * c 
                   
              if resul >0 :
                 for c in range (1,valor1+1,1):
                  resul1 = resul1 * c

              if va == 2 :
                  print(f'\n RESULTADO FATORIAL [VALOR1] :{resul} \n RESULTADO FATORIAL [VALOR2] :{resul1} \n')
             

          if funcao == '6' :
                   pa = int (input('Digite a primeira PA ' ))
                   razao = int (input('Digite a razão ' ))
                   paf = int(input('Digite o final da sua pa. ' ))
                   for c in range(pa,paf +1,razao):
                          print(f'{c}',end='  ')

          if funcao == '7':
            print('Encerrando o programa. ' )
            break
            #Esse programa, é um mini menu que da 7 opcoes ao usuario, sendo elas : calcular, multiplicar, maior numero, fatorial, pa, adicionar novos numeros e opcao para sair        
               
               