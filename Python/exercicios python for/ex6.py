#Exercício 6. Crie um programa que solicita o nome e o estado civil de 20 pessoas pelo
#teclado. Ao final, imprima apenas o nome das pessoas separadas por estado civil:
#solteiras, casadas, divorciadas e viúvas (nesta ordem!)
solteiro = []
casado = []
divorciado = []
viuvo = []

for i in range(0,20):
  nome = input("[Digite seu nome]: ")
  estadocivil = input("[Digite seu estado civil]: ")
  if estadocivil == "solteiro" or estadocivil == "solteira":
    solteiro.append(nome)
  elif estadocivil == "casado" or estadocivil == "casada":
    casado.append(nome)
  elif estadocivil == "divorciado" or estadocivil == "divorciada":
    divorciado.append(nome)
  elif estadocivil == "viuvo" or estadocivil == "viuva":
    viuvo.append(nome)
print("=ESTADO CIVIL=")
print("[Solteiros]:",solteiro)
print("[Casados]:",casado)
print("[Divorciados]:",viuvo)
print("[Viuvos]:",divorciado)