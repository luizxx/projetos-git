import colorama
colorama.init(1)
cores = { 'limpa ': '\033[0;30;40m' , 'branco ':'\033[30m' ,
 'vermelho ' : '\033[31m' ,
  'verde ' : '\033[32m' , 
  'amarelo ' : '\033[33m', 
  'azul ' : '\033[34m' ,  
  'roxo ' : '\033[35m' , 
  'azul ciano ' : '\033[36m', 
'cinza ': '\033[37m'}
cores1 = { 'limpa ': '\033[m' ,'branco f vermelho ':'\033[30;41m' ,
 'vermelho f branco ' : '\033[31;40m' ,
  'verde f branco ' : '\033[32;40m' , 
  'amarelo f branco ' : '\033[33;40m', 
  'azul f branco ' : '\033[34;40 m' , 
  'roxo f branco ' : '\033[35;40 m' , 
  'azul ciano f branco ' : '\033[36;40m', 
'cinza f branco ': '\033[37;40m' ,
  'branco f verde ':'\033[30;42m' ,
 'vermelho f verde ' : '\033[31;42m' ,
  'verde f vermelho ' : '\033[32;41m' , 
  'amarelo f verde ' : '\033[33;42m', 
  'azul f verde ' : '\033[34;42m' , 
  'roxo f verde ' : '\033[35;42m' , 
  'azul ciano f verde ' : '\033[36;42m', 
'cinza f verde ': '\033[37;42m', 
'branco f amarelo ':'\033[30;43m' ,
 'vermelho f amarelo ' : '\033[31;43m' ,
  'verde f amarelo ' : '\033[32;43m' ,      
  'azul f amarelo ' : '\033[34;43m' , 
  'roxo f amarelo ' : '\033[35;43m' , 
  'azul ciano f amarelo ' : '\033[36;43m', 
  'cinza f amarelo ': '\033[37;43m' , 
'branco f azul ':'\033[30;44m' ,
 'vermelho f vermelho ' : '\033[31;41m' ,
  'verde f azul ' : '\033[32;44m' , 
  'amarelo f vermelho ' : '\033[33;41m', 
  'azul f vermelho ' : '\033[34;41m' , 
  'roxo f vermelho ' : '\033[35;41m' , 
  'azul ciano f vermelho ' : '\033[36;41m', 
 'cinza f vermelho ': '\033[37;41m'  , 'branco f roxo ':'\033[30;45m' ,
 'vermelho f roxo ' : '\033[31;45m' ,
  'verde f roxo ' : '\033[32;45m' , 
  'amarelo f roxo ' : '\033[33;45m', 
  'azul f roxo ' : '\033[34;45m' ,  
  'roxo f roxo ' : '\033[35;45m' , 
  'azul ciano f roxo ' : '\033[36;45m', 
 'cinza ': '\033[37m' , 
 'branco f ciano ':'\033[30;46m' ,
 'vermelho f ciano ' : '\033[31;46m' ,
  'verde f ciano ' : '\033[32;46m' , 
  'amarelo f ciano ' : '\033[33;46m', 
  'azul f ciano ' : '\033[34;46m' ,  
  'roxo f ciano ' : '\033[35;46m' , 
  'azul ciano f ciano ' : '\033[36;46m', 
 'cinza f ciano': '\033[37;46m' , 
 'branco f cinza':'\033[30;47m' ,
 'vermelho f cinza ' : '\033[31;47m' ,
  'verde f cinza ' : '\033[32;47m' , 
  'amarelo f cinza ' : '\033[33;47m', 
  'azul f cinza ' : '\033[34;47m' ,  
  'roxo f cinza ' : '\033[35;47m' , 
  'azul ciano f cinza ' : '\033[36;47m', 
 'cinza f cinza ': '\033[37;47m', 
 'vermelho  f azul' : '\033[31;44m' ,
  'amarelo f azul ' : '\033[33;44m', 
  'azul f azul ' : '\033[34;44m' ,  
  'roxo f azul ' : '\033[35;44m' , 
  'azul ciano f azul' : '\033[36;44m', 
 'cinza f azul ': '\033[37;44m', 'preto e branco ' : '\033[7;40m'}
print (' Olá vamos converter algumas coisas.')
r2 = int (input ('Digite o valor inteiro que deseja converter.'))
r = input ('Caso queira converter decimal para binario digite 1 \n caso seja para hexadecimal digite 2 \n caso seja pra octamal digite 3. ')

if r == '1':
  rf =  bin(r2) [2:]
  print (f'{rf}')
elif r == '2':
     hexa = hex(r2) [2:]
     print(hexa)
     #print ( '  {} hexadecimal {} {} = '.format(cores['azul '] ,cores['limpa '],cores['vermelho '], hexaa ))
elif r == '3':
           octal = oct(r2) [2:]
           print (f'octal = {octal}')
else:
      print ('ERROR')