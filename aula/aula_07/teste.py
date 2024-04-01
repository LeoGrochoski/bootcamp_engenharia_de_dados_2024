import random

notas = []
for i in range(5):
    notas.append(random.randint(1, 10))


def media_valores(lista_valores: list) -> float:
    media_numeros: float = sum(lista_valores) / len(lista_valores)
    return media_numeros


media_notas: float = media_valores(notas)

lista_quadrado_diferenca = []


def quadrado_diferenca(lista_valores: list) -> list:
    for valor in lista_valores:
        lista_quadrado_diferenca.append((valor - media_notas) ** 2)
    return lista_quadrado_diferenca


quadrado_diferenca_valores: list = quadrado_diferenca(notas)


def variancia_conjunto(lista_valores: list):
    variancia = sum(lista_valores) / len(lista_valores)
    return variancia


valor_variancia = variancia_conjunto(quadrado_diferenca_valores)


def desvio_padrao(valor: float) -> float:
    desvio_padrão = valor**0.5
    return desvio_padrão


dp: float = desvio_padrao(valor_variancia)
print(f"O valor do Desvio Padrão da lista: {notas} é de {dp}")
