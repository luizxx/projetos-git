a = float (input (' Digite um angulo '))
b = float (input (' Digita outro angulo '))
c = float (input ('Digite outro algulo denovo '))



if a < b + c and b < a + c and c < a + b and a < b + a :
     print ('PODE fazer triangulo. ' , end ='')
     if a == b and b != c or a == c and c != b or b == c and c != a or b == a and a != c :
      print ('Esse triangulo é o  isosceles')
     elif a == b and a == c or c == a and c == b or b == a and b == c :
      print (' Esse triangulo é o Equilatedo') 
     elif a != b and a != c  or c != b and c != a or b != a and b != c :
      print ('esse triangulo é o  escaleno.')



else:

     print('NAO pode fazer triangulo')