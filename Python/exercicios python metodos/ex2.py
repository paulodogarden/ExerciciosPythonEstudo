#Crie um método chamado maiorValor que recebe 3 valores por parâmetro (assuma
#que serão inteiros) e retorna o maior dos três valores.

val1 = int(input("Digite o primeiro número: "))
val2 = int(input("Digite o segundo número: "))
val3 = int(input("Digite o terceiro número: "))
def maiorValor (a, b, c):
  if a > b and a > c:
    print("O maior valor é", a)
  elif b > a and b > c:
    print("O maior valor é", b)
  elif c > b and c > a:
    print("O maior valor é", c)

maiorValor(val1, val2, val3)




  
