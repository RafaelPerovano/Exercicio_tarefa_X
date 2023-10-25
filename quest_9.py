from Funções_9 import adicionar, visualizar, excluir, atualizar, somar, verifica_arquivo
compras = {}
sair = True
dados = {}
soma = 0
nome_arquivo = 'arquivos(compras).txt'
while sair:
    # Verifica se o arquivo existe
    arquivo_existe = verifica_arquivo(nome_arquivo)
    if arquivo_existe == True:
        # Se o arquivo existir tribui os valores para a variável compras
        with open('arquivos(compras).txt', 'r') as arquivo:   
            for linha in arquivo:
                produto = linha.split('produto: ')[1].split(', ')[0].strip()
                valor = linha.split('valor: ')[1].split(', ')[0].strip()

                novos_dados = {produto:valor}
                compras.update(novos_dados)

        # Interface das opções
        print('[0] Adicionar produtos\n[1] Visualizar a compra\n[2] Excluir produtos da compra\n[3] Atualizar produtos da compra\n[4] Ver o valor total das compras \n[5] Sair da da interface de compra')
        decisao = int(input('Digite o que deseja fazer nas compras: '))
        if decisao == 0:
            compras = adicionar(compras)
        elif decisao == 1:
            visu = visualizar()
        elif decisao == 2:
            compras = excluir(compras)
        elif decisao == 3:
            compras = atualizar(compras)
        elif decisao == 4:
            soma = somar(compras)
        else:
            break
    else:
        print('As compras onde são armazenado os dados dos produtos nao existe ainda, vamos começar adicionando os produtos e seus valores: ')
        compras = adicionar(compras)