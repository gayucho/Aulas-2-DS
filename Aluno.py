nota1 = int (input("Escreva sua primeira nota: "))
nota2 = int (input("Escreva sua Segunda nota: "))
soma = int (nota1 + nota2)
media = int (soma / 2)

if media >= 5:
    print("APROVADO!")
else:
    print("REPROVADO!")