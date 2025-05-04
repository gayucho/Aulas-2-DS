soma = 0
quantidade = 0
continuar = 1
while continuar != 0:
    numero = int(input("Digite um número: "))
    soma += numero
    quantidade += 1
    continuar = int(input("Deseja continuar? (0 - Não, 1 - Sim): "))

print("A soma dos números é:", soma)
print("A quantidade de números digitados é:", quantidade)
