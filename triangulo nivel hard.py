a = float (input (' Digite um angulo '))
b = float (input (' Digita outro angulo '))
c = float (input ('Digite outro algulo denovo '))



if a < b + c and b < a + c and c < a + b and a < b + a :
     print ('pode faze triangulo')

else: 
     print ('n pode faze triangulo')





# equilatero = todos os lados iguais
#isosceles = dois lados iguals e um diferente
# escaleno = todos os lados diferentes 

#if a < b + c and b < a + c and c < a + b and a < b + a :
   # print ('Da pra construir um triangulo')
#else:
   # print('n da pra construir.')



#if a == b and b != c or a == c and c != b or b == c and c != a or b == a and a != c :
      print ('Seu triangulo é isosceles')


##lif a == b and a == c or c == a and c == b or b == a and b == c :
     #print ('Equilatedo') 

#elif a != b and a != c  or c != b and c != a or b != a and b != c :
    print ('Seu triangulo é escaleno.')