produto1: str = "Agua"
produto2: str = "Bolacha Agua e Sal"
produto3: str = "Leite Integral"
produto4: str = "Pão de Forma"

produtos: list = []

produtos.append(produto1)
produtos.append(produto2)
produtos.append(produto3)
produtos.append(produto4)

print(produtos)

produtos.pop()

print(produtos)

numeros = []

numeros.extend(range(1,5))

print(numeros)