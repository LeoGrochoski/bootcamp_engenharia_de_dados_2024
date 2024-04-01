# Funções são uteis ma reutilização de codigo,
# por exemplo a função abaixo
# Não precisamos ficar criando a operação mais de uma vez,
# Assim podemos chamara a operação assim que precisassemos utilizar.
# Basta chamar a função e incluir ela numa variavel.


def soma(a: float, b: float) -> float:
    operacao: float = a + b
    return operacao


print(soma(5, 6))


def saudacao(nome: str, mensagem: str) -> str:
    return mensagem + "!" + " " + nome


print(saudacao(mensagem="Bem vindo", nome="Lucas"))
