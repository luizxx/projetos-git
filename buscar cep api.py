import requests
cep1 =  input('Digite seu cep.  1 ' ).strip() # pede ao usuário um cep
cepf = len(cep1) # ira ler o cep, para filtrar a apenas 8 digitos mais tarde..
res = 'l' # so pro comando sair funcionar..
while True:
    cep2 = requests.get(f'https://viacep.com.br/ws/{cep1}/json/')
    cep3 = (cep2.json()) #basicamente essa é a api do cep

    if cepf == 8: # ele so ira rodar a linha de comando se tiver 8 digitos.
         res = input('Quer continuar? \n [1] - SIM \n [2] - NAO') 
         if res == '1' : # se o usuario concordar em continuar ele iniciara, caso contrarior fechara
             print('Seu cep: {} \n sua cidade {} \n seu estado {} \n seu DDD {} \n logradouro {} \n complemento {} \n bairro {} '.format(cep1,cep3['localidade'],cep3['uf'],cep3['ddd'], cep3 ['logradouro'], cep3['complemento'], cep3['bairro']))
         elif res == '2':
             print('encerrando o programa')
             break
         elif cep3 == KeyError: # tava tentando fazer funcionar mas nao ta dando, se o usuario digita um cep inexistente ele mostrara uma mensagem de erro muito feia.., ai queria ue mostrasse oque eu quisesse
             print('error ')
             
    elif cepf <8 or cepf >8: # caso o usuario digitar um menor menor ou maior que 8 o programa não rodara.
          print('O cep precisa ter 8 digitos, ou você digitou menos ou mais que digites que 8 \n ou digitou letras.')
    res = input('Quer continuar? \n [1] - SIM \n [2] - NAO')     
    if res == '1':
         cep1 =  input('Digite O novo cep. ' ).strip()
         cepf = len(cep1)
    elif res == '2':
         print('encerrando..')
         break  

         
    
