# Faça um Programa que leia três números e mostre-os em ordem decrescente.

n = int(input("Informe um numero: "))
n1 = int(input("Informe um numero: "))
n2 = int(input("Informe um numero: "))

if n > n1 and n > n2 and n1 > n2:
    ordem = n, n1, n2
elif n > n2 and n > n1 and n1 < n2:
    ordem = n, n2, n1
elif n1 > n2 and n1 > n and n > n2:
    ordem = n1, n, n2
elif n1 > n and n1 > n2 and n < n2:
    ordem = n1, n2, n
elif n2 > n1 and n2 > n and n > n1:
    ordem = n2, n, n1
else:
    ordem = n2, n1, n

print(ordem)
