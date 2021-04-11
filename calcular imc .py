altura = float (input ('Olá vamos calcular o seu imc e dizer se você esta acima do peso ou não \n primeiro digite a sua altura.'))
peso = float (input ('Agora digite quantos kilos você pesa: '))

altura1 = altura * altura 
imc = peso / altura1 

if imc < 18.5 :
    print ('Abaixo do peso')
    print (f'Seu imc : {imc:.2f}')
elif imc > 18.5 and imc <= 25 :
    print (f'Seu imc : {imc:.2f}')
    print ('Peso ideal.')
elif imc > 25 and imc <= 30 :
    print (f'Seu imc : {imc:.2f}')
    print ('Sobrepeso. ')
elif imc > 30 and imc <= 40 :
    print ('Obesidade. ')
    print (f'Seu imc : {imc:.2f}')
elif imc > 40 :
    print ('Obesidade morbida')
    print (f'Seu imc : {imc:.2f}')