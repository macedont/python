#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


sexo = str(input("Informe seu sexo [M/F]: ")).upper()

if sexo == "M":
    print("você é do sexo Masculino!")
elif sexo == "F":
    print("Você é do sexo Feminino")
else:
    print("Sexo Inválido!")
