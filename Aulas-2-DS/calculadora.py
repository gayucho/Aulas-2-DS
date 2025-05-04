n1 = int (input("Digite o primeiro número: "))
n2 = int (input("Digite o segundo número: "))
operacao = int (input("Digite a operação desejada: [1]subtração, [2]adição, [3]multiplicação, [4]divisão: "))
if operacao == 1:
    resultado = int (n1 - n2)
elif operacao == 2:
    resultado = int (n1 + n2)
elif operacao == 3:
    resultado = int (n1 * n2)
elif operacao == 4:
    resultado = int (n1 / n2)

print ("O resultado da operação é:",resultado)