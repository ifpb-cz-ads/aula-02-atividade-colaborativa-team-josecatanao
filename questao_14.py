#14. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

quantidadeKM = float(input('Digite a quantidade de Km percorrido: '))
quantidadeDia = float(input('Digite a quantidade de dias alugado: '))

preco =  (quantidadeDia * 60) + (quantidadeKM * 0.15)

print('O preço a pagar é de : R$',preco)

