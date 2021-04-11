
import random
import time
print ('Vamos jogar pedra papel tesoura?  ')
r2 = str (input ('Digite pedra ou papel ou tesoura: (digite em minusculo SEM ESPACOS) '))
r = ['pedra', 'papel','tesoura']
r1 = random.choice(r,) 
print ('JO')
time.sleep(1)
print ('KEN')
time.sleep(1)
print('PO')



if r2 == 'pedra' and r1 == 'tesoura' or r2 == 'tesoura' and r1 == 'papel' or r2 == 'papel' and r1 == 'pedra' :
       print (f' PARABÉNS você ganhou, eu escolhi {r1} e você {r2} \n {r2} ganha de {r1}')      
elif r2 == r1 :
    print(f'A gente jogou igual affs, deu empate porque vc escolheu {r2} e eu tambem')
elif  r1 == 'pedra' and r2 == 'tesoura' or r1 == 'tesoura' and r2 == 'papel' or r1 == 'papel' and r2 == 'pedra' :
        print (f'eu ganheii, você escolheu {r2} e eu {r1} \n {r1} ganha de {r2} portanto eu maquina te venci xD ')


else:
    print('FATAL ERROR, TENTE NOVAMENTE') 

