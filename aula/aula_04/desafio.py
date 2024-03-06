# Desafio Aula 4

# Inclui funções para as validações de nome e salario, bonus e o calculo do bonus, 
# chamamos função por função para prosseguir no sistema.
# Inclui type hint nas variaveis como boa pratica de codigo.

def validacao_nome() -> str:
    while True:
        try:
            nome: str = input("Digite o nome: ")
            if nome.strip().isalpha() and len(nome.strip()) >= 2:
                return nome
            else:
                raise ValueError('Erro: Digite um nome válido')
        except ValueError as e:
            print(e)

nome_valido = validacao_nome()
print("Nome Registrado")

def validacao_salario() -> float:
    while True:
        try:
            salario: float = float(input("Digite o valor do seu salario: "))
            if salario > 0:
                return salario
            else:
                raise ValueError('Erro: Digite um valor positivo')
        except ValueError:
            print("Não foi possivel efetuar a conversão de tipo de dados")
            
salario_valido = validacao_salario()
print("Salario Registrado")

def validacao_bonus() -> float:
    while True:
        try:
            bonus_perc: float = float(input("Digite a porcentagem do seu bonus recebido: "))
            if bonus_perc > 0:
                return bonus_perc
            else:
                raise ValueError('Erro: A porcentagem do bonus não pode ser negativa')
        except ValueError: 
            print('Erro: Digite um valor de bonus valido')

bonus_valido = validacao_bonus()
print(f"Bonus Registrado")    

def calc_bonus() -> float:
    bonus_perc: float = bonus_valido / 100
    bonus_fixo: int = 1000
    bonus: float = bonus_fixo + salario_valido * bonus_perc
    if bonus < 0:
        print('Erro de sistema: Problema com sistema, volte mais tarde!')
    else:
        return bonus
    
bonus_calculado = calc_bonus()
print("Calculo Registrado")

def mensagem_usuario(nome: str, salario: float, bonus: float) -> str:
    return f'''Ola {nome}, seja muito bem vindo ao Portal Finanças'
                 Seu salario é de: R$ {salario:.2f}
                 Seu bonus foi de: R$ {bonus:.2f}'''

