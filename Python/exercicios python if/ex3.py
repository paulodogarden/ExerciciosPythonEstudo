#Crie um programa que recebe dois valores inteiros A e B 
# pelo teclado eimprime o valor de A dividido por B. 
# Entretanto, se o valor de B for 0, imprima uma mensagem de erro e não faça a divisão.
A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))
while B == 0:
  print("Erro!!")
  B = int(input("Digite o segundo número: "))
print("O valor de", A ,"divido por", B ,"é",(A/B))