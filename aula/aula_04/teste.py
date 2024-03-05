
# Exercicio 20 - Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas.

alunos: dict = {"aluno_02":"Jose","aluno_01":"Leonardo", "aluno_05":"Felipe", "aluno_03":"Paulo", "aluno_06":"Mateus", "aluno_04":"Kleber"}
ordem_alunos: list = [] 

def ordenador(dicionario: dict):
    dicionario_ordenado = dict(sorted(dicionario.items()))   
    return dicionario_ordenado

print(ordenador(alunos))

# print(ordenador(alunos))