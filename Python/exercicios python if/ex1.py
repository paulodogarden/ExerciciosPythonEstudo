#Exercício 1. Crie um programa que recebe um inteiro pelo teclado e imprime se ele é par ou ímpar.
num = int(input("Digite um número: "))
if num % 2 == 0:
  print("O número", num, "é par!!")
else:
  print("O número", num, "é ímpar!!")