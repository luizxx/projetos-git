import requests
cep1 =  input('Digite seu cep.  1 ' ).strip() #pergunta cep ao usuario
cepf = len(cep1) # lê o numero de caracteres do cep.
while True:
    

    if cepf == 8: # aqui ele só rodara o codigo se o numero de caracteres for exatamente igual a 8, a api só aceita esse valor.
         res = input('Quer continuar? \n [1] - SIM \n [2] - NAO')
         if res == '1' :
             cep2 = requests.get(f'https://viacep.com.br/ws/{cep1}/json/') #api
             cep3 = (cep2.json())
             if 'erro' in cep3 : #aqui ele ta dizendo que caso o cep apresente algum erro ele ira mostra mensagem de erro
                 print('erro, o cep digitado não confere com nosso banco de dados, portanto não existe. ')
             else: # se nao tiver nenhum erro,ele logo vai mostrar esses dados
                 print('Seu cep: {} \n sua cidade {} \n seu estado {} \n seu DDD {} \n logradouro {} \n complemento {} \n bairro {} '.format(cep1,cep3['localidade'],cep3['uf'],cep3['ddd'], cep3 ['logradouro'], cep3['complemento'], cep3['bairro']))
                 
         elif res == '2': #fecha o programa
             print('encerrando o programa')
             break
         
    elif cepf <8 or cepf >8: # aqui, se o usuario digitar menos ou mais que 8 caracteres ele vai mostrar essa mensagem.
          print('O cep precisa ter 8 digitos, ou você digitou menos ou mais que digites que 8 \n ou digitou letras.')
    res = input('Quer continuar? \n [1] - SIM \n [2] - NAO')     
    if res == '1':
         cep1 =  input('Digite O novo cep. ' ).strip()
         cepf = len(cep1)
         
    elif res == '2':
         print('encerrando..')
         break  

         
    