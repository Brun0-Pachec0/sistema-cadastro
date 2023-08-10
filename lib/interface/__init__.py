def val_idade(msg):
    while True:
        dado1 = str(input(f'{msg}'))
        if dado1.isnumeric():
            return dado1
        else:
            print('Opção inválida!')

def titulo(msg):
    print(20 * '--')
    print(f'{msg}'.center(40))
    print(20 * '--')

def titulomenu(msg):
    print(30 * '--')
    print(f'{msg}'.center(40))
    print(30 * '--')

def programa_principal():
    from time import sleep
    geral = list()
    dados = dict()
    arq = 'pessoasCadastradas.txt'
    from lib.arquivo import lerarquivo, cadastrar
    # importei o modulo 'arquivo' para poder colocar a função 'ler arquivo' na opc 1
    while True:
        titulo('MENU PRINCIPAL')
        try:
            escolha = int(input('\033[33m[1] - \033[34mVer pessoas cadastradas\n\033[33m[2] - \033[34mCadastrar nova pessoa\n\033[33m[3] - \033[34mSair do sistema\n\033[33mSua opção:\033[m'))
        except:
            print('\033[31mOpção inválida!! Digite uma opção válida.\033[m')
            sleep(1)
            continue
        if escolha == 0 or escolha >= 4:
            # Opções inválidas
            print('\033[31mOpção inválida!! Digite um opção válida.\033[m')
            sleep(0.5)
        elif escolha == 2:
            # Opção 2 para cadastrar uma nova pessoa
            titulo('NOVO CADASTRO')
            nome = str(input('Nome:')).capitalize().strip()
            idade = val_idade('Idade:')
            sexo = str(input('Sexo [M/F]:')).upper().strip()
            while True:
                if sexo == 'M' or sexo == 'F':
                    break
                else:
                    sexo = str(input('Informe um sexo válido! \nSexo [M/F]:')).upper().strip()
            cadastrar(arq, nome, idade, sexo)
        elif escolha == 1:
            # Opção 1 para mostrar todas as pessoas cadastradas
            lerarquivo('pessoasCadastradas.txt')
        elif escolha == 3:
            # Opção 3 para finalizar o programa
            print('\033[34mFinalizando programa...\033[m')
            sleep(1.5)
            titulo('OBRIGADO, VOLTE SEMPRE!')
            break