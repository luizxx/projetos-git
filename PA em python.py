s = 0 
pa = int (input ('Digite o primeiro termo da PA '))
razao = int (input ('Digite a razão da PA '))
razao1 = razao * 10
for c in range(pa,razao1+1,razao):
    s = razao + s
    print(s)
