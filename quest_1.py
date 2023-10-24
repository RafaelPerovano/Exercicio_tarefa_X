from funções import criar_arquivo_estudantes
dados ={}
parar = True
print('Se deseja parar digite "parar".')
while parar:
    nome = input('Digite o nome da aluno: ')
    if nome == 'parar':
        break
    idade = input('Digite a idade da aluno: ')
    if idade == 'parar':
        break
    curso = input('Digite o curso que o aluno está cursando: ')
    if curso == 'parar':
        break
    
    novos_dados = {nome:{'idade':idade,'curso':curso}}
    dados.update(novos_dados)
    
criar_arquivo = criar_arquivo_estudantes(dados)