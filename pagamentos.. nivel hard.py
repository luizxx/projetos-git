valor = str (input ('[1]NO DINHEIRO A VISTA \n [2] NO CARTÃO DE CREDITO A VISTA \n [3] EM 2 VEZES NO CARTÃO \n [4] EM 3 X OU MAIS NO CARTÃO.'))
valorf = float (input ('Digite o valor do produto: R$  '))


desconto1 = (valorf * 10 / 100)   #a vista no dinheiro ou cheque 10% desconto
descontof = valorf - desconto1

cartao1 = (valorf * 5 / 100)       # a vista cartao 5% desconto
cartaof = (valorf - cartao1)
cartao3x = (valorf * 20 / 100)
cartao3xf = (valorf + cartao3x)

print ('*' * 50 )
print ('TABELA DE PRECOS DE ACORDO COM AS NOSSAS CONDIÇÕES: ')
print ('*' * 50 )
if valor == '1':
    print (f'O valor do produto sera de  {descontof} reais. desconto de {desconto1} reais ')
    print ('MUITO OBRIGADO POR COMPRAR NA NOSSA LOJA, VOLTE SEMPRE <3 ')

elif valor == '2' :
    print(f'O valor do produto sera de {cartaof} reais. desconto de {cartao1} reais.')
    print ('MUITO OBRIGADO POR COMPRAR NA NOSSA LOJA, VOLTE SEMPRE <3 ')
elif valor == '3' :
    cartaosemjuros = (valorf / 2)
    print(f' voce pagara em 2x de  {cartaosemjuros} reais. desconto de 0 reais. ')
    print ('MUITO OBRIGADO POR COMPRAR NA NOSSA LOJA, VOLTE SEMPRE <3 ')
elif valor == '4' :
    valorff = int (input('Quantas parcelas serão?'))
    cartao3x = (valorf * 20 / 100)
    cartao3xf = (valorf + cartao3x)
    cartao4x = (cartao3xf / valorff)
    juros =  (cartao3x / valorff)

    print (f'voce pagara {valorff}x parcelas de  {cartao4x} reais com juros total de {cartao3x} \n cada parcela paga {juros} de juros em cada parcela sobre o valor total do produto {valorf}')
    print ('MUITO OBRIGADO POR COMPRAR NA NOSSA LOJA, VOLTE SEMPRE <3 ')
else:
    print('ERROR, você digitou algo de errado, tente novamente.')
