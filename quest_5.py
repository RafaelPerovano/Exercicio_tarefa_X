from funções import excluir
parar = True
print('Se deseja parar digite "parar".')
dados = {}
while parar:
    deletar = excluir()
    if deletar == 'parar':
        break