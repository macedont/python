letra = str(input("Informe uma letra para saber se é vogal ou consoante: ")).lower()

if letra in ["a", "e", "i", "o", "u"]:
    print("A letra {} é uma vogal!".format(letra))
else:
    print("A letra {} é uma consoante!".format(letra))
