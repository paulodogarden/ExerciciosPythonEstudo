#Crie um programa que pede para o usuário digitar números positivos via
#Teclado. Quando o usuário digitar um número negativo, informe a média de todos os
#números que ele informou.
total = 0
quant = 0

while True:
  valor = int(input("Digite um valor positivo (negativo para sair): "))
  if valor < 0:
    break
  total += valor
  quant += 1

print("M�dia dos valores digitados:",(total/quant))