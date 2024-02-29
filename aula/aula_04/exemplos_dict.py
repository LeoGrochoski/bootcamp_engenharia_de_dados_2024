import json

produto01: dict = {
    "Nome":"Bola",
    "Preco":"60.5",
    "Quantidade":"100",
    "disponibilidade": True
}

produto02: dict = {
    "Nome":"Chuteira",
    "Preco":"200",
    "Quantidade":"20",
    "disponibilidade": True
}

produto03: dict = {
    "Nome":"Camiseta",
    "Preco":"80",
    "Quantidade":"5",
    "disponibilidade": False
}

carrinho: list = []

carrinho.append(produto01)
carrinho.append(produto02)

# conversão do dicionario para JSON

carrinho_json = json.dumps(carrinho)
print(carrinho_json)