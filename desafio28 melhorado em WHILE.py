jogar = '6'
while jogar != '1' and jogar !='2':
     


   jogar =  input('Eu sou o computador e me chamo izaki, vamos jogar ? \n [1] PARA SIM \n [2] PARA NÃO ' )
if jogar == '1' :
     import random
     import time
     numero = [1,2,3,4,5,6,7,8,9,10]
     numeros = random.choice(numero)
     num = 0 
     tentativas = 0
     print('  \n TENTE ADVINHAR O NUMERO QUE EU PENSEI.\n ...........................')
     while True :
         
         num = int (input('Qual numero você acha que eu pensei? \n R:  ' ))
         if num =='sair' :
             print('Programa encerrado pelo usuário.')
             break
         tentativas = tentativas +1
         if numeros != num:
             resposta_maior = ('Você errou!!! eu pensei em um numero maior que esse.')
             resposta_menor = ('Você errou!!! eu pensei em um numero menor que esse.')
             if numeros > num :
                r_maior = len(resposta_maior)
                print('=' * r_maior )
                print('Você errou!!! eu pensei em um numero MAIOR que esse.')
                print('=' * r_maior )
                opcao = input('[1] TENTAR NOVAMENTE \n [2] RESETAR NUMERO \n [3] SAIR \n R:  ' )
                if opcao == '2':
                    numeros = random.choice(numero)
                    print('Certo, pensarei em um outro numero..')
                elif opcao == '3':
                    break
             elif numeros < num :
                r_menor = len(resposta_menor)
                print('=' * r_menor)
                print('Você errou!!! eu pensei em um numero MENOR que esse.')
                print('=' * r_menor )
                opcao = input('[1] TENTAR NOVAMENTE \n [2] RESETAR NUMERO \n [3] SAIR \n R:  ' )
                if opcao == '2':
                    numeros = random.choice(numero)
                    print('Certo, pensarei em um outro numero..')
                elif opcao == '3':
                    break
             

         if num == numeros :
             print(f'\n ===FIM DE JOGO VOCÊ GANHOU===\n \n \n AAffz vc me venceu :(, muito bem mas você teve que tentar  {tentativas} vezes para me vencer')
             opcao = input('Quer jogo denovo? \n [1] - SIM \n [2] - NÃO \n R:  ' )
             if opcao == '2':
              break
             if opcao == '1':
                 numeros = random.choice(numero)



elif jogar == '2' : 
    print('que pena que vc não quer jogar comigo :( \n encerrando programa.')
    exit


 