#Exercício 4. Crie um programa que recebe três valores inteiros 
# pelo teclado e imprime qual dos três é menor.
A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))
C = int(input("Digite o terceiro número: "))
if A < B and A < C:
  print("O menor número é", A,"!!")
elif B < A and B < C:
  print("O menor número é", B,"!!")
else:
  print("O menor número é", C,"!!")