from jogabilidade import PassarPelosGuardas

personagem = {
    "nome": "Mario",
    "dinheiro": 30,
    "vida": 50,
    "mochila": [],
    "espada": 30
}

guarda1 = {
        "nome": "Guarda 01",
        "machado": 20,
        "vidasdoguarda": 15,
        "dinheiro": 50
    }
guarda2 = {
        "nome": "Guarda 02",
        "machado": 30,
        "vidasdoguarda": 25,
        "dinheiro": 100
    }
guarda3 = {
        "nome": "Guarda 03",
        "machado": 80,
        "vidasdoguarda": 40,
        "dinheiro": 200
    }

guardas = [guarda1,guarda2,guarda3]


# Ao invés quantidadeGuardas ter uma 
# lista de guardas
quantidadeGuardas = 5

print("Boas vindas ao seu pior pesadelo, está na hora de provar que você não é um mediocre. Mate o rei.")
print(f"Durante o jogo você irá precisar enfrentar desafios gigantes, são {quantidadeGuardas} guardas antes de chegar ao Rei, mate todos eles.")
print(f"Durante a tua vida mediocre, você conseguiu acumular {personagem['dinheiro']}$, antes de cada batalha você pode passar na loja.")

PassarPelosGuardas(guardas,personagem)