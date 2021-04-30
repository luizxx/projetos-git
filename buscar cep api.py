import requests
cep1 =  input('Digite seu cep.  1 ' ).strip()
cepf = len(cep1)
res = 'l'
while True:
    cep2 = requests.get(f'https://viacep.com.br/ws/{cep1}/json/')
    cep3 = (cep2.json())

    if cepf == 8:
         res = input('Quer continuar? \n [1] - SIM \n [2] - NAO')
         if res == '1' :
             print('Seu cep: {} \n sua cidade {} \n seu estado {} \n seu DDD {} \n logradouro {} \n complemento {} \n bairro {} '.format(cep1,cep3['localidade'],cep3['uf'],cep3['ddd'], cep3 ['logradouro'], cep3['complemento'], cep3['bairro']))
         elif res == '2':
             print('encerrando o programa')
             break
         elif cep3 == KeyError:
             print('error ')
             
    elif cepf <8 or cepf >8:
          print('O cep precisa ter 8 digitos, ou você digitou menos ou mais que digites que 8 \n ou digitou letras.')
    res = input('Quer continuar? \n [1] - SIM \n [2] - NAO')     
    if res == '1':
         cep1 =  input('Digite O novo cep. ' ).strip()
         cepf = len(cep1)
    elif res == '2':
         print('encerrando..')
         break  

         
    