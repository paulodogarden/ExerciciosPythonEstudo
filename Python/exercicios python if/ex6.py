#Exercício 6. Crie um programa que aplica uma taxa de juros em um determinado preço
#digitado pelo teclado. A taxa aplicada deve ser:
#• Aumento de 10% caso o valor seja menor do que 100
#• Aumento de 20% caso o valor esteja entre 100 (inclusive) e 300
#• Aumento de 50% caso o valor esteja entre 300 (inclusive) e 1000
#• Imprima uma mensagem de erro se o valor for negativo
#• Ao final, seu programa deve imprimir o novo valor, já com a taxa aplicada.

preco = float(input("Digite o preço [R$] do produto: "))
if preco <= 0:
  print("==ERRO!!==")
elif preco > 0 and preco < 100:
  preco = preco + preco * 0.1
elif preco >= 100 and preco < 300:
  preco = preco + preco * 0.2
elif preco >= 300 and preco < 1000:
  preco = preco + preco * 0.5
print("Valor com taxa de juros aplicada:" ,preco)