def criar_arquivo_estudantes(dados):
    with open ('alunos.txt', 'w') as arquivos:
        for nomes in dados:
            arquivos.write('nome: {}, idade: {}, curso: {}\n'.format(nomes, dados[nomes]['idade'], dados[nomes]['curso']))

def inserir_no_arquivo_estudantes(dados):
    with open ('alunos.txt', 'a') as arquivos:
        for nomes in dados:
            arquivos.write('nome: {}, idade: {}, curso: {}\n'.format(nomes, dados[nomes]['idade'], dados[nomes]['curso']))

def ler_arquivos_estudantes():
    dados = {}
    with open('alunos.txt', 'r') as arquivo:
        for linha in arquivo:
            nome = linha.split('nome: ')[1].split(', ')[0].strip()
            idade = linha.split('idade: ')[1].split(', ')[0].strip()
            curso = linha.split('curso: ')[1].split(', ')[0].strip()

            novos_dados = {nome: {'idade': idade, 'curso': curso}}
            dados.update(novos_dados)
    return dados

def imprimir(dados):
    for nomes in dados:
        print('nome: {} : idade: {} | curso: {}\n'.format(nomes, dados[nomes]['idade'], dados[nomes]['curso']))
        
def mudar():
    dados = ler_arquivos_estudantes()
    nome_cha = str(input('Digite qual nome deseja alterar os dados: '))

    if nome_cha == 'parar':
        return 'parar'
    
    if nome_cha in dados:
        idade_cha = int(input('Digite qual a nova idade de {} que deseja alterar: '.format(nome_cha)))
        curso_cha = str(input('Digite qual o novo curso de {} que deseja alterar: '.format(nome_cha)))
        dados[nome_cha]['idade'] = idade_cha
        dados[nome_cha]['curso'] = curso_cha
        
        mudar_arquivos = criar_arquivo_estudantes(dados)
    else:
        print('O nome nao esta nos arquivos.')

    return dados

def excluir():
    dados = ler_arquivos_estudantes()
    nome_cha = str(input('Digite qual nome deseja excluir dos dados: '))

    if nome_cha == 'parar':
        return 'parar'
    if nome_cha in dados:
        del dados[nome_cha]
    else:
        print('Esse nome nao esta nos dados')
    criar_arquivo_estudantes(dados)
    
    return dados