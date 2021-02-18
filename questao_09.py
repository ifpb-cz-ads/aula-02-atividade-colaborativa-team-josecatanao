#9. Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.

dias = input("Informe a quantidade de dias: ")

horas = input("Informe a quantidade de horas: ")

minutos = input("Informe a quantidade de minutos: ")

segundos = input("Informe a quantidade de segundos: ")

tot_seg = (((dias * 24 + horas) * 60 + minutos) * 60 + segundos)

print (tot_seg)