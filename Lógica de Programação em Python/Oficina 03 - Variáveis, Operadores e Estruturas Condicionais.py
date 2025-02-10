def range10():
  n = int (input("Digite um numero: "))
  if (n>10):
    print("Sim")
  else:
    print("Não")

def potencia(n):
  return n**3

def repeteString(n):
  return n*5

def media(n1,n2,n3):
  media = (n1+n2+n3)/3
  if (media>20):
    print("Maior que 20")
  elif (media<20):
    print("Menor que 20")
  else:
    print("Igual a 20")

def divisivel(n):
  if (n%3==0 and n%5==0):
    print("Divisível por 3 e 5")
  else:
    print("Não é divisível")

# Crie um programa que verifique se o número 15 é maior que 10 e exiba "Sim" ou "Não" no console.
rangeN()

# Escreva um programa que use o operador ** para calcular 2³ e exiba o resultado.
print(potencia(2))

# Crie um programa que use o operador * para repetir a string "Oi!" cinco vezes.
print(repeteString("Oi!"))

# Escreva um programa que calcule a média de três números inteiros 10, 20 e 30, e exiba no console se a média é maior, menor ou igual a 20.
media(10,20,30)

# Crie um programa que determine se o número 45 é divisível por 3 e por 5 simultaneamente. O programa deve exibir "Divisível por 3 e 5" ou "Não é divisível .
divisivel(45)