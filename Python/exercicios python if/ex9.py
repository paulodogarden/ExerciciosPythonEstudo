#Exercício 9. Crie um programa que recebe a nota do Grau A e a nota do Grau B pelo
#teclado e imprime na tela se será necessário ou não realizar o Grau C (considere o
#sistema de avaliação da Unisinos). Caso algum valor informado seja negativo, informe
#uma mensagem de erro e não realize o cálculo.

grauA = float(input("Digite a nota de [GRAU A]: "))
grauB = float(input("Digite a nota de [GRAU B]: "))
grauA = grauA * 0.30
grauB = grauB * 0.70
media = grauA + grauB
if media >= 6:
  print("Não será necessario realizar a prova de GRAU C, pois sua nota é", media,"!")
else:
  print("Será necessario realizar a prova de GRAU C, pois sua nota é", media,"!")