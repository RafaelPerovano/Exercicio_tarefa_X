import os
import csv
# Função que verifica se o arquivo existe
def verifica_arquivo(nome_arquivo):
    return os.path.isfile(nome_arquivo)

# Função para adicionar produtos às compras    
def adicionar(compras):
    print('Se deseja parar digite "parar": ')
    while True:
        produto = input('Digite o nome do produto: ')
        if produto == 'parar':
            break
        valor = input('Digite o valor do produto: ')
        if valor == 'parar':
            break

        compras[produto] = valor

    with open('arquivos(compras).txt', 'a') as arquivos:
        for produto, valor in compras.items():
            arquivos.write('produto: {}, valor: {}\n'.format(produto, valor))
    return compras

# Função para visualizar os produtos das compras
def visualizar():
    with open('arquivos(compras).txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

# Função para excluir os produtos das compras
def excluir(compras):
    parar = True
    print('Se deseja parar digite "parar": ')
    while parar:
        produto_cha = str(input('Digite qual produto deseja excluir das compras: '))
        if produto_cha == 'parar':
            break
        elif produto_cha in compras:
            del compras[produto_cha]
        else:
            print('Esse produto nao esta na lista de compras.')
            
    with open ('arquivos(compras).txt', 'w') as arquivos:
        for produtos in compras:
            arquivos.write('produto: {}, valor: {}\n'.format(produtos,compras[produtos]))

    return compras

# Função para atualizar produtos das compras
def atualizar(compras):
    parar = True
    print('Se deseja parar digite "parar": ')
    while parar:    
        produto = str(input('Digite qual o produto que deseja alterar das compras: '))
        if produto == 'parar':
            break
        if produto in compras:
            valor_cha = input('Digite qual o novo valor de {} que deseja alterar: '.format(produto))
            if valor_cha == 'parar':
                break
            produto_cha = str(input('Digite qual o novo nome de {} que deseja alterar: '.format(compras)))
            if produto_cha == 'parar':
                break
            compras[produto] = valor_cha
            compras[produto_cha] = compras.pop(produto)
        else:
            print('O produto nao esta nas compras.')
        
    with open ('arquivos(compras).txt', 'w') as arquivos:
        for produtos in compras:
            arquivos.write('produto: {}, valor: {}\n'.format(produtos,compras[produtos]))

    return compras

# Função para somar os valores dos produtos das compras
def somar(compras):
    soma = 0
    for produtos in compras:
        soma += int(compras[produtos])
    print('O valor total das compras são:',soma)
    return soma
def importar_compras():
    dados = {}
    with open('arquivos(compras).txt', 'r') as arquivo:
        for linha in arquivo:
            produto = linha.split('produto: ')[1].split(', ')[0].strip()
            valor = linha.split('valor: ')[1].split(', ')[0].strip()

            novos_dados = {produto:valor}
            dados.update(novos_dados)

    return dados