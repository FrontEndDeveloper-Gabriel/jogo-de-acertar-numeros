n1 = [3,2,1]
for c in n:
    randomico = random.randint(1,10)
    meu_numero = int(input("Digite seu número: "))
    numero_adversario = int(input("Número adversário: "))
    

    if randomico == meu_numero and numero_adversario == randomico:
        c = c - 1
        print(f"Parabéns! Ambos os jogadores acertaram o número {randomico}!")
        break
    elif meu_numero == randomico:
        print(f"Minha aposta acertou o número {randomico} em {c} tentativas.")
        print(f"Aposta adversária errou. O número era {randomico}.")
        break
    elif numero_adversario == randomico:
        print(f"Aposta adversária acertou o número {randomico} em {c} tentativas.")
        print(f"Minha aposta errou. O número era {randomico}.")
        break
    else:
        print("Nenhum dos jogadores acertou. Tente novamente!")
