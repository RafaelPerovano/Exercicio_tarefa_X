from funções import ler_arquivos_estudantes

dados = ler_arquivos_estudantes()
parar = True
print('Se deseja parar digite "parar".')
while parar:
    procurar = str(input('Digite o nome de quem deseja verificar os dados: '))
    if procurar == 'parar':
        break
    else:
        if procurar in dados:
            print(dados[procurar])
        else:
            print('Esse nome nao existe no banco de dados')