# Desafio Aula 03

# Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas

while True:
    nome = input("Digite seu nome: ")
    if nome.isalpha() and len(nome) >= 2:
        print(f'Registrado: {nome}')
        break
    else:
        print('Erro de Caracteres: Digite um nome valido')

while True:
    try:
        salario = float(input("Digite o valor do seu salario: "))
        if salario > 0:
            print(f'Registrado: {salario}')
            break
        else:
            print('Erro de Valor Negativo: Digite um valor positivo')
    except:
        print('Erro de Valor Invalido: Digite um valor valido')

try:
   bonus_perc = float(input("Digite a porcentagem do seu bonus recebido: "))
   if bonus_perc > 0:
       print(f'Registrado: {bonus_perc}')
   else:
       print('Erro de Valor Negativo: Digite um valor positivo')
except:
    print('Erro de Valor Invalido: Digite um valor de bonus valido')


bonus_perc = bonus_perc / 100
bonus_fixo = 1000
bonus = bonus_fixo + salario * bonus_perc

if bonus < 0:
    print('Erro de sistema: Problema com sistema, volte mais tarde!')

print(f'Ola {nome}, seja muito bem vindo ao Portal Finanças')
print(f'Seu salario é de: R$ {salario}')
print(f'Seu bonus foi de: R$ {bonus}')

# Encontrei 7 possiveis bugs, e tentei implmentar processos de validação para garantir a qualidade e imprimir os erros caso necessario.

