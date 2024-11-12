#Exercício 8. Crie um programa que pergunta para o usuário (via Teclado) quantos
#números ele irá digitar e armazena em uma variável chamada quant. Logo após, faça
#com que o usuário digite quant números inteiros, e para cada número digitado imprima
#na tela se o número é negativo, positivo ou zero.

count = 0
quant = int(input("Quantos numeros gostaria de digitar?"))
while (count) < (quant):
  numero =int(input("Digite um número: "))
  count += 1
  if numero == 0:
    print("O número é zero[0]")
  elif numero > 0:
    print("O número", numero ,"é positivo")
  elif numero < 0:
    print("O número", numero ,"é negativo")