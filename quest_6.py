from Funções import ler_arquivos_estudantes

dados = {}
dados = ler_arquivos_estudantes()
soma = 0

for nomes in dados:
    soma += int(dados[nomes]['idade'])
media = soma/len(dados)

print('A media da idade dos alunos é',media)