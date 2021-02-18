#11. Faça um programa que solicite o preço de uma mercadoria e o per- centual de desconto. Exiba o valor do desconto e o preço a pagar.

precoMerca = float(input('digite o valor da mercadoria : '))
pDesconto = float(input('digite o valor do percentual de desconto : '))
desconto = (precoMerca * (pDesconto/100))
apagar = precoMerca - (precoMerca * (pDesconto/100))
#print('O aumento foi de R$',poraumento,"e o novo salario é :",)
print('O preço agora a novo :',apagar,'seu desconto foi de R$',desconto)


