from funções import ler_arquivos_estudantes
dados = ler_arquivos_estudantes()
for nomes in dados:
    print(nomes,':', dados[nomes])