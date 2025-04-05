'''
  Práctica sobre listas
'''

array=["futbol", "Pc", 18.6, 18, [6,7,10.4], True, False]

print("Ejemplo de array")
print(array)
print(array[1])
print(array[4])
print(array[-1])
print(array[0:3])
print(array[:2])
print(array[2:])

print(len(array))

array.append(66)
print(array)

# Indicar la posicion a insertar el valor
array.insert(0, 88)
print(array)


# Agregar valores al final de la lista
array.extend([1, 88, True, 100])
print(array)
