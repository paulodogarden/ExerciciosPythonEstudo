#. Crie um programa que recebe dois valores inteiros pelo teclado e imprime qual dos dois é maior.
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1 > n2 :
  print("O número", n1 ,"é maior que o", n2, "!!")
elif n1 == n2:
  print("Os números são iguais!!")
else:
  print("O número", n2 ,"é maior que o", n1, "!!")