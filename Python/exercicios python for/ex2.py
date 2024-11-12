#. Crie um programa que imprime na tela todos os valores entre dois valores
#digitados pelo teclado.
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
if(a > b):
  print("Erro: o primeiro valor deve ser menor do que o segundo!")
else:
  for i in range(a, b+1):
    print(i)

