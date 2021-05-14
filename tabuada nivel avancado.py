
cont = 0
while True:
        cont = 0
        numero_f = 0
        numero = 0
        numero = str (input('Digite o numero da sua tabuada'))
        verdadeiro = False
        if numero == '' :
           print('Digitou algo errado, tente novamente \n estamos encerrando o programa para evitar problemas.')
           verdadeiro = True
           break

        if verdadeiro == False:
            verdadeiro == False
        
        if verdadeiro == False:

            if int (numero) <= 0 :
                print('programa encerrado.')
                break
            elif int (numero) > 0:
                falso = True

        
        while falso == True:
           while cont < int (numero) :
             cont = cont + 1
             numero_f = cont * int (numero) 
             print(f'{cont} x {numero_f}')
             falso = False
            
            
