res = 'o'
valor = int (input ('Digite algum valor e iremos calcular seu factorial..'))
valor1 = valor 
while  res != '1' or res != '2' or valor != '99999' :
      resul = 1
      if valor == valor1 or res == '1' :
          for c in range (1,valor+1,1):
             resul = resul * c 
            
             
      
          
      print(f'RESPOSTA : {resul}')
      res = input('[1] CONTINUAR(insetir novo numero) \n [2] ENCERRAR ')
      if res == '2':
        print('Programa encerrado pelo usuário.')
        break
      elif res == '1' :
        valor = int (input('Digite um novo valor: ' ))
          