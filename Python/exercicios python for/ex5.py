#Crie um programa que permita que o usuário crie sua lista de compras.
#Primeiramente, solicite que ele informe quantos produtos serão adicionados na lista.
#Depois disto, peça para que o usuário digite os produtos que ele vai comprar, e
#armazene em uma lista. Ao final, imprima a lista de compras do usuário.
quant = int(input("[Quantos itens terá sua lista de compras?]"))
lista = []
for prod in range (0,quant):
 lista.append(input("Digite um produto: "))
print("[Minha lista de compras]:",lista)