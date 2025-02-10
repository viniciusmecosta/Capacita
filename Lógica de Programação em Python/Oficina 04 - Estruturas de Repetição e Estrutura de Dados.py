def imprimiRange(n1, n2):
  for n1 in range (n2):
    print(n1+1)

def lista():
  list_a = [10,20,30,40,50]
  print(list_a[0])

def soma10():
  n=1
  soma = 0
  while (n<11):
    soma = n+soma
    n= n+1
  print(soma)

def idade():
  dicio = {"nome": "Ana", "idade": 25, "cidade": "Fortaleza"}
  print(dicio["idade"])

def inverteString(string):
  return string[::-1]

def frequencia(string):
  freq = {}
  for char in string:
    if char in freq:
      freq[char] += 1
    else:
      freq[char] = 1
  return freq

# Crie um programa que use um laço for para imprimir os números de 1 a 5 no console.
imprimiRange(1,5)

# Escreva um programa que declare uma lista com os números [10, 20, 30, 40, 50] e exiba o primeiro elemento.
lista()

# Faça um programa que use um laço while para somar todos os números de 1 a 10 e exiba o resultado no console.
soma10()

# Crie um programa que declare um dicionário com as seguintes chaves e valores: {"nome": "Ana", "idade": 25, "cidade": "Fortaleza"} e exiba o valor associado à chave "idade"
idade()

# Escreva um programa que inverta uma string utilizando um laço for. Por exemplo, para a string "Python", o resultado deve ser "nohtyP".
inverteString("Python")

# Escreva um programa que calcule a frequência de cada caractere em uma string. Por exemplo, na string "banana", o programa deve exibir: {'b': 1, 'a': 3, 'n': 2}
frequencia("banana")