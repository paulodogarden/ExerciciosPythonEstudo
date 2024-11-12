count = 0
while count < 10:
  num = int(input("Digite um número: "))
  if num == 0:
    print("[ZERO]")
  elif num > 0:
    print("[Número positivo]:")
  elif num < 0:
    print("[Número negativo]")
  count += 1
    
  