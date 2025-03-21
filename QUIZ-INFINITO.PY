import random
quer_continuar = True
contador = 1
acertos = 0
erros = 0
while(quer_continuar):
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    print(f"Q{contador}:{n1}+{n2}")
    
    resp = int(input("R:"))
    if(resp == n1 + n2):
        print("Acertou imbecil!")
        acertos+=1
       
    else:
        print("Mula do caralho")
        erros+=1
    contador = contador+1
    continuar = input("Quer continuar? [1]SIM [2]Não? ")
    if(continuar == 2):
        quer_continuar = False


print("FIM")