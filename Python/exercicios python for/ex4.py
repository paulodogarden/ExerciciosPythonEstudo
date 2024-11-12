#Sabendo que uma string é uma lista de letras, peça para o usuário digitar
#um texto e imprima na tela a quantidade de vogais que existem no texto.
vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
count = 0
texto = input("Digite um texto: ")
for i in texto:
  if i in vogais:
    count += 1
    

print(count)