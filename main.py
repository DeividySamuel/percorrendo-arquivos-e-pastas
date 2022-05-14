import os

caminho_procura = input('digite um caminho:')
termo_procura = input('digite um termo:')

def formata_tamanho(tamanho):
    base = 1024
    Kilo = base
    Mega = base ** 2
    Giga = base ** 3
    Tera = base ** 4
    Peta = base ** 5

    if tamanho < Kilo:
        texto = 'B'
    elif tamanho < Mega:
        tamanho /= Kilo
        texto = 'K'
    elif tamanho < Giga:
        tamanho /= Mega
        texto = 'M'
    elif tamanho < Tera:
        tamanho /= Giga
        texto = 'G'
    elif tamanho < Peta:
        tamanho /= Tera
        texto = 'T'
    else:
        tamanho /= Peta
        texto = 'P'

    tamanho = round(tamanho , 2)
    return f'{tamanho} {texto}'

conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                print()
                print('encontrei o arquivo', arquivo)
                print('caminho:', caminho_completo)
                print('nome:', nome_arquivo)
                print('extensão:', ext_arquivo)
                print('tamanho:', tamanho)
                print('tamanho formatado', formata_tamanho(tamanho))
            except PermissionError as e:
                print('Sem Permissões.')
            except FileNotFoundError as e:
                print('arquivo não encontrado')
            except Exception as e:
                print('Erro Desconhecido', e)
print()
print(f'{conta} arquivos encotrados')