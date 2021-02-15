#12. Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = int(input('Digite a distância a percorrer :'))
velocidadeMedia = int(input('Digite velocidade média esperada para a viagem :'))
tempo = distancia/velocidadeMedia
print('O tempo da viagem vai ser',tempo)