from funções import mudar 
from funções import ler_arquivos_estudantes

parar = True
print('Se quiser parar de modificar digite "parar".')
while parar:
    mude = mudar()
    ler = ler_arquivos_estudantes()
    if mude == 'parar':
        break
    for nomes in ler:
        print(nomes,':', ler[nomes])
    