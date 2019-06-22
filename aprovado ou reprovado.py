#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.

n = float(input("Informe a sua primeira nota: "))
n1 = float(input("Informe a sua segunda nota: "))

nota = (n + n1) / 2

if nota >= 7 and nota < 10:
    situacao = "Aprovado!"
elif nota == 10:
    situacao = "Aprovado com distinção!"
else:
    situacao = "Reprovado!"

print(situacao)
