#Crie um programa que exibe um menu de calculadora na tela. O menu
#exibido deve ser o seguinte:
#• Digite 1 para somar dois valores
#• Digite 2 para subtrair dois valores
#• Digite 3 para multiplicar dois valores
#• Digite 4 para dividir dois valores
#• Digite 5 para realizar uma potência entre dois valores
#• Digite 6 para realizar uma radiciação entre dois valores
#• Digite qualquer outro número para sair
#De acordo com a opção informada pelo usuário, solicite os valores necessários para o
#usuário e imprima na tela o resultado da operação realizada.

print("==CALCULADORA==")
print("[Digite [1] para somar dois valores]")
print("[Digite [2] para subtrair dois valores]")
print("[Digite [3] para multiplicar dois valores")
print("[Digite [4] para dividir dois valores]")
print("[Digite [5] para realizar uma potência entre dois valores]")
print("[Digite [6] para realizar uma radiciação entre dois valores]")
print("[Digite qualquer outro número para sair]")
op = int(input())
if op == 1:
  n1 = int(input("Digite o primeiro valor: "))
  n2 = int(input("Digite o primeiro valor: "))
  print("[RESULTADO]: ",n1 + n2)
elif op == 2:
  n1 = int(input("Digite o primeiro valor: "))
  n2 = int(input("Digite o primeiro valor: "))
  print("[RESULTADO]: ",n1 - n2)
elif op == 3:
  n1 = int(input("Digite o primeiro valor: "))
  n2 = int(input("Digite o primeiro valor: "))
  print("[RESULTADO]: ",n1 * n2)
elif op == 4:
  n1 = int(input("Digite o primeiro valor: "))
  n2 = int(input("Digite o primeiro valor: "))
  print("[RESULTADO]: ",n1 / n2)
elif op == 5:
  n1 = int(input("Digite o primeiro valor: "))
  n2 = int(input("Digite o primeiro valor: "))
  print("[RESULTADO]: ",n1 ** n2)
elif op == 6:
  n1 = int(input("Digite o primeiro valor: "))
  n2 = int(input("Digite o primeiro valor: "))
  print("[RESULTADO]: ",n1 ** (1/n2))
else:
  print("[Você saiu!]")
