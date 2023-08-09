def barganhar(personagem):
    return personagem

    print("loja")
    print("[1] - poção de vida : 10 R$ , aumenta 50")
    print("[2] - durabilidade espada: 15 R$, aumenta 40 de durabilidade")
    print("[3] - espada de diamante: 150 R$ , 500 de poder")
    print("[4] poção do sono: 50 , faz o personagem dormir")
    print()
    print("escolha um item da loja:")
    escolhaitem = input()
    if escolhaitem == 1:
        personagem["vida"] += 50
        personagem["dinheiro"] -= 10

    elif escolhaitem == 2:
        personagem["espada"] += 40
        personagem["dinheiro"] -= 15

    elif escolhaitem == 3:
        bladeofolympus = 500
        personagem["mochila"].append(bladeofolympus)

    elif escolhaitem == 4:
        pocaodosono = guarda["vidadoguarda"] - guarda["vidadoguarda"], guarda["machado"] - guarda["machado"]
        personagem["mochila"].append(pocaodosono)

    else:
        print("não temos esse item na loja")
