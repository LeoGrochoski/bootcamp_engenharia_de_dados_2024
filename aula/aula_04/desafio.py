# Aula 4

while True:
    nome: str = input("Digite seu nome: ")
    if nome.isalpha() and len(nome) == 0:
        raise ValueError('Erro: O nome não pode estar em branco')
    elif nome.isalpha() and len(nome) >= 2:
        print(f'Nome Registrado: {nome}')
        break
    else:
        print('Erro: Digite um nome valido')

while True:
    try:
        salario: float = float(input("Digite o valor do seu salario: "))
        if salario > 0:
            print(f'SalarioRegistrado: {salario}')
            break
        else:
            print('Erro: Digite um valor positivo')
    except:
        print('Erro: Digite um valor valido')

while True:
    try:
        bonus_perc: float = float(input("Digite a porcentagem do seu bonus recebido: "))
        if bonus_perc < 0:
            print('Erro: A porcentagem do bonus não pode ser negativa')
        else:
            print(f'Bonus Registrado: {bonus_perc}')    
            break
    except ValueError: 
        print('Erro: Digite um valor de bonus valido')


bonus_perc: float = bonus_perc / 100
bonus_fixo: int = 1000
bonus: float = bonus_fixo + salario * bonus_perc

if bonus < 0:
    print('Erro de sistema: Problema com sistema, volte mais tarde!')

print(f'Ola {nome}, seja muito bem vindo ao Portal Finanças')
print(f'Seu salario é de: R$ {salario:.2f}')
print(f'Seu bonus foi de: R$ {bonus:.2f}')

