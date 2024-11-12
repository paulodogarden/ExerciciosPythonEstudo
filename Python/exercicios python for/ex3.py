#. Crie um programa que imprime a tabuada de um número qualquer digitado
#pelo usuário.
num = int(input("Digite um número: "))
tabuada= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("[TABUADA DO NÚMERO",num,"]")
for vezes in tabuada:
  print(vezes,"x", num," =",vezes*num)
