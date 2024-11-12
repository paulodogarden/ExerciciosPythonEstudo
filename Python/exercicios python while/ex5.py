#Exercício 5. Crie um programa que solicita o time de 10 usuários pelo teclado. Ao final,
#imprima quantos torcedores torcem para o Grêmio.
cont = 0
contGremio = 0
while cont < 3:
  time = input("Digite seu time: ")
  if time == "Gremio" or time == "gremio":
    contGremio += 1
  cont += 1
print("Quantidade de gremista:", contGremio)