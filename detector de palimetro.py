r = input ('Digite algo')

r2 = r.replace(' ','')
r3 = r2.lower()
r4 = r3.strip()
r1 = r4[::-1]


if r4 == r1 :
    print ('É POLIMETRO CARAIOO')
elif r4 != r1 :
    print('nao é polimetro')
else: print('ERROR')