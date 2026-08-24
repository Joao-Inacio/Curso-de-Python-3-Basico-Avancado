from pathlib import Path


def explorar_diretorio(caminho):
    caminho = Path(caminho)
    if caminho.exists():
        dicionario_final = {}
        qtd_arquivos = 0
        arquivos = []
        qtd_diretorios = 0
        try:
            for item in caminho.iterdir():
                if item.is_file():
                    arquivos.append(item.name)
                    qtd_arquivos += 1
                else:
                    qtd_diretorios += 1
            dicionario_final["quantidade_arquivos"] = qtd_arquivos
            dicionario_final["quantidade_diretorios"] = qtd_diretorios
            dicionario_final["arquivos"] = arquivos
            return dicionario_final
        except NotADirectoryError:
            arquivos.append(caminho.name)
            dicionario_final["quantidade_arquivos"] = qtd_arquivos + 1
            dicionario_final["quantidade_diretorios"] = qtd_diretorios
            dicionario_final["arquivos"] = arquivos
            return dicionario_final
    else:
        return "Diretorio não exite"


caminho = "/home/joao-inac-io/Curso-de-Python-3-Basico-Avancado/Python-Basico"
print(explorar_diretorio(caminho))
