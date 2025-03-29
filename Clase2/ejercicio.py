'''
  Ejercicio 1: 
  Crear un programa que pida dos números
  y obtenga como resultado cuál de ellos es par
  o si ambos lo son.
'''

def is_int(nro):
  try:
    return int(nro)
  except:
    return None

def validate(nro):
  if nro == "0":
    nro = "stop"
  else:
    nro = is_int(nro)
  while nro == None or not nro:
    nro= input("Error, ingrese un número:")
    nro = is_int(nro)
    if nro == 0:
      nro = "stop"

  return nro

while True:
  print("\n----------------------------------")
  print("¿PAR O IMPAR? (ingrese 0 (cero) para terminar)")

  n1= input("Ingrese un número entero:")
  n1 = validate(n1)  
  if n1 == "stop":
    break

  n2= input("Ingrese el siguiente número entero:")
  n2 = validate(n2) 
  if n2 == "stop":
    break 

  if (n1 % 2 == 0) and (n2 % 2 == 0):
    print(f"Los números {n1} y {n2} son pares.")
  elif (n1 % 2 == 0) and (n2 % 2 == 1):
      print(f"El número {n1} es par y {n2} es impar.")
  elif (n1 % 2 == 1) and (n2 % 2 == 0):
      print(f"El número {n1} es impar y {n2} es par.")
  else:
    print(f"Los números {n1} y {n2} son impares.")

