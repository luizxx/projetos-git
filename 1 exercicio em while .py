resposta = 'g'
while resposta != 'f' and resposta != 'm':
    resposta = input('===Digite seu sexo===\n [F] FEMININO \n [M] MASCULINO.').strip().lower()[0]

    mul = 'f'
    hom = 'm'
    print('Digite certo por favor, não conseguimos reconhecer. ')
if resposta == 'm' or resposta =='f':
    if resposta =='m':
        print('Parabéns, você é HOMEM ')
    elif resposta == 'f' :
        print('Parabéns, você é MULHER')
print('resposta')
