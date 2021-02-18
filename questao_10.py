#10. Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.
salário = float(input('digite o valor do salario : '))
aumento = float(input('digite o valor do aumento : '))
novosalario = (salário + (salário * (aumento/100)))
poraumento = (salário * (aumento/100))
print('O aumento foi de R$',poraumento,"e o novo salario é :",novosalario)
