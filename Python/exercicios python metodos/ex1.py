#Crie um método que recebe dois valores val1 e val2 (assuma que serão inteiros). O
#método deve retornar verdadeiro se val1 for divisível por val2 e falso caso contrário.

val1 = int(input("Digite um numero: "))
val2 = int(input("Digite outro numero: "))
def nomeMetodo (a, b):
  if a % b == 0:
    print("[VERDADEIRO]")
  else:
    print('[FALSO]')

nomeMetodo(val1, val2)
