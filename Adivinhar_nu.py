import random
numero = random.randint(1,100)
resposta = 0
tentativas = 0
print("Adivinhe o número entre 1 e 100")

while resposta != numero:
    resposta = int(input("Digite um número: "))
    if resposta < numero:
        print("O número é maior")
    elif resposta > numero:
        print("O número é menor")
    tentativas += 1

print(f"\nVocê acertou o número {numero} em {tentativas} tentativas")