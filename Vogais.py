frase = (input("Digite uma frase: "))
for letra in frase:
    if letra in "aeiouAEIOU":
        print(letra, end=" ")