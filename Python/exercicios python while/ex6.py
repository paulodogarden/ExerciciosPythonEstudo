#Exercício 6. Crie um programa que pede para o usuário digitar 20 números com ponto
#flutuante pelo teclado. Ao final, seu programa deve imprimir todos os números
#digitados. Dica: armazene-os em uma string e concatene os valores digitados. No final,
#imprima a string.
cont = 0
numeros = ""
while cont < 20:
  valor = float(input("Digite um valor com ponto flutuante:"))
  numeros = numeros + str(valor)+ "\n"
  cont += 1
print("Valores digitados:\n"+numeros)