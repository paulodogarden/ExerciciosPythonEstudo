#Crie um método que recebe um valor por parâmetro (assuma que será inteiro) e
#retorna a soma de todos os valores entre 0 e o valor recebido. Caso o valor seja negativo, o
#método deve retornar -1.

val = int(input("Digite um valor: "))
def valor(a):
  count = 0
  num = 0
  if a < 0:
    print("-1")
  else:
    while count < a:
      count +=1
      num += count
      print(count,"+")
    print("RESULTADO =",num)
      

valor(val)
  