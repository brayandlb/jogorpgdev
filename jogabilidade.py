from batalha import batalhar
from loja import barganhar
from random import randint

def escolherAcao(guarda, personagem):
    print("Escolha o que você quer fazer?")
    print(f"[1] - Batalha com o guarda nº {guarda}")
    print("[2] - Entrar na loja")

    escolha = int(input())
    if (escolha == 1):
        # que pra batalha é importe também passar 
        # o guarda envolvido / o inimigo
        personagem = batalhar(personagem)
    elif (escolha == 2):
        personagem = barganhar(personagem)

    return personagem



def PassarPelosGuardas(quantidadeGuardas,personagem):
    for guarda in range(guardas):
        print("lutem")

        if personagem["espada"] >= guarda["machado"]:
            personagem["espada"] -= guarda["machado"]
            print(f"voce destroiu a espada do {guarda}")
        else:
            print("sua espada foi destruida")

        if personagem["vida"] >= guarda["machado"]:
            personagem["vida"] -= guarda["vidasdoguarda"]
            print("voce sobreviveu a luta")
            personagem["dinheiro"] += guarda["dinheiro"]
        else:
            print("voce morreu")
            
        if personagem["vida"] <= 0:
            print("game over")
        else:
            escolherAcao(guarda, personagem)