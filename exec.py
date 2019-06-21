#Faça um Programa que peça dois números e imprima o maior deles.

n = float(input("Informe um numero: "))
n1 = float(input("Informe outro numero: "))

if n > n1:
    maior = n
else:
    maior = n1

print("O maior numero é {:.1f}".format(maior))
