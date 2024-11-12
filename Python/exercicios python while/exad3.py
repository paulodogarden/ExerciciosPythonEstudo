#Faça um programa que escreva na
#tela todos os valores inteiros que estão entre dois
#valores digitados pelo usuário (num1 e num2).
#Caso num1 seja maior do que num2, imprima uma
#mensagem de erro e não imprima.
count = 0
num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))
if num1 > num2:
  print("=ERRO[num 1 > num2]=")
while num1 < num2 - 1 :
    num1 += 1
    print(num1)