vc = float (input ('Digite o valor da casa que você deseja comprar.'))
vs = float (input ('Digite o seu salario mensal.'))
a = float (input ('Digite um numero em anos que você ira pagar tudo '))
a1 = a * 12             # calcular quantos meses ira pagar
a2 = vc / a1                # calcular o valor do pag por mes.

salario70 = (vs * 70 / 100)                #calcula 70% do salario
salario30 = (vs * 30 / 100)               #calcula 30% do salario
valor = a2 - vs
valorf = a2 - salario30 

if salario30 > valor :
      print (f'Para o o Sr. comprar uma casa no valor de {a2} o seu salario tinha que ser de 30% no valor do aluguel \n 30porcento do seu salario é de {salario30} portanto não aprovamos seu emprestimo. \n ficou faltando {valorf} reais para completar sua compra')

else: print (f'Parabéns voce foi aprovado, sua mensalidade sera de {a2} reais por mês.')



print (salario30)

# if vs1 < vvs:
  #  print ('Emprestimo negado.')
#else:
   # print ('parabens foi aprovado.')
   
