#Exercício 7. Crie um programa que solicita para o usuário que ele digite 10 valores
#inteiros. Ao final, imprima a soma de todos os valores digitados.

count = 0
soma = 0
while count < 10:
  soma += int(input("Digite um valor: "))
  count += 1
print("A soma dos valores é: ",soma)