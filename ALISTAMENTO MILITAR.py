import colorama
colorama.init()
import time
import datetime
data = datetime.date.today().year
cores = { 'limpa ': '\033[m' ,
 'vermelho ' : '\033[31m' ,
 'verde ' : '\033[32m' , 
 'amarelo ' : '\033[33m', 
 'azul ' : '\033[34m'  , 
 'azul ciano ' : '\033[36m', 
 'vermelho claro ' : '\033[91m' ,
 'mangeta claro ' : '\033[95m',
 'cyan claro ' : '\033[96m'}
cores1 = { 'limpa ': '\033[m',  'amarelo f roxo ' : '\033[33;45m' }
  
print (' {} OLA VOCÊ FOI CONVIDADO PARA SE ALISTAR NO EXERCITO BRASILEIRO.'.format(cores['amarelo ']))
n = int (input (' Primeiro digite o ano do seu nascimento. ()  '   ))
print ('{}{}='  .format (cores['limpa '],cores ['azul ciano ']) * 70)
print ('{}{} CERTO, AGUARDE UM POUCO ENQUANTO ESTAMOS VERIFICANDO AS SUAS IMFORMAÇÕES'.format(cores['limpa '],cores['mangeta claro ']))
print ('{}{}='  .format (cores['limpa '],cores ['azul ciano ']) * 70)
time.sleep(3)
r = data - n             # descobrir quantos anos o usuario tem
r2 = r - 18               # descobrir quantos anos de atraso o mesmo tem
r3 = 18 - r                # descobrir quantos anos falta pro mesmo se alistar
r4 = n + 18
if r >18 :
    print (' {} {} ATENÇÃO: {} {} VOCÊ ESTA ATRASADO, POR FAVOR SE ALISTE O MAIS RAPIDO POSSIVEL. \n estas atrasado em  {}{}{}{}{} ano, na verdade o você deveria ter se alistado em {} {}{} {}{}. '.format (cores['limpa '],cores['vermelho '],cores['limpa '],cores ['verde '],cores['limpa '],cores['azul ciano '],r2,cores['limpa '],cores['verde '],cores['limpa '],cores['azul ciano '], r4 ,cores['limpa '],cores['verde '], ))
elif r == 18 :
    print ('{}{}='  .format (cores['limpa '],cores ['azul ']) * 70)
    print (' {} P A R A B É N S!!!'.format (cores1['amarelo f roxo ']))
    print ('{}{}='  .format(cores['limpa '],cores ['azul ']) * 70 )
    print (' {}{} Você já pode se{} {} alistar,{} {} basta ir em qualquer quartel e se apresentar como voluntário.'.format (cores['limpa '],cores['vermelho '],cores['limpa '],cores ['azul ciano '],cores['limpa '],cores['vermelho '], r2))
elif r < 18 :
    print ('{} {} infelismente você é muito novo ainda para se alistar, mas não fique triste \n pois poderar se alistar em {}{}{}{}{} ano, seu alista ocorrerá em {}{}{}{}{}.'.format (cores['limpa '],cores['vermelho '],cores['limpa '],cores ['azul ciano '],r3,cores ['limpa '],cores['vermelho '],cores['limpa '],cores['azul ciano '],r4, cores['limpa '],cores['vermelho ']  ))
elif n == str :
    print('Voce Digitou letras , quero somente numeros.')
else: print('Não entendi oque você quis dizer, desculpe tente novamente mais tarde. ')
print ('{}{}*'  .format (cores['limpa '],cores ['mangeta claro ']) * 40)
print (' {} CODIGO ESCRITO POR {} {}LUIZ OTÁVIO {}{}.' .format(cores['vermelho claro '], cores['limpa '], cores['cyan claro '], cores ['limpa '], cores ['vermelho claro '] ))
print ('{}{}*'  .format (cores['limpa '],cores ['mangeta claro ']) * 40)

