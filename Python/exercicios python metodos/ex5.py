#: Crie um método que recebe dois parâmetros, que serão um inteiro N e uma string
#S (nesta ordem). O método deve imprimir na tela N vezes a string S

def texto():
  S = input("Digite uma palavra: ")
  N = int(input("Quantas vezes quer essa palavra? "))
  count = 0
  while count < N:
    count +=1
    print("[",S,"]")

texto()