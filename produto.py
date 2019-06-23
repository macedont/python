# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p = float(input("Informe o preço de um produto: "))
p1 = float(input("Informe o preço de um produto: "))
p2 = float(input("Informe o preço de um produto: "))

if p < p1 and p < p2:
    menor = p
elif p1 < p2 and p1 < p:
    menor = p1
else:
    menor = p2

print("Voce deve comprar o produto com o preço de: R${:.2f}".format(menor))
