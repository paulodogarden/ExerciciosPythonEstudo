#Exercício 7. Crie um programa que recebe um valor inteiro referente a um
#determinado ano. Imprima na tela se o ano informado é bissexto ou não.

ano = int(input("Digite o ano: "))
if ano % 4 == 0:
  print("O ano", ano ,"é bissexto!")
else:
  print("O ano", ano ,"não é bissexto")