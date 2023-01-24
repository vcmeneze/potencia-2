a=int(input('Qual numero deseja saber se é potência de 2? '))
  
while a>2 and a%2 == 0:
  a1 = a%2
  a /= 2
  while a>1 and a1 == 0:
    a1 = a%2
    a /=2

if a==1: print ('Sim')
else: print('Não é.')
