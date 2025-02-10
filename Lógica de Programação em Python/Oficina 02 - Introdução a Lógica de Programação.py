import math

def soma(n1,n2):
  return n1+n2

def equacao(n1,n2,n3,n4):
  return ((n1*n2) + (n3/n4))

def areaCirculo(r):
  return (math.pi*r*r)

def restoDivisao(n1,n2):
  return (n1 % n2)

# Escreva um programa que exiba o resultado da soma 25+17.
print(soma(25,17))

# Faça um programa que calcule e exiba o resultado da expressão (12×8)+(45÷5)
print(equacao(12,8,45,5))

# Crie um programa que exiba o valor da área de um círculo com raio 5. Fórmula: Área=π×raio² -  π=3.14159.
print(areaCirculo(5))

# Faça um programa que exiba o resultado do resto da divisão de 100 por 7.

print(restoDivisao(100,7))