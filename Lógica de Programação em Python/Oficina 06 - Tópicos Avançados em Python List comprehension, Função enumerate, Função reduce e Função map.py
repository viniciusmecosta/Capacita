def indices(lista):
  for i, valor in enumerate(lista):
        print(f"Índice {i}: {valor}")

def pares():
  return [x for x in range(1, 11) if x % 2 == 0]

def multiplicar_tres(lista):
  return list(map(lambda x: x * 3, lista))

def indices_quadrados(lista):
  return [(i, x**2) for i, x in enumerate(lista)]

# Escreva um código usando enumerate para exibir os índices e valores da lista ["maçã", "banana", "uva"].
indices(["maçã", "banana", "uva"])

# Crie uma lista com os números pares de 1 a 10 usando List Comprehension.
print(pares())

# Escreva um programa que use map para multiplicar cada elemento da lista [1, 2, 3, 4] por 3.
print(multiplicar_tres([1, 2, 3, 4]))

# Escreva um programa que use enumerate e List Comprehension para criar uma lista de tuplas com os índices e valores ao quadrado de [2, 4, 6]
print(indices_quadrados([2, 4, 6]))