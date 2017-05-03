print("Bem Vindo a Adivinha a soma!")
jogador1=input("Por favor digite o nome do jogador 1:")
jogador2=input("Por favor digite o nome do jogador 2:")
print(jogador1," vs ", jogador2)
print("FIGHT!!!")
print('-',jogador1,'-')
soma1=int(input("Por favor digite seu número, entre 1 e 10:"))
while soma1<0 or soma1>10:
    print("O número precisa estar entre 0 e 10.")
    soma1=int(input("Por favor digite seu número:"))
print('-',jogador2,'-')
soma2=int(input("Por favor digite seu número, entre 1 e 10:"))
while soma2<0 or soma2>10:
    print("O número precisa estar entre 0 e 10.")
    soma2=int(input("Por favor digite seu número:"))
somatotal=soma1+soma2
print('-',jogador1,'-')
adv1=int(input("Digite seu palpite:"))
while adv1<0 or adv1>20:
    print("O número precisa estar entre 0 e 20.")
    adv1=int(input("Digite seu palpite:"))
print('-',jogador2,'-')
adv2=int(input("Digite seu palpite:"))
while adv2<0 or adv2>20:
    print("O número precisa estar entre 0 e 20.")
    adv2=int(input("Digite seu palpite:"))
if adv1>somatotal and adv2>somatotal:
    r1=adv1-somatotal
    r2=adv2-somatotal
    if r1<r2:
        print("Jogador 1 ganhou!")
    elif r2<r1:
        print("Jogador 2 ganhou!")
    
if adv1<somatotal and adv2>somatotal:
    r1=adv1-somatotal
    r2=somatotal-adv2
    if r1<r2:
        print("Jogador 1 ganhou!")
    elif r2<r1:
        print("Jogador 2 ganhou!")
    else:
        print("empate")
    if adv1>somatotal and adv2<somatotal:
        r1=somatotal-adv1
        r2=adv2-somatotal
        if r1<r2:
            print("Jogador 1 ganhou!")
        elif r2<r1:
            print("Jogador 2 ganhou!")
        else:
            print("empate")
    if adv1>somatotal and adv2>somatotal:
        r1=somatotal-adv1
        r2=somatotal-adv1
        if r1<r2:
            print("Jogador 1 ganhou!")
        elif r2<r1:
            print("Jogador 2 ganhou!")
        else:
            print("empate")
        
         







